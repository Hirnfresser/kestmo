import streamlit as st
import pandas as pd
import time
import pandas as pd
from utils.data_manager import DataManager
import matplotlib.pyplot as plt
import altair as alt
import numpy as np


ects_dict = {
    'Gesundheitsdaten': 2,
    'Haematologie und Haemostaseologie 1': 2,
    'Medizinische Mikrobiologie 1': 3,
    'Systemerkrankungen': 3,
    'Biologie 1': 5,
    'Chemie 1': 3,
    'Informatik 1': 2,
    'Mathematik 1': 3,
    'Englisch 1': 2,
    'Gesellschaftlicher Kontext und Sprache 1': 2,
    
    'Haematologie und Haemostaseologie 2': 3,
    'Histologie und Zytologie 1': 3,
    'Klinische Chemie und Immunologie 1': 2,
    'Medizinische Mikrobiologie 2': 2,
    'Biologie 2': 3,
    'Chemie 2': 3,
    'Informatik 2': 2,
    'Mathematik 2': 3,
    'Physik': 2,
    'Englisch 2': 2,
    'Gesellschaftlicher Kontext und Sprache 2': 2,
    
    'Klinische Chemie und Immunologie 2': 2,
    'Histologie und Zytologie 2': 2,
    'Immunhaematologie und Transfusionsmedizin 1': 2,
    'Herz-Kreislauf- und respiratorische Erkrankungen': 3,
    'Neoplasien und haematologische Erkrankungen': 3,
    'Selbst- und patientennahe Diagnostik': 3,
    'Hygiene und Epidemiologie': 2,
    
    'Immunhaematologie und Transfusionsmedizin 2': 2,
    'Medizinische Genetik 1': 2,
    'Bewegungsapparat und neurologische Erkrankungen': 3,
    'Endokrinologie, Stoffwechselerkrankungen': 3,
    
    'Medizinische Genetik 2': 2,
    'Urogenitale und gastrointestinale Erkrankungen': 3,
    'Entwicklungsstörungen und vererbbare Erkrankungen': 3,
    'Projekt-, Change- und Risikomanagement 1': 4,
    'Kommunikation 1': 4,
    'Evidenzbasiertes Handeln': 2,
    'Entwicklungen, Trends, Unternehmertum': 2,
    'Gesundheitsförderung und Praevention': 2,
    'Projektarbeit': 6,
    'Forschungsmethoden 1': 2,
    
    'Klinische Pharmakologie und personalisierte Medizin': 4,
    'Gesundheitssystem und Digital Health': 2,
    'Projekt-, Change- und Risikomanagement 2': 2,
    'Forschungsmethoden 2': 2,
    'Kommunikation 2': 2,
    'Bachelorarbeit': 15}

