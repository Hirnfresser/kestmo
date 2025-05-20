import streamlit as st
from functions.notenrechner import manage_pruefungen, schnitt_modul_berechnen, schnitt_modulgruppe_berechnen, grundlagenpraktikum
from functions.design import trennlinie_duenn, trennlinie_stark, sidebar_anzeige, logout_button

# ====== Seiten-Setup =====
st.set_page_config(
    page_title="Kestmo - Modulgruppen",
    page_icon="📚",
    layout="wide"
    )
sidebar_anzeige()
logout_button("Modulgruppen-Uebersicht")
# ====== Seiten-Setup =====

# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('pages/Login.py') 
# ====== End Login Block ======

semesters = ['Herbstsemester 1', 'Fruehlingssemester 1', 
             'Herbstsemester 2', 'Fruehlingssemester 2', 
             'Herbstsemester 3', 'Fruehlingssemester 3']

if 'semester' not in st.session_state:
    st.session_state.semester = semesters[0]

semester = st.selectbox('Wähle das Semester', semesters, index=semesters.index(st.session_state.semester))

if semester != st.session_state.semester:
    st.session_state.semester = semester
    st.rerun()

if semester == 'Herbstsemester 1':
    tab1, tab2, tab3, tab4 = st.tabs(['Basiswissen BMLD 1', 'Wissenschaftliche Grundlagen 1', 'Sprache', 'Grundlagenpraktikum 1'])

    with tab1:
        schnitt_modulgruppe_berechnen('Basiswissen BMLD 1')
        
        trennlinie_stark()

        schnitt_modul_berechnen('Gesundheitsdaten')

        manage_pruefungen(
            fach_name='Gesundheitsdaten',
            session_state_key='pruefungen_geda')

        trennlinie_duenn()

        schnitt_modul_berechnen('Haematologie und Haemostaseologie 1')

        manage_pruefungen(
            fach_name='Haematologie und Haemostaseologie 1',
            session_state_key='pruefungen_haehae1')

        trennlinie_duenn()

        schnitt_modul_berechnen('Medizinische Mikrobiologie 1')

        manage_pruefungen(
            fach_name='Medizinische Mikrobiologie 1',
            session_state_key='pruefungen_memi1')

        trennlinie_duenn()

        schnitt_modul_berechnen('Systemerkrankungen')

        manage_pruefungen(
            fach_name='Systemerkrankungen',
            session_state_key='pruefungen_sys')


    with tab2:
        schnitt_modulgruppe_berechnen('Wissenschaftliche Grundlagen 1')    

        trennlinie_stark()

        schnitt_modul_berechnen('Biologie 1')

        manage_pruefungen(
            fach_name='Biologie 1',
            session_state_key='pruefungen_bio1')
        
        trennlinie_duenn()   

        schnitt_modul_berechnen('Chemie 1')

        manage_pruefungen(
            fach_name='Chemie 1',
            session_state_key='pruefungen_che1')
        
        trennlinie_duenn()

        schnitt_modul_berechnen('Informatik 1')

        manage_pruefungen(
            fach_name='Informatik 1',
            session_state_key='pruefungen_inf1')
        
        trennlinie_duenn()

        schnitt_modul_berechnen('Mathematik 1')

        manage_pruefungen(
            fach_name='Mathematik 1',
            session_state_key='pruefungen_mat1')

    with tab3:
        schnitt_modulgruppe_berechnen('Sprache')
        
        trennlinie_stark()

        schnitt_modul_berechnen('Englisch 1')

        manage_pruefungen(
            fach_name='Englisch 1',
            session_state_key='pruefungen_eng1')

        trennlinie_duenn()

        schnitt_modul_berechnen('Gesellschaftlicher Kontext und Sprache 1')

        manage_pruefungen(
            fach_name='Gesellschaftlicher Kontext und Sprache 1',
            session_state_key='pruefungen_gks1')

    with tab4:
        grundlagenpraktikum('Grundlagenpraktikum 1')


