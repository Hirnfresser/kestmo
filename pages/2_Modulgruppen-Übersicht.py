import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from functions.notenrechner import manage_pruefungen
from functions.notenrechner import schnitt_modulgruppe
from functions.notenrechner import modulgruppen
from functions.notenrechner import grundlagenpraktikum
from functions.notenrechner import grundlagenpraktika

st.title('Modulgruppen-Übersicht')

if 'semester' not in st.session_state:
    semester = st.selectbox('Wähle das Semester', ['Herbstsemester 1', 'Frühlingssemester 1', 'Herbstsemester 2', 'Frühlingssemester 2', 'Herbstsemester 3', 'Frühlingssemester 3'])
    st.session_state.semester = semester

else:
    semester = st.selectbox('Wähle das Semester', ['Herbstsemester 1', 'Frühlingssemester 1', 'Herbstsemester 2', 'Frühlingssemester 2', 'Herbstsemester 3', 'Frühlingssemester 3' ], index=['Herbstsemester 1', 'Frühlingssemester 1', 'Herbstsemester 2', 'Frühlingssemester 2', 'Herbstsemester 3', 'Frühlingssemester 3'].index(st.session_state.semester))
    st.session_state.semester = semester

if semester == 'Herbstsemester 1':
    tab1, tab2, tab3, tab4 = st.tabs(['Basiswissen 1', 'Wissenschaftliche Grundlagen 1', 'Sprache', 'Grundlagenpraktikum 1'])

    with tab1:
        schnitt_modulgruppe(modulgruppen, 'Basiswissen Biomedizinische Labordiagnostik 1' )
        
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
        grundlagenpraktikum(grundlagenpraktika, 'Grundlagenpraktikum 1')


elif semester == 'Frühlingssemester 1':
    tab1, tab2, tab3 = st.tabs(['Basiswissen 2', 'Wissenschaftliche Grundlagen 2', 'Grundlagenpraktikum 2'])

    with tab1:
        schnitt_modulgruppe(modulgruppen, 'Basiswissen Biomedizinische Labordiagnostik 2' )
        
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
        grundlagenpraktikum(grundlagenpraktika, 'Grundlagenpraktikum 2')


if semester == 'Herbstsemester 2':
    tab1, tab2, tab3 = st.tabs(['Analyseprozesse & Labordiagnostik 1', ' Analyse Prozesse & Labordiagnostik 2', ' Externes Praktikum'])

    with tab1:
        schnitt_modulgruppe(modulgruppen, 'Analyseprozesse und Labordiagnostik 1' )
        
        manage_pruefungen(
            fach_name='Klinische Chemie und Immunologie 2',
            session_state_key='pruefungen_kci2',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])
  
        manage_pruefungen(
            fach_name='Histologie und Zytologie 2',
            session_state_key='pruefungen_histo2',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])

        manage_pruefungen(
            fach_name='Immunhämatologie und Transfusionsmedizin 1',
            session_state_key='pruefungen_iht1',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])


    with tab2:
        schnitt_modulgruppe(modulgruppen, 'Analyseprozesse und Labordiagnostik 2' )
    
        manage_pruefungen(
            fach_name='Herz-Kreislauf- und respiratorische Erkrankungen',
            session_state_key='pruefungen_hkr',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])
        
        manage_pruefungen(
            fach_name='Neoplasien und hämatologische Erkrankungen',
            session_state_key='pruefungen_neopla',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])
        
        manage_pruefungen(
            fach_name='Selbst- und patientennahe Diagnostik',
            session_state_key='pruefungen_spd',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])
        
        manage_pruefungen(
            fach_name='Hygiene und Epidemiologie',
            session_state_key='pruefungen_hyep',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])
            
    
    with tab3:
        grundlagenpraktikum(grundlagenpraktika, 'Externes Praktikum Fachbereich A')


