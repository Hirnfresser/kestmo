import streamlit as st
from functions.design import sidebar_anzeige

# ======= Seiten-Setup =====
st.set_page_config(
    page_title="Kestmo - Startseite",
    page_icon="🏠",
    layout="wide"
    )

sidebar_anzeige()
# ======= Seiten-Setup =====

col1, col3 = st.columns([4, 1])
with col1:
    st.title("Notenrechner - kestmo")
with col3:
    st.markdown(
        """
        <div style='border:2px solid #79085E; border-radius:8px; padding:6px; display:inline-block; margin-top: 24px;'>
            <a href='?page=pages/Login.py' style='text-decoration:none; color:#79085E; font-weight:bold;'>
                🔑 Login & Registrierung
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )


st.markdown('''Die clevere Noten-App für BMLD-Studierende!
Behalte jederzeit den Überblick über deine Leistungen: Der Notenrechner zeigt dir alle bisherigen Noten, berechnet deinen aktuellen Gesamtschnitt sowie die Durchschnittswerte je Modulgruppe – natürlich inklusive ECTS-Gewichtung.''')

st.html('''<strong>Features:</strong>
            <ul style="margin-left: 18px;">
                <li>Übersichtliche Darstellung aller Noten</li>
                <li>Automatische Berechnung des Gesamtdurchschnitts</li>
                <li>Durchschnittswerte pro Modulgruppe (ECTS-basiert)</li>   
                <li>Visualisierung des ECTS-Fortschritts über das gesamte Bachelorstudium</li>
            </ul>
         ''')

st.html('''<strong>Coming Soon:</strong>
            <ul style="margin-left: 18px;">
                <li>Wunschnotenrechner</li>
                <li>Notendownload als PDF</li>
                <li>Überarbeitung der Login-Seite (Passwort vergessen, Remember Me Funktion)</li>
            <ul>
         ''')

st.write('''Diese App wurde von folgenden Studierenden der ZHAW LSFM entwickelt:
- **Alessia Molignini**
- **Noëlle Keel**
- **Sara Stettler**
''')