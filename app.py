import streamlit as st
import requests
from urllib.parse import quote

# ==================================================
# CHEMNEXA - AURORA GLASS LAB
# ==================================================

st.set_page_config(
    page_title="ChemNexa | Molecular Explorer",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================================================
# AURORA GLASS LAB THEME
# ==================================================

st.markdown("""
<style>
@import url(
'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'
);

.stApp {
    background:
        radial-gradient(
            ellipse at 5% 0%,
            rgba(124, 58, 237, 0.20),
            transparent 35%
        ),
        radial-gradient(
            ellipse at 95% 15%,
            rgba(6, 182, 212, 0.14),
            transparent 30%
        ),
        #080c18;
    color: #e2e8f0;
    font-family: 'Inter', sans-serif;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #17142d,
        #0c1426 70%,
        #101b2d
    );
    border-right: 1px solid rgba(139, 92, 246, 0.30);
}

h1 {
    color: #ffffff !important;
    font-weight: 800 !important;
    letter-spacing: -1px;
}

h2 {
    color: #a5f3fc !important;
    font-weight: 700 !important;
}

h3 {
    color: #c4b5fd !important;
    font-weight: 700 !important;
}

p, li {
    color: #cbd5e1;
    line-height: 1.7;
}

[data-testid="stMetric"] {
    background: linear-gradient(
        135deg,
        rgba(124, 58, 237, 0.15),
        rgba(8, 145, 178, 0.12)
    );
    border: 1px solid rgba(139, 92, 246, 0.32);
    padding: 18px;
    border-radius: 18px;
}

[data-testid="stMetricValue"] {
    color: #67e8f9;
    font-weight: 800;
}

[data-testid="stMetricLabel"] {
    color: #c4b5fd;
}

[data-testid="stExpander"] {
    background: rgba(20, 27, 48, 0.72);
    border: 1px solid rgba(139, 92, 246, 0.25);
    border-radius: 14px;
}

.stButton > button {
    background: linear-gradient(
        110deg,
        #7c3aed,
        #0891b2
    );
    color: white;
    border: 1px solid rgba(103, 232, 249, 0.35);
    border-radius: 12px;
    padding: 0.65rem 1rem;
    font-weight: 700;
    transition: all 0.2s ease;
}

.stButton > button:hover {
    border-color: #67e8f9;
    box-shadow: 0 0 18px rgba(34, 211, 238, 0.25);
    color: white;
}

.stLinkButton > a {
    background: linear-gradient(
        110deg,
        #7c3aed,
        #0891b2
    );
    color: white !important;
    border: 1px solid rgba(103, 232, 249, 0.35);
    border-radius: 12px;
    font-weight: 700;
}

.stTextInput input {
    background: #111a2e;
    color: #f8fafc;
    border-radius: 10px;
    border: 1px solid #334155;
}

[data-baseweb="select"] > div {
    background: #111a2e;
    border-color: #475569;
    border-radius: 10px;
}

[data-testid="stImage"] img {
    border-radius: 16px;
}

[data-testid="stAlert"] {
    border-radius: 14px;
}

hr {
    border-color: rgba(148, 163, 184, 0.20);
}

[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label {
    color: #ddd6fe !important;
}

small {
    color: #94a3b8;
}
</style>
""", unsafe_allow_html=True)

# ==================================================
# MOLECULE DATABASE
# ==================================================

MOLECULES = {
    "Aspirin": "Aspirin",
    "Paracetamol": "Acetaminophen",
    "Ibuprofen": "Ibuprofen",
    "Caffeine": "Caffeine",
    "Amoxicillin": "Amoxicillin",
    "Penicillin G": "Penicillin G",
    "Metformin": "Metformin",
    "Omeprazole": "Omeprazole",
    "Atorvastatin": "Atorvastatin",
    "Insulin": "Insulin",
    "Glucose": "Glucose",
    "Sucrose": "Sucrose",
    "Citric Acid": "Citric acid",
    "Vitamin C": "Ascorbic acid",
    "Urea": "Urea",
    "Ethanol": "Ethanol",
    "Methanol": "Methanol",
    "Acetic Acid": "Acetic acid",
    "Benzene": "Benzene",
    "Toluene": "Toluene",
    "Phenol": "Phenol",
    "Aniline": "Aniline",
    "Naphthalene": "Naphthalene",
    "Cholesterol": "Cholesterol",
    "Adrenaline": "Epinephrine",
    "Dopamine": "Dopamine",
    "Serotonin": "Serotonin",
    "Nicotine": "Nicotine",
    "Lactic Acid": "Lactic acid",
    "Formaldehyde": "Formaldehyde",
    "Acetone": "Acetone",
    "Ethylene": "Ethylene",
    "Propane": "Propane",
    "Butane": "Butane",
    "Glycine": "Glycine",
    "Alanine": "Alanine",
    "Adenine": "Adenine",
    "Guanine": "Guanine",
    "Cytosine": "Cytosine",
    "Thymine": "Thymine",
    "ATP": "Adenosine triphosphate",
    "ADP": "Adenosine diphosphate",
    "Water": "Water",
    "Ammonia": "Ammonia",
    "Carbon Dioxide": "Carbon dioxide",
    "Hydrogen Peroxide": "Hydrogen peroxide",
    "Calcium Carbonate": "Calcium carbonate",
    "Lidocaine": "Lidocaine",
    "Warfarin": "Warfarin",
    "Dexamethasone": "Dexamethasone",
    "Ciprofloxacin": "Ciprofloxacin",
    "Azithromycin": "Azithromycin",
    "Losartan": "Losartan",
    "Naproxen": "Naproxen",
    "Diclofenac": "Diclofenac",
    "Fluoxetine": "Fluoxetine",
    "Propranolol": "Propranolol",
    "Melatonin": "Melatonin",
    "Riboflavin": "Riboflavin",
    "Thiamine": "Thiamine",
    "Folic Acid": "Folic acid",
    "Loratadine": "Loratadine",
    "Cetirizine": "Cetirizine",
    "Montelukast": "Montelukast",
    "Levodopa": "Levodopa",
    "Vitamin D3": "Cholecalciferol",
    "Vitamin B12": "Cyanocobalamin",
    "Hydroxychloroquine": "Hydroxychloroquine",
    "Hydrocortisone": "Hydrocortisone",
    "Lactose": "Lactose",
    "Maltose": "Maltose",
    "Fructose": "Fructose",
    "Acetone": "Acetone",
    "Ethylene Glycol": "Ethylene glycol",
    "Sodium Bicarbonate": "Sodium bicarbonate",
    "Sulfuric Acid": "Sulfuric acid",
    "Hydrochloric Acid": "Hydrochloric acid"
}

DRUGS = [
    "Aspirin",
    "Paracetamol",
    "Ibuprofen",
    "Amoxicillin",
    "Metformin",
    "Omeprazole",
    "Atorvastatin",
    "Ciprofloxacin",
    "Azithromycin",
    "Lidocaine",
    "Warfarin",
    "Dexamethasone",
    "Losartan",
    "Naproxen",
    "Diclofenac",
    "Fluoxetine",
    "Propranolol",
    "Hydroxychloroquine",
    "Loratadine",
    "Cetirizine",
    "Montelukast",
    "Levodopa"
]

# ==================================================
# PUBCHEM API
# ==================================================

@st.cache_data(ttl=3600, show_spinner=False)
def get_pubchem_data(name):
    url = (
        "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/"
        + quote(name, safe="")
        + "/property/MolecularFormula,MolecularWeight,"
        "IUPACName,ConnectivitySMILES/JSON"
    )

    try:
        response = requests.get(url, timeout=20)
        response.raise_for_status()

        result = response.json()
        properties = result["PropertyTable"]["Properties"]

        if properties:
            return properties[0]

        return None

    except (
        requests.RequestException,
        ValueError,
        KeyError,
        IndexError
    ):
        return None


def get_structure_image(name):
    return (
        "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/"
        + quote(name, safe="")
        + "/PNG"
    )


def get_pubchem_link(name):
    return (
        "https://pubchem.ncbi.nlm.nih.gov/#query="
        + quote(name, safe="")
    )


# ==================================================
# MOLECULE DISPLAY FUNCTION
# ==================================================

def display_molecule(name):
    with st.spinner("Loading molecular information..."):
        data = get_pubchem_data(name)

    if data is None:
        st.error(
            "Molecule information could not be loaded. "
            "Check the name or try again later."
        )
        st.link_button(
            "Search on PubChem",
            get_pubchem_link(name)
        )
        return

    st.success("Molecular information loaded!")

    st.markdown(f"## 🧬 {name}")
    st.divider()

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("### 2D Molecular Structure")

        st.image(
            get_structure_image(name),
            caption=f"Structure of {name}",
            use_container_width=True
        )

    with col2:
        st.markdown("### ⚗️ Chemical Properties")

        st.write(
            "**Molecular Formula**",
            data.get("MolecularFormula", "Unavailable")
        )

        st.write(
            "**Molecular Weight**",
            str(data.get("MolecularWeight", "Unavailable"))
            + " g/mol"
        )

        st.write(
            "**IUPAC Name**",
            data.get("IUPACName", "Unavailable")
        )

        st.write(
            "**Canonical SMILES**",
            data.get("ConnectivitySMILES", "Unavailable")
        )

    st.link_button(
        "🌐 Explore on PubChem",
        get_pubchem_link(name)
    )


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:
    st.markdown("# 🧪 ChemNexa")
    st.caption("AURORA GLASS LAB")
    st.caption("Explore Molecules. Discover Chemistry.")

    st.divider()

    page = st.radio(
        "EXPLORE",
        [
            "Home",
            "Molecule Explorer",
            "Drug Database",
            "Chemistry Library",
            "About"
        ]
    )

    st.divider()

    st.markdown("### 🔬 Research Tools")
    st.caption("Chemical data powered by PubChem.")
    st.caption("Educational use only.")


# ==================================================
# HOME PAGE
# ==================================================

if page == "Home":
    st.markdown("## ✨ WELCOME TO")

    st.title("🧪 ChemNexa")

    st.markdown(
        "### Explore Molecules. Discover Chemistry."
    )

    st.markdown("""
    An interactive molecular exploration platform designed
    for students, researchers and chemistry enthusiasts.
    Discover chemical structures and explore molecular properties
    through a clean, modern interface.
    """)

    st.divider()

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Molecule Catalogue",
            f"{len(MOLECULES)}+"
        )

    with c2:
        st.metric(
            "Drug Compounds",
            f"{len(DRUGS)}+"
        )

    with c3:
        st.metric(
            "Data Source",
            "PubChem"
        )

    st.markdown("## 💎 Explore Your Lab")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### 🔍 Molecule Explorer

        Search chemical compounds and discover their
        molecular formula, weight, IUPAC name, SMILES
        and 2D molecular structures.
        """)

    with col2:
        st.markdown("""
        ### 💊 Drug Database

        Browse selected pharmaceutical compounds and
        explore their publicly available chemical properties.
        """)

    st.markdown("## 🧬 Featured Molecules")

    featured = [
        "Caffeine",
        "Aspirin",
        "Glucose",
        "Dopamine"
    ]

    cols = st.columns(4)

    for index, molecule in enumerate(featured):
        with cols[index]:
            st.markdown(f"### {molecule}")
            st.caption("Explore chemical information")

            if st.button(
                "Explore",
                key=f"featured_{molecule}"
            ):
                st.session_state["selected_molecule"] = molecule
                st.session_state["open_featured"] = True

    if st.session_state.get("open_featured", False):
        selected_molecule = st.session_state.get(
            "selected_molecule",
            "Caffeine"
        )

        st.divider()
        display_molecule(selected_molecule)

        if st.button("Close molecule details"):
            st.session_state["open_featured"] = False
            st.rerun()


# ==================================================
# MOLECULE EXPLORER
# ==================================================

elif page == "Molecule Explorer":
    st.title("🔍 Molecule Explorer")

    st.markdown(
        "Search the catalogue or enter a compound name."
    )

    search_method = st.radio(
        "Choose Search Method",
        ["Catalogue Search", "Custom Search"],
        horizontal=True
    )

    compound_name = ""

    if search_method == "Catalogue Search":
        selected_label = st.selectbox(
            "Select Molecule",
            sorted(MOLECULES.keys())
        )

        compound_name = MOLECULES[selected_label]

    else:
        compound_name = st.text_input(
            "Enter Compound Name",
            placeholder="Example: Caffeine, Aspirin, Glucose"
        ).strip()

    if st.button(
        "🔬 Explore Molecule",
        use_container_width=True
    ):
        if not compound_name:
            st.warning("Please enter or select a molecule.")
        else:
            display_molecule(compound_name)


# ==================================================
# DRUG DATABASE
# ==================================================

elif page == "Drug Database":
    st.title("💊 Drug Database")

    st.warning(
        "Educational reference only. This application does not "
        "provide medical advice, diagnosis or dosage recommendations."
    )

    selected_drug = st.selectbox(
        "Select a Drug Compound",
        DRUGS
    )

    if st.button(
        "View Drug Molecule",
        use_container_width=True
    ):
        display_molecule(selected_drug)


# ==================================================
# CHEMISTRY LIBRARY
# ==================================================

elif page == "Chemistry Library":
    st.title("📚 Chemistry Library")

    st.markdown(
        "Browse the catalogue and find chemical compounds."
    )

    search_text = st.text_input(
        "Search Catalogue",
        placeholder="Type a compound name"
    ).strip().lower()

    matches = [
        (label, name)
        for label, name in MOLECULES.items()
        if search_text in label.lower()
        or search_text in name.lower()
    ]

    st.write(f"**Matching Compounds:** {len(matches)}")

    for label, name in matches:
        with st.expander(f"🧪 {label}"):
            st.write("**Compound Name:**", name)

            st.link_button(
                "🌐 Open on PubChem",
                get_pubchem_link(name)
            )

            if st.button(
                f"Explore {label}",
                key=f"library_{label}"
            ):
                st.session_state["library_selected"] = name

    if "library_selected" in st.session_state:
        st.divider()

        display_molecule(
            st.session_state["library_selected"]
        )


# ==================================================
# ABOUT PAGE
# ==================================================

elif page == "About":
    st.title("ℹ️ About ChemNexa")

    st.markdown("""
    ### Explore Molecules. Discover Chemistry.

    **ChemNexa** is an educational chemistry application
    built to make molecular exploration accessible and interactive.

    ### ✨ Key Features

    - Search chemical compounds
    - View molecular formula and molecular weight
    - Explore IUPAC names and SMILES
    - View 2D molecular structures
    - Browse a drug compound catalogue
    - Access external chemical reference information

    ### 🛠️ Technologies

    - Python
    - Streamlit
    - Requests
    - PubChem PUG REST API

    ### 🌐 Data Source

    Chemical information is requested from PubChem,
    a public chemical information resource.

    ### ⚠️ Disclaimer

    This application is intended for educational purposes.
    Chemical data may not be available for every compound.
    Drug information is not medical advice.
    """)

    st.link_button(
        "Visit PubChem",
        "https://pubchem.ncbi.nlm.nih.gov/"
    )

    st.divider()

    st.caption(
        "ChemNexa | Aurora Glass Lab | Educational Project"
    )