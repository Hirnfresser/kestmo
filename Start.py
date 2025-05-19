import streamlit as st

# ======= Seiten-Setup =====
st.set_page_config(
    page_title="Kestmo - Startseite",
    page_icon="🏠",
    layout="wide")
# ======= Seiten-Setup =====

st.title("Notenrechner - kestmo")
st.sidebar.page_link('Start.py', label='Startseite')
st.sidebar.page_link('pages/1_Dashboard.py', label='Dashboard')
st.sidebar.page_link('pages/2_Modulgruppen-Uebersicht.py', label='Modulgruppen-Uebersicht')

st.markdown('''Die clevere Noten-App für BMLD-Studierende!
Behalte jederzeit den Überblick über deine Leistungen: Der Notenrechner zeigt dir alle bisherigen Noten, berechnet deinen aktuellen Gesamtschnitt sowie die Durchschnittswerte je Modulgruppe – natürlich inklusive ECTS-Gewichtung.''')

st.html('''<strong>Features:</strong>
            <ul style="margin-left: 18px;">
                <li>Übersichtliche Darstellung aller Noten</li>
                <li>Automatische Berechnung des Gesamtdurchschnitts</li>
                <li>Durchschnittswerte pro Modulgruppe (ECTS-basiert)</li>   
                <li>Wunschnotenrechner (in Planung): Finde heraus, welche Noten du brauchst, um dein Wunschziel zu erreichen!</li>
            </ul>
         ''')

st.write('''Diese App wurde von folgenden Studierenden der ZHAW LSFM entwickelt:
- **Alessia Molignini**
- **Noëlle Keel**
- **Sara Stettler**
''')