modulgruppen = {
    'Basiswissen BMLD 1': {
        'semester': 'Herbstsemester 1',
        'ects': 10,
        'faecher': {
            'Gesundheitsdaten': {'key': 'pruefungen_geda', 'ects': ects_dict['Gesundheitsdaten']},
            'Haematologie und Haemostaseologie 1': {'key': 'pruefungen_haehae1', 'ects': ects_dict['Haematologie und Haemostaseologie 1']},
            'Medizinische Mikrobiologie 1': {'key': 'pruefungen_memi1', 'ects': ects_dict['Medizinische Mikrobiologie 1']},
            'Systemerkrankungen': {'key': 'pruefungen_sys', 'ects': ects_dict['Systemerkrankungen']}}},
    'Wissenschaftliche Grundlagen 1': {
        'semester': 'Herbstsemester 1',
        'ects': 13,
        'faecher': {
            'Biologie 1': {'key': 'pruefungen_bio1', 'ects': ects_dict['Biologie 1']},
            'Chemie 1': {'key': 'pruefungen_che1', 'ects': ects_dict['Chemie 1']},
            'Informatik 1': {'key': 'pruefungen_inf1', 'ects': ects_dict['Informatik 1']},
            'Mathematik 1': {'key': 'pruefungen_mat1', 'ects': ects_dict['Mathematik 1']}}},
    'Sprache': {
        'semester': 'Herbstsemester 1',
        'ects': 4,
        'faecher': {
            'Englisch 1': {'key': 'pruefungen_eng1', 'ects': ects_dict['Englisch 1']},
            'Gesellschaftlicher Kontext und Sprache 1': {'key': 'pruefungen_gks1', 'ects': ects_dict['Gesellschaftlicher Kontext und Sprache 1']}}},

    'Basiswissen BMLD 2': {
        'semester': 'Fruehlingssemester 1',
        'ects': 12,
        'faecher': {
            'Haematologie und Haemostaseologie 2': {'key': 'pruefungen_haehae2', 'ects': ects_dict['Haematologie und Haemostaseologie 2']},
            'Histologie und Zytologie 1': {'key': 'pruefungen_histo1', 'ects': ects_dict['Histologie und Zytologie 1']},
            'Klinische Chemie und Immunologie 1': {'key': 'pruefungen_kcl1', 'ects': ects_dict['Klinische Chemie und Immunologie 1']},
            'Medizinische Mikrobiologie 2': {'key': 'pruefungen_memi2', 'ects': ects_dict['Medizinische Mikrobiologie 2']}}},
    'Wissenschaftliche Grundlagen 2': {
        'semester': 'Fruehlingssemester 1',
        'ects': 17,
        'faecher': {
            'Biologie 2': {'key': 'pruefungen_bio2', 'ects': ects_dict['Biologie 2']},
            'Chemie 2': {'key': 'pruefungen_che2', 'ects': ects_dict['Chemie 2']},
            'Informatik 2': {'key': 'pruefungen_inf2', 'ects': ects_dict['Informatik 2']},
            'Mathematik 2': {'key': 'pruefungen_mat2', 'ects': ects_dict['Mathematik 2']},
            'Physik': {'key': 'pruefungen_phy', 'ects': ects_dict['Physik']},
            'Englisch 2': {'key': 'pruefungen_eng2', 'ects': ects_dict['Englisch 2']},
            'Gesellschaftlicher Kontext und Sprache 2': {'key': 'pruefungen_gks2', 'ects': ects_dict['Gesellschaftlicher Kontext und Sprache 2']}}},
            
    'Analyseprozesse & Labordiagnostik 1':{
        'semester': 'Herbstsemester 2',
        'ects': 6,
        'faecher': {
            'Klinische Chemie und Immunologie 2': {'key': 'pruefungen_kcl2', 'ects': ects_dict['Klinische Chemie und Immunologie 2']},
            'Histologie und Zytologie 2': {'key': 'pruefungen_histo2', 'ects': ects_dict['Histologie und Zytologie 2']},
            'Immunhaematologie und Transfusionsmedizin 1': {'key': 'pruefungen_iht1', 'ects': ects_dict['Immunhaematologie und Transfusionsmedizin 1']}}},
    'Analyseprozesse & Labordiagnostik 2':{
        'semester': 'Herbstsemester 2',
        'ects': 11,
        'faecher': {
            'Herz-Kreislauf- und respiratorische Erkrankungen': {'key': 'pruefungen_hkr', 'ects': ects_dict['Herz-Kreislauf- und respiratorische Erkrankungen']},
            'Neoplasien und haematologische Erkrankungen': {'key': 'pruefungen_neopla', 'ects': ects_dict['Neoplasien und haematologische Erkrankungen']},
            'Selbst- und patientennahe Diagnostik': {'key': 'pruefungen_spd', 'ects': ects_dict['Selbst- und patientennahe Diagnostik']},
            'Hygiene und Epidemiologie': {'key': 'pruefungen_hyep', 'ects': ects_dict['Hygiene und Epidemiologie']}}},
    
    'Analyseprozesse & Labordiagnostik 3':{
        'semester': 'Fruehlingssemester 2',
        'ects': 10,
        'faecher': {
            'Immunhaematologie und Transfusionsmedizin 2': {'key': 'pruefungen_iht2', 'ects': ects_dict['Immunhaematologie und Transfusionsmedizin 2']},
            'Medizinische Genetik 1': {'key': 'pruefungen_gen1', 'ects': ects_dict['Medizinische Genetik 1']},
            'Bewegungsapparat und neurologische Erkrankungen': {'key': 'pruefungen_bene', 'ects': ects_dict['Bewegungsapparat und neurologische Erkrankungen']},
            'Endokrinologie, Stoffwechselerkrankungen': {'key': 'pruefungen_endo', 'ects': ects_dict['Endokrinologie, Stoffwechselerkrankungen']}}},

    'Analyseprozesse & Labordiagnostik 4':{
        'semester': 'Herbstsemester 3',
        'ects': 7,
        'faecher': {
            'Medizinische Genetik 2': {'key': 'pruefungen_gen2', 'ects': ects_dict['Medizinische Genetik 2']},
            'Urogenitale und gastrointestinale Erkrankungen': {'key': 'pruefungen_uro', 'ects': ects_dict['Urogenitale und gastrointestinale Erkrankungen']},
            'Entwicklungsstörungen und vererbbare Erkrankungen': {'key': 'pruefungen_entw', 'ects': ects_dict['Entwicklungsstörungen und vererbbare Erkrankungen']}}},                                                  
    'Kommunikation & Management 1': {
        'semester': 'Herbstsemester 3',
        'ects': 14,
        'faecher': {
            'Projekt-, Change- und Risikomanagement 1': {'key': 'pruefungen_pcr1', 'ects': ects_dict['Projekt-, Change- und Risikomanagement 1']},
            'Kommunikation 1': {'key': 'pruefungen_kom1', 'ects': ects_dict['Kommunikation 1']},
            'Evidenzbasiertes Handeln': {'key': 'pruefungen_ebh', 'ects': ects_dict['Evidenzbasiertes Handeln']},
            'Entwicklungen, Trends, Unternehmertum': {'key': 'pruefungen_etu', 'ects': ects_dict['Entwicklungen, Trends, Unternehmertum']},
            'Gesundheitsförderung und Praevention': {'key': 'pruefungen_gepr', 'ects': ects_dict['Gesundheitsförderung und Praevention']}}},
    'Angewandte Forschung': {
        'semester': 'Herbstsemester 3',
        'ects': 8,
        'faecher': {
            'Projektarbeit': {'key': 'pruefungen_proj', 'ects': ects_dict['Projektarbeit']},
            'Forschungsmethoden 1': {'key': 'pruefungen_fors1', 'ects': ects_dict['Forschungsmethoden 1']}}},
    'Gesellschaft, Kultur & Gesundheit':{
        'ects': 3},

    'Gesundheitssystem':{
        'semester': 'Fruehlingssemester 3',
        'ects': 6,
        'faecher': {
            'Klinische Pharmakologie und personalisierte Medizin': {'key': 'pruefungen_pharma', 'ects': ects_dict['Klinische Pharmakologie und personalisierte Medizin']},
            'Gesundheitssystem und Digital Health': {'key': 'pruefungen_gedh', 'ects': ects_dict['Gesundheitssystem und Digital Health']}}},
    'Kommunikation & Management 2': {
        'semester': 'Fruehlingssemester 3',
        'ects': 6,
        'faecher': {
            'Projekt-, Change- und Risikomanagement 2': {'key': 'pruefungen_pcr2', 'ects': ects_dict['Projekt-, Change- und Risikomanagement 2']},
            'Forschungsmethoden 2': {'key': 'pruefungen_fors2', 'ects': ects_dict['Forschungsmethoden 2']}}}
            }

