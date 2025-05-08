from utils.data_manager import DataManager
from utils.login_manager import LoginManager
import pandas as pd
import streamlit as st
from utils.helpers import nav_page

st.title('Login & Registrierung')

st.sidebar.page_link('Start.py', label='Startseite')
st.sidebar.page_link('pages/1_Dashboard.py', label='Dashboard')
st.sidebar.page_link('pages/2_Modulgruppen-Uebersicht.py', label='Modulgruppen-Uebersicht')

data_manager = DataManager(fs_protocol='webdav', fs_root_folder="Institution/kestmo_App")  # switch drive 

# initialize the login manager
login_manager = LoginManager(data_manager)

if login_manager.login_register():  # Login erfolgreich
    st.success("Login erfolgreich! Daten werden geladen...")

    # Nutzerspezifische Daten laden
    username = st.session_state["username"]  # Benutzername aus dem session_state
    pruefungen_key = f"{username}_Pruefungen"
    praktika_key = f"{username}_Grundlagenpraktika"

    # Daten registrieren und laden, falls sie nicht im session_state existieren
    if pruefungen_key not in st.session_state:
        data_manager.register_user_data(
            session_state_key=pruefungen_key,
            file_name=f"{username}_Pruefungen.csv",
            initial_value=pd.DataFrame(columns=["Prüfung", "Datum", "Gewichtung", "Note"])
        )
    if praktika_key not in st.session_state:
        data_manager.register_user_data(
            session_state_key=praktika_key,
            file_name=f"{username}_Grundlagenpraktika.csv",
            initial_value=pd.DataFrame(columns=["Grundlagenpraktikum", "Status", "ECTS", "timestamp"])
        )

    # Daten in den session_state laden
    data_manager.load_user_data(
        session_state_key=pruefungen_key,
        file_name=f"{username}_Pruefungen.csv",
        initial_value=pd.DataFrame(columns=["Prüfung", "Datum", "Gewichtung", "Note"])
    )
    data_manager.load_user_data(
        session_state_key=praktika_key,
        file_name=f"{username}_Grundlagenpraktika.csv",
        initial_value=pd.DataFrame(columns=["Grundlagenpraktikum", "Status", "ECTS", "timestamp"])
    )
    
    # Weiterleitung zur Dashboard-Seite
    nav_page('Dashboard')