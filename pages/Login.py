from utils.data_manager import DataManager
from utils.login_manager import LoginManager
import pandas as pd
import streamlit as st

st.title('Hier folgt das Loginfenster')

st.sidebar.page_link('Start.py', label='Startseite')
st.sidebar.page_link('pages/1_Dashboard.py', label='Dashboard')
st.sidebar.page_link('pages/2_Modulgruppen-Übersicht.py', label='Modulgruppen-Übersicht')

data_manager = DataManager(fs_protocol='webdav', fs_root_folder="Institution/kestmo_App")  # switch drive 

# initialize the login manager
login_manager = LoginManager(data_manager)
login_manager.login_register()  # open login/register page