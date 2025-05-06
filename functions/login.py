import streamlit as st
import streamlit_authenticator as stauth
import yaml
import os
import re
from yaml.loader import SafeLoader

CREDENTIALS_FILE = "credentials.yaml"

# Initialisiere Credentials-Datei, wenn sie nicht existiert
def init_credentials_file():
    if not os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, "w") as file:
            yaml.dump({"usernames": {}}, file)

def load_credentials():
    with open(CREDENTIALS_FILE, 'r') as file:
        return yaml.load(file, Loader=SafeLoader)

def save_credentials(credentials):
    with open(CREDENTIALS_FILE, "w") as file:
        yaml.dump(credentials, file)

def validate_password(pw):
    if len(pw) < 8:
        return "Passwort muss mindestens 8 Zeichen lang sein."
    if not re.search(r"[A-Z]", pw):
        return "Passwort muss mindestens einen Großbuchstaben enthalten."
    if not re.search(r"[!&%*?\$]", pw):
        return "Passwort muss mindestens ein Sonderzeichen (!&%*?$) enthalten."
    return None

def register_user():
    st.subheader("Registrieren")
    with st.form("registration_form"):
        first_name = st.text_input("Vorname")
        last_name = st.text_input("Nachname")
        username = st.text_input("Benutzername")
        email = st.text_input("E-Mail")
        email_confirm = st.text_input("E-Mail bestätigen")
        password = st.text_input("Passwort", type="password")
        password_confirm = st.text_input("Passwort bestätigen", type="password")
        submitted = st.form_submit_button("Registrieren")

        if submitted:
            if not all([first_name, last_name, username, email, email_confirm, password, password_confirm]):
                st.error("Bitte alle Felder ausfüllen.")
                return

            if email != email_confirm:
                st.error("Die E-Mail-Adressen stimmen nicht überein.")
                return

            if password != password_confirm:
                st.error("Die Passwörter stimmen nicht überein.")
                return

            password_issue = validate_password(password)
            if password_issue:
                st.error(password_issue)
                return

            credentials = load_credentials()
            if username in credentials["usernames"]:
                st.error("Benutzername existiert bereits.")
                return

            hasher = stauth.Hasher([password])
            hashed_pw = hasher.hash(password)[0]
            credentials["usernames"][username] = {
                "name": f"{first_name} {last_name}",
                "email": email,
                "password": hashed_pw
            }

            try:
                save_credentials(credentials)
                st.success("Registrierung erfolgreich! Sie können sich jetzt einloggen.")
            except Exception as e:
                st.error(f"Fehler beim Speichern der Anmeldedaten: {e}")

def login_user():
    st.subheader("Login")
    with st.form("login_form"):
        username = st.text_input("Benutzername")
        password = st.text_input("Passwort", type="password")
        submitted = st.form_submit_button("Login")

        if submitted:
            credentials = load_credentials()
            
            if username not in credentials["usernames"]:
                st.error("Benutzername existiert nicht.")
                return

            # Benutzer gefunden, jetzt Passwort-Hash vergleichen
            stored_hash = credentials["usernames"][username]["password"]

            # Hasher verwenden, um den Hash des eingegebenen Passworts zu berechnen
            hasher = stauth.Hasher([password])
            entered_hash = hasher.hash(password)[0]

            if entered_hash == stored_hash:
                st.session_state["authentication_status"] = True
                st.success("Login erfolgreich!")
                # Weitere Aktionen nach dem erfolgreichen Login (z. B. Weiterleitung)
            else:
                st.session_state["authentication_status"] = False
                st.error("Benutzername oder Passwort sind falsch.")

def login_main():
    st.set_page_config(page_title="Login & Registrierung", layout="centered")
    st.title("Benutzerverwaltung")

    init_credentials_file()

    tab1, tab2 = st.tabs(["Login", "Registrieren"])

    with tab1:
        login_user()
    with tab2:
        register_user()

if __name__ == "__login_main__":
    login_main()
