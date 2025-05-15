import streamlit as st
import pandas as pd
import time
import pandas as pd
from utils.data_manager import DataManager


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
        'ects': 10,
        'faecher': {
            'Gesundheitsdaten': {'key': 'pruefungen_geda', 'ects': ects_dict['Gesundheitsdaten']},
            'Haematologie und Haemostaseologie 1': {'key': 'pruefungen_haehae1', 'ects': ects_dict['Haematologie und Haemostaseologie 1']},
            'Medizinische Mikrobiologie 1': {'key': 'pruefungen_memi1', 'ects': ects_dict['Medizinische Mikrobiologie 1']},
            'Systemerkrankungen': {'key': 'pruefungen_sys', 'ects': ects_dict['Systemerkrankungen']}}},
    'Wissenschaftliche Grundlagen 1': {
        'ects': 13,
        'faecher': {
            'Biologie 1': {'key': 'pruefungen_bio1', 'ects': ects_dict['Biologie 1']},
            'Chemie 1': {'key': 'pruefungen_che1', 'ects': ects_dict['Chemie 1']},
            'Informatik 1': {'key': 'pruefungen_inf1', 'ects': ects_dict['Informatik 1']},
            'Mathematik 1': {'key': 'pruefungen_mat1', 'ects': ects_dict['Mathematik 1']}}},
    'Sprache': {
        'ects': 4,
        'faecher': {
            'Englisch 1': {'key': 'pruefungen_eng1', 'ects': ects_dict['Englisch 1']},
            'Gesellschaftlicher Kontext und Sprache 1': {'key': 'pruefungen_gks1', 'ects': ects_dict['Gesellschaftlicher Kontext und Sprache 1']}}},

    'Basiswissen BMLD 2': {
        'ects': 12,
        'faecher': {
            'Haematologie und Haemostaseologie 2': {'key': 'pruefungen_haehae2', 'ects': ects_dict['Haematologie und Haemostaseologie 2']},
            'Histologie und Zytologie 1': {'key': 'pruefungen_histo1', 'ects': ects_dict['Histologie und Zytologie 1']},
            'Klinische Chemie und Immunologie 1': {'key': 'pruefungen_kcl1', 'ects': ects_dict['Klinische Chemie und Immunologie 1']},
            'Medizinische Mikrobiologie 2': {'key': 'pruefungen_memi2', 'ects': ects_dict['Medizinische Mikrobiologie 2']}}},
    'Wissenschaftliche Grundlagen 2': {
        'ects': 17,
        'faecher': {
            'Biologie 2': {'key': 'pruefungen_bio2', 'ects': ects_dict['Biologie 2']},
            'Chemie 2': {'key': 'pruefungen_che2', 'ects': ects_dict['Chemie 2']},
            'Informatik 2': {'key': 'pruefungen_inf2', 'ects': ects_dict['Informatik 2']},
            'Mathematik 2': {'key': 'pruefungen_mat2', 'ects': ects_dict['Mathematik 2']},
            'Physik': {'key': 'pruefungen_phy', 'ects': ects_dict['Physik']},
            'Englisch 2': {'key': 'pruefungen_eng2', 'ects': ects_dict['Englisch 2']},
            'Gesellschaftlicher Kontext und Sprache 2': {'key': 'pruefungen_gks2', 'ects': ects_dict['Gesellschaftlicher Kontext und Sprache 2']}}},
            
    'Analyseprozesse und Labordiagnostik 1':{
        'ects': 6,
        'faecher': {
            'Klinische Chemie und Immunologie 2': {'key': 'pruefungen_kcl2', 'ects': ects_dict['Klinische Chemie und Immunologie 2']},
            'Histologie und Zytologie 2': {'key': 'pruefungen_histo2', 'ects': ects_dict['Histologie und Zytologie 2']},
            'Immunhaematologie und Transfusionsmedizin 1': {'key': 'pruefungen_iht1', 'ects': ects_dict['Immunhaematologie und Transfusionsmedizin 1']}}},
    'Analyseprozesse und Labordiagnostik 2':{
        'ects': 11,
        'faecher': {
            'Herz-Kreislauf- und respiratorische Erkrankungen': {'key': 'pruefungen_hkr', 'ects': ects_dict['Herz-Kreislauf- und respiratorische Erkrankungen']},
            'Neoplasien und haematologische Erkrankungen': {'key': 'pruefungen_neopla', 'ects': ects_dict['Neoplasien und haematologische Erkrankungen']},
            'Selbst- und patientennahe Diagnostik': {'key': 'pruefungen_spd', 'ects': ects_dict['Selbst- und patientennahe Diagnostik']},
            'Hygiene und Epidemiologie': {'key': 'pruefungen_hyep', 'ects': ects_dict['Hygiene und Epidemiologie']}}},
    
    'Analyseprozesse und Labordiagnostik 3':{
        'ects': 10,
        'faecher': {
            'Immunhaematologie und Transfusionsmedizin 2': {'key': 'pruefungen_iht2', 'ects': ects_dict['Immunhaematologie und Transfusionsmedizin 2']},
            'Medizinische Genetik 1': {'key': 'pruefungen_gen1', 'ects': ects_dict['Medizinische Genetik 1']},
            'Bewegungsapparat und neurologische Erkrankungen': {'key': 'pruefungen_bene', 'ects': ects_dict['Bewegungsapparat und neurologische Erkrankungen']},
            'Endokrinologie, Stoffwechselerkrankungen': {'key': 'pruefungen_endo', 'ects': ects_dict['Endokrinologie, Stoffwechselerkrankungen']}}},

    'Analyseprozesse und Labordiagnostik 4':{
        'ects': 7,
        'faecher': {
            'Medizinische Genetik 2': {'key': 'pruefungen_gen2', 'ects': ects_dict['Medizinische Genetik 2']},
            'Urogenitale und gastrointestinale Erkrankungen': {'key': 'pruefungen_uro', 'ects': ects_dict['Urogenitale und gastrointestinale Erkrankungen']},
            'Entwicklungsstörungen und vererbbare Erkrankungen': {'key': 'pruefungen_entw', 'ects': ects_dict['Entwicklungsstörungen und vererbbare Erkrankungen']}}},                                                  
    'Kommunikation und Management 1': {
        'ects': 14,
        'faecher': {
            'Projekt-, Change- und Risikomanagement 1': {'key': 'pruefungen_pcr1', 'ects': ects_dict['Projekt-, Change- und Risikomanagement 1']},
            'Kommunikation 1': {'key': 'pruefungen_kom1', 'ects': ects_dict['Kommunikation 1']},
            'Evidenzbasiertes Handeln': {'key': 'pruefungen_ebh', 'ects': ects_dict['Evidenzbasiertes Handeln']},
            'Entwicklungen, Trends, Unternehmertum': {'key': 'pruefungen_etu', 'ects': ects_dict['Entwicklungen, Trends, Unternehmertum']},
            'Gesundheitsförderung und Praevention': {'key': 'pruefungen_gepr', 'ects': ects_dict['Gesundheitsförderung und Praevention']}}},
    'Angewandte Forschung': {
        'ects': 8,
        'faecher': {
            'Projektarbeit': {'key': 'pruefungen_proj', 'ects': ects_dict['Projektarbeit']},
            'Forschungsmethoden 1': {'key': 'pruefungen_fors1', 'ects': ects_dict['Forschungsmethoden 1']}}},
    'Gesellschaft, Kultur und Gesundheit':{
        'ects': 3},

    'Gesundheitssystem':{
        'ects': 6,
        'faecher': {
            'Klinische Pharmakologie und personalisierte Medizin': {'key': 'pruefungen_pharma', 'ects': ects_dict['Klinische Pharmakologie und personalisierte Medizin']},
            'Gesundheitssystem und Digital Health': {'key': 'pruefungen_gedh', 'ects': ects_dict['Gesundheitssystem und Digital Health']}}},
    'Kommunikation und Management 2': {
        'ects': 6,
        'faecher': {
            'Projekt-, Change- und Risikomanagement 2': {'key': 'pruefungen_pcr2', 'ects': ects_dict['Projekt-, Change- und Risikomanagement 2']},
            'Forschungsmethoden 2': {'key': 'pruefungen_fors2', 'ects': ects_dict['Forschungsmethoden 2']}}}}