elif semester == 'Fruehlingssemester 1':
    tab1, tab2, tab3 = st.tabs(['Basiswissen BMLD 2', 'Wissenschaftliche Grundlagen 2', 'Grundlagenpraktikum 2'])

    with tab1:
        schnitt_modulgruppe_berechnen('Basiswissen BMLD 2')
        
        trennlinie_stark()

        schnitt_modul_berechnen('Haematologie und Haemostaseologie 2')

        manage_pruefungen(
            fach_name='Haematologie und Haemostaseologie 2',
            session_state_key='pruefungen_haehae2')
        
        trennlinie_duenn()

        schnitt_modul_berechnen('Histologie und Zytologie 1')

        manage_pruefungen(
            fach_name='Histologie und Zytologie 1',
            session_state_key='pruefungen_histo1')
        
        trennlinie_duenn()

        schnitt_modul_berechnen('Klinische Chemie und Immunologie 1')

        manage_pruefungen(
            fach_name='Klinische Chemie und Immunologie 1',
            session_state_key='pruefungen_kci1')

        trennlinie_duenn()

        schnitt_modul_berechnen('Medizinische Mikrobiologie 2')

        manage_pruefungen(
            fach_name='Medizinische Mikrobiologie 2',
            session_state_key='pruefungen_memi2')


    
    with tab2:
        schnitt_modulgruppe_berechnen('Wissenschaftliche Grundlagen 2')
        
        trennlinie_stark()

        schnitt_modul_berechnen('Biologie 2')

        manage_pruefungen(
            fach_name='Biologie 2',
            session_state_key='pruefungen_bio2')
        
        trennlinie_duenn()

        schnitt_modul_berechnen('Chemie 2')

        manage_pruefungen(
            fach_name='Chemie 2',
            session_state_key='pruefungen_che2')
        
        trennlinie_duenn()

        schnitt_modul_berechnen('Informatik 2')

        manage_pruefungen(
            fach_name='Informatik 2',
            session_state_key='pruefungen_inf2')
        
        trennlinie_duenn()

        schnitt_modul_berechnen('Mathematik 2')

        manage_pruefungen(
            fach_name='Mathematik 2',
            session_state_key='pruefungen_mat2')

        trennlinie_duenn()

        schnitt_modul_berechnen('Physik')

        manage_pruefungen(
            fach_name='Physik',
            session_state_key='pruefungen_phy')

        trennlinie_duenn()

        schnitt_modul_berechnen('Englisch 2')

        manage_pruefungen(
            fach_name='Englisch 2',
            session_state_key='pruefungen_eng2')
        
        trennlinie_duenn()

        schnitt_modul_berechnen('Gesellschaftlicher Kontext und Sprache 2')

        manage_pruefungen(
            fach_name='Gesellschaftlicher Kontext und Sprache 2',
            session_state_key='pruefungen_gks2')

    with tab3:
        grundlagenpraktikum('Grundlagenpraktikum 2')


