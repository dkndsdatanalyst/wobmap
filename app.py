import streamlit as st
import pandas as pd
import gspread

# 1. Konfiguration
st.set_page_config(page_title="WOBmap", layout="wide")
st.title("🐺 WOBmap - Fan-Storys")

# 2. Verbindung zu Google Sheets
def get_google_sheet():
    # Lädt die credentials.json aus deinem Ordner
    gc = gspread.service_account(filename='credentials.json')
    # Öffnet das Sheet WOBmap_Data
    return gc.open("WOBmap_Data").sheet1

# 3. Hilfsfunktion für Landkreise
@st.cache_data
def get_landkreis_liste():
    return pd.read_csv('landkreise.csv')['landkreis'].tolist()

# 4. Sidebar Eingabemaske
with st.sidebar:
    st.header("Dein Steckbrief")
    with st.form("wob_form"):
        name = st.text_input("Name")
        kreis = st.selectbox("Landkreis", get_landkreis_liste())
        alter = st.number_input("Alter", 1, 100)
        fan_seit = st.text_input("Fan seit (Jahr)")
        erstes_spiel = st.text_input("Erstes Mal Stadion")
        lieblings_spieler = st.text_input("Lieblings-Spieler*in")
        lieblings_klischee = st.text_input("Lieblings-Klischee")
        geschichte = st.text_area("Was verbindet dich mit dem VfL?")
        
        if st.form_submit_button("Story abschicken"):
            sheet = get_google_sheet()
            # Reihenfolge angepasst an: Name, Landkreis, Alter, Fan_seit, Erstes_Spiel, Lieblings_Spieler*in, Lieblings_Klischee, Geschichte
            sheet.append_row([name, kreis, alter, fan_seit, erstes_spiel, lieblings_spieler, lieblings_klischee, geschichte])
            st.success("Danke für deine grün-weiße Story!")