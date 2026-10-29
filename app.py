import streamlit as st
import requests
from urllib.parse import quote

# ==========================================
# CHEMNEXA - PEACH GLOW AESTHETIC
# ==========================================

st.set_page_config(
    page_title="ChemNexa | Molecular Discovery",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# PASTEL GLOW THEME
# ==========================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

:root {
    --peach: #FFBFA3;
    --pink: #F58DB5;
    --lavender: #C7B5F5;
    --cream: #FFF9F2;
    --rose: #E8759E;
    --text: #624956;
}

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background:
        radial-gradient(ellipse at 5% 5%,
        rgba(255, 190, 190, 0.35), transparent 35%),
        radial-gradient(ellipse at 95% 10%,
        rgba(255, 211, 169, 0.40), transparent 35%),
        radial-gradient(ellipse at 50% 100%,
        rgba(213, 194, 255, 0.25), transparent 40%),
        #FFF9F5;
    color: var(--text);
}

header[data-testid="stHeader"] {
    background: rgba(255, 249, 245, 0.8);
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1250px;
}

h1, h2, h3 {
    color: #A84F78 !important;
    font-weight: 700 !important;
}

p, label, li {
    color: #705565;
}

.hero {
    padding: 38px 25px;
    border-radius: 28px;
    text-align: center;
    background: linear-gradient(
        135deg,
        rgba(255, 218, 206, 0.95),
        rgba(255, 237, 237, 0.96),
        rgba(234, 220, 255, 0.95)
    );
    border: 1px solid rgba(255,255,255,0.9);
    box-shadow:
        0 12px 35px rgba(225, 139, 170, 0.18),
        0 0 24px rgba(245, 141, 181, 0.12);
    margin-bottom: 24px;
}

.hero-title {
    font-size: clamp(36px, 6vw, 60px);
    font-weight: 800;
    letter-spacing: -2px;
    background: linear-gradient(
        90deg, #DB6798, #E99A75, #A18BE5
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    font-size: 17px;
    color: #805A70;
    margin-top: 8px;
}

.hero-badge {
    display: inline-block;
    margin-top: 14px;
    padding: 7px 17px;
    border-radius: 30px;
    background: rgba(255,255,255,0.65);
    color: #AD5A83;
    border: 1px solid rgba(235,150,185,0.35);
    font-size: 12px;
    font-weight: 600;
}

.section-title {
    font-size: 25px;
    font-weight: 700;
    color: #A84F78;
    margin: 20px 0 12px 0;
}

.glass-card {
    background: rgba(255,255,255,0.72);
    border: 1px solid rgba(255, 255, 255, 0.95);
    border-radius: 22px;
    padding: 22px;
    box-shadow: 0 8px 28px rgba(183, 119, 150, 0.12);
    margin-bottom: 15px;
    transition: all 0.25s ease;
}

.glass-card:hover {
    box-shadow:
        0 12px 35px rgba(231, 126, 169, 0.22),
        0 0 16px rgba(245, 141, 181, 0.13);
    transform: translateY(-3px);
}

.card-icon {
    font-size: 32px;
    margin-bottom: 8px;
}

.card-title {
    color: #A84F78;
    font-size: 18px;
    font-weight: 700;
}

.card-text {
    color: #826879;
    font-size: 13px;
    line-height: 1.7;
}

div.stButton > button {
    width: 100%;
    border-radius: 15px;
    border: 1px solid rgba(255,255,255,0.9);
    background: linear-gradient(110deg, #F6A4C3, #FFC5A8);
    color: #713E58;
    font-weight: 600;
    padding: 11px 15px;
    box-shadow: 0 5px 16px rgba(224, 123, 163, 0.18);
    transition: all 0.25s ease;
}

div.stButton > button:hover {
    color: #713E58;
    border-color: #E98AB0;
    box-shadow:
        0 6px 22px rgba(232, 117, 158, 0.30),
        0 0 14px rgba(245, 141, 181, 0.20);
    transform: translateY(-2px);
}

div.stButton > button:focus {
    color: #713E58;
    border-color: #E98AB0;
}

div[data-testid="stTextInput"] input,
div[data-testid="stSelectbox"] div[data-baseweb="select"] {
    border-radius: 13px;
}

div[data-testid="stMetric"] {
    background: rgba(255,255,255,0.72);
    border: 1px solid white;
    border-radius: 18px;
    padding: 16px;
    box-shadow: 0 5px 18px rgba(200, 133, 161, 0.10);
}

div[data-testid="stMetricLabel"] {
    color: #956C84;
}

div[data-testid="stMetricValue"] {
    color: #C45F8A;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #FFF0EA 0%,
        #FFEAF1 55%,
        #F2ECFF 100%
    );
    border-right: 1px solid #F6D5E2;
}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #A84F78 !important;
}