modulgruppen_farben = {
    # Herbstsemester 1
    'Basiswissen BMLD 1': ["#1565c0", "#1976d2", "#42a5f5", "#90caf9"],  # Blautöne
    'Wissenschaftliche Grundlagen 1': ["#1b5e20", "#388e3c", "#66bb6a", "#a5d6a7"],  # Grüntöne
    'Sprache': ["#b71c1c", "#e57373"],  # Rottöne

    # Fruehlingssemester 1
    'Basiswissen BMLD 2': ["#1565c0", "#1976d2", "#42a5f5", "#90caf9"],  # Blautöne
    'Wissenschaftliche Grundlagen 2': ["#1b5e20", "#388e3c", "#66bb6a", "#a5d6a7", "#558b2f", "#9ccc65", "#c5e1a5"],  # Grüntöne

    # Herbstsemester 2
    'Analyseprozesse & Labordiagnostik 1': ["#1565c0", "#1976d2", "#42a5f5"],  # Blautöne
    'Analyseprozesse & Labordiagnostik 2': ["#1b5e20", "#388e3c", "#66bb6a", "#a5d6a7"],  # Grüntöne

    # Fruehlingssemester 2
    'Analyseprozesse & Labordiagnostik 3': ["#1565c0", "#1976d2", "#42a5f5", "#90caf9"],  # Blautöne

    # Herbstsemester 3
    'Analyseprozesse & Labordiagnostik 4': ["#1565c0", "#1976d2", "#42a5f5"],  # Blautöne
    'Kommunikation & Management 1': ["#1b5e20", "#388e3c", "#66bb6a", "#a5d6a7", "#558b2f"],  # Grüntöne
    'Angewandte Forschung': ["#b71c1c", "#e57373"],  # Rottöne

    # Fruehlingssemester 3
    'Gesundheitssystem': ["#1565c0", "#1976d2"],  # Blautöne
    'Kommunikation & Management 2': ["#1b5e20", "#388e3c"],  # Grüntöne
}

