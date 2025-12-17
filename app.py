import streamlit as st
from datetime import datetime

# --- CONFIGURARE PAGINĂ ---
st.set_page_config(
    page_title="CardioReport 8-BIT",
    page_icon="👾",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CSS PENTRU STIL 8-BIT / RETRO ---
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">
    <style>
    /* --- FONT GLOBAL --- */
    html, body, [class*="css"] {
        font-family: 'Press Start 2P', cursive;
    }
    
    /* --- FUNDAL --- */
    .stApp {
        background-color: #202040;
        background-image: linear-gradient(to right, #252550 1px, transparent 1px),
                          linear-gradient(to bottom, #252550 1px, transparent 1px);
        background-size: 20px 20px;
    }

    /* --- CONTAINERE GENERICE --- */
    .block-container {
        padding-top: 2rem;
    }

    /* --- HEADERS --- */
    h1, h2, h3 {
        color: #ffcc00 !important;
        text-shadow: 4px 4px #000000;
        text-transform: uppercase;
        line-height: 1.5 !important;
    }
    p, label, .stMarkdown {
        color: #ffffff !important;
        font-size: 0.8rem !important;
    }

    /* --- INPUTURI & WIDGET-URI --- */
    .stTextInput > div > div, 
    .stNumberInput > div > div, 
    .stSelectbox > div > div {
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 4px solid #000000 !important;
        border-radius: 0px !important;
        box-shadow: 6px 6px 0px #000000 !important;
    }
    
    input, .stSelectbox [data-baseweb="select"] span {
        color: #000000 !important;
        font-family: 'Press Start 2P', cursive !important;
        font-size: 0.7rem !important;
    }

    /* --- EXPANDER (Retro Box) --- */
    .streamlit-expanderHeader {
        background-color: #6c5ce7 !important;
        color: white !important;
        border: 4px solid #000000 !important;
        border-radius: 0px !important;
        margin-bottom: 10px;
    }
    .streamlit-expanderContent {
        border: 4px solid #000000 !important;
        border-top: none !important;
        background-color: #303060 !important;
        border-radius: 0px !important;
        margin-bottom: 20px;
    }

    /* --- BUTOANE --- */
    .stButton > button {
        background-color: #ff3333 !important;
        color: white !important;
        border: 4px solid #000000 !important;
        border-radius: 0px !important;
        font-family: 'Press Start 2P', cursive !important;
        box-shadow: 6px 6px 0px #000000 !important;
        transition: all 0.1s;
    }
    .stButton > button:active {
        transform: translate(4px, 4px);
        box-shadow: 2px 2px 0px #000000 !important;
    }

    /* --- ZONA RAPORT (CRT MONITOR STYLE) --- */
    .report-container {
        background-color: #000000;
        padding: 20px;
        border: 8px solid #444;
        border-radius: 0px;
        box-shadow: inset 0 0 20px rgba(0,255,0,0.5);
        color: #33ff33;
        font-family: 'Courier New', monospace; /* Monospace pt lizibilitate la text mult */
        font-weight: bold;
        line-height: 1.6;
        position: relative;
    }
    /* Linie de scanare decorativă */
    .report-container::before {
        content: " ";
        display: block;
        position: absolute;
        top: 0;
        left: 0;
        bottom: 0;
        right: 0;
        background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%), linear-gradient(90deg, rgba(255, 0, 0, 0.06), rgba(0, 255, 0, 0.02), rgba(0, 0, 255, 0.06));
        z-index: 2;
        background-size: 100% 2px, 3px 100%;
        pointer-events: none;
    }
    
    /* Textarea stilat */
    .stTextArea textarea {
        background-color: #000000 !important;
        color: #33ff33 !important;
        font-family: 'Courier New', monospace !important;
        border: 4px solid #33ff33 !important;
        border-radius: 0px !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
c_head1, c_head2 = st.columns([1, 5])
with c_head1:
    # Imagine pixelată (Heart Container din Zelda style)
    st.image("https://media.tenor.com/images/1c8f654df24458f31518b52f99092497/tenor.png", width=100)
with c_head2:
    st.title("CardioReport 8-BIT")
    st.markdown("PRESS START TO GENERATE REPORT")

st.markdown("---")

# --- LAYOUT PRINCIPAL ---
col_input, col_preview = st.columns([1.1, 1])

with col_input:
    st.subheader("INSERT COIN / DATA")
    
    with st.expander("1. PLAYER INFO (GENERAL)", expanded=True):
        c1, c2 = st.columns(2)
        medecin = c1.text_input("MEDECIN", value="Dr. AL HALABY")
        infirmiere = c2.text_input("INFIRMIERE", value="FARRAPEIRA")
        protocole = st.selectbox("LEVEL / PROTOCOLE", ["VELO FEMME", "30W/2'/30W", "BRUCE", "RAMPE"], index=1)

    with st.expander("2. STAMINA (EFFORT)", expanded=True):
        c1, c2, c3 = st.columns(3)
        duree = c1.text_input("TIME (min:sec)", value="06:08")
        charge = c2.number_input("POWER (Watts)", value=120, step=10)
        mets = c3.number_input("METS", value=4.6, step=0.1)
        motif = st.selectbox("GAME OVER REASON", ["Essoufflement + Fatigue des jambes", "Douleur thoracique", "Épuisement", "Haut risque tensionnel"])

    with st.expander("3. HEALTH BAR (HEMO)", expanded=True):
        st.markdown("HP (Heart Rate - bpm)")
        fc1, fc2, fc3 = st.columns(3)
        fc_repos = fc1.number_input("HP Start", value=71)
        fc_max = fc2.number_input("HP Max", value=116)
        fc_recup = fc3.number_input("HP Recov", value=91)
        
        c_fmt1, c_fmt2 = st.columns(2)
        fmt_calc = c_fmt1.number_input("Max HP Calc", value=145)
        
        if fmt_calc > 0:
            perc_calc = int((fc_max / fmt_calc) * 100)
        else:
            perc_calc = 0
            
        # Bara de progres retro
        st.write(f"SCORE: {perc_calc}% FMT")
        st.progress(min(perc_calc, 100))

        st.markdown("PRESSURE (mmHg)")
        ta1, ta2 = st.columns(2)
        ta_repos = ta1.text_input("TA Start", value="115/60")
        ta_max = ta2.text_input("TA Max", value="174/70")

    with st.expander("4. STATUS EFFECTS (ECG)", expanded=True):
        douleur = st.radio("DAMAGE RECEIVED?", ["Absence de douleurs", "Angor typique", "Douleur atypique"])
        st_seg = st.text_input("ST Segment", value="Modification non significative")
        rythme = st.text_input("Rhythm", value="Quelques ESA, absence de troubles majeurs")
        profil_ta = st.selectbox("Pressure Profile", ["Normal à l'effort", "Hypertensif", "Hypotensif"])

    with st.expander("5. FINAL BOSS (CONCLUSION)", expanded=True):
        perf_type = st.selectbox("Performance Rank", ["Sous-maximale", "Maximale"])
        conclusion_type = st.selectbox("Mission Outcome", 
                                       ["Test d'effort négatif cliniquement et électriquement", 
                                        "Test positif (ischémique)", 
                                        "Test non concluant"])

# --- GENERARE RAPORT (TEXT) ---
def generate_text():
    report = f"""**COMPTE RENDU D'ÉPREUVE D'EFFORT**

**Médecin :** {medecin}
**Infirmière :** {infirmiere}
**Protocole :** {protocole}

---
### **DÉROULEMENT DE L'ÉPREUVE**
* **Durée de l'effort :** {duree} min.
* **Charge maximale :** {charge} Watts ({mets} METS).
* **Motif d'arrêt :** {motif}.

### **DONNÉES HÉMODYNAMIQUES**
* **Fréquence Cardiaque (FC) :**
    * Repos : {fc_repos} bpm.
    * Max : {fc_max} bpm ({perc_calc}% de la FMT {fmt_calc}).
    * Récupération : {fc_recup} bpm.
* **Tension Artérielle (TA) :**
    * Repos : {ta_repos} mmHg.
    * Max : {ta_max} mmHg.
    * Profil : {profil_ta}.

### **DONNÉES CLINIQUES ET ECG**
* **Symptômes :** {douleur}.
* **ECG Repos :** Normal.
* **ECG Effort :** {st_seg}. {rythme}.
* **ECG Récupération :** Retour au calme sans particularité.

### **CONCLUSION**
Performance **{perf_type.lower()}**.
L'ECG de repos est normal. Pas de modification ischémique significative du segment ST.
{rythme}.

**SYNTHÈSE : {conclusion_type.upper()}**
"""
    return report

report_text = generate_text()

# --- COLOANA PREVIEW ---
with col_preview:
    st.subheader("💾 SAVE GAME / PREVIEW")
    
    # Monitor CRT Simulat
    st.markdown(f"""
    <div class="report-container">
        {report_text.replace(chr(10), '<br>')}
        <br><br>
        <span style="animation: blink 1s infinite;">_</span>
    </div>
    <style>
    @keyframes blink {{
      0% {{ opacity: 0; }}
      50% {{ opacity: 1; }}
      100% {{ opacity: 0; }}
    }}
    </style>
    """, unsafe_allow_html=True)
    
    st.write("---")
    st.subheader("📋 COPY LOOT")
    st.text_area("RAW DATA", value=report_text, height=200)
    
    if st.button("RESTART LEVEL"):
        st.experimental_rerun()
