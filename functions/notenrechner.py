import streamlit as st
import pandas as pd
import time
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
        'semester': 'Fruehlingssemester 2',
        'ects': 9},
    'Praxisreflexion und interprofessionelles Handeln':{
        'semester': 'Fruehingssemester 2',
        'ects': 2},
        
    'Gesellschaft, Kultur & Gesundheit': {
        'semester': 'Herbstsemester 3',
        'ects': 3}}


def manage_pruefungen(fach_name, session_state_key):
    # Prüfen, ob ein Benutzer eingeloggt ist
    if "username" not in st.session_state:
        st.error("Kein Benutzer eingeloggt. Bitte melden Sie sich an.")
        return

    # ECTS für das aktuelle Fach holen
    ects = ects_dict.get(fach_name)
    # Den DataFrame mit den gespeicherten Prüfungen aus dem Session State holen
    df_pruefungen = st.session_state["Pruefungen"]

    # Wenn bereits Prüfungsdaten existieren, zeige sie an
    if not df_pruefungen.empty:
        # Filter für das aktuelle Fach
        data = df_pruefungen[df_pruefungen['Modul'] == fach_name]

        # Spalten für die Anzeige der Prüfungen definieren
        col1, col2, col3, col4, col5 = st.columns([3, 2, 2, 2, 5])
        with col1:
            st.markdown("**Prüfung**")
        with col2:
            st.markdown("**Datum**")
        with col3:
            st.markdown("**Gewichtung**")
        with col4:
            st.markdown("**Note**")

        #Ausrichtung des Löschen-Buttons auf der gleichen Zeile, wie die Prüfung selbst
        st.markdown(""" 
            <style>
            div[data-testid="stButton"] button {
                margin-top: -8px !important;
                margin-bottom: 0px !important;
                padding-top: 4px !important;
                padding-bottom: 4px !important;
            }
            </style>
        """, unsafe_allow_html=True)

        # Jede vorhandene Prüfung als Zeile anzeigen, inkl. Lösch-Button
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
                # Lösch-Button für diese Prüfungszeile
                if st.button(f'{row["Pruefung"]} löschen', key=f"delete_{df_pruefungen}_{idx}"):
                    # Zeile aus dem DataFrame löschen und Index neu setzen
                    st.session_state["Pruefungen"] = st.session_state["Pruefungen"].drop(row.name).reset_index(drop=True)
                    # Änderungen in der Datei speichern
                    DataManager().save_data("Pruefungen")
                    # Seite neuladen, damit die Löschung sichtbar wird
                    st.rerun()

    # Formular zum Hinzufügen einer neuen Prüfung
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

        # Button zum Speichern der Prüfung
        submit_button = st.form_submit_button('Prüfung hinzufügen')

        if submit_button:
            fehler = []  # Liste zur Sammlung von Fehlern

            # Validierung: Prüfungsname muss angegeben sein
            if not name.strip():
                fehler.append('Bitte einen Namen für die Prüfung eingeben.')

            # Gewichtung prüfen, damit sie 100% nicht übersteigt
            if "Gewichtung" in df_pruefungen.columns and not df_pruefungen.empty:
                gesamt_gewichtung = data['Gewichtung'].sum() + gewichtung
            else:
                gesamt_gewichtung = gewichtung  # Nur die neue Gewichtung zählen, wenn vorher nichts da ist

            if gesamt_gewichtung > 100:
                fehler.append('Die Gesamtgewichtung der Prüfungen darf 100% nicht überschreiten.')
            if gewichtung <= 0:
                fehler.append('Die Gewichtung muss größer als 0 sein.')
            if gewichtung > 100:
                fehler.append('Die Gewichtung darf nicht grösser als 100 sein.')
            if note < 1 or note > 6:
                fehler.append('Die Note muss zwischen 1.0 und 6.0 liegen.')

            # Falls es Validierungsfehler gibt, zeige sie an
            if fehler:
                for msg in fehler:
                    st.error(msg)
            else:
                # Prüfung ist valide → Dictionary zum Speichern vorbereiten
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

                # Datensatz zur Session speichern und persistieren
                DataManager().append_record(session_state_key='Pruefungen', record_dict=result_dict)

                # Flag setzen, um Erfolgsmeldung anzuzeigen
                st.session_state[f'{session_state_key}_added'] = True

                # Seite neuladen
                st.rerun()

        # Erfolgsmeldung anzeigen, wenn Flag gesetzt ist
        flag_key = f'{session_state_key}_added'
        if flag_key in st.session_state and st.session_state[flag_key]:
            platzhalter = st.empty()
            platzhalter.success('Prüfung erfolgreich hinzugefügt!')
            time.sleep(3)  # Erfolgsmeldung 3 Sekunden anzeigen
            platzhalter.empty()
            del st.session_state[flag_key]  # Flag wieder löschen



