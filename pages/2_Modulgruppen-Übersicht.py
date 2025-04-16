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
            st.write('10')
        
        st.subheader('Gesundheitsdaten')
        if 'pruefungen_gesundheitsdaten' not in st.session_state:
            st.session_state.pruefungen_gesundheitsdaten = pd.DataFrame(columns=['Prüfung', 'Datum', 'Gewichtung', 'Note'])
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('**Notendurchschnitt des Moduls**')
            gesamt_gewichtung = st.session_state.pruefungen_gesundheitsdaten['Gewichtung'].sum()
            if 0 < gesamt_gewichtung < 100:
                gewichtete_note = (
                    st.session_state.pruefungen_gesundheitsdaten['Note'] * 
                    st.session_state.pruefungen_gesundheitsdaten['Gewichtung']).sum() / gesamt_gewichtung
                st.markdown(f'**Ø** {gewichtete_note:.2f}')

            elif gesamt_gewichtung > 100:
                st.warning('Die Gesamtgewichtung überschreitet 100%. Bitte überprüfen Sie die Eingaben.')
            
            elif gesamt_gewichtung < 0:
                st.warning('Die Gesamtgewichtung beträgt 0%. Bitte überprüfen Sie die Eingaben.')
                
        with col2:
            st.markdown('**ECTS**')
            st.write('2')
    
        


        if len(st.session_state.pruefungen_gesundheitsdaten) > 0:
            data = st.session_state.pruefungen_gesundheitsdaten[['Prüfung', 'Datum', 'Gewichtung', 'Note']]
            
            col1, col2, col3, col4, col5 = st.columns([2, 2, 2, 2, 5])
            with col1:
                st.markdown("**Prüfung**")
            with col2:
                st.markdown("**Datum**")
            with col3:
                st.markdown("**Gewichtung**")
            with col4:
                st.markdown("**Note**")
            
               # Tabelle mit einem Löschen-Button für jede Zeile
            for idx, row in data.iterrows():
                col1, col2, col3, col4, col5 = st.columns([2, 2, 2, 2, 5])
        
                with col1:
                    st.write(row['Prüfung'])
                with col2:
                    st.write(row['Datum'])
                with col3:
                    st.write(f"{row['Gewichtung']} %")
                with col4:
                    st.write(row['Note'])
                with col5:
                    if st.button(f'{row["Prüfung"]} löschen', key=f"delete_{idx}"):
                # Lösche die Zeile basierend auf dem Index
                        st.session_state.pruefungen_gesundheitsdaten = st.session_state.pruefungen_gesundheitsdaten.drop(idx)
                        st.success(f'Prüfung {row["Prüfung"]} erfolgreich gelöscht!')
                        st.rerun()
        else:
            st.info('Noch keine Prüfungen eingetragen. Bitte eine Prüfung hinzufügen.')
    
    
        with st.form(key='form_gesundheitsdaten'):
            col1, col2, col3 =st.columns([2, 2, 2])
            
            with col1:
                name = st.text_input('Prüfung')
            with col2:
                datum = st.date_input('Datum')
            with col3:
                gewichtung = st.number_input('Gewichtung in Prozent', min_value=0.0, max_value=100.0, step=1.0)
            
            col4, col5 = st.columns([2, 2])

            with col4:
                note = st.number_input('Note', min_value=1.0, max_value=6.0, step=0.05) 

            with col5:
                submit_button = st.form_submit_button(label='Prüfung hinzufügen')
            
            if submit_button:
                new_row = pd.DataFrame({
                    'Prüfung': [name], 
                    'Datum': [datum], 
                    'Gewichtung': [gewichtung], 
                    'Note': [note]})
                st.session_state.pruefungen_gesundheitsdaten = pd.concat([st.session_state.pruefungen_gesundheitsdaten, new_row], ignore_index=True)
                st.success('Prüfung erfolgreich hinzugefügt!')
                st.rerun()
        
  

        st.subheader('Hämatologie und Hämostaseologie 1')
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('**Notendurchschnitt des Moduls**')
            st.write('XX.X')
        with col2:
            st.markdown('**ECTS**')
            st.write('2')

        

        st.subheader('Medizinische Mikrobiologie 1')
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('**Notendurchschnitt des Moduls**')
            st.write('XX.X')
        with col2:
            st.markdown('**ECTS**')
            st.write('3')

        st.subheader('Systemerkrankungen')
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('**Notendurchschnitt des Moduls**')
            st.write('XX.X')
        with col2:
            st.markdown('**ECTS**')
            st.write('3')

    with tab2:
        st.header('Wissenschaftliche Grundlagen 1')
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('**Notendurchschnitt der Modulgruppe**')
            st.write('XX.X')
        with col2:
            st.markdown('**ECTS**')
            st.write('13')
        
        st.subheader('Biologie 1')
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('**Notendurchschnitt des Moduls**')
            st.write('XX.X')
        with col2:
            st.markdown('**ECTS**')
            st.write('5')
        
        st.subheader('Chemie 1')
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('**Notendurchschnitt des Moduls**')
            st.write('XX.X')
        with col2:
            st.markdown('**ECTS**')
            st.write('3')

        st.subheader('Informatik 1')
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('**Notendurchschnitt des Moduls**')
            st.write('XX.X')
        with col2:
            st.markdown('**ECTS**')
            st.write('2')

        st.subheader('Mathematik 1')
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('**Notendurchschnitt des Moduls**')
            st.write('XX.X')
        with col2:
            st.markdown('**ECTS**')
            st.write('3')

    with tab3:
        st.header('Sprache')
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('**Notendurchschnitt der Modulgruppe**')
            st.write('XX.X')
        with col2:
            st.markdown('**ECTS**')
            st.write('4')

        st.subheader('Englisch 1')
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('**Notendurchschnitt des Moduls**')
            st.write('XX.X')
        with col2:
            st.markdown('**ECTS**')
            st.write('2')

        st.subheader('Gesellschaftlicher Kontext und Sprache 1')
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('**Notendurchschnitt des Moduls**')
            st.write('XX.X')
        with col2:
            st.markdown('**ECTS**')
            st.write('2')

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
        st.header('Basiswissen 2')
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('**Notendurchschnitt der Modulgruppe**')
            st.write('XX.X')
        with col2:
            st.markdown('**ECTS**')
            st.write('10')

        st.subheader('Hämatologie und Hämostaseologie 2')
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('**Notendurchschnitt des Moduls**')
            st.write('XX.X')
        with col2:
            st.markdown('**ECTS**')
            st.write('3')

        st.subheader('Histologie und Zytologie 1')
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('**Notendurchschnitt des Moduls**')
            st.write('XX.X')
        with col2:
            st.markdown('**ECTS**')
            st.write('3')

        st.subheader('Klinische Chemie und Immunologie 1')
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('**Notendurchschnitt des Moduls**')
            st.write('XX.X')
        with col2:
            st.markdown('**ECTS**')
            st.write('2')

        st.subheader('Medizinische Mikrobiologie 2')
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('**Notendurchschnitt des Moduls**')
            st.write('XX.X')
        with col2:
            st.markdown('**ECTS**')
            st.write('2')
    
    with tab2:
        st.header('Wissenschaftliche Grundlagen 2')
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('**Notendurchschnitt der Modulgruppe**')
            st.write('XX.X')
        with col2:
            st.markdown('**ECTS**')
            st.write('17')

        st.subheader('Biologie 2')
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('**Notendurchschnitt des Moduls**')
            st.write('XX.X')
        with col2:
            st.markdown('**ECTS**')
            st.write('3')

        st.subheader('Chemie 2')
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('**Notendurchschnitt des Moduls**')
            st.write('XX.X')
        with col2:
            st.markdown('**ECTS**')
            st.write('3')

        st.subheader('Informatik 2')
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('**Notendurchschnitt des Moduls**')
            st.write('XX.X')
        with col2:
            st.markdown('**ECTS**')
            st.write('2')

        st.subheader('Mathematik 2')
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('**Notendurchschnitt des Moduls**')
            st.write('XX.X')
        with col2:
            st.markdown('**ECTS**')
            st.write('3')

        st.subheader('Physik')
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('**Notendurchschnitt des Moduls**')
            st.write('XX.X')
        with col2:
            st.markdown('**ECTS**')
            st.write('2')

        st.subheader('Englisch 2')
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('**Notendurchschnitt des Moduls**')
            st.write('XX.X')
        with col2:
            st.markdown('**ECTS**')
            st.write('2')

        st.subheader('Gesellschaftlicher Kontext und Sprache 2')
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('**Notendurchschnitt des Moduls**')
            st.write('XX.X')
        with col2:
            st.markdown('**ECTS**')
            st.write('2')

    with tab3:
        st.header('Grundlagenpraktikum 2')
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('**Notendurchschnitt der Modulgruppe**')
            st.write('XX.X')
        with col2:
            st.markdown('**ECTS**')
            st.write('3')