if semester == 'Herbstsemester 2':
    tab1, tab2, tab3 = st.tabs(['Analyseprozesse & Labordiagnostik 1', ' Analyse Prozesse & Labordiagnostik 2', ' Externes Praktikum'])

    with tab1:
        schnitt_modulgruppe_berechnen('Analyseprozesse & Labordiagnostik 1')
        
        trennlinie_stark()

        schnitt_modul_berechnen('Klinische Chemie und Immunologie 2')

        manage_pruefungen(
            fach_name='Klinische Chemie und Immunologie 2',
            session_state_key='pruefungen_kci2')
  
        trennlinie_duenn()

        schnitt_modul_berechnen('Histologie und Zytologie 2')

        manage_pruefungen(
            fach_name='Histologie und Zytologie 2',
            session_state_key='pruefungen_histo2')

        trennlinie_duenn()

        schnitt_modul_berechnen('Immunhaematologie und Transfusionsmedizin 1')

        manage_pruefungen(
            fach_name='Immunhaematologie und Transfusionsmedizin 1',
            session_state_key='pruefungen_iht1')


    with tab2:
        schnitt_modulgruppe_berechnen('Analyseprozesse & Labordiagnostik 2')
    
        trennlinie_stark()

        schnitt_modul_berechnen('Herz-Kreislauf- und respiratorische Erkrankungen')

        manage_pruefungen(
            fach_name='Herz-Kreislauf- und respiratorische Erkrankungen',
            session_state_key='pruefungen_hkr')
        
        trennlinie_duenn()

        schnitt_modul_berechnen('Neoplasien und haematologische Erkrankungen')

        manage_pruefungen(
            fach_name='Neoplasien und haematologische Erkrankungen',
            session_state_key='pruefungen_neopla')
        
        trennlinie_duenn()

        schnitt_modul_berechnen('Selbst- und patientennahe Diagnostik')

        manage_pruefungen(
            fach_name='Selbst- und patientennahe Diagnostik',
            session_state_key='pruefungen_spd')
        
        trennlinie_duenn()

        schnitt_modul_berechnen('Hygiene und Epidemiologie')

        manage_pruefungen(
            fach_name='Hygiene und Epidemiologie',
            session_state_key='pruefungen_hyep')
            
    
    with tab3:
        grundlagenpraktikum('Externes Praktikum Fachbereich A')


if semester == 'Fruehlingssemester 2':
    tab1, tab2 = st.tabs(['Analyseprozesse & Labordiagnostik 3', ' Externe Praktika'])

    with tab1:
        schnitt_modulgruppe_berechnen('Analyseprozesse & Labordiagnostik 3')
        
        trennlinie_stark()

        schnitt_modul_berechnen('Immunhaematologie und Transfusionsmedizin 2')

        manage_pruefungen(
            fach_name='Immunhaematologie und Transfusionsmedizin 2',
            session_state_key='pruefungen_iht2')
  
        trennlinie_duenn()

        schnitt_modul_berechnen('Medizinische Genetik 1')
        
        manage_pruefungen(
            fach_name='Medizinische Genetik 1',
            session_state_key='pruefungen_gen1')
        
        trennlinie_duenn()

        schnitt_modul_berechnen('Bewegungsapparat und neurologische Erkrankungen')

        manage_pruefungen(
            fach_name='Bewegungsapparat und neurologische Erkrankungen',
            session_state_key='pruefungen_bene')
        
        trennlinie_duenn()

        manage_pruefungen(
            fach_name='Endokrinologie, Stoffwechselerkrankungen',
            session_state_key='pruefungen_endo')
        
    with tab2:
        grundlagenpraktikum('Externes Praktikum Fachbereich B')
        grundlagenpraktikum('Externes Praktikum Fachbereich C')
        grundlagenpraktikum('Praxisreflexion und interprofessionelles Handeln')