grundlagenpraktika_dict = {
    'Grundlagenpraktikum 1': {
        'ects': 3},
    'Grundlagenpraktikum 2': {
        'ects': 3},
    'Externes Praktikum Fachbereich A': {
        'ects': 11},
    'Externes Praktikum Fachbereich B': {
        'ects': 11},
    'Externes Praktikum Fachbereich C': {
        'ects': 9},
    'Praxisreflexion und interprofessionelles Handeln':{
        'ects': 2},
        
    'Gesellschaft, Kultur und Gesundheit': {
        'ects': 3}}

data_manager = DataManager(fs_protocol='webdav', fs_root_folder="Institution/kestmo_App")

def manage_pruefungen(fach_name, session_state_key, spalten
                      ):
    if "username" not in st.session_state:
        st.error("Kein Benutzer eingeloggt. Bitte melden Sie sich an.")
        return

    st.subheader(f'{fach_name}')

    ects = ects_dict.get(fach_name)
    df_pruefungen = st.session_state["Pruefungen"]

    # Anzeigen der Pruefungsdaten
    if not df_pruefungen.empty:
        data = df_pruefungen[df_pruefungen['Modul'] == fach_name]
        #farbe = 'green' if st.session_state[gewichtete_note_key] >= 4 else 'red'

        #col1, col2, col3 = st.columns([2, 1, 1])
        #with col1:
         #   st.markdown("**Notendurchschnitt des Moduls**")
          #  st.markdown(f"**Ø** <span style='color:{farbe}'>{st.session_state[gewichtete_note_key]:.2f}</span>", unsafe_allow_html=True)
        #with col2:
         #   st.markdown("**erreichte ECTS**")
          #  erreichte_ects = ects if st.session_state[gewichtete_note_key] >= 4 else 0
           # ects_farbe = 'green' if erreichte_ects > 0 else 'red'
            #st.markdown(f"<span style='color:{ects_farbe}'><strong>{erreichte_ects}</strong></span>", unsafe_allow_html=True)
        #with col3:
         #   st.markdown("**maximale ECTS**")
          #  st.markdown(f"<span style='color:black'>{ects}</strong></span>", unsafe_allow_html=True)


        col1, col2, col3, col4, col5 = st.columns([3, 2, 2, 2, 5])
        with col1:
            st.markdown("**Pruefung**")
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
                    data_manager.save_data("Pruefungen")

                    st.rerun()

    else:
        col1, col2 = st.columns(2)
        with col1:
            st.write('**Maximale ECTS des Moduls**')
        with col2:
            st.write(ects)
        st.info('Noch keine Pruefungen eingetragen. Bitte eine Pruefung hinzufuegen.')

    with st.form(key=f'{fach_name}_form'):
        col1, col2, col3, col4 = st.columns([1.2, 0.8, 1, 0.8])
        with col1:
            name = st.text_input('Pruefungsname')
        with col2:
            datum = st.date_input('Datum')
        with col3:
            gewichtung = st.number_input('Gewichtung in Prozent', min_value=1.0, max_value=100.0, step=1.0)
        with col4:
            note = round(st.number_input('Note', min_value=1.0, max_value=6.0, step=0.05), 2)

        submit_button = st.form_submit_button('Pruefung hinzufuegen')

        if submit_button:
            fehler = []
            if not name.strip():
                fehler.append('Bitte einen Namen fuer die Pruefung eingeben.')
            # Überprüfen, ob die Spalte "Gewichtung" existiert und der DataFrame nicht leer ist
            if "Gewichtung" in df_pruefungen.columns and not df_pruefungen.empty:
                gesamt_gewichtung = data['Gewichtung'].sum() + gewichtung
            else:
                gesamt_gewichtung = gewichtung # Nur die neue Gewichtung verwenden, wenn keine Daten vorhanden sind
            if gesamt_gewichtung > 100:
                fehler.append('Die Gesamtgewichtung der Pruefungen darf 100% nicht ueberschreiten.')
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
        
                data_manager.append_record(session_state_key='Pruefungen', record_dict=result_dict)
                
                # **Hinzufuegen eines Flags fuer erfolgreiches Hinzufuegen**
                st.session_state[f'{session_state_key}_added'] = True

                st.rerun()

                    
        flag_key = f'{session_state_key}_erfolgreich_hinzugefuegt'
        
        if flag_key in st.session_state and st.session_state[flag_key]:
            platzhalter = st.empty()
            platzhalter.success('Pruefung erfolgreich hinzugefuegt!')                
            time.sleep(3)
            platzhalter.empty()   
            del st.session_state[flag_key]


