import streamlit as st

# --- 1. CONFIGURARE PAGINĂ (TREBUIE SĂ FIE PRIMA LINIE DE COD) ---
st.set_page_config(
    page_title="Cardio 8-BIT",
    page_icon="👾",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. CSS STABILIZAT PENTRU STIL 8-BIT ---
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">
<style>
    /* --- STILURI GENERALE --- */
    .stApp {
        background-color: #2b2b45; /* Albastru închis Retro */
    }
    
    /* Fontul Retro pentru titluri */
    h1, h2, h3, .retro-font {
        font-family: 'Press Start 2P', monospace !important;
        text-transform: uppercase;
        color: #fceea7 !important; /* Galben pal */
        text-shadow: 2px 2px #000000;
    }
    
    /* Etichetele (Labels) */
    .stTextInput label, .stNumberInput label, .stSelectbox label {
        color: #ffffff !important;
        font-family: 'Courier New', monospace !important;
        font-weight: bold;
        font-size: 14px !important;
    }

    /* --- INPUT BOXES (Câmpurile de text) --- */
    /* Targetăm containerul de input pentru a-l face pătrat */
    div[data-baseweb="input"], div[data-baseweb="select"] > div {
        background-color: #ffffff !important;
        border: 2px solid #000000 !important;
        border-radius: 0px !important;
        box-shadow: 4px 4px 0px #000000 !important; /* Umbra solidă */
    }
    
    /* Textul din interiorul inputului */
    input[type="text"], input[type="number"], div[data-baseweb="select"] span {
        color: #000000 !important;
        font-family: 'Courier New', monospace !important;
        font-size: 16px !important;
        font-weight: bold !important;
    }

    /* --- EXPANDER (Cutii pliabile) --- */
    .streamlit-expanderHeader {
        background-color: #e74c3c !important; /* Rosu Retro */
        color: #ffffff !important;
        border: 2px solid #000000 !important;
        border-radius: 0px !important;
        font-family: 'Press Start 2P', monospace !important;
        font-size: 12px !important;
    }
    
    div[data-testid="stExpander"] {
        background-color: #ecf0f1 !important;
        border: 2px solid #000000 !important;
        border-radius: 0px !important;
        box-shadow: 4px 4px 0px #000000 !important;
    }
    
    div[data-testid="stExpanderDetails"] {
        border-top: 2px solid #000000;
        background-color: #d6eaf8; /* Albastru deschis fundal interior */
    }

    /* --- BUTOANE --- */
    .stButton > button {
        background-color: #2ecc71 !important; /* Verde */
        color: #000000 !important;
        font-family: 'Press Start 2P', monospace !important;
        border: 2px solid #000000 !important;
        border-radius: 0px !important;
        box-shadow: 4px 4px 0px #000000 !important;
        transition: all 0.1s;
    }
    .stButton > button:active {
        transform: translate(2px, 2px);
        box-shadow: 2px 2px 0px #000000 !important;
    }

    /* --- MONITORUL DE PREVIEW --- */
    .monitor-frame {
        background-color: #333;
        padding: 20px;
        border-radius: 10px; /* Monitorul e puțin rotund */
        border: 4px solid #111;
        box-shadow: inset 0 0 10px #000;
    }
    
    .monitor-screen {
        background-color: #000000;
        border: 2px solid #555;
        padding: 15px;
        color: #33ff00; /* Verde terminal */
        font-family: 'Courier New', monospace;
        font-size: 14px;
        line-height: 1.5;
        white-space: pre-wrap; /* Păstrează formatarea textului */
        height: 500px;
        overflow-y: auto;
        box-shadow: inset 0 0 20px rgba(0, 255, 0, 0.2);
    }
    
    /* Cursor care clipește */
    .cursor {
        display: inline-block;
        width: 8px;
        height: 15px;
        background-color: #33ff00;
        animation: blink 1s infinite;
    }
    @keyframes blink { 0% { opacity: 0; } 50% { opacity: 1; } 100% { opacity: 0; } }

</style>
""", unsafe_allow_html=True)

# --- 3. HEADER ---
c1, c2 = st.columns([1, 6])
with c1:
    st.markdown("<div style='font-size:50px; text-align:center;'>❤️</div>", unsafe_allow_html=True)
with c2:
    st.title("8-BIT CARDIO GEN")
    st.markdown("PRESS START TO CREATE MEDICAL REPORT")

st.markdown("---")

# --- 4. LAYOUT PRINCIPAL (INPUT vs PREVIEW) ---
col_left, col_right = st.columns([1.2, 1])

# === COLOANA STÂNGA: INPUT DATA ===
with col_left:
    st.markdown("### >> INSERT DATA")

    # Sectiunea 1
    with st.expander("PLAYER 1 (GENERAL)", expanded=True):
        c_a, c_b = st.columns(2)
        medecin = c_a.text_input("MEDIC", value="Dr. AL HALABY")
        infirmiere = c_b.text_input("ASISTENT", value="FARRAPEIRA")
        protocole = st.selectbox("LEVEL (PROTOCOL)", ["VELO FEMME", "30W/2'/30W", "BRUCE", "RAMPE"], index=1)

    # Sectiunea 2
    with st.expander("STAMINA (EFORT)", expanded=True):
        c_a, c_b = st.columns(2)
        duree = c_a.text_input("TIME (MM:SS)", value="06:08")
        charge = c_b.number_input("POWER (WATTS)", value=120, step=10)
        
        c_c, c_d = st.columns(2)
        mets = c_c.number_input("METS", value=4.6, step=0.1)
        motif = st.selectbox("GAME OVER (MOTIF)", ["Essoufflement", "Douleur thoracique", "Épuisement", "TA Elevee"])

    # Sectiunea 3
    with st.expander("HP & STATS (HEMO)", expanded=True):
        st.markdown("**HEART RATE (BPM)**")
        r1, r2, r3 = st.columns(3)
        fc_repos = r1.number_input("START HP", value=71)
        fc_max = r2.number_input("MAX HP", value=116)
        fc_recup = r3.number_input("RECOV HP", value=91)
        
        fmt_calc = st.number_input("TARGET MAX HP", value=145)
        
        # Logică calcul procent
        perc_calc = 0
        if fmt_calc > 0:
            perc_calc = int((fc_max / fmt_calc) * 100)
        
        st.write(f"SCORE: **{perc_calc}%** of Target")
        st.progress(min(perc_calc, 100))
        
        st.markdown("---")
        st.markdown("**PRESSURE (mmHg)**")
        p1, p2 = st.columns(2)
        ta_repos = p1.text_input("TA START", value="115/60")
        ta_max = p2.text_input("TA MAX", value="174/70")

    # Sectiunea 4
    with st.expander("SYSTEM LOGS (ECG & CONCLUZIE)", expanded=True):
        douleur = st.selectbox("DAMAGE", ["Absence de douleurs", "Angor typique", "Douleur atypique"])
        st_seg = st.text_input("ST SEGMENT", value="Modif. non significative")
        rythme = st.text_input("RHYTHM", value="Quelques ESA")
        
        st.markdown("---")
        perf_type = st.selectbox("RANK", ["SOUS-MAXIMALE", "MAXIMALE"])
        conclusion_type = st.selectbox("MISSION RESULT", ["NEGATIF (NORMAL)", "POSITIF (ISCHEMIQUE)", "NON CONCLUANT"])

# --- GENERARE TEXT RAPORT ---
report_content = f"""
========================================
   COMPTE RENDU D'ÉPREUVE D'EFFORT
========================================

[1] GENERAL
    Médecin    : {medecin}
    Infirmière : {infirmiere}
    Protocole  : {protocole}

[2] EFFORT
    Durée      : {duree} min
    Charge     : {charge} W ({mets} METS)
    Arrêt      : {motif}

[3] HEMODYNAMIQUE
    > FC Repos : {fc_repos} bpm
    > FC Max   : {fc_max} bpm ({perc_calc}% FMT)
    > FC Récup : {fc_recup} bpm
    > TA Repos : {ta_repos} mmHg
    > TA Max   : {ta_max} mmHg

[4] CLINIQUE & ECG
    Symptômes  : {douleur}
    ECG Repos  : Normal
    ECG Effort : {st_seg}
    Rythme     : {rythme}

----------------------------------------
CONCLUSION: {conclusion_type}
Performance {perf_type}
----------------------------------------
"""

# === COLOANA DREAPTA: PREVIEW ===
with col_right:
    st.markdown("### >> PREVIEW")
    
    # Afișare stil Monitor CRT folosind HTML pur
    st.markdown(f"""
    <div class="monitor-frame">
        <div class="monitor-screen">{report_content}<span class="cursor"></span></div>
    </div>
    """, unsafe_allow_html=True)

    st.write("") # Spațiu
    
    # Butoane de acțiune
    if st.button("🔄 RESTART LEVEL"):
        st.rerun() # Comanda modernă pentru refresh în Streamlit
        
    # Buton download (Text simplu)
    st.download_button(
        label="💾 SAVE GAME (DOWNLOAD)",
        data=report_content,
        file_name="cardio_report.txt",
        mime="text/plain"
    )