hr {
    border-color: #F1D5E1;
}

.small-note {
    background: rgba(255,255,255,0.68);
    border-left: 4px solid #E99AB8;
    padding: 13px 16px;
    border-radius: 10px;
    color: #805A70;
    font-size: 13px;
}

.footer {
    text-align: center;
    color: #A67D91;
    font-size: 12px;
    padding: 25px 0 8px 0;
}

[data-testid="stImage"] img {
    border-radius: 18px;
}

@media (max-width: 600px) {
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .hero {
        padding: 28px 15px;
    }

    .hero-subtitle {
        font-size: 14px;
    }
}
</style>
""", unsafe_allow_html=True)


# ==========================================
# MOLECULE CATALOGUE
# ==========================================

MOLECULES = {
    "Aspirin": ("Drug", "Pain reliever"),
    "Paracetamol": ("Drug", "Pain and fever relief"),
    "Ibuprofen": ("Drug", "Anti-inflammatory drug"),
    "Caffeine": ("Drug", "Stimulant"),
    "Amoxicillin": ("Drug", "Antibiotic"),
    "Penicillin G": ("Drug", "Antibiotic"),
    "Azithromycin": ("Drug", "Antibiotic"),
    "Ciprofloxacin": ("Drug", "Antibiotic"),
    "Metformin": ("Drug", "Antidiabetic drug"),
    "Omeprazole": ("Drug", "Acid-reducing drug"),
    "Cetirizine": ("Drug", "Antihistamine"),
    "Loratadine": ("Drug", "Antihistamine"),
    "Naproxen": ("Drug", "Anti-inflammatory drug"),
    "Diclofenac": ("Drug", "Anti-inflammatory drug"),
    "Lidocaine": ("Drug", "Local anaesthetic"),
    "Atorvastatin": ("Drug", "Cholesterol-lowering drug"),
    "Losartan": ("Drug", "Blood pressure medication"),
    "Amlodipine": ("Drug", "Blood pressure medication"),
    "Warfarin": ("Drug", "Anticoagulant"),
    "Fluoxetine": ("Drug", "Antidepressant"),
    "Sertraline": ("Drug", "Antidepressant"),
    "Diazepam": ("Drug", "Benzodiazepine"),
    "Melatonin": ("Drug", "Sleep-related hormone"),
    "Dexamethasone": ("Drug", "Corticosteroid"),
    "Hydrocortisone": ("Drug", "Corticosteroid"),
    "Prednisone": ("Drug", "Corticosteroid"),
    "Furosemide": ("Drug", "Diuretic"),
    "Tramadol": ("Drug", "Pain medication"),
    "Triclosan": ("Drug", "Antimicrobial compound"),
    "Nicotine": ("Drug", "Alkaloid"),
    "Theobromine": ("Natural Compound", "Cocoa alkaloid"),
    "Morphine": ("Drug", "Opioid analgesic"),
    "Cholesterol": ("Biomolecule", "Sterol"),
    "Glucose": ("Biomolecule", "Monosaccharide"),
    "Fructose": ("Biomolecule", "Monosaccharide"),
    "Sucrose": ("Biomolecule", "Disaccharide"),
    "Lactose": ("Biomolecule", "Disaccharide"),
    "Maltose": ("Biomolecule", "Disaccharide"),
    "ATP": ("Biomolecule", "Energy-carrying molecule"),
    "Adenine": ("Biomolecule", "Nucleobase"),
    "Guanine": ("Biomolecule", "Nucleobase"),
    "Cytosine": ("Biomolecule", "Nucleobase"),
    "Thymine": ("Biomolecule", "Nucleobase"),
    "Uracil": ("Biomolecule", "Nucleobase"),
    "Glycine": ("Amino Acid", "Simplest amino acid"),
    "Alanine": ("Amino Acid", "Non-essential amino acid"),
    "Valine": ("Amino Acid", "Essential amino acid"),
    "Leucine": ("Amino Acid", "Essential amino acid"),
    "Lysine": ("Amino Acid", "Essential amino acid"),
    "Tryptophan": ("Amino Acid", "Essential amino acid"),
    "Glutamic acid": ("Amino Acid", "Acidic amino acid"),
    "Aspartic acid": ("Amino Acid", "Acidic amino acid"),
    "Water": ("Common Compound", "Universal solvent"),
    "Hydrogen peroxide": ("Common Compound", "Oxidising compound"),
    "Ethanol": ("Common Compound", "Alcohol"),
    "Methanol": ("Common Compound", "Alcohol"),
    "Acetic acid": ("Common Compound", "Organic acid"),
    "Citric acid": ("Common Compound", "Organic acid"),
    "Lactic acid": ("Common Compound", "Organic acid"),
    "Urea": ("Common Compound", "Nitrogen compound"),
    "Ammonia": ("Common Compound", "Nitrogen compound"),
    "Benzene": ("Organic Compound", "Aromatic hydrocarbon"),
    "Toluene": ("Organic Compound", "Aromatic hydrocarbon"),
    "Phenol": ("Organic Compound", "Aromatic compound"),
    "Aniline": ("Organic Compound", "Aromatic amine"),
    "Naphthalene": ("Organic Compound", "Aromatic hydrocarbon"),
    "Pyridine": ("Organic Compound", "Heterocyclic compound"),
    "Imidazole": ("Organic Compound", "Heterocyclic compound"),
    "1,3-Butadiene": ("Organic Compound", "Conjugated diene"),
    "Styrene": ("Organic Compound", "Aromatic compound"),
    "Formaldehyde": ("Organic Compound", "Aldehyde"),
    "Acetone": ("Organic Compound", "Ketone"),
    "Ethylene glycol": ("Organic Compound", "Diol"),
    "Vitamin C": ("Vitamin", "Ascorbic acid"),
    "Vitamin D3": ("Vitamin", "Cholecalciferol"),
    "Vitamin B12": ("Vitamin", "Cobalamin"),
    "Vitamin B6": ("Vitamin", "Pyridoxine"),
    "Niacin": ("Vitamin", "Vitamin B3"),
    "Riboflavin": ("Vitamin", "Vitamin B2"),
    "Thiamine": ("Vitamin", "Vitamin B1"),
    "Folic acid": ("Vitamin", "Vitamin B9"),
    "Adrenaline": ("Biomolecule", "Hormone"),
    "Dopamine": ("Biomolecule", "Neurotransmitter"),
    "Serotonin": ("Biomolecule", "Neurotransmitter"),
    "Melanin": ("Biomolecule", "Pigment"),
    "Quercetin": ("Natural Compound", "Plant flavonoid"),
    "Curcumin": ("Natural Compound", "Turmeric compound"),
    "Resveratrol": ("Natural Compound", "Plant polyphenol"),
    "Capsaicin": ("Natural Compound", "Chilli compound"),
    "Limonene": ("Natural Compound", "Terpene"),
    "Vanillin": ("Natural Compound", "Vanilla flavour compound"),
    "Menthol": ("Natural Compound", "Mint compound"),
    "Linalool": ("Natural Compound", "Terpene alcohol"),
    "Oleic acid": ("Biomolecule", "Fatty acid"),
    "Palmitic acid": ("Biomolecule", "Fatty acid"),
    "Stearic acid": ("Biomolecule", "Fatty acid"),
    "Linoleic acid": ("Biomolecule", "Fatty acid"),
    "Glycerol": ("Common Compound", "Polyol"),
    "Acetylsalicylic acid": ("Drug", "Aspirin chemical name"),
    "Carbon dioxide": ("Common Compound", "Inorganic compound"),
    "Sodium chloride": ("Common Compound", "Ionic compound"),
    "Sulfuric acid": ("Common Compound", "Mineral acid"),
    "Nitric acid": ("Common Compound", "Mineral acid"),
    "Phosphoric acid": ("Common Compound", "Mineral acid")
}


# ==========================================
# PUBCHEM API
# ==========================================

@st.cache_data(ttl=3600, show_spinner=False)
def get_molecule_data(name):
    """Fetch molecular properties from PubChem."""
    safe_name = quote(name, safe="")
    url = (
        "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/"
        + safe_name
        + "/property/"
        "MolecularFormula,MolecularWeight,IUPACName,"
        "CanonicalSMILES,IsomericSMILES,XLogP,TPSA,"
        "HBondDonorCount,HBondAcceptorCount/JSON"
    )

    try:
        response = requests.get(url, timeout=15)

        if response.status_code != 200:
            return None

        payload = response.json()
        properties = payload.get("PropertyTable", {}).get("Properties", [])

        if not properties:
            return None

        return properties[0]

    except (requests.RequestException, ValueError, KeyError):
        return None


@st.cache_data(ttl=3600, show_spinner=False)
def get_molecule_image(name):
    """Fetch 2D structure image from PubChem."""
    safe_name = quote(name, safe="")
    url = (
        "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/"
        + safe_name
        + "/PNG?record_type=2d"
    )

    try:
        response = requests.get(url, timeout=15)

        if response.status_code == 200:
            return response.content

    except requests.RequestException:
        pass

    return None


# ==========================================
# DISPLAY MOLECULE DETAILS
# ==========================================

def display_molecule(name):
    st.markdown("---")
    st.markdown(
        f'<div class="section-title">🧬 {name}</div>',
        unsafe_allow_html=True
    )

    category, description = MOLECULES.get(
        name, ("Compound", "Chemical compound")
    )

    st.markdown(
        f"""
        <div class="glass-card">
            <div class="card-title">🌸 {name}</div>
            <div class="card-text">
                Category: {category}<br>
                Description: {description}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    with st.spinner("✨ Fetching molecular information..."):
        data = get_molecule_data(name)
        image_data = get_molecule_image(name)

    if image_data:
        st.subheader("🔬 2D Molecular Structure")
        st.image(
            image_data,
            caption=f"2D structure of {name} — PubChem",
            width=340
        )
    else:
        st.info(
            "The 2D structure image could not be loaded. "
            "Please check your internet connection or try another compound."
        )

    if data:
        formula = data.get("MolecularFormula", "Not available")
        weight = data.get("MolecularWeight", "Not available")
        iupac = data.get("IUPACName", "Not available")
        smiles = data.get(
            "ConnectivitySMILES",
            data.get("CanonicalSMILES", "Not available")
        )
        logp = data.get("XLogP", "Not available")
        tpsa = data.get("TPSA", "Not available")
        donors = data.get("HBondDonorCount", "Not available")
        acceptors = data.get("HBondAcceptorCount", "Not available")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("🧪 Molecular Formula", formula)

        with col2:
            st.metric("⚖️ Molecular Weight", f"{weight} g/mol")

        with col3:
            st.metric("💧 H-Bond Donors", str(donors))

        col4, col5, col6 = st.columns(3)

        with col4:
            st.metric("🌿 XLogP", str(logp))

        with col5:
            st.metric("🫧 TPSA", f"{tpsa} Å²")

        with col6:
            st.metric("🔗 H-Bond Acceptors", str(acceptors))

        with st.expander("📚 Advanced Molecular Information"):
            st.write("**IUPAC Name:**")
            st.write(iupac)

            st.write("**Canonical SMILES:**")
            st.code(smiles, language=None)

        st.caption(
            "Source: PubChem. Values may vary with the selected compound record."
        )

    else:
        st.warning(
            "Molecular properties are unavailable from PubChem right now. "
            "Try again later or check the spelling."
        )

    st.markdown(
        f"""
        <div class="small-note">
        💡 <b>Study note:</b> {name} is listed under
        <b>{category}</b>. Use this page for educational exploration
        of chemical structures and molecular properties.
        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================
# SIDEBAR NAVIGATION
# ==========================================

st.sidebar.markdown(
    """
    <div style="text-align:center; padding:15px 5px;">
        <div style="font-size:48px;">🧬</div>
        <div style="
            font-size:25px;
            font-weight:800;
            color:#C45F8A;">
            ChemNexa
        </div>
        <div style="
            font-size:11px;
            color:#A57991;
            letter-spacing:1px;">
            PEACH GLOW EDITION
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "🌷 Explore ChemNexa",
    [
        "🏠 Home",
        "🧬 Molecule Explorer",
        "💊 Drug Database",
        "📚 Chemistry Library",
        "✨ About ChemNexa"
    ]
)