grundlagenpraktika_dict = {
    'Grundlagenpraktikum 1': {
        'semester': 'Herbstsemester 1',
        'ects': 3},
    'Grundlagenpraktikum 2': {
        'semester': 'Fruehlingssemester 1',
        'ects': 3},
    'Externes Praktikum Fachbereich A': {
        'semester': 'Herbstsemester 2',
        'ects': 11},
    'Externes Praktikum Fachbereich B': {
        'semester': 'Fruehlingssemester 2',
        'ects': 11},
    'Externes Praktikum Fachbereich C': {
        'semester': 'Herbstsemester 3',
        'ects': 9},
    'Praxisreflexion und interprofessionelles Handeln':{
        'semester': 'Fruehingssemester 3',
        'ects': 2},
        
    'Gesellschaft, Kultur & Gesundheit': {
        'ects': 3}}


def manage_pruefungen(fach_name, session_state_key, spalten
                      ):
    if "username" not in st.session_state:
        st.error("Kein Benutzer eingeloggt. Bitte melden Sie sich an.")
        return

    ects = ects_dict.get(fach_name)
    df_pruefungen = st.session_state["Pruefungen"]

    # Anzeigen der Pruefungsdaten
    if not df_pruefungen.empty:
        data = df_pruefungen[df_pruefungen['Modul'] == fach_name]
    
        col1, col2, col3, col4, col5 = st.columns([3, 2, 2, 2, 5])
        with col1:
            st.markdown("**Prüfung**")
        with col2:
            st.markdown("**Datum**")
        with col3:
            st.markdown("**Gewichtung**")
        with col4:
            st.markdown("**Note**")

        # Tabelle mit einem Löschen-Button fuer jede Zeile
        for idx, row in data.iterrows():
            col1, col2, col3, col4, col5 = st.columns([3, 2, 2, 2, 5])

            with col1:
                st.write(row["Pruefung"])
            with col2:
                st.write(row["Datum"])
            with col3:
                st.write(f"{row['Gewichtung']} %")
            with col4:
                st.write(row['Note'])
            with col5:
               if st.button(f'{row["Pruefung"]} löschen', key=f"delete_{df_pruefungen}_{idx}"):

                #Zeile aus Session-DataFrame löschen und Index zuruecksetzen
                    st.session_state["Pruefungen"] = st.session_state["Pruefungen"].drop(row.name).reset_index(drop=True)

                # Speichern
                    DataManager().save_data("Pruefungen")

                    st.rerun()

    else:
        col1, col2 = st.columns(2)
        with col1:
            st.write('**Maximale ECTS des Moduls**')
        with col2:
            st.write(ects)
        st.info('Noch keine Prüfungen eingetragen. Bitte eine Prüfung hinzufügen.')

    with st.form(key=f'{fach_name}_form'):
        col1, col2, col3, col4 = st.columns([1.2, 0.8, 1, 0.8])
        with col1:
            name = st.text_input('Prüfungsname')
        with col2:
            datum = st.date_input('Datum')
        with col3:
            gewichtung = st.number_input('Gewichtung in Prozent', min_value=1.0, max_value=100.0, step=1.0)
        with col4:
            note = round(st.number_input('Note', min_value=1.0, max_value=6.0, step=0.05), 2)

        submit_button = st.form_submit_button('Prüfung hinzufügen')

        if submit_button:
            fehler = []
            if not name.strip():
                fehler.append('Bitte einen Namen für die Prüfung eingeben.')
            # Überprüfen, ob die Spalte "Gewichtung" existiert und der DataFrame nicht leer ist
            if "Gewichtung" in df_pruefungen.columns and not df_pruefungen.empty:
                gesamt_gewichtung = data['Gewichtung'].sum() + gewichtung
            else:
                gesamt_gewichtung = gewichtung # Nur die neue Gewichtung verwenden, wenn keine Daten vorhanden sind
            if gesamt_gewichtung > 100:
                fehler.append('Die Gesamtgewichtung der Prüfungen darf 100% nicht überschreiten.')
            if gewichtung <= 0:
                fehler.append('Die Gewichtung muss größer als 0 sein.')
            if gewichtung > 100:
                fehler.append('Die Gewichtung darf nicht grösser als 100 sein.')
            if note < 1 or note > 6:
                fehler.append('Die Note muss zwischen 1.0 und 6.0 liegen.')
            
            if fehler:
                for msg in fehler:
                    st.error(msg)
            else:
                result_dict = {
                    "username": st.session_state["username"],
                    "semester": st.session_state["semester"],
                    "Modul": fach_name,
                    "Pruefung": name,
                    "Datum": datum,
                    "Gewichtung": gewichtung,
                    "Note": note,
                    "timestamp": pd.Timestamp.now()
                    }
                
                DataManager().append_record(session_state_key='Pruefungen', record_dict=result_dict)
                
                #Hinzufügen eines Flags für erfolgreiches Hinzufuegen, damit der Plathalter angezeigt werden kann
                st.session_state[f'{session_state_key}_added'] = True

                st.rerun()

                    
        flag_key = f'{session_state_key}_erfolgreich_hinzugefuegt'
        
        if flag_key in st.session_state and st.session_state[flag_key]:
            platzhalter = st.empty()
            platzhalter.success('Prüfung erfolgreich hinzugefügt!')                
            time.sleep(3)
            platzhalter.empty()   
            del st.session_state[flag_key]


