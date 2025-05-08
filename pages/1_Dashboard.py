import streamlit as st
from utils.data_manager import DataManager
import pandas as pd

# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('pages/Login.py') 
# ====== End Login Block ======

st.title('Dashboard')

data_manager = DataManager(fs_protocol='webdav', fs_root_folder="Institution/kestmo_App")  # switch drive 

# load the data from the persistent storage into the session state
data_manager.load_user_data(
    session_state_key='Pruefungen', 
    file_name='Pruefungen.csv', 
    initial_value=pd.DataFrame(),
    parse_dates=['timestamp'])

data_manager.load_user_data(
    session_state_key='Grundlagenprakikum_Ja_Nein',
    file_name='Grundlagenpraktikum_Ja_Nein.csv',
    initial_value=pd.DataFrame(),
    parse_dates=['timestamp'])

st.sidebar.page_link('Start.py', label='Startseite')
st.sidebar.page_link('pages/1_Dashboard.py', label='Dashboard')
st.sidebar.page_link('pages/2_Modulgruppen-Übersicht.py', label='Modulgruppen-Übersicht')

data_manager = DataManager(fs_protocol='webdav', fs_root_folder="Institution/kestmo_App")  # switch drive 
data_manager.load_user_data(
        session_state_key='data_df', 
        file_name='data.csv', 
        initial_value=pd.DataFrame(),
        parse_dates=['timestamp']
    )

semesters = ['Herbstsemester 1', 'Frühlingssemester 1',
             'Herbstsemester 2', 'Frühlingssemester 2', 
             'Herbstsemester 3', 'Frühlingssemester 3']

if 'semester' not in st.session_state:
    st.session_state.semester = semesters[0]

semester = st.selectbox('Wähle das Semester', semesters, index=semesters.index(st.session_state.semester))

if semester != st.session_state.semester:
    st.session_state.semester = semester
    st.rerun()
