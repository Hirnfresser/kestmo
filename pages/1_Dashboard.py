import streamlit as st
from functions.design import sidebar_anzeige

# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('pages/Login.py') 
# ====== End Login Block ======

st.title('Dashboard')

sidebar_anzeige()

semesters = ['Herbstsemester 1', 'Fruehlingssemester 1',
             'Herbstsemester 2', 'Fruehlingssemester 2', 
             'Herbstsemester 3', 'Fruehlingssemester 3']

if 'semester' not in st.session_state:
    st.session_state.semester = semesters[0]

semester = st.selectbox('Wähle das Semester', semesters, index=semesters.index(st.session_state.semester))

if semester != st.session_state.semester:
    st.session_state.semester = semester
    st.rerun()
