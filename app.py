import streamlit as st
import requests
from urllib.parse import quote

# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title="ChemNexa | Molecular Explorer",
    page_icon="🧪",
    layout="wide"
)

# ---------------- CUSTOM DESIGN ----------------

st.markdown("""
<style>
.stApp {
    background-color: #0b1020;
    color: #f1f5f9;
}
[data-testid="stSidebar"] {
    background-color: #111a2e;
}
h1, h2, h3 {
    color: #67e8f9;
}
div.stButton > button {
    border-radius: 10px;
    border: 1px solid #22d3ee;
}
</style>
""", unsafe_allow_html=True)

# ---------------- MOLECULE DATABASE ----------------

MOLECULES = {
    "Aspirin": "Aspirin",
    "Paracetamol": "Acetaminophen",
    "Ibuprofen": "Ibuprofen",
    "Caffeine": "Caffeine",
    "Amoxicillin": "Amoxicillin",
    "Penicillin": "Penicillin G",
    "Metformin": "Metformin",
    "Omeprazole": "Omeprazole",
    "Atorvastatin": "Atorvastatin",
    "Insulin": "Insulin",
    "Glucose": "Glucose",
    "Sucrose": "Sucrose",
    "Citric Acid": "Citric acid",
    "Ascorbic Acid": "Ascorbic acid",
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
    "DNA base Adenine": "Adenine",
    "Guanine": "Guanine",
    "Cytosine": "Cytosine",
    "Thymine": "Thymine",
    "Urea": "Urea",
    "Chlorophyll": "Chlorophyll a",
    "Hemoglobin": "Hemoglobin",
    "Lidocaine": "Lidocaine",
    "Warfarin": "Warfarin",
    "Hydroxychloroquine": "Hydroxychloroquine",
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
    "ATP": "Adenosine triphosphate",
    "ADP": "Adenosine diphosphate",
    "Carbon Dioxide": "Carbon dioxide",
    "Water": "Water",
    "Ammonia": "Ammonia",
    "Sodium Chloride": "Sodium chloride",
    "Hydrogen Peroxide": "Hydrogen peroxide",
    "Sulfuric Acid": "Sulfuric acid",
    "Calcium Carbonate": "Calcium carbonate"
}

# ---------------- PUBCHEM FUNCTIONS ----------------

@st.cache_data(ttl=3600, show_spinner=False)
def get_pubchem_data(name):
    url = (
        "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/"
        + quote(name, safe="")
        + "/property/MolecularFormula,MolecularWeight,"
        "IUPACName,CanonicalSMILES/JSON"
    )

    try:
        response = requests.get(url, timeout=20)
        response.raise_for_status()
        result = response.json()
        properties = result["PropertyTable"]["Properties"]

        if properties:
            return properties[0]

        return None

    except (requests.RequestException, ValueError, KeyError, IndexError):
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


# ---------------- SIDEBAR ----------------

with st.sidebar:
    st.markdown("# 🧪 ChemNexa")
    st.caption("Explore Molecules. Discover Chemistry.")
    st.divider()

    page = st.radio(
        "NAVIGATION",
        [
            "Home",
            "Molecule Explorer",
            "Drug Database",
            "Chemistry Library",
            "About"
        ]
    )

    st.divider()
    st.caption("Powered by PubChem")
    st.caption("Educational Chemistry Project")


# ---------------- HOME PAGE ----------------

if page == "Home":
    st.title("🧪 ChemNexa")
    st.subheader("Explore Molecules. Discover Chemistry.")

    st.markdown("""
    Welcome to **ChemNexa**, an interactive molecular exploration
    platform designed for students and chemistry enthusiasts.

    Discover chemical structures, molecular formulas, molecular
    weights, IUPAC names and molecular information.
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Molecules in Catalogue", len(MOLECULES))

    with col2:
        st.metric("Main Features", "5+")

    with col3:
        st.metric("Data Source", "PubChem")

    st.divider()
    st.header("✨ Explore Chemistry")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("""
        ### 🔍 Molecule Explorer
        Search for a chemical compound and explore its properties
        and 2D structure.
        """)

    with c2:
        st.markdown("""
        ### 💊 Drug Database
        Explore information about selected pharmaceutical compounds.
        This is an educational reference, not medical advice.
        """)

    st.info(
        "Select a section from the sidebar to begin exploring."
    )


# ---------------- MOLECULE EXPLORER ----------------

elif page == "Molecule Explorer":
    st.title("🔍 Molecule Explorer")

    st.write(
        "Select a molecule or enter a compound name to explore it."
    )

    search_mode = st.radio(
        "Choose search method",
        ["Choose from catalogue", "Enter molecule name"],
        horizontal=True
    )

    if search_mode == "Choose from catalogue":
        selected_label = st.selectbox(
            "Select a molecule",
            sorted(MOLECULES.keys())
        )
        compound_name = MOLECULES[selected_label]

    else:
        compound_name = st.text_input(
            "Enter compound name",
            placeholder="Example: Aspirin, Caffeine, Glucose"
        ).strip()

    if st.button("🔬 Explore Molecule", use_container_width=True):
        if not compound