import streamlit as st

def sidebar_anzeige():
    st.sidebar.page_link('Start.py', label='Startseite')
    st.sidebar.page_link('pages/1_Dashboard.py', label='Dashboard')
    st.sidebar.page_link('pages/2_Modulgruppen-Uebersicht.py', label='Modulgruppen-Uebersicht')
    

def trennlinie_duenn(farbe="#888", hoehe="1px", abstand="20px"):
    st.markdown(
        f"""
        <div style='margin:{abstand} 0;'>
            <hr style='height:{hoehe}; border:none; background-color:{farbe};'>
        </div>
        """,
        unsafe_allow_html=True)
    
def trennlinie_stark(farbe="#888", hoehe="3px", abstand="30px"):
    st.markdown(
        f"""
        <div style='margin:{abstand} 0;'>
            <hr style='height:{hoehe}; border:none; background-color:{farbe}; border-radius:2px;'>
        </div>
        """,
        unsafe_allow_html=True)