def schnitt_modul_berechnen(fach_name):
    if 'username' not in st.session_state:
        st.error("Kein Benutzer eingeloggt. Bitte melden Sie sich an.")
        return

    st.subheader(fach_name)

    aktuelles_semester = st.session_state['semester']
    ects = ects_dict.get(fach_name)

    df_pruefungen = st.session_state['Pruefungen']
    df_modulschnitt = df_pruefungen[
        (df_pruefungen['Modul'] == fach_name) &
        (df_pruefungen['semester'] == aktuelles_semester)
    ]
    
    if not df_modulschnitt.empty:
        aktuelle_gesamt_gewichtung = df_modulschnitt['Gewichtung'].sum()
        schnitt_modul = (df_modulschnitt['Note'] * df_modulschnitt['Gewichtung']).sum() / aktuelle_gesamt_gewichtung if aktuelle_gesamt_gewichtung > 0 else None
        farbe = 'green' if schnitt_modul is not None and schnitt_modul >= 4 else 'red'
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Notendurchschnitt des Moduls**")
            if schnitt_modul is not None:
                st.markdown(f"**Ø** <span style='color:{farbe}'>{schnitt_modul:.2f}</span>", unsafe_allow_html=True)
            else:
                st.markdown("<span style='color:gray'>-</span>", unsafe_allow_html=True)
        with col2:
            st.markdown("**erreichte ECTS**")
            if aktuelle_gesamt_gewichtung == 100 and schnitt_modul is not None:
                erreichte_ects = ects if schnitt_modul >= 4 else 0
                ects_farbe = 'green' if erreichte_ects > 0 else 'red'
                st.markdown(
                    f"<span style='color:{ects_farbe}'><strong>{erreichte_ects} / {ects}</strong></span>",
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    f"<span style='color:gray'><strong>0 / {ects}</strong></span>",
                    unsafe_allow_html=True
                )
        if aktuelle_gesamt_gewichtung < 0:
            st.info('Die Gewichtung der Prüfungen ist kleiner als 0%. Bitte Prüfungen erfassen.')
    else:
        col1, col2 = st.columns(2)
        with col1:
            st.write('**Maximale ECTS des Moduls**')
        with col2:
            st.write(ects)
        st.info("Noch keine gültigen Noten vorhanden.")