def schnitt_modulgruppe(modulgruppen, modulgruppe_name):
    if "username" not in st.session_state:
        st.error("Kein Benutzer eingeloggt. Bitte melden Sie sich an.")
        return

    # Nutzerspezifischer Praefix
    user_key_prefix = st.session_state["username"]

    gruppe = modulgruppen.get(modulgruppe_name)
    if not gruppe:
        st.error(f"Modulgruppe '{modulgruppe_name}' nicht gefunden.")
        return

    faecher = gruppe['faecher']
    max_ects = gruppe['ects']

    gesamt_note = 0
    gesamt_ects = 0

    for fachname, infos in faecher.items():
        # Nutzerspezifischer Schluessel fuer das Fach
        key = f"{user_key_prefix}_{infos['key']}"
        ects = infos['ects']

        if key in st.session_state and not st.session_state[key].empty:
            df = st.session_state[key]
            gewichtung = df['Gewichtung'].sum()
            if gewichtung > 0:
                schnitt = (df['Note'] * df['Gewichtung']).sum() / gewichtung
                gesamt_note += schnitt * ects
                gesamt_ects += ects

    if gesamt_ects > 0:
        schnitt_modulgruppe = gesamt_note / gesamt_ects
        farbe = 'green' if schnitt_modulgruppe >= 4 else 'red'
        erreichte_ects = max_ects if schnitt_modulgruppe >= 4 else 0

        st.markdown(f'## {modulgruppe_name}')
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1:
            st.markdown("**Notendurchschnitt der Modulgruppe**")
            st.markdown(f"**Ø** <span style='color:{farbe}'>{schnitt_modulgruppe:.2f}</span>", unsafe_allow_html=True)
        with col2:
            st.markdown("**erreichte ECTS**")
            ects_farbe = 'green' if erreichte_ects > 0 else 'red'
            st.markdown(f"<span style='color:{ects_farbe}'><strong>{erreichte_ects}</strong></span>", unsafe_allow_html=True)
        with col3:
            st.markdown("**maximale ECTS**")
            st.markdown(f"<span style='color:black'>{max_ects}</strong></span>", unsafe_allow_html=True)
    else:
        st.markdown(f'## {modulgruppe_name}')
        col1, col2 = st.columns(2)
        with col1:
            st.write('**Maximale ECTS der Modulgruppe**')
        with col2:
            st.write(max_ects)
        st.info("Noch keine gueltigen Noten vorhanden.")


