import streamlit as st
from functions.design import sidebar_anzeige
from functions.notenrechner import semesterschnitt_berechnen, bestes_modul_anzeigen, noten_verteilung, berechne_gesamt_ects
import time

# ====== Seiten-Setup =====
st.set_page_config(
    page_title="Kestmo - Dashboard",
    page_icon="📚",
    layout="wide")
# ====== Seiten-Setup =====


# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('pages/Login.py') 
# ====== End Login Block ======

sidebar_anzeige()

st.title('Dashboard')


semesters = ['Herbstsemester 1', 'Fruehlingssemester 1',
             'Herbstsemester 2', 'Fruehlingssemester 2', 
             'Herbstsemester 3', 'Fruehlingssemester 3']

if 'semester' not in st.session_state:
    st.session_state.semester = semesters[0]

semester = st.selectbox('Wähle das Semester', semesters, index=semesters.index(st.session_state.semester))

if semester != st.session_state.semester:
    st.session_state.semester = semester
    st.rerun()


semesterschnitt = semesterschnitt_berechnen(semester)

col1, = st.columns(1, border=True, vertical_alignment='center')
with col1:
    if semesterschnitt is None:
        st.warning("Je härter ich arbeite, umso mehr Glück scheine ich zu haben. ~Thomas Jefferson")
    elif semesterschnitt < 4.0:
        st.warning("Der bequemste Weg geht immer bergab. ~Jochen Simbrig ")
    elif semesterschnitt >= 4.0:
        st.success("Je härter ich arbeite, umso mehr Glück scheine ich zu haben. ~Thomas Jefferson")


bestes_modul, beste_note = bestes_modul_anzeigen(semester)

farbe_semesterschnitt = 'red' if semesterschnitt is not None and semesterschnitt < 4 else 'black'

col1, col2, col3 = st.columns(3, border=True)
with col1:
    st.markdown(
        f"""
        <div style='text-align:center;'>
            <div style='font-size: 1.3em; font-weight: bold; color: #000;'>Aktueller Semesterdurchschnitt</div>
            <div style='font-size: 1.2em; color: #000;'>{semester}</div>
        </div>
        """, unsafe_allow_html=True
    )

    if semesterschnitt is None:
        st.info("Der Semesterschnitt kann nicht berechnet werden, da nicht alle Noten vorhanden sind.")
    else:
        st.markdown(
            f"""
            <div style='text-align:center; font-size: 1.2em; font-weight: bold; color: {farbe_semesterschnitt}'>
                Ø {semesterschnitt}
            </div>
            """, unsafe_allow_html=True
        )

with col2:
    st.markdown(
        """
        <div style='text-align:center;'>
            <div style='font-size: 1.3em; font-weight: bold; color: #000;'>Bestes Modul des Semesters</div>
        </div>
        """, unsafe_allow_html=True
    )
    

    if bestes_modul is None or beste_note is None:
        st.info("Für dieses Semester sind noch keine Noten vorhanden.")
    else:
        st.markdown(
            f"""
            <div style='text-align:center'>
                <div style='font-size: 1.2em; color: #000;'>{bestes_modul}</div>
                <div style='font-size: 1.2em; font-weight: bold; color: #000;'>Mit der Note {beste_note}</div>
            </div>
            """, unsafe_allow_html=True
        )

with col3:
    total_ects = 180
    current_ects =  berechne_gesamt_ects() # Beispielwert ANPASSEN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    st.markdown(
        """
        <div style='text-align:center;'>
            <div style='font-size: 1.3em; font-weight: bold; color: #000;'>Aktueller ECTS-Stand</div>
        </div>
        """, unsafe_allow_html=True
    )
    # Fortschrittsbalken grün einfärben
    st.markdown("""
        <style>
        .stProgress > div > div > div > div {
            background-color: #21ba45;
        }
        </style>
    """, unsafe_allow_html=True)

    # Fortschrittsbalken und animierte Zahl
    progress_bar = st.progress(0)
    text_placeholder = st.empty()

    for i in range(current_ects + 1):
        progress = i / total_ects
        progress_bar.progress(progress)
        text_placeholder.markdown(
            f"<div style='text-align:center; font-weight:bold;'>{i} von {total_ects} ECTS erreicht</div>",
            unsafe_allow_html=True
        )
        time.sleep(0.02)  # Geschwindigkeit der Animation

            

noten_verteilung(semester)