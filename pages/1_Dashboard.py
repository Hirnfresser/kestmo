import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Dashboard')

if 'semester' not in st.session_state:
    semester = st.selectbox('Wähle das Semester', ['Herbstsemester 1', 'Frühlingssemester 1', 'Herbstsemester 2', 'Frühlingssemester 2', 'Herbstsemester 3', 'Frühlingssemester 3'])
    st.session_state.semester = semester

else:
    semester = st.selectbox('Wähle das Semester', ['Herbstsemester 1', 'Frühlingssemester 1', 'Herbstsemester 2', 'Frühlingssemester 2', 'Herbstsemester 3', 'Frühlingssemester 3' ], index=['Herbstsemester 1', 'Frühlingssemester 1', 'Herbstsemester 2', 'Frühlingssemester 2', 'Herbstsemester 3', 'Frühlingssemester 3'].index(st.session_state.semester))
    st.session_state.semester = semester
