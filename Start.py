import pandas as pd
from functions.data_manager import DataManager
from functions.login_manager import LoginManager

# Platz für Login

###

import streamlit as st

st.title("Notenrechner - kestmo")
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