def schnitt_modulgruppe_berechnen(modulgruppe):
    # Prüfen, ob ein Benutzer eingeloggt ist
    if 'username' not in st.session_state:
        st.error("Kein Benutzer eingeloggt. Bitte melden Sie sich an.")
        return

    st.header(modulgruppe)  # Titel anzeigen

    aktuelles_semester = st.session_state['semester']
    df_pruefungen = st.session_state['Pruefungen']
    
    # Modulgruppen-Daten abrufen
    gruppe = modulgruppen.get(modulgruppe)
    if not gruppe or 'faecher' not in gruppe:
        st.info("Keine Fächer in dieser Modulgruppe hinterlegt.")
        return

    faecher = gruppe['faecher']
    gesamt_gewichtete_note = 0
    gesamt_gewichtete_ects = 0
    gesamt_ects = 0

    module_vollstaendig = []
    module_ects = {}
    module_schnitte = {}

    # Über alle Fächer der Modulgruppe iterieren
    for fach_name, infos in faecher.items():
        key = infos['key']
        ects = infos['ects']
        gesamt_ects += ects

        df_fach = df_pruefungen[
            (df_pruefungen['Modul'] == fach_name) & 
            (df_pruefungen['semester'] == aktuelles_semester)
        ]

        if not df_fach.empty:
            gesamt_gewichtung = df_fach['Gewichtung'].sum()
            if gesamt_gewichtung == 100:
                schnitt = (df_fach['Note'] * df_fach['Gewichtung']).sum() / gesamt_gewichtung
                module_vollstaendig.append(fach_name)
                module_schnitte[fach_name] = schnitt
                module_ects[fach_name] = ects
                # Für Gruppenschnitt
                gesamt_gewichtete_note += schnitt * ects
                gesamt_gewichtete_ects += ects

    alle_module_vollstaendig = len(module_vollstaendig) == len(faecher)
    modulgruppe_schnitt = (gesamt_gewichtete_note / gesamt_gewichtete_ects) if gesamt_gewichtete_ects > 0 else None

    # ECTS-Anzeige-Logik
    ects_anzeigen = 0
    for fach_name in module_vollstaendig:
        schnitt = module_schnitte[fach_name]
        if schnitt >= 4.0:
            ects_anzeigen += module_ects[fach_name]
        elif alle_module_vollstaendig and modulgruppe_schnitt is not None and modulgruppe_schnitt >= 4.0:
            ects_anzeigen += module_ects[fach_name]
        # sonst keine ECTS für dieses Modul

    # Farblogik für Darstellung
    farbe = 'green' if modulgruppe_schnitt is not None and modulgruppe_schnitt >= 4 else 'red'
    if modulgruppe_schnitt is None:
        ects_farbe = 'gray'
    else:
        ects_farbe = 'green' if ects_anzeigen > 0 else 'red'

    # Darstellung in zwei Spalten
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**Notendurchschnitt der Modulgruppe**")
        if modulgruppe_schnitt is not None:
            st.markdown(
                f"<span style='font-size:1.5em; color:{farbe}; font-weight:bold;'>Ø {modulgruppe_schnitt:.2f}</span>",
                unsafe_allow_html=True
            )
        else:
            st.markdown("<span style='font-size:1.5em; color:gray; font-weight:bold;'>-</span>", unsafe_allow_html=True)
    with col2:
        st.markdown("**Erreichte ECTS**")
        st.markdown(
            f"<span style='font-size:1.5em; color:{ects_farbe}; font-weight:bold;'>{ects_anzeigen} / {gesamt_ects}</span>",
            unsafe_allow_html=True
        )
    with col3:
        if ects_anzeigen == 0:
            st.markdown("&nbsp;") # leerer Platzhalter
            st.markdown(
                f"<span style='font-size:1.0em; color:gray; font-weight:bold; '>Verfügbar, wenn für mind. ein Modul alle Prüfungen erfasst wurden.</span>",
                unsafe_allow_html=True
            )
    