def schnitt_modul_berechnen(fach_name):
    # Sicherstellen, dass ein Benutzer eingeloggt ist
    if 'username' not in st.session_state:
        st.error("Kein Benutzer eingeloggt. Bitte melden Sie sich an.")
        return

    # Modulüberschrift anzeigen
    st.subheader(fach_name)

    # Aktuelles Semester und ECTS des Fachs abrufen
    aktuelles_semester = st.session_state['semester']
    ects = ects_dict.get(fach_name)

    # Alle gespeicherten Prüfungen laden
    df_pruefungen = st.session_state['Pruefungen']

    # Nur die Prüfungen des aktuellen Moduls und Semesters filtern
    df_modulschnitt = df_pruefungen[
        (df_pruefungen['Modul'] == fach_name) &
        (df_pruefungen['semester'] == aktuelles_semester)
    ]
    
    # Wenn es zu diesem Modul bereits Prüfungen gibt
    if not df_modulschnitt.empty:
        # Gesamtgewichtung der erfassten Prüfungen berechnen
        aktuelle_gesamt_gewichtung = df_modulschnitt['Gewichtung'].sum()

        # Notendurchschnitt berechnen (gewichtetes Mittel)
        schnitt_modul = (
            (df_modulschnitt['Note'] * df_modulschnitt['Gewichtung']).sum() / 
            aktuelle_gesamt_gewichtung
        ) if aktuelle_gesamt_gewichtung > 0 else None

        # Farbe je nach Bestehen (grün = bestanden, rot = nicht bestanden)
        farbe = 'green' if schnitt_modul is not None and schnitt_modul >= 4 else 'red'

        # Drei Spalten zur Darstellung von Durchschnitt, ECTS, Info
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("**Notendurchschnitt des Moduls**")
            if schnitt_modul is not None:
                # Durchschnitt in Farbe darstellen
                st.markdown(f"<span style='color:{farbe}; font-size:1.2em; font-weight:bold'>Ø {schnitt_modul:.2f}</span>", unsafe_allow_html=True)
            else:
                # Kein Schnitt vorhanden
                st.markdown("<span style='color:gray'>-</span>", unsafe_allow_html=True)

        with col2:
            st.markdown("**erreichte ECTS**")
            # Nur anzeigen, wenn alle Prüfungen vorhanden sind (Gewichtung = 100)
            if aktuelle_gesamt_gewichtung == 100 and schnitt_modul is not None:
                erreichte_ects = ects if schnitt_modul >= 4 else 0
                ects_farbe = 'green' if erreichte_ects > 0 else 'red'
                st.markdown(
                    f"<span style='color:{ects_farbe}; font-size:1.2em; font-weight:bold;'>{erreichte_ects} / {ects}</span>",
                    unsafe_allow_html=True
                )
            else:
                # Noch keine vollständige Bewertung
                st.markdown(
                    f"<span style='color:gray; font-size:1.2em; font-weight:bold;'>0 / {ects}</span>",
                    unsafe_allow_html=True
                )

        with col3:
            # Hinweis, dass noch nicht alle Prüfungen erfasst wurden
            if aktuelle_gesamt_gewichtung != 100 or schnitt_modul is None:
                st.markdown("&nbsp;")  # Leerzeile zur Formatierung
                st.markdown(
                    f"<span style='color:gray'><strong>ECTS verfügbar, wenn alle Prüfungen dieses Moduls erfasst wurden.</strong></span>",
                    unsafe_allow_html=True
                )
            else:
                # Wenn alles vollständig, leer lassen
                st.markdown("&nbsp;")

        # Zusätzliche Info, falls Gewichtung aus unerklärlichem Grund < 0 ist
        if aktuelle_gesamt_gewichtung < 0:
            st.info('Die Gewichtung der Prüfungen ist kleiner als 0%. Bitte Prüfungen erfassen.')

    else:
        # Falls noch keine Prüfungen vorhanden sind, Hinweis anzeigen
        col1, col2 = st.columns(2)
        with col1:
            st.write('**Maximale ECTS des Moduls**')
        with col2:
            st.write(ects)
        st.info("Noch keine gültigen Noten vorhanden. Bitte eine Prüfung hinzufügen.")



