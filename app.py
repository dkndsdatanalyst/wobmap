import streamlit as st
import pandas as pd
import gspread
import json

# 1. Konfiguration
st.set_page_config(page_title="WOBmap", layout="wide")
st.title("🐺 sagenumWOBen - Geschichten & Stories von Fans des VfL Wolfsburg")

def get_google_sheet():
    if "GCP_BASE64" in st.secrets:
        # Dekodiere den Base64-String zurück in die originalen JSON-Daten
        creds_json = base64.b64decode(st.secrets["GCP_BASE64"]).decode('utf-8')
        creds_dict = json.loads(creds_json)
        
        gc = gspread.service_account_from_dict(creds_dict)
    else:
        # Lokaler Fall
        gc = gspread.service_account(filename='credentials.json')
    
    return gc.open("WOBmap_Data").worksheet("Tabellenblatt1")
    
    # Zugriff auf dein spezifisches Blatt
    return gc.open("WOBmap_Data").worksheet("Tabellenblatt1")

# 3. Hilfsfunktion für Landkreise
@st.cache_data
def get_landkreis_liste():
    # Test-Liste statt CSV-Zugriff
    return ["Wolfsburg", "Göttingen", "Hannover"]

# 4. Sidebar Eingabemaske
with st.sidebar:
    st.header("Dein Steckbrief")
    with st.form("wob_form"):  # <--- Start des Formulars
        name = st.text_input("Name")
        kreis = st.selectbox("Landkreis", get_landkreis_liste())
        alter = st.number_input("Alter", 1, 100)
        fan_seit = st.text_input("Fan seit (Jahr)")
        erstes_spiel = st.text_input("Erstes Mal Stadion")
        lieblings_spieler = st.text_input("Lieblings-Spieler*in")
        lieblings_klischee = st.text_input("Lieblings-Klischee")
        geschichte = st.text_area("Was verbindet dich mit dem VfL?")
        submitted = st.form_submit_button("Story abschicken")
        
        if submitted:
            sheet = get_google_sheet()
            sheet.append_row([name, kreis, alter, fan_seit, erstes_spiel, lieblings_spieler, lieblings_klischee, geschichte])
            st.success("Danke für deine Story!")
