import secrets
import streamlit as st
import streamlit_authenticator as stauth
from utils.data_manager import DataManager


class LoginManager:
    """
    Singleton-Klasse, die den Anwendungsstatus, die Speicherung und die Benutzerauthentifizierung verwaltet.
    
    Verwaltet den Zugriff auf das Dateisystem, Benutzeranmeldedaten und den Authentifizierungsstatus mithilfe des
    `session_state` von Streamlit für die Persistenz zwischen Wiederholungen. Bietet Schnittstellen für den Zugriff
    auf benutzerspezifische und anwendungsweite Datenspeicherung.
    """
    def __new__(cls, *args, **kwargs):
        """
        Implementiert das Singleton-Muster, indem eine vorhandene Instanz aus dem `session_state` zurückgegeben wird,
        falls verfügbar.

        Rückgabe:
            AppManager: Die Singleton-Instanz, entweder eine vorhandene oder eine neu erstellte.
        """
        if 'login_manager' in st.session_state:
            return st.session_state.login_manager
        else:
            instance = super(LoginManager, cls).__new__(cls)
            st.session_state.login_manager = instance
            return instance
    
    def __init__(self, data_manager: DataManager = None,
                 auth_credentials_file: str = 'credentials.yaml',
                 auth_cookie_name: str = 'bmld_inf2_streamlit_app'):
        """
        Initialisiert die Dateisystem- und Authentifizierungskomponenten, falls sie noch nicht initialisiert wurden.

        Richtet den Zugriff auf das Dateisystem mit dem angegebenen Protokoll ein und konfiguriert die Authentifizierung
        mit cookie-basierter Sitzungsverwaltung.

        Parameter:
            data_manager: Die DataManager-Instanz, die für die Datenspeicherung verwendet wird.
            auth_credentials_file (str): Der Dateiname, der für die Speicherung der Benutzerdaten verwendet wird.
            auth_cookie_name (str): Der Name des Cookies, der für die Sitzungsverwaltung verwendet wird.
        """
        if hasattr(self, 'authenticator'):  # Überprüfen, ob die Instanz bereits initialisiert ist
            return
        
        if data_manager is None:
            return

        # Initialisierung der Streamlit-Authentifizierungs-Komponenten
        self.data_manager = data_manager
        self.auth_credentials_file = auth_credentials_file
        self.auth_cookie_name = auth_cookie_name
        self.auth_cookie_key = secrets.token_urlsafe(32)
        self.auth_credentials = self._load_auth_credentials()
        self.authenticator = stauth.Authenticate(self.auth_credentials, self.auth_cookie_name, self.auth_cookie_key)


    def _load_auth_credentials(self):
        """
        Lädt die Benutzerdaten aus der konfigurierten Anmeldedatei.

        Rückgabe:
            dict: Benutzerdaten, standardmäßig ein leeres `usernames`-Dictionary, falls die Datei nicht gefunden wird.
        """
        dh = self.data_manager._get_data_handler()
        return dh.load(self.auth_credentials_file, initial_value= {"usernames": {}})

    def _save_auth_credentials(self):
        """
        Speichert die aktuellen Benutzerdaten in der Anmeldedatei.
        """
        dh = self.data_manager._get_data_handler()
        dh.save(self.auth_credentials_file, self.auth_credentials)

    def login_register(self, login_title = 'Login', register_title = 'Register new user'):
        """
        Rendert die Authentifizierungsschnittstelle.
        
        Zeigt das Login-Formular und optional das Registrierungsformular an. Verarbeitet die Benutzeranmeldung
        und Registrierungsabläufe. Stoppt die weitere Ausführung nach dem Rendern.

        Parameter:
            login_title: Der Titel des Login-Tabs.
            register_title: Der Titel des Registrierungs-Tabs.
        """
        if st.session_state.get("authentication_status") is True:
            self.authenticator.logout()
        else:
            login_tab, register_tab = st.tabs((login_title, register_title))
            with login_tab:
                self.login(stop=False)
            with register_tab:
                self.register()

    def login(self, stop=True):
        """
        Rendert das Login-Formular und verarbeitet Authentifizierungsstatusmeldungen.
        """
        if st.session_state.get("authentication_status") is True:
            self.authenticator.logout()
        else:
            self.authenticator.login()
            if st.session_state["authentication_status"] is False:
                st.error("Benutzername/Passwort ist falsch.")
            else:
                st.warning("Bitte geben Sie Ihren Benutzernamen und Ihr Passwort ein.")
            if stop:
                st.stop()

    def register(self, stop=True):
        """
        Rendert das Registrierungsformular und verarbeitet den Registrierungsablauf.
        
        Zeigt Passwortanforderungen an, verarbeitet Registrierungsversuche
        und speichert die Anmeldedaten bei erfolgreicher Registrierung.
        """
        if st.session_state.get("authentication_status") is True:
            self.authenticator.logout()
        else:
            st.info("""
            Das Passwort muss 8-20 Zeichen lang sein und mindestens einen Großbuchstaben, 
            einen Kleinbuchstaben, eine Ziffer und ein Sonderzeichen aus @$!%*?& enthalten.
            """)

            # Benutzerdefiniertes Registrierungsformular
            with st.form("register_form"):
                username = st.text_input("Benutzername")
                email = st.text_input("E-Mail")
                name = st.text_input("Vollständiger Name")
                password = st.text_input("Passwort", type="password")
                confirm_password = st.text_input("Passwort bestätigen", type="password")
                submit_button = st.form_submit_button("Registrieren")

            if submit_button:
                # Überprüfen, ob die Passwörter übereinstimmen
                if password != confirm_password:
                    st.error("Die Passwörter stimmen nicht überein.")
                    return

                # Überprüfen, ob das Passwort die Anforderungen erfüllt
                if not self._validate_password(password):
                    st.error("Das Passwort erfüllt nicht die Anforderungen.")
                    return

                # Benutzer registrieren
                try:
                    self.auth_credentials["usernames"][username] = {
                        "email": email,
                        "name": name,
                        "password": stauth.Hasher([password]).generate()[0],
                    }
                    self._save_auth_credentials()
                    st.success(f"Benutzer {username} erfolgreich registriert.")
                except Exception as e:
                    st.error(f"Fehler bei der Registrierung: {e}")

            if stop:
                st.stop()

    def _validate_password(self, password):
        """
        Überprüft, ob das Passwort die Anforderungen erfüllt.

        Anforderungen:
        - 8-20 Zeichen lang
        - Mindestens ein Großbuchstabe
        - Mindestens ein Kleinbuchstabe
        - Mindestens eine Ziffer
        - Mindestens ein Sonderzeichen aus @$!%*?&

        Rückgabe:
            bool: True, wenn das Passwort gültig ist, sonst False.
        """
        import re
        if len(password) < 8 or len(password) > 20:
            return False
        if not re.search(r"[A-Z]", password):
            return False
        if not re.search(r"[a-z]", password):
            return False
        if not re.search(r"\d", password):
            return False
        if not re.search(r"[@$!%*?&]", password):
            return False
        return True

    def go_to_login(self, login_page_py_file):
        """
        Erstellt eine Logout-Schaltfläche, die den Benutzer abmeldet und zur Login-Seite weiterleitet.
        Wenn der Benutzer nicht eingeloggt ist, wird die Login-Seite angezeigt.

        Parameter:
            login_page_py_file (str): Der Pfad zur Python-Datei, die die Login-Seite enthält.
        """
        if st.session_state.get("authentication_status") is not True:
            st.switch_page(login_page_py_file)
        else:
            self.authenticator.logout()  # Erstellt die Logout-Schaltfläche