import streamlit as st
from datetime import datetime

# --- CONFIGURARE PAGINĂ ---
st.set_page_config(
    page_title="Cardio 8-BIT",
    page_icon="❤",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CSS RE-DESIGN (ROBUST & CLEAN) ---
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&family=VT323&display=swap" rel="stylesheet">
    <style>
    /* --- RESET & FONTURI --- */
    .stApp {
        background-color: #bcbcbc; /* Gri Retro */
        font-family: 'VT323', monospace;
    }
    
    /* Titluri Pixelate */
    h1, h2, h3 {
        font-family: 'Press Start 2P', cursive;
        color: #2d2d2d;
        text-transform: uppercase;
        line-height: 1.6 !important;
    }
    
    h1 {
        text-shadow: 3px 3px 0px #ffffff;
        color: #cf1020; /* Roșu Mario */
        font-size: 24px !important;
    }

    /* --- INPUTURI (SĂ FIE VIZIBILE) --- */
    /* Etichetele de deasupra inputurilor */
    .stTextInput label, .stNumberInput label, .stSelectbox label {
        font-family: 'Press Start 2P', cursive;
        font-size: 10px !important;
        color: #000000 !important;
        margin-bottom: 5px;
    }

    /* Cutiile de input propriu-zise */
    div[data-baseweb="input"], div[data-baseweb="select"] > div {
        background-color: #ffffff !important;
        border: 2px solid #000000 !important;
        border-radius: 0px !important;
        box-shadow: 4px 4px 0px #888888 !important;
    }

    /* Textul din interiorul inputurilor */
    input, .stSelectbox div {
        font-family: 'VT323', monospace !important;
        font-size: 20px !important;
        color: #000000 !important;
    }

    /* --- EXPANDERS (Ferestre Retro) --- */
    .streamlit-expanderHeader {
        background-color: #5c94fc !important; /* Albastru deschis */
        border: 2px solid #000000;
        border-radius: 0px;
        font-family: 'Press Start 2P', cursive;
        font-size: 12px !important;
        color: #ffffff !important;
        text-shadow: 2px 2px 0px #000000;
    }
    
    .streamlit-expanderContent {
        background-color: #e0e0e0 !important;
        border: 2px solid #000000;
        border-top: none;
        color: #000000 !important;
    }

    /* --- BUTOANE --- */
    .stButton > button {
        width: 100%;
        background-color: #ffcc00 !important;
        color: #000000 !important;
        font-family: 'Press Start 2P', cursive !important;
        font-size: 12px !important;
        border: 2px solid #000000 !important;
        border-radius: 0px !important;
        box-shadow: 4px 4px 0px #000000 !important;
        padding: 15px !important;
    }
    .stButton > button:hover {
        background-color: #ffe066 !important;
        top: -2px;
    }
    .stButton > button:active {
        box-shadow: 0px 0px 0px #000000 !important;
        transform: translate(4px, 4px);
    }

    /* --- ECRAN TERMINAL (PREVIEW) --- */
    .retro-terminal {
        background-color: #1a1a1a;
        border: 4px solid #555;
        border-radius: 10px; /* Ușor rotunjit ca un TV vechi */
        padding: 20px;
        color: #00ff00;
        font-family: 'VT323', monospace;
        font-size: 18px;
        line-height: 1.4;
        box-shadow: inset 0 0 20px #000;
        height: 500px;
        overflow-y: auto;
    }
    .scanline {
        width: 100%;
        height: 100px;
        z-index: 10;
        background: linear-gradient(0deg, rgba(0,0,0,0) 0%, rgba(255, 255, 255, 0.04) 50%, rgba(0,0,0,0) 100%);
        opacity: 0.1;
        position: absolute;
        bottom: 100%;
        animation: scanline 10s linear infinite;
        pointer-events: none;
    }
    @keyframes scanline {
        0% { bottom: 100%; }
        100% { bottom: -100%; }
    }
    
    /* Ascundere elemente default Streamlit inutile */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
col_logo, col_title = st.columns([1, 5])
with col_logo:
    st.markdown("<div style='font-size: 60px; text-align: center;'>❤️</div>", unsafe_allow_html=True)
with col_title:
    st.title("CARDIO REPORT GEN")
    st.markdown("**Version 1.0 // 8-BIT EDITION**")

st.markdown("---")

# --- LOGICA APLICAȚIEI ---

col_left, col_right = st.columns([1, 1])

with col_left:
    st.markdown("### 1. INSERT DATA")
    
    with st.expander("👤 PLAYER INFO", expanded=True):
        c1, c2 = st.columns(2)
        medecin = c1.text_input("MEDIC", value="Dr. AL HALABY")
        infirmiere = c2.text_input("ASISTENT", value="FARRAPEIRA")
        protocole = st.selectbox("LEVEL SELECT", ["VELO FEMME", "30W/2'/30W", "BRUCE", "RAMPE"], index=1)

    with st.expander("⚡ STAMINA / EFFORT", expanded=True):
        c1, c2 = st.columns(2)
        duree = c1.text_input("TIME (MIN)", value="06:08")
        charge = c2.number_input("POWER (W)", value=120, step=10)
        
        c3, c4 = st.columns(2)
        mets = c3.number_input("METS", value=4.6, step=0.1)
        motif = c4.selectbox("GAME OVER REASON", ["Essoufflement", "Douleur thoracique", "Épuisement", "Haut risque TA"])

    with st.expander("💓 HEART STATS", expanded=True):
        st.caption("BEATS PER MINUTE")
        fc1, fc2, fc3 = st.columns(3)
        fc_repos = fc1.number_input("FC START", value=71)
        fc_max = fc2.number_input("FC MAX", value=116)
        fc_recup = fc3.number_input("FC END", value=91)
        
        fmt_calc = st.number_input("TARGET MAX (FMT)", value=145)
        
        # Calcul procent
        if fmt_calc > 0:
            perc_calc = int((fc_max / fmt_calc) * 100)
        else:
            perc_calc = 0
            
        st.markdown(f"**ACHIEVEMENT:** {perc_calc}% OF MAX")
        st.progress(min(perc_calc, 100))

        st.markdown("---")
        st.caption("PRESSURE (mmHg)")
        ta1, ta2 = st.columns(2)
        ta_repos = ta1.text_input("TA START", value="115/60")
        ta_max = ta2.text_input("TA MAX", value="174/70")

    with st.expander("📟 SYSTEM LOGS (ECG)", expanded=True):
        douleur = st.selectbox("SYMPTOMS", ["Absence de douleurs", "Angor typique", "Douleur atypique"])
        st_seg = st.text_input("ST SEGMENT", value="Modif. non significative")
        rythme = st.text_input("RHYTHM", value="Quelques ESA, pas de troubles majeurs")
        
        c_end1, c_end2 = st.columns(2)
        perf_type = c_end1.selectbox("RANK", ["Sous-maximale", "Maximale"])
        conclusion_type = c_end2.selectbox("RESULT", ["NEGATIF", "POSITIF (Ischemique)", "NON CONCLUANT"])

# --- GENERARE TEXT ---
def generate_report():
    return f"""
========================================
      RAPORT TEST DE EFORT - v8.0
========================================

>> PERSONAL MEDICAL
   Medic    : {medecin}
   Asistent : {infirmiere}
   Protocol : {protocole}

>> PERFORMANTA
   Timp     : {duree}
   Sarcina  : {charge} W ({mets} METS)
   Stop     : {motif}

>> HEMODINAMICA [FC]
   Repos    : {fc_repos} bpm
   Maxim    : {fc_max} bpm
   Target   : {perc_calc}% din {fmt_calc}
   Recup.   : {fc_recup} bpm

>> TENSIUNE ARTERIALA [TA]
   Repos    : {ta_repos} mmHg
   Maxim    : {ta_max} mmHg

>> ANALIZA ECG
   Simptome : {douleur}
   ECG Repos: Normal
   ECG Efort: {st_seg}
   Ritm     : {rythme}

----------------------------------------
CONCLUZIE: {conclusion_type}
Performanta {perf_type}
----------------------------------------
    """

raport_final = generate_report()

with col_right:
    st.markdown("### 2. PREVIEW MONITOR")
    
    # Simulare Monitor CRT
    st.markdown(f"""
    <div class="retro-terminal">
        <div class="scanline"></div>
        {raport_final.replace(chr(10), '<br>').replace(' ', '&nbsp;')}
        <br>
        <span style="animation: blink 1s infinite; background-color: #00ff00; color: #000;">_</span>
    </div>
    <style>
    @keyframes blink {{ 0% {{opacity: 0;}} 50% {{opacity: 1;}} 100% {{opacity: 0;}} }}
    </style>
    """, unsafe_allow_html=True)
    
    st.write("")
    
    c_btn1, c_btn2 = st.columns(2)
    with c_btn1:
        if st.button("RELOAD"):
            st.rerun()
    with c_btn2:
        st.download_button("SAVE TO DISK", data=raport_final, file_name="raport_8bit.txt")
