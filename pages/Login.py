from utils.data_manager import DataManager
from utils.login_manager import LoginManager
import pandas as pd
import streamlit as st
from utils.helpers import nav_page
from functions.design import sidebar_anzeige

st.title('Login & Registrierung')

sidebar_anzeige()

data_manager = DataManager(fs_protocol='webdav', fs_root_folder="Institution/kestmo_App")  # Switchdrive


# initialize the login manager
login_manager = LoginManager(data_manager)
login_manager.login_register()

data_manager.load_user_data(
    session_state_key="Pruefungen",
    file_name="Pruefungen.csv",
    initial_value=pd.DataFrame()
    )

data_manager.load_user_data(
    session_state_key="Grundlagenpraktika",
    file_name="Grundlagenpraktika.csv",
    initial_value=pd.DataFrame()
)

#nav_page('Dashboard')