from utils.data_manager import DataManager
from utils.login_manager import LoginManager
import pandas as pd
import streamlit as st
from utils.helpers import nav_page

st.title('Login & Registrierung')

st.sidebar.page_link('Start.py', label='Startseite')
st.sidebar.page_link('pages/1_Dashboard.py', label='Dashboard')
st.sidebar.page_link('pages/2_Modulgruppen-Uebersicht.py', label='Modulgruppen-Uebersicht')

st.write('username', st.session_state.get('username','-'))

data_manager = DataManager(fs_protocol='webdav', fs_root_folder="Institution/kestmo_App")  # Switchdrive

st.write(data_manager.info())

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

st.write(data_manager.info())