def schnitt_modulgruppe_berechnen(modulgruppe):
    # Prüfen, ob ein Benutzer eingeloggt ist
    if 'username' not in st.session_state:
        st.error("Kein Benutzer eingeloggt. Bitte melden Sie sich an.")
        return

    # Überschrift mit dem Namen der Modulgruppe anzeigen
    st.header(modulgruppe)

    # Aktuelles Semester und gespeicherte Prüfungen laden
    aktuelles_semester = st.session_state['semester']
    df_pruefungen = st.session_state['Pruefungen']
    
    # Abrufen der Konfigurationsdaten zur Modulgruppe
    gruppe = modulgruppen.get(modulgruppe)
    if not gruppe or 'faecher' not in gruppe:
        st.info("Keine Fächer in dieser Modulgruppe hinterlegt.")
        return

    faecher = gruppe['faecher']  # Alle Fächer der Modulgruppe
    gesamt_gewichtete_note = 0  
    gesamt_gewichtete_ects = 0  
    gesamt_ects = 0  # Gesamte ECTS der Modulgruppe

    # Zwischenspeicher
    module_vollstaendig = []  # Module mit vollständig erfassten Prüfungen
    module_ects = {}          # ECTS pro Modul
    module_schnitte = {}      # Durchschnittsnoten pro Modul

    # Iteration über alle Fächer der Modulgruppe
    for fach_name, infos in faecher.items():
        ects = infos['ects']
        gesamt_ects += ects  # Gesamte ECTS der Gruppe summieren

        # Alle Prüfungen für das Fach im aktuellen Semester filtern
        df_fach = df_pruefungen[
            (df_pruefungen['Modul'] == fach_name) & 
            (df_pruefungen['semester'] == aktuelles_semester)
        ]

        # Wenn für das Fach bereits Prüfungen existieren
        if not df_fach.empty:
            gesamt_gewichtung = df_fach['Gewichtung'].sum()
            if gesamt_gewichtung == 100:
                # Notendurchschnitt (gewichtetes Mittel) berechnen
                schnitt = (df_fach['Note'] * df_fach['Gewichtung']).sum() / gesamt_gewichtung
                
                # Modul als vollständig erfassen
                module_vollstaendig.append(fach_name)
                module_schnitte[fach_name] = schnitt
                module_ects[fach_name] = ects

                # Für die Gesamtnote der Modulgruppe aufsummieren
                gesamt_gewichtete_note += schnitt * ects
                gesamt_gewichtete_ects += ects

    # Prüfen, ob alle Module vollständig sind
    alle_module_vollstaendig = len(module_vollstaendig) == len(faecher)

    # Gesamtschnitt der Modulgruppe berechnen (gewichteter Durchschnitt)
    modulgruppe_schnitt = (
        gesamt_gewichtete_note / gesamt_gewichtete_ects
    ) if gesamt_gewichtete_ects > 0 else None

    # Berechnung der erreichten ECTS in der Modulgruppe
    ects_anzeigen = 0
    for fach_name in module_vollstaendig:
        schnitt = module_schnitte[fach_name]
        
        if schnitt >= 4.0:
            # Wenn Modul bestanden, ECTS zählen
            ects_anzeigen += module_ects[fach_name]
        elif alle_module_vollstaendig and modulgruppe_schnitt is not None and modulgruppe_schnitt >= 4.0:
            # Wenn alle Module vollständig, aber einzelne knapp nicht bestanden, zählt die Gruppennote (Kulanzregel)
            ects_anzeigen += module_ects[fach_name]
            # Sonst: keine ECTS für dieses Modul

    # Farbe der Anzeige abhängig vom Ergebnis
    farbe = 'green' if modulgruppe_schnitt is not None and modulgruppe_schnitt >= 4 else 'red'
    ects_farbe = 'gray' if modulgruppe_schnitt is None else ('green' if ects_anzeigen > 0 else 'red')

    # Darstellung der Ergebnisse in drei Spalten
    col1, col2, col3 = st.columns(3)

    with col1:
        # Durchschnitt der Modulgruppe anzeigen
        st.markdown("**Notendurchschnitt der Modulgruppe**")
        if modulgruppe_schnitt is not None:
            st.markdown(
                f"<span style='font-size:1.5em; color:{farbe}; font-weight:bold;'>Ø {modulgruppe_schnitt:.2f}</span>",
                unsafe_allow_html=True
            )
        else:
            # Noch kein Schnitt vorhanden
            st.markdown("<span style='font-size:1.5em; color:gray; font-weight:bold;'>-</span>", unsafe_allow_html=True)

    with col2:
        # Erreichte ECTS anzeigen
        st.markdown("**Erreichte ECTS**")
        st.markdown(
            f"<span style='font-size:1.5em; color:{ects_farbe}; font-weight:bold;'>{ects_anzeigen} / {gesamt_ects}</span>",
            unsafe_allow_html=True
        )

    with col3:
        # Hinweis anzeigen, wenn keine ECTS erreicht wurden
        if ects_anzeigen == 0:
            st.markdown("&nbsp;")  # Leerzeile
            st.markdown(
                f"<span style='font-size:1.0em; color:gray; font-weight:bold;'>Verfügbar, wenn für mind. ein Modul alle Prüfungen erfasst wurden.</span>",
                unsafe_allow_html=True
            )


