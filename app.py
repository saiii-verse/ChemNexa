import streamlit as st
import requests
from urllib.parse import quote

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="ChemNexa | Molecular Explorer",
    page_icon="🧪",
    layout="wide"
)

# ==========================================
# CUSTOM STYLE
# ==========================================

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
.stButton button {
    border-radius: 10px;
    border: 1px solid #22d3ee;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# MOLECULE DATABASE
# ==========================================

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
    "Insulin": "Insulin",
    "Chlorophyll": "Chlorophyll a",
    "Hemoglobin": "Hemoglobin",
    "Hydroxychloroquine": "Hydroxychloroquine",
    "Naproxen Sodium": "Naproxen sodium",
    "Loratadine": "Loratadine",
    "Cetirizine": "Cetirizine",
    "Montelukast": "Montelukast",
    "Levodopa": "Levodopa"
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
    "Montelukast"
]

# ==========================================
# PUBCHEM DATA FUNCTIONS
# ==========================================

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

    st.success("Molecule information loaded!")

    st.subheader(name)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🧬 2D Structure")
        st.image(
            get_structure_image(name),
            caption="2D molecular structure",
            use_container_width=True
        )

    with col2:
        st.markdown("### ⚗️ Chemical Properties")

        st.write(
            "**Molecular Formula:**",
            data.get("MolecularFormula", "Unavailable")
        )

        st.write(
            "**Molecular Weight:**",
            str(data.get("MolecularWeight", "Unavailable"))
            + " g/mol"
        )

        st.write(
            "**IUPAC Name:**",
            data.get("IUPACName", "Unavailable")
        )

        st.write(
            "**Canonical SMILES:**",
            data.get("ConnectivitySMILES", "Unavailable")
        )

    st.link_button(
        "🌐 View Full Information on PubChem",
        get_pubchem_link(name)
    )

# ==========================================
# SIDEBAR NAVIGATION
# ==========================================

with st.sidebar:
    st.title("🧪 ChemNexa")
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
    st.caption("Chemical Information: PubChem")
    st.caption("Educational Project")

# ==========================================
# HOME PAGE
# ==========================================

if page == "Home":
    st.title("🧪 ChemNexa")
    st.subheader("Explore Molecules. Discover Chemistry.")

    st.markdown("""
    Welcome to **ChemNexa**, an interactive chemistry application.

    Explore chemical compounds, discover molecular structures,
    and learn about important chemical properties.

    ### ✨ What can you explore?
    - Molecular formula and molecular weight
    - IUPAC chemical names
    - Canonical SMILES
    - 2D molecular structures
    - Pharmaceutical compounds
    - A searchable chemical catalogue
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Molecules", len(MOLECULES))

    with col2:
        st.metric("Drug Compounds", len(DRUGS))

    with col3:
        st.metric("Data Source", "PubChem")

    st.divider()
    st.info(
        "Choose a page from the sidebar to start exploring."
    )

# ==========================================
# MOLECULE EXPLORER
# ==========================================

elif page == "Molecule Explorer":
    st.title("🔍 Molecule Explorer")

    st.write(
        "Select a compound from the catalogue or search by name."
    )

    search_type = st.radio(
        "Search Method",
        ["Catalogue", "Custom Search"],
        horizontal=True
    )

    compound_name = ""

    if search_type == "Catalogue":
        selected = st.selectbox(
            "Choose a molecule",
            sorted(MOLECULES.keys())
        )
        compound_name = MOLECULES[selected]

    else:
        compound_name = st.text_input(
            "Enter molecule name",
            placeholder="Example: Caffeine or Glucose"
        ).strip()

    if st.button("🔬 Explore Molecule", use_container_width=True):
        if not compound_name:
            st.warning("Please enter or select a molecule.")
        else:
            display_molecule(compound_name)

# ==========================================
# DRUG DATABASE
# ==========================================

elif page == "Drug Database":
    st.title("💊 Drug Database")

    st.warning(
        "For educational purposes only. This page does not provide "
        "medical advice or dosage recommendations."
    )

    selected_drug = st.selectbox(
        "Select a drug compound",
        DRUGS
    )

    if st.button("View Drug Molecule", use_container_width=True):
        display_molecule(selected_drug)

# ==========================================
# CHEMISTRY LIBRARY
# ==========================================

elif page == "Chemistry Library":
    st.title("📚 Chemistry Library")

    search_text = st.text_input(
        "Search the catalogue",
        placeholder="Type a chemical or molecule name"
    ).strip().lower()

    matches = [
        (label, name)
        for label, name in MOLECULES.items()
        if search_text in label.lower()
        or search_text in name.lower()
    ]

    st.write("Matching molecules:", len(matches))

    for label, name in matches:
        with st.expander("🧪 " + label):
            st.write("Compound:", name)

            if st.button(
                "Explore " + label,
                key="explore_" + label
            ):
                display_molecule(name)

            st.link_button(
                "Open on PubChem",
                get_pubchem_link(name)
            )

# ==========================================
# ABOUT PAGE
# ==========================================

elif page == "About":
    st.title("ℹ️ About ChemNexa")

    st.markdown("""
    **ChemNexa** is an educational chemistry application created
    to make molecular exploration simple and accessible.

    ### Technologies Used
    - Python
    - Streamlit
    - Requests
    - PubChem PUG REST API

    ### Main Features
    - Chemical compound search
    - Molecular property display
    - 2D structure images
    - Drug molecule catalogue
    - Links to chemical reference information

    ### Data Source
    Chemical data is retrieved from PubChem when available.

    ### Disclaimer
    This application is intended for educational use only.
    Information may be unavailable for certain compounds.
    It is not a medical diagnosis or treatment tool.
    """)

    st.link_button(
        "🌐 Visit PubChem",
        "https://pubchem.ncbi.nlm.nih.gov/"
    )

    st.divider()
    st.caption("ChemNexa | Explore Molecules. Discover Chemistry.")