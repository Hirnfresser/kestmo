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


from utils.data_manager import DataManager
import pandas as pd

# initialize the data manager
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="Institution/BMLD_App_RPI_Rechner")  # switch drive 

# load the data from the persistent storage into the session state
data_manager.load_user_data(
    session_state_key='data_df', 
    file_name='data.csv', 
    initial_value = pd.DataFrame(),
    parse_dates = ['timestamp']
    )