if semester == 'Herbstsemester 3':
    tab1, tab2, tab3, tab4 = st.tabs(['Analyseprozesse & Labordiagnostik 4', 'Kommunikation & Management 1', 'Angewandte Forschung', 'Gesellschaft, Kultur & Gesundheit'])
    
    with tab1:
        schnitt_modulgruppe_berechnen('Analyseprozesse & Labordiagnostik 4')
        
        trennlinie_stark()

        schnitt_modul_berechnen('Medizinische Genetik 2')

        manage_pruefungen(
            fach_name='Medizinische Genetik 2',
            session_state_key='pruefungen_gen2')
        
        trennlinie_duenn()

        schnitt_modul_berechnen('Urogenitale und gastrointestinale Erkrankugnen')

        manage_pruefungen(
            fach_name='Urogenitale und gastrointestinale Erkrankugnen',
            session_state_key='pruefungen_uro')
        
        trennlinie_duenn()

        schnitt_modul_berechnen('Entwicklungsstörungen und vererbbare Erkrankungen')

        manage_pruefungen(
            fach_name='Entwicklungsstörungen und vererbbare Erkrankungen',
            session_state_key='pruefungen_entw')
        
    with tab2:
        schnitt_modulgruppe_berechnen('Kommunikation & Management 1')
        
        trennlinie_stark()

        schnitt_modul_berechnen('Projekt-, Change- und Risikomanagement 1')

        manage_pruefungen(
            fach_name='Projekt-, Change- und Risikomanagement 1',
            session_state_key='pruefungen_pcr1')
        
        trennlinie_duenn()    

        schnitt_modul_berechnen('Kommunikation 1')

        manage_pruefungen(
            fach_name='Kommunikation 1',
            session_state_key='pruefungen_kom1')
        
        trennlinie_duenn()

        schnitt_modul_berechnen('Evidenzbasiertes Handeln')

        manage_pruefungen(
            fach_name='Evidenzbasiertes Handeln',
            session_state_key='pruefungen_ebh')
        
        trennlinie_duenn()

        schnitt_modul_berechnen('Entwicklungen, Trends, Unternehmertum')

        manage_pruefungen(
            fach_name='Entwicklungen, Trends, Unternehmertum',
            session_state_key='pruefungen_etu')
        
        trennlinie_duenn()

        schnitt_modul_berechnen('Gesundheitsförderung und Praevention')

        manage_pruefungen(
            fach_name='Gesundheitsförderung und Praevention',
            session_state_key='pruefungen_gepr')
        
    with tab3:
        schnitt_modulgruppe_berechnen('Angewandte Forschung')
        
        trennlinie_stark()

        schnitt_modul_berechnen('Projektarbeit')

        manage_pruefungen(
            fach_name='Projektarbeit',
            session_state_key='pruefungen_proj')
        
        trennlinie_duenn()

        schnitt_modul_berechnen('Forschungmethoden 1')

        manage_pruefungen(
            fach_name='Forschungsmethoden 1',
            session_state_key='pruefungen_fors1')
        
    with tab4:
        grundlagenpraktikum('Gesellschaft, Kultur und Gesundheit')
        st.markdown('*Einzelne Module nicht bekannt!*')
        
if semester == 'Fruehlingssemester 3':
    tab1, tab2, tab3 = st.tabs(['Gesundheitssystem', 'Kommunikation & Management 2', 'Bachelorarbeit'])

    with tab1:
        schnitt_modulgruppe_berechnen('Gesundheitssystem')

        trennlinie_stark()

        schnitt_modul_berechnen('Klinische Pharmakologie und personalisierte Medizin')

        manage_pruefungen(
            fach_name='Klinische Pharmakologie und personalisierte Medizin',
            session_state_key='pruefungen_pharma')
        
        trennlinie_duenn()

        schnitt_modul_berechnen('Gesundheitssystem und Digital Health')

        manage_pruefungen(
            fach_name='Gesundheitssystem und Digital Health',
            session_state_key='pruefungen_gedh')
    
    with tab2:
        schnitt_modulgruppe_berechnen('Kommunikation & Management 2')

        trennlinie_stark()

        schnitt_modul_berechnen('Projekt-, Change- und Risikomanagement 2')

        manage_pruefungen(
            fach_name='Projekt-, Change- und Risikomanagement 2',
            session_state_key='pruefungen_pcr2')
        
        trennlinie_duenn()

        schnitt_modul_berechnen('Forschungsmethoden 2')

        manage_pruefungen(
            fach_name='Forschungsmethoden 2',
            session_state_key='pruefungen_fors2')

        trennlinie_duenn()

        schnitt_modul_berechnen('Kommunikation 2')

        manage_pruefungen(
            fach_name='Kommunikation 2',
            session_state_key='pruefungen_kom2')

    with tab3:
        schnitt_modul_berechnen('Bachelorarbeit')

        manage_pruefungen(
            fach_name='Bachelorarbeit',
            session_state_key='pruefungen_ba')