def semesterschnitt_berechnen(semester):
    # DataFrame mit Prüfungen aus dem Session-State laden
    df_pruefungen = st.session_state['Pruefungen']

    # Initialisierung von Variablen für die gewichtete Notensumme und die Summe der ECTS
    gesamtgewichtete_note = 0
    gesamtsumme_ects = 0

    # Über alle Modulgruppen iterieren, die im globalen dict 'modulgruppen' definiert sind
    for modulgruppe_name, gruppe in modulgruppen.items():
        # Nur Modulgruppen berücksichtigen, die zum gewünschten Semester gehören
        if gruppe.get('semester') != semester:
            continue

        # Fächer (Module) der Modulgruppe auslesen
        faecher = gruppe.get('faecher')
        if not faecher:
            # Wenn keine Fächer definiert sind, Modulgruppe überspringen
            continue

        # Maximale ECTS-Punkte der gesamten Modulgruppe abfragen
        max_ects = gruppe.get('ects', 0)

        # Listen zum Sammeln der Noten und der jeweiligen ECTS-Gewichtungen
        noten = []
        gewichtungen = []

        # Für jedes Fach/Modul in der Modulgruppe
        for fach_name, infos in faecher.items():
            # Prüfungsdaten filtern nach aktuellem Fach und Semester
            df_modul = df_pruefungen[
                (df_pruefungen['Modul'] == fach_name) &
                (df_pruefungen['semester'] == semester)
            ]

            if not df_modul.empty:
                # Summe der Gewichtungen (Prozent) der einzelnen Prüfungen im Fach berechnen
                gewichtung_summe = df_modul['Gewichtung'].sum()

                # Nur berechnen, wenn Gewichtung > 0 (d.h. gültige Prüfungen vorhanden)
                if gewichtung_summe > 0:
                    # Gewichteter Notendurchschnitt für das Fach berechnen
                    schnitt = (df_modul['Note'] * df_modul['Gewichtung']).sum() / gewichtung_summe
                    noten.append(schnitt)  # Note hinzufügen
                    gewichtungen.append(infos.get('ects', 0))  # ECTS als Gewichtung hinzufügen

        # Wenn Noten und Gewichtungen vorhanden sind, berechne den gewichteten Modulgruppen-Schnitt
        if noten and gewichtungen and sum(gewichtungen) > 0:
            modulgruppen_schnitt = sum([n * e for n, e in zip(noten, gewichtungen)]) / sum(gewichtungen)

            # Zur Gesamtnote des Semesters addieren, gewichtet mit der ECTS-Gesamtzahl der Modulgruppe
            gesamtgewichtete_note += modulgruppen_schnitt * max_ects

            # ECTS-Summe für das Semester aktualisieren
            gesamtsumme_ects += max_ects

        # Wenn keine Noten vorhanden, wird die Modulgruppe ignoriert

    # Am Ende: Falls Gesamt-ECTS > 0, berechne den Semesterschnitt als gewichteten Durchschnitt
    if gesamtsumme_ects > 0:
        semesterschnitt = round(gesamtgewichtete_note / gesamtsumme_ects, 2)
        return semesterschnitt
    else:
        # Wenn keine ECTS gesammelt wurden (keine Noten), gib None zurück
        return None


