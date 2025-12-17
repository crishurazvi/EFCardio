import streamlit as st
from datetime import datetime

# --- CONFIGURARE PAGINĂ ---
st.set_page_config(
    page_title="CardioReport Gen",
    page_icon="🫀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS PENTRU STIL MODERN ---
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stTextArea, .stTextInput, .stNumberInput, .stSelectbox {
        background-color: #ffffff;
        border-radius: 8px;
    }
    h1, h2, h3 {
        color: #2c3e50;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .report-container {
        background-color: white;
        padding: 30px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border-left: 5px solid #3498db;
    }
    .success-box {
        padding: 10px;
        background-color: #d4edda;
        color: #155724;
        border-radius: 5px;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# --- TITLU ---
col_header_1, col_header_2 = st.columns([1, 4])
with col_header_1:
    st.image("https://img.icons8.com/color/96/heart-monitor.png", width=80)
with col_header_2:
    st.title("Générateur de Compte Rendu d'Effort")
    st.markdown("Interface moderne pour la saisie rapide des tests d'effort cardiologique.")

st.markdown("---")

# --- LAYOUT PRINCIPAL (2 COLOANE) ---
col_input, col_preview = st.columns([1, 1.2])

with col_input:
    st.subheader("📝 Saisie des Données")
    
    with st.expander("1. Informations Générales", expanded=True):
        c1, c2 = st.columns(2)
        medecin = c1.text_input("Médecin", value="Dr. AL HALABY")
        infirmiere = c2.text_input("Infirmière", value="FARRAPEIRA")
        protocole = st.selectbox("Protocole", ["VELO FEMME", "30W/2'/30W", "BRUCE", "RAMPE"], index=1)

    with st.expander("2. Données d'Effort", expanded=True):
        c1, c2, c3 = st.columns(3)
        duree = c1.text_input("Durée (min:sec)", value="06:08")
        charge = c2.number_input("Charge Max (Watts)", value=120, step=10)
        mets = c3.number_input("METS", value=4.6, step=0.1)
        motif = st.selectbox("Motif d'arrêt", ["Essoufflement + Fatigue des jambes", "Douleur thoracique", "Épuisement", "Haut risque tensionnel"])

    with st.expander("3. Hémodynamique (FC & TA)", expanded=True):
        st.caption("Fréquence Cardiaque (bpm)")
        fc1, fc2, fc3 = st.columns(3)
        fc_repos = fc1.number_input("FC Repos", value=71)
        fc_max = fc2.number_input("FC Max", value=116)
        fc_recup = fc3.number_input("FC Récup (1-3 min)", value=91)
        
        c_fmt1, c_fmt2 = st.columns(2)
        fmt_calc = c_fmt1.number_input("FMT Calculée", value=145)
        # Calcul automat al procentului
        if fmt_calc > 0:
            perc_calc = int((fc_max / fmt_calc) * 100)
        else:
            perc_calc = 0
        st.info(f"Pourcentage atteint : **{perc_calc}%** de la FMT")

        st.caption("Tension Artérielle (mmHg)")
        ta1, ta2 = st.columns(2)
        ta_repos = ta1.text_input("TA Repos", value="115/60")
        ta_max = ta2.text_input("TA Max", value="174/70")

    with st.expander("4. ECG & Clinique", expanded=True):
        douleur = st.radio("Douleurs Thoraciques ?", ["Absence de douleurs", "Angor typique", "Douleur atypique"], horizontal=True)
        st_seg = st.text_input("Segment ST", value="Modification non significative")
        rythme = st.text_input("Rythme / Arythmie", value="Quelques ESA, absence de troubles majeurs")
        profil_ta = st.selectbox("Profil Tensionnel", ["Normal à l'effort", "Hypertensif", "Hypotensif"])

    with st.expander("5. Conclusion & Synthèse", expanded=True):
        perf_type = st.selectbox("Type de performance", ["Sous-maximale", "Maximale"])
        conclusion_type = st.selectbox("Conclusion Globale", 
                                       ["Test d'effort négatif cliniquement et électriquement", 
                                        "Test positif (ischémique)", 
                                        "Test non concluant"])

# --- GENERARE RAPORT ---
def generate_text():
    # Construirea textului pe baza inputurilor
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
    st.subheader("📄 Aperçu du Rapport")
    
    # Container vizual
    st.markdown(f"""
    <div class="report-container">
        {report_text.replace(chr(10), '<br>')}
    </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    st.subheader("📋 Copier le texte")
    st.text_area("Texte brut (Ctrl+C pour copier)", value=report_text, height=300)
    
    if st.button("Réinitialiser le formulaire"):
        st.experimental_rerun()