if semester == 'Frühlingssemester 2':
    tab1, tab2 = st.tabs(['Analyseprozesse & Labordiagnostik 3', ' Externe Praktika'])

    with tab1:
        schnitt_modulgruppe(modulgruppen, 'Analyseprozesse und Labordiagnostik 3' )
        
        manage_pruefungen(
            fach_name='Immunhämatologie und Transfusionsmedizin 2',
            session_state_key='pruefungen_iht2',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])
  
        manage_pruefungen(
            fach_name='Medizinische Genetik 1',
            session_state_key='pruefungen_gen1',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])
        
        manage_pruefungen(
            fach_name='Bewegungsapparat und neurologische Erkrankungen',
            session_state_key='pruefungen_bene',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])
        
        manage_pruefungen(
            fach_name='Endokrinologie, Stoffwechselerkrankungen',
            session_state_key='pruefungen_endo',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])
        
    with tab2:
        grundlagenpraktikum(grundlagenpraktika, 'Externes Praktikum Fachbereich B')
        grundlagenpraktikum(grundlagenpraktika, 'Externes Praktikum Fachbereich C')
        grundlagenpraktikum(grundlagenpraktika, 'Praxisreflexion und interprofessionelles Handeln')


if semester == 'Herbstsemester 3':
    tab1, tab2, tab3, tab4 = st.tabs(['Analyseprozesse & Labordiagnostik 4', 'Kommunikation und Management 1', 'Angewandte Forschung', 'Gesellschaft, Kultur und Gesundheit'])
    
    with tab1:
        schnitt_modulgruppe(modulgruppen, 'Analyseprozesse und Labordiagnostik 4' )
        
        manage_pruefungen(
            fach_name='Medizinische Genetik 2',
            session_state_key='pruefungen_gen2',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])
        
        manage_pruefungen(
            fach_name='Urogenitale und gastrointestinale Erkrankugnen',
            session_state_key='pruefungen_uro',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])
        
        manage_pruefungen(
            fach_name='Entwicklungsstörungen und vererbbare Erkrankungen',
            session_state_key='pruefungen_entw',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])
        
    with tab2:
        schnitt_modulgruppe(modulgruppen, 'Kommunikation und Management 1' )
        
        manage_pruefungen(
            fach_name='Projekt-, Change- und Risikomanagement 1',
            session_state_key='pruefungen_pcr1',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])
        
        manage_pruefungen(
            fach_name='Kommunikation 1',
            session_state_key='pruefungen_kom1',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])
        
        manage_pruefungen(
            fach_name='Evidenzbasiertes Handeln',
            session_state_key='pruefungen_ebh',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])
        
        manage_pruefungen(
            fach_name='Entwicklungen, Trends, Unternehmertum',
            session_state_key='pruefungen_etu',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])
        
        manage_pruefungen(
            fach_name='Gesundheitsförderung und Prävention',
            session_state_key='pruefungen_gepr',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])
        
    with tab3:
        schnitt_modulgruppe(modulgruppen, 'Angewandte Forschung' )
        
        manage_pruefungen(
            fach_name='Projektarbeit',
            session_state_key='pruefungen_proj',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])
        
        manage_pruefungen(
            fach_name='Forschungsmethoden 1',
            session_state_key='pruefungen_fors1',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])
        
    with tab4:
        st.header('Gesellschaft, Kultur und Gesundheit')
        st.markdown('*Module noch nicht bekannt!*')
        
if semester == 'Frühlingssemester 3':
    tab1, tab2, tab3 = st.tabs(['Gesundheitssystem', 'Kommunikation und Management 2', 'Bachelorarbeit'])

    with tab1:
        schnitt_modulgruppe(modulgruppen, 'Gesundheitssystem' )

        manage_pruefungen(
            fach_name='Klinische Pharmakologie und personalisierte Medizin',
            session_state_key='pruefungen_pharma',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])
        
        manage_pruefungen(
            fach_name='Gesundheitssystem und Digital Health',
            session_state_key='pruefungen_gedh',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])
    
    with tab2:
        schnitt_modulgruppe(modulgruppen, 'Kommunikation und Management 2' )

        manage_pruefungen(
            fach_name='Projekt-, Change- und Risikomanagement 2',
            session_state_key='pruefungen_pcr2',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])
        
        manage_pruefungen(
            fach_name='Forschungsmethoden 2',
            session_state_key='pruefungen_fors2',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])

        manage_pruefungen(
            fach_name='Kommunikation 2',
            session_state_key='pruefungen_kom2',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])

    with tab3:
        
        manage_pruefungen(
            fach_name='Bachelorarbeit',
            session_state_key='pruefungen_ba',
            spalten=['Prüfung', 'Datum', 'Gewichtung', 'Note'])
        

