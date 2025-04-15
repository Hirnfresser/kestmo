import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.title('Modulgruppen-Übersicht')

if 'semester' not in st.session_state:
    semester = st.selectbox('Wähle das Semester', ['Herbstsemester 1', 'Frühlingssemester 1'])
    st.session_state.semester = semester

else:
    semester = st.selectbox('Wähle das Semester', ['Herbstsemester 1', 'Frühlingssemester 1'], index=['Herbstsemester 1', 'Frühlingssemester 1'].index(st.session_state.semester))
    st.session_state.semester = semester

if semester == 'Herbstsemester 1':
    tab1, tab2, tab3, tab4 = st.tabs(['Basiswissen 1', 'Wissenschaftliche Grundlagen 1', 'Sprache', 'Grundlagenpraktikum 1'])

    with tab1:
        st.header('Basiswissen 1')
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('**Notendurchschnitt der Modulgruppe**')
            st.write('XX.X')
        with col2:
            st.markdown('**ECTS**')
            st.write('XX')
        st.subheader('Gesundheitsdaten')
        st.subheader('Hämatologie und Hämostaseologie 1')
        st.subheader('Medizinische Mikrobiologie 1')
        st.subheader('Systemerkrankungen')

    with tab2:
        st.header('Wissenschaftliche Grundlagen 1')
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('**Notendurchschnitt der Modulgruppe**')
            st.write('XX.X')
        with col2:
            st.markdown('**ECTS**')
            st.write('XX')
        st.subheader('Biologie 1')
        st.subheader('Chemie 1')
        st.subheader('Informatik 1')
        st.subheader('Mathematik 1')

    with tab3:
        st.header('Sprache')
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('**Notendurchschnitt der Modulgruppe**')
            st.write('XX.X')
        with col2:
            st.markdown('**ECTS**')
            st.write('XX')
        st.subheader('Englisch 1')
        st.subheader('Gesellschaftlicher Kontext und Sprache 1')

    with tab4:
        st.header('Grundlagenpraktikum 1')
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('**Notendurchschnitt der Modulgruppe**')
            st.write('XX.X')
        with col2:
            st.markdown('**ECTS**')
            st.write('XX')

elif semester == 'Frühlingssemester 1':
    tab1, tab2, tab3 = st.tabs(['Basiswissen 2', 'Wissenschaftliche Grundlagen 2', 'Grundlagenpraktikum 2'])

    with tab1:
        st.header('Basiswissen 2')
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('**Notendurchschnitt der Modulgruppe**')
            st.write('XX.X')
        with col2:
            st.markdown('**ECTS**')
            st.write('XX')
        st.subheader('Hämatologie und Hämostaseologie 2')
        st.subheader('Histologie und Zytologie 1')
        st.subheader('Klinische Chemie und Immunologie 1')
        st.subheader('Medizinische Mikrobiologie 2')
    
    with tab2:
        st.header('Wissenschaftliche Grundlagen 2')
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('**Notendurchschnitt der Modulgruppe**')
            st.write('XX.X')
        with col2:
            st.markdown('**ECTS**')
            st.write('XX')
        st.subheader('Biologie 2')
        st.subheader('Chemie 2')
        st.subheader('Informatik 2')
        st.subheader('Mathematik 2')
        st.subheader('Physik')
        st.subheader('Englisch 2')
        st.subheader('Gesellschaftlicher Kontext und Sprache 2')

    with tab3:
        st.header('Grundlagenpraktikum 2')
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('**Notendurchschnitt der Modulgruppe**')
            st.write('XX.X')
        with col2:
            st.markdown('**ECTS**')
            st.write('XX')