def semesterschnitt_berechnen(semester):
    df_pruefungen = st.session_state['Pruefungen']

    gesamtgewichtete_note = 0
    gesamtsumme_ects = 0

    for modulgruppe_name, gruppe in modulgruppen.items():
        if gruppe.get('semester') != semester:
            continue

        faecher = gruppe.get('faecher')
        if not faecher:
            continue

        max_ects = gruppe.get('ects', 0)

        # Berechne gewichteten Schnitt der Modulgruppe
        noten = []
        gewichtungen = []
        for fach_name, infos in faecher.items():
            df_modul = df_pruefungen[
                (df_pruefungen['Modul'] == fach_name) &
                (df_pruefungen['semester'] == semester)
            ]
            if not df_modul.empty:
                gewichtung_summe = df_modul['Gewichtung'].sum()
                if gewichtung_summe > 0:
                    schnitt = (df_modul['Note'] * df_modul['Gewichtung']).sum() / gewichtung_summe
                    noten.append(schnitt)
                    gewichtungen.append(infos.get('ects', 0))
        # Modulgruppen-Schnitt berechnen (nur wenn Noten vorhanden)
        if noten and gewichtungen and sum(gewichtungen) > 0:
            modulgruppen_schnitt = sum([n * e for n, e in zip(noten, gewichtungen)]) / sum(gewichtungen)
            gesamtgewichtete_note += modulgruppen_schnitt * max_ects
            gesamtsumme_ects += max_ects
        # Falls keine Noten vorhanden, ignoriere die Modulgruppe

    if gesamtsumme_ects > 0:
        semesterschnitt = round(gesamtgewichtete_note / gesamtsumme_ects, 2)
        return semesterschnitt
    else:
        return None


def bestes_modul_anzeigen(semester):
    df_pruefungen = st.session_state['Pruefungen']
    df_semester = df_pruefungen[df_pruefungen['semester'] == semester]

    if df_semester.empty:
        return None, None
    gruppieren = df_semester.groupby('Modul').apply(
        lambda x: (x['Note'] * x['Gewichtung']).sum() / x['Gewichtung'].sum())
    bestes_modul = gruppieren.idxmax()
    beste_note = round(gruppieren.max(), 2)
    return(bestes_modul, beste_note)


def noten_verteilung(semester):
    df_pruefungen = st.session_state['Pruefungen']
    df_semester = df_pruefungen[df_pruefungen['semester'] == semester]

    if df_semester.empty:
        st.info("Keine Notendaten für dieses Semester vorhanden.")
        return

    # Noten in 0.5er-Bins einsortieren
    bins = np.arange(1.0, 6.5, 0.5)
    bereiche = [f"{bins[i]:.1f}–{bins[i+1]:.1f}" for i in range(len(bins)-1)]
    df_semester['Notenklasse'] = pd.cut(df_semester['Note'], bins=bins, labels=bereiche, include_lowest=True, right=False)

    # Gruppiere nach Notenklasse und Modul
    grouped = df_semester.groupby(['Notenklasse', 'Modul'])['Note'].agg([
        ('Anzahl', 'count'),
        ('Tatsaechliche_Noten', lambda x: ', '.join(f"{n:.2f}" for n in sorted(x)))
    ]).reset_index()

    # Alle Kombinationen von Notenklasse und Modul sicherstellen (auch 0en)
    alle_modul = df_semester['Modul'].unique()
    alle_kombis = pd.MultiIndex.from_product([bereiche, alle_modul], names=['Notenklasse', 'Modul'])
    grouped = grouped.set_index(['Notenklasse', 'Modul']).reindex(alle_kombis, fill_value=0).reset_index()

    # --- Farben zuordnen ---
    # Mapping Modulname -> Farbe anhand der Modulgruppe
    modul_farbe = {}
    for gruppenname, gruppe in modulgruppen.items():
        if gruppe.get('semester') == semester:
            faecher = list(gruppe.get('faecher', {}).keys())
            farben = modulgruppen_farben.get(gruppenname, [])
            for i, fach in enumerate(faecher):
                if i < len(farben):
                    modul_farbe[fach] = farben[i]

    # Füge das Feld für die Legende hinzu
    grouped["Modul_Legende"] = grouped["Modul"]

    import altair as alt
    chart = alt.Chart(grouped).mark_bar().encode(
        x=alt.X('Notenklasse:O', title="Note", sort=bereiche),
        y=alt.Y('Anzahl:Q', title="Anzahl Noten", axis=alt.Axis(format='d')),
        color=alt.Color(
            'Modul_Legende:N',
            scale=alt.Scale(domain=list(modul_farbe.keys()), range=list(modul_farbe.values())),
            legend=alt.Legend(title="Modul")
        ),
        tooltip=['Notenklasse', 'Modul', 'Anzahl', alt.Tooltip('Tatsaechliche_Noten:N', title='Tatsächliche Noten')],
    ).properties(
        title="📊 Notenverteilung (in 0.5er-Schritten)",
        width=600,
        height=400
    )

    with st.container(border=True):
        st.altair_chart(chart, use_container_width=True)
        


    