def bestes_modul_anzeigen(semester):
    # Lade alle Prüfungen aus dem Session-State
    df_pruefungen = st.session_state['Pruefungen']
    # Filtere die Prüfungen für das angegebene Semester
    df_semester = df_pruefungen[df_pruefungen['semester'] == semester]

    # Wenn es keine Prüfungen in diesem Semester gibt, gib None zurück
    if df_semester.empty:
        return None, None

    # Gruppiere die Daten nach 'Modul' und berechne für jede Gruppe den gewichteten Notendurchschnitt
    gruppieren = df_semester.groupby('Modul').apply(
        lambda x: (x['Note'] * x['Gewichtung']).sum() / x['Gewichtung'].sum())

    # Bestimme das Modul mit dem besten (höchsten) Durchschnitt
    bestes_modul = gruppieren.idxmax()

    # Rundet die beste Note auf zwei Nachkommastellen
    beste_note = round(gruppieren.max(), 2)

    # Rückgabe des besten Moduls und der besten Note
    return(bestes_modul, beste_note)


def noten_verteilung(semester):
    # Lade alle Prüfungen aus dem Session-State
    df_pruefungen = st.session_state['Pruefungen']
    # Filtere die Prüfungen für das angegebene Semester
    df_semester = df_pruefungen[df_pruefungen['semester'] == semester]

    # Falls keine Notendaten vorhanden sind, Info ausgeben und Funktion beenden
    if df_semester.empty:
        st.info("Keine Notendaten für dieses Semester vorhanden.")
        return

    # Definiere Notenklassen (Bins) in 0.5er Schritten von 1.0 bis 6.0
    bins = np.arange(1.0, 6.5, 0.5)

    # Erstelle Beschriftungen für diese Bins (z.B. "1.0–1.5", "1.5–2.0", ...)
    bereiche = [f"{bins[i]:.1f}–{bins[i+1]:.1f}" for i in range(len(bins)-1)]

    # Weise jeder Note eine Notenklasse zu, abhängig davon, in welchen Bin sie fällt
    df_semester['Notenklasse'] = pd.cut(
    df_semester['Note'],
    bins=bins,
    labels=bereiche,
    include_lowest=True,
    right=True
    )
    
    # Gruppiere nach Notenklasse und Modul und berechne:
    # - Anzahl der Noten in der jeweiligen Klasse
    # - Tatsächliche Noten als sortierte Liste als String (für Tooltip)
    grouped = df_semester.groupby(['Notenklasse', 'Modul'])['Note'].agg([
        ('Anzahl', 'count'),
        ('Tatsaechliche_Noten', lambda x: ', '.join(f"{n:.2f}" for n in sorted(x)))
    ]).reset_index()

    # Erzeuge alle möglichen Kombinationen von Notenklasse und Modul (auch wenn keine Noten vorhanden sind)
    alle_modul = df_semester['Modul'].unique()
    alle_kombis = pd.MultiIndex.from_product([bereiche, alle_modul], names=['Notenklasse', 'Modul'])

    # Setze den Index auf Notenklasse und Modul und ergänze fehlende Kombinationen mit 0
    grouped = grouped.set_index(['Notenklasse', 'Modul']).reindex(alle_kombis, fill_value=0).reset_index()

    # --- Farben für Module zuordnen ---
    modul_farbe = {}
    for gruppenname, gruppe in modulgruppen.items():
        # Nur Modulgruppen für das aktuelle Semester verwenden
        if gruppe.get('semester') == semester:
            faecher = list(gruppe.get('faecher', {}).keys())
            farben = modulgruppen_farben.get(gruppenname, [])
            # Jedem Fach der Gruppe eine Farbe zuordnen
            for i, fach in enumerate(faecher):
                if i < len(farben):
                    modul_farbe[fach] = farben[i]
    # ...vor Altair-Chart...

    # Ergänze Farben für Module, die im DataFrame vorkommen, aber nicht im modul_farbe dict sind
    for fach in alle_modul:
        if fach not in modul_farbe:
            modul_farbe[fach] = "#888888"  # Standardfarbe für unbekannte Module

    # Spalte für die Legende hinzufügen (Modulname)
    grouped["Modul_Legende"] = grouped["Modul"]

    import altair as alt

    # Erstelle ein Altair-Balkendiagramm:
    # X-Achse: Notenklasse (ordinal)
    # Y-Achse: Anzahl der Noten
    # Farbe: Modul (mit den definierten Farben)
    # Tooltip zeigt detaillierte Infos an
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

    # Diagramm in einem Container anzeigen
    with st.container(border=True):
        st.altair_chart(chart, use_container_width=True)

        


 