st.sidebar.markdown("---")

st.sidebar.markdown(
    """
    <div class="glass-card" style="padding:15px;">
        <div class="card-title">🌸 Your Lab</div>
        <div class="card-text">
            Explore compounds, discover structures,
            and learn chemistry beautifully.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.caption("Made for curious chemistry minds ✨")


# ==========================================
# HOME PAGE
# ==========================================

if page == "🏠 Home":

    st.markdown(
        """
        <div class="hero">
            <div style="font-size:42px;">🌷 🧬 🌷</div>
            <div class="hero-title">ChemNexa</div>
            <div class="hero-subtitle">
                Explore Molecules. Discover Chemistry.
            </div>
            <div class="hero-badge">
                ✨ YOUR AESTHETIC MOLECULAR LAB ✨
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">🌸 Welcome to your lab</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Discover chemical compounds, explore molecular structures, "
        "and learn about the science behind everyday molecules."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="glass-card">
                <div class="card-icon">🧬</div>
                <div class="card-title">Molecule Explorer</div>
                <div class="card-text">
                    Search compounds and explore molecular
                    formulas, structures, and properties.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="glass-card">
                <div class="card-icon">💊</div>
                <div class="card-title">Drug Database</div>
                <div class="card-text">
                    Explore drug-related compounds and
                    learn their chemical information.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="glass-card">
                <div class="card-icon">🔬</div>
                <div class="card-title">Chemistry Library</div>
                <div class="card-text">
                    Discover organic compounds, amino acids,
                    vitamins, and biomolecules.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        '<div class="section-title">✨ Quick Discover</div>',
        unsafe_allow_html=True
    )

    featured = [
        ("Aspirin", "💊"),
        ("Caffeine", "☕"),
        ("Glucose", "🍯"),
        ("Vitamin C", "🍊"),
        ("Dopamine", "🧠"),
        ("Benzene", "🧪")
    ]

    columns = st.columns(3)

    for index, item in enumerate(featured):
        molecule, icon = item

        with columns[index % 3]:
            st.markdown(
                f"""
                <div class="glass-card" style="text-align:center;">
                    <div class="card-icon">{icon}</div>
                    <div class="card-title">{molecule}</div>
                    <div class="card-text">Featured compound</div>
                </div>
                """,
                unsafe_allow_html=True
            )

            if st.button(
                f"Explore {molecule} ✨",
                key=f"home_{molecule}"
            ):
                st.session_state["selected_molecule"] = molecule
                st.session_state["show_molecule"] = True
                st.rerun()

    if st.session_state.get(