def grundlagenpraktikum(grundlagenpraktika, grundlagenpraktika_name):
    if "username" not in st.session_state:
        st.error("Kein Benutzer eingeloggt. Bitte melden Sie sich an.")
        return

    ects = grundlagenpraktika_dict.get(grundlagenpraktika_name, {}).get('ects')   # Holen der Anzahl-ECTS aus dem 'grundlagenpraktika_dict'
    df_grundlagenpraktika = st.session_state["Grundlagenpraktika"] # vollstaendiger DataFrame

    # Filtere den DataFrame für das angegebene Praktikum
    df_grundlagenpraktika = df_grundlagenpraktika[df_grundlagenpraktika['Modul'] == grundlagenpraktika_name] # Gefilterter DataFrame für das angegebene Praktikum

    st.subheader(grundlagenpraktika_name)
    
    if not df_grundlagenpraktika.empty:
         
        # Filtere den DataFrame für das angegebene Praktikum
        #df_grundlagenpraktika = df_grundlagenpraktika[df_grundlagenpraktika['Modul'] == grundlagenpraktika_name] # Gefilterter DataFrame für das angegebene Praktikum
        
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

    
        # Radio-Box mit vorausgewaehltem aktuellem Status, mit on-change-Callback
        status = st.radio(
            '**Bestanden?**',
            ["Ja", "Nein"],
            index=0 if aktueller_status == "Ja" else 1,
            key=f"{grundlagenpraktika_name}_status",
            on_change = update_status # Wird automatisch aufgerufen, wenn der Wert sich aendert
        )
    
        #Feedback je nach Status
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

        data_manager.append_record(session_state_key='Grundlagenpraktika', record_dict=neuer_eintrag)
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

    