def grundlagenpraktikum(grundlagenpraktika_name):
    # 1. Sicherstellen, dass ein Benutzer eingeloggt ist
    if "username" not in st.session_state:
        st.error("Kein Benutzer eingeloggt. Bitte melden Sie sich an.")
        return  # Funktion abbrechen, wenn kein Benutzer

    # 2. Werte vorbereiten:
    # - ECTS-Punkte für das angegebene Grundlagenpraktikum aus einem Dictionary holen
    ects = grundlagenpraktika_dict.get(grundlagenpraktika_name, {}).get('ects')
    # - DataFrame mit allen Grundlagenpraktika aus dem Session-State holen (oder leerer DataFrame, falls nicht vorhanden)
    df = st.session_state.get("Grundlagenpraktika", pd.DataFrame())

    # 3. Überschrift für das Grundlagenpraktikum anzeigen
    st.subheader(grundlagenpraktika_name)

    # 4. Prüfen, ob für den aktuellen Benutzer bereits ein Eintrag für dieses Praktikum existiert
    eintrag_vorhanden = not df.empty and any(
        (df["Modul"] == grundlagenpraktika_name) & (df["username"] == st.session_state["username"])
    )

    if eintrag_vorhanden:
        # 5. Wenn ja, den bestehenden Eintrag laden (Filtern nach Modul und Benutzername)
        eintrag = df[(df["Modul"] == grundlagenpraktika_name) & (df["username"] == st.session_state["username"])]
        aktueller_status = eintrag.iloc[0]["Status"]  # aktuellen Status (Bestanden/Nein) auslesen
        index = eintrag.index[0]  # Index des Eintrags im DataFrame

        # 6. Funktion zum Aktualisieren des Status definieren
        def update_status():
            # neuen Status aus dem Session-State holen (z.B. aus Radio-Button)
            neuer_status = st.session_state.get(f"{grundlagenpraktika_name}_status", aktueller_status)
            timestamp = pd.Timestamp.now()  # Zeitstempel der Änderung setzen

            # Status und Zeitstempel im DataFrame aktualisieren
            st.session_state["Grundlagenpraktika"].loc[index, "Status"] = neuer_status
            st.session_state["Grundlagenpraktika"].loc[index, "timestamp"] = timestamp

            # Änderungen persistent speichern
            DataManager().save_data(session_state_key="Grundlagenpraktika")

        # 7. Radio-Auswahlfeld anzeigen mit dem aktuellen Status vorausgewählt
        st.radio(
            "**Bestanden?**",
            ["Ja", "Nein"],
            index=0 if aktueller_status == "Ja" else 1,  # Position des vorausgewählten Radio-Buttons
            key=f"{grundlagenpraktika_name}_status",
            on_change=update_status  # bei Änderung update_status ausführen
        )

    else:
        # 8. Wenn noch kein Eintrag vorhanden ist, neuen Eintrag anlegen
        neuer_eintrag = {
            "username": st.session_state["username"],  # Benutzername
            "semester": st.session_state.get("semester"),  # aktuelles Semester
            "Modul": grundlagenpraktika_name,  # Name des Praktikums
            "Status": "Nein",  # Standardwert: nicht bestanden
            "timestamp": pd.Timestamp.now()  # aktueller Zeitstempel
        }

        # 9. Neuen Eintrag anhängen und Daten speichern
        DataManager().append_record(session_state_key="Grundlagenpraktika", record_dict=neuer_eintrag)
        st.rerun()  # Seite neu laden, um den neuen Eintrag anzuzeigen

    # 10. Feedback für den Nutzer anzeigen, je nachdem ob bestanden oder nicht
    final_status = st.session_state.get(f"{grundlagenpraktika_name}_status", "Nein")
    if final_status == "Ja":
        st.success(f"{grundlagenpraktika_name} bestanden (+ {ects} ECTS)")
    else:
        st.error(f"{grundlagenpraktika_name} nicht bestanden (0 von {ects} ECTS)")



