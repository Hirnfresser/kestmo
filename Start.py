import streamlit as st
from utils.data_manager import DataManager
from utils.login_manager import LoginManager
import pandas as pd

st.title("Notenrechner - kestmo")
st.sidebar.page_link('Start.py', label='Startseite')
st.sidebar.page_link('pages/1_Dashboard.py', label='Dashboard')
st.sidebar.page_link('pages/2_Modulgruppen-Übersicht.py', label='Modulgruppen-Übersicht')

st.markdown('''Die clevere Noten-App für BMLD-Studierende!
Behalte jederzeit den Überblick über deine Leistungen: Der Notenrechner zeigt dir alle bisherigen Noten, berechnet deinen aktuellen Gesamtschnitt sowie die Durchschnittswerte je Modulgruppe – natürlich inklusive ECTS-Gewichtung.

Features:   
✔️ Übersichtliche Darstellung aller Noten   
✔️ Automatische Berechnung des Gesamtdurchschnitts   
✔️ Durchschnittswerte pro Modulgruppe (ECTS-basiert)   
✔️ Wunschnotenrechner (in Planung): Finde heraus, welche Noten du brauchst, um dein Wunschziel zu erreichen!''')

st.write('''Diese App wurde von folgenden Studierenden der ZHAW LSFM entwickelt:
- **Alessia Molignini**
- **Noëlle Keel**
- **Sara Stettler**
''')


