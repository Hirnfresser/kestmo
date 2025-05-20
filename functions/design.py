import streamlit as st

def sidebar_anzeige():
    # Fügt in der Sidebar Links zu verschiedenen Seiten hinzu, damit man einfach navigieren kann
    st.sidebar.page_link('Start.py', label='Startseite')
    st.sidebar.page_link('pages/1_Dashboard.py', label='Dashboard')
    st.sidebar.page_link('pages/2_Modulgruppen-Uebersicht.py', label='Modulgruppen-Uebersicht')
    

def trennlinie_duenn(farbe="#888", hoehe="1px", abstand="20px"):
    # Erstellt eine dünne horizontale Trennlinie mit einstellbarer Farbe, Höhe und Abstand nach oben und unten
    st.markdown(
        f"""
        <div style='margin:{abstand} 0;'>
            <hr style='height:{hoehe}; border:none; background-color:{farbe};'>
        </div>
        """,
        unsafe_allow_html=True)
    
def trennlinie_stark(farbe="#888", hoehe="3px", abstand="30px"):
    # Erstellt eine dickere und optisch auffälligere Trennlinie mit abgerundeten Ecken
    st.markdown(
        f"""
        <div style='margin:{abstand} 0;'>
            <hr style='height:{hoehe}; border:none; background-color:{farbe}; border-radius:2px;'>
        </div>
        """,
        unsafe_allow_html=True)
    
def logout_button(title):
    # Zeigt eine Titelüberschrift links und rechts daneben einen Logout-Button an
    col1, col3 = st.columns([4, 1])  # Spalten mit Größenverhältnis 4:1
    with col1:
        st.title(title)  # Zeigt den Titel an
    with col3:
        # Logout-Button, der bei Klick den Session-State löscht und die Seite neu lädt
        if st.button("🔒 Logout", key="logout_btn"):
            st.session_state.clear()
            st.rerun()
        # Stil-Definition für den Button (Rahmenfarbe, Textfarbe, runde Ecken, kein Hintergrund)
        st.markdown(
            """
            <style>
            div[data-testid="stButton"] button {
                border:2px solid #79085E;
                color:#79085E;
                font-weight:bold;
                border-radius:8px;
                background: none;
                margin-top: 26px;  /* Abstand nach oben, um auf Titel-Höhe zu kommen */
            }
            </style>
            """,
            unsafe_allow_html=True
        )

def login_reg_button():
    # Ähnlich wie logout_button: zeigt einen Titel und rechts einen Button für Login & Registrierung an
    col1, col3 = st.columns([4, 1])
    with col1:
        st.title("Startseite")
    with col3:
        if st.button("🔑 Login & Registrierung", key="login_btn"):
            st.switch_page("pages/Login.py")
        # Gleiche Button-Styling wie beim Logout-Button
        st.markdown(
            """
            <style>
            div[data-testid="stButton"] button {
                border:2px solid #79085E;
                color:#79085E;
                font-weight:bold;
                border-radius:8px;
                background: none;
                margin-top: 26px;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