def berechne_gesamt_ects(): #für die ECTS-Anzeige auf dem Dashboard
    df_pruefungen = st.session_state["Pruefungen"]
    df_grundlagen = st.session_state.get("Grundlagenpraktika", None)
    ects_summe = 0

    # 1. Modulgruppen-ECTS (wenn alle Noten erfasst und Schnitt >= 4.0)
    for gruppenname, gruppe in modulgruppen.items():
        faecher = gruppe.get("faecher", {})
        ects_modulgruppe = gruppe.get("ects", 0)
        alle_faecher_vollstaendig = True
        noten = []
        gewichtungen = []
        for fach_name, infos in faecher.items():
            df_modul = df_pruefungen[
                (df_pruefungen["Modul"] == fach_name)]
            gewichtung_summe = df_modul["Gewichtung"].sum()
            if gewichtung_summe < 100:
                alle_faecher_vollstaendig = False
                break
            # Schnitt pro Fach
            if gewichtung_summe > 0:
                schnitt = (df_modul["Note"] * df_modul["Gewichtung"]).sum() / gewichtung_summe
                noten.append(schnitt)
                gewichtungen.append(infos.get("ects", 0))
        # Modulgruppen-Schnitt berechnen (nur wenn Noten vorhanden)
        if alle_faecher_vollstaendig and noten and sum(gewichtungen) > 0:
            modulgruppen_schnitt = sum([n * e for n, e in zip(noten, gewichtungen)]) / sum(gewichtungen)
            if modulgruppen_schnitt >= 4.0:
                ects_summe += ects_modulgruppe

    # 2. Bestandene Grundlagenpraktika-ECTS (über alle Semester)
    if df_grundlagen is not None and not df_grundlagen.empty:
        for idx, row in df_grundlagen.iterrows():
            if str(row.get("Status", "")).strip().lower() == "ja":
                ects = grundlagenpraktika_dict.get(row["Modul"], {}).get("ects", 0)
                if ects > 0:
                    ects_summe += ects

    return ects_summe