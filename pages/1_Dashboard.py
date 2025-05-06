import streamlit as st


# ====== Start Login Block ======
from functions.login_manager import LoginManager
LoginManager().go_to_login('pages/Login.py') 
# ====== End Login Block ======

st.title('Dashboard')


semesters = ['Herbstsemester 1', 'Frühlingssemester 1',
             'Herbstsemester 2', 'Frühlingssemester 2', 
             'Herbstsemester 3', 'Frühlingssemester 3']

if 'semester' not in st.session_state:
    st.session_state.semester = semesters[0]

semester = st.selectbox('Wähle das Semester', semesters, index=semesters.index(st.session_state.semester))

if semester != st.session_state.semester:
    st.session_state.semester = semester
    st.rerun()
