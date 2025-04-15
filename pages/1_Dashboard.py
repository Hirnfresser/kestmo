import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Dashboard')

if 'semester' not in st.session_state:
    semester = st.selectbox('Wähle das Semester', ['Herbstsemester 1', 'Frühlingssemester 1'])
    st.session_state.semester = semester

else:
    semester = st.selectbox('Wähle das Semester', ['Herbstsemester 1', 'Frühlingssemester 1'], index=['Herbstsemester 1', 'Frühlingssemester 1'].index(st.session_state.semester))
    st.session_state.semester = semester
