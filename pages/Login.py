from utils.data_manager import DataManager
from utils.login_manager import LoginManager
import pandas as pd
import streamlit as st

st.title('Hier folgt das Loginfenster')

data_manager = DataManager(fs_protocol='webdav', fs_root_folder="Institution/kestmo_APP")  # switch drive 

# Überprüfen, ob ein Benutzer eingeloggt ist
if st.session_state.get("username"):
    # load the data from the persistent storage into the session state
    data_manager.load_user_data(
        session_state_key='data_df', 
        file_name='data.csv', 
        initial_value=pd.DataFrame(),
        parse_dates=['timestamp']
    )
else:
    pass

# initialize the login manager
login_manager = LoginManager(data_manager)
login_manager.login_register()  # open login/register page