def grundlagenpraktikum(grundlagenpraktika, grundlagenpraktika_name):
    if "username" not in st.session_state:
        st.error("Kein Benutzer eingeloggt. Bitte melden Sie sich an.")
        return

    ects = grundlagenpraktika_dict.get(grundlagenpraktika_name, {}).get('ects')   # Holen der Anzahl-ECTS aus dem 'grundlagenpraktika_dict'
    df_grundlagenpraktika = st.session_state["Grundlagenpraktika"] # vollständiger DataFrame

    st.subheader(grundlagenpraktika_name)
    
    if not df_grundlagenpraktika.empty:
         
        # Filtere den DataFrame für das angegebene Praktikum
        df_grundlagenpraktika = df_grundlagenpraktika[df_grundlagenpraktika['Modul'] == grundlagenpraktika_name] # Gefilterter DataFrame für das angegebene Praktikum
        
        # Der passende Eintrag (aktuelle Status und Index)
        aktueller_status = df_grundlagenpraktika.iloc[0]['Status']
        index = df_grundlagenpraktika.index[0]

        # Funktion, die beim Aendern des Radio-Status ausgeführt wird
        def update_status():
            neuer_status = st.session_state.get(f"{grundlagenpraktika_name}_status", aktueller_status)  # aktueller Status aus Session State
            timestamp = pd.Timestamp.now()

            # Überschreibe den bestehenden Eintrag im DataFrame im Session-State
            st.session_state["Grundlagenpraktika"].loc[index, 'Status'] = neuer_status
            st.session_state["Grundlagenpraktika"].loc[index, 'timestamp'] = timestamp
            
            # Aenderungen im CSV-File speichern
            data_manager.save_data(session_state_key="Grundlagenpraktika")

    
        # Radio-Box mit vorausgewähltem aktuellem Status, mit on-change-Callback
        status = st.radio(
            '**Bestanden?**',
            ["Ja", "Nein"],
            index=0 if aktueller_status == "Ja" else 1,
            key=f"{grundlagenpraktika_name}_status",
            on_change = update_status # Wird automatisch aufgerufen, wenn der Wert sich aendert
        )
    
########## Feedback je nach Status
        if status == "Ja":
            st.success(f"{grundlagenpraktika_name} bestanden (+ {ects} ECTS)")
        else:
            st.error(f"{grundlagenpraktika_name} nicht bestanden (0 von {ects} ECTS)")

    else: 
        # neuen Eintrag erstellen, wenn noch keiner existiert
        neuer_eintrag = {
        "username": st.session_state["username"],
        "semester": st.session_state["semester"],
        "Modul": grundlagenpraktika_name,
        "Status": "Nein", 
        "timestamp": pd.Timestamp.now()
        }

        DataManager().append_record(session_state_key='Grundlagenpraktika', record_dict=neuer_eintrag)
        st.rerun()

    #else:
     #   st.session_state["Grundlagenpraktika"] = {
      #      "status": "Nein",
       #     "ects": 0
        #}
    
        # Feedback anzeigen
        #if status == "Ja":
         #   st.success(f"{grundlagenpraktika_name} bestanden (+{grundlagenpraktikum['ects']} ECTS)")
        #else:
         #   st.error(f"{grundlagenpraktika_name} nicht bestanden (0 von {grundlagenpraktikum['ects']} ECTS)")


