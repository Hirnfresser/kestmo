import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from functions.notenrechner import manage_pruefungen
from functions.notenrechner import schnitt_modulgruppe
from functions.notenrechner import modulgruppen

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
        schnitt_modulgruppe(modulgruppen, 'Basiswissen 1' )
        
        manage_pruefungen(
            fach_name='Gesundheitsdaten',
            session_state_key='pruefungen_geda',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])
  
        manage_pruefungen(
            fach_name='Hämatologie und Hämostaseologie 1',
            session_state_key='pruefungen_hähä1',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])

        manage_pruefungen(
            fach_name='Medizinische Mikrobiologie 1',
            session_state_key='pruefungen_memi1',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])

        manage_pruefungen(
            fach_name='Systemerkrankungen',
            session_state_key='pruefungen_sys',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])


    with tab2:
        schnitt_modulgruppe(modulgruppen, 'Wissenschaftliche Grundlagen 1' )
    
        manage_pruefungen(
            fach_name='Biologie 1',
            session_state_key='pruefungen_bio1',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])
        
        manage_pruefungen(
            fach_name='Chemie 1',
            session_state_key='pruefungen_che1',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])
        
        manage_pruefungen(
            fach_name='Informatik 1',
            session_state_key='pruefungen_inf1',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])
        
        manage_pruefungen(
            fach_name='Mathematik 1',
            session_state_key='pruefungen_mat1',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])
    

    with tab3:
        schnitt_modulgruppe(modulgruppen, 'Sprache' )
        
        manage_pruefungen(
            fach_name='Englisch 1',
            session_state_key='pruefungen_eng1',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])

        manage_pruefungen(
            fach_name='Gesellschaftlicher Kontext und Sprache 1',
            session_state_key='pruefungen_gks1',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])



    with tab4:
        st.header('Grundlagenpraktikum 1')
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('**Notendurchschnitt der Modulgruppe**')
            st.write('XX.X')
        with col2:
            st.markdown('**ECTS**')
            st.write('3')

elif semester == 'Frühlingssemester 1':
    tab1, tab2, tab3 = st.tabs(['Basiswissen 2', 'Wissenschaftliche Grundlagen 2', 'Grundlagenpraktikum 2'])

    with tab1:
        schnitt_modulgruppe(modulgruppen, 'Basiswissen 2' )
        
        manage_pruefungen(
            fach_name='Hämatologie und Hämostaseologie 2',
            session_state_key='pruefungen_hähä2',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])
        
        manage_pruefungen(
            fach_name='Histologie und Zytologie 1',
            session_state_key='pruefungen_histo1',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])
        
        manage_pruefungen(
            fach_name='Klinische Chemie und Immunologie 1',
            session_state_key='pruefungen_kci1',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])

        manage_pruefungen(
            fach_name='Medizinische Mikrobiologie 2',
            session_state_key='pruefungen_memi2',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])


    
    with tab2:
        schnitt_modulgruppe(modulgruppen, 'Wissenschaftliche Grundlagen 2' )
        
        manage_pruefungen(
            fach_name='Biologie 2',
            session_state_key='pruefungen_bio2',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])
        
        manage_pruefungen(
            fach_name='Chemie 2',
            session_state_key='pruefungen_che2',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])
        
        manage_pruefungen(
            fach_name='Informatik 2',
            session_state_key='pruefungen_inf2',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])
        
        manage_pruefungen(
            fach_name='Mathematik 2',
            session_state_key='pruefungen_mat2',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])

        manage_pruefungen(
            fach_name='Physik',
            session_state_key='pruefungen_phy',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])
    
        manage_pruefungen(
            fach_name='Englisch 2',
            session_state_key='pruefungen_eng2',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])
        
        manage_pruefungen(
            fach_name='Gesellschaftlicher Kontext und Sprache 2',
            session_state_key='pruefungen_gks2',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])

    with tab3:
        st.header('Grundlagenpraktikum 2')
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('**Notendurchschnitt der Modulgruppe**')
            st.write('XX.X')
        with col2:
            st.markdown('**ECTS**')
            st.write('3')

