import streamlit as st
import requests
import json

st.set_page_config(
page_title="ChemNexa | Molecular Explorer",
page_icon="🧪",
layout="wide"
)

st.markdown("""

<style>
.stApp {
    background-color: #081421;
    color: #f1f5f9;
}
[data-testid="stSidebar"] {
    background-color: #102438;
}
h1, h2, h3 {
    color: #55E6C1 !important;
}
div[data-testid="stMetric"] {
    background: #142B40;
    padding: 15px;
    border-radius: 12px;
    border: 1px solid #28516A;
}
div.stButton > button {
    background-color: #55E6C1;
    color: #081421;
    border-radius: 8px;
    font-weight: bold;
}
</style>""", unsafe_allow_html=True)

MOLECULES = {
"Aspirin": ("C9H8O4", 180.16),
"Paracetamol": ("C8H9NO2", 151.16),
"Ibuprofen": ("C13H18O2", 206.28),
"Caffeine": ("C8H10N4O2", 194.19),
"Glucose": ("C6H12O6", 180.16),
"Benzene": ("C6H6", 78.11),
"Ethanol": ("C2H6O", 46.07),
"Methane": ("CH4", 16.04),
"Urea": ("CH4N2O", 60.06),
"Citric Acid": ("C6H8O7", 192.12),
"Lactic Acid": ("C3H6O3", 90.08),
"Glycine": ("C2H5NO2", 75.07),
"Alanine": ("C3H7NO2", 89.09),
"Naproxen": ("C14H14O3", 230.26),
"Cholesterol": ("C27H46O", 386.65),
"Vitamin C": ("C6H8O6", 176.12),
"Metformin": ("C4H11N5", 129.16),
"Amoxicillin": ("C16H19N3O5S", 365.40),
"Lidocaine": ("C14H22N2O", 234.34),
"Benzamide": ("C7H7NO", 121.14),
"Acetic Acid": ("C2H4O2", 60.05),
"Formaldehyde": ("CH2O", 30.03),
"Propane": ("C3H8", 44.10),
"Uric Acid": ("C5H4N4O3", 168.11),
"Nicotinamide": ("C6H6N2O", 122.12)
}

DRUGS = [
"Aspirin", "Paracetamol", "Ibuprofen", "Caffeine",
"Naproxen", "Metformin", "Amoxicillin", "Lidocaine"
]

def get_pubchem_data(name):
url = (
"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/"
f"name/{requests.utils.quote(name)}/property/"
"MolecularFormula,MolecularWeight,CanonicalSMILES,"
"IUPACName/JSON"
)
response = requests.get(url, timeout=15)
response.raise_for_status()
data = response.json()
return data["PropertyTable"]["Properties"][0]

def get_structure_image(name):
return (
"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/"
f"name/{requests.utils.quote(name)}/PNG"
)

st.sidebar.markdown("# 🧪 ChemNexa")
st.sidebar.caption("MOLECULAR DISCOVERY PLATFORM")

page = st.sidebar.radio(
"NAVIGATION",
[
"Home",
"Molecule Explorer",
"Drug Database",
"3D Molecular Lab",
"Chemistry Library",
"About"
]
)

st.sidebar.divider()
st.sidebar.caption("Explore Molecules. Discover Chemistry.")

if page == "Home":
st.title("🧪 ChemNexa")
st.subheader("Explore Molecules. Discover Chemistry.")
st.write(
"Your interactive platform for exploring chemical "
"compounds, molecular structures and drug molecules."
)

c1, c2, c3 = st.columns(3)
c1.metric("Compound Library", len(MOLECULES))
c2.metric("Drug Compounds", len(DRUGS))
c3.metric("Data Source", "PubChem")

st.markdown("## ✨ Featured Molecules")

cols = st.columns(2)

for i, name in enumerate(
    ["Aspirin", "Caffeine", "Glucose", "Benzene"]
):
    formula, weight = MOLECULES[name]

    with cols[i % 2]:
        st.markdown(f"### 🧬 {name}")
        st.write(f"Formula: `{formula}`")
        st.write(f"Molecular weight: {weight} g/mol")
        st.divider()

st.info("Select Molecule Explorer to investigate compounds.")

elif page == "Molecule Explorer":
st.title("🔬 Molecule Explorer")

query = st.text_input(
    "Search by compound name",
    placeholder="Example: Aspirin, Caffeine, Glucose"
)

if query:
    if query.strip().lower() in {
        n.lower() for n in MOLECULES
    }:
        name = next(
            n for n in MOLECULES
            if n.lower() == query.strip().lower()
        )

        formula, weight = MOLECULES[name]

        st.markdown(f"## 🧬 {name}")
        c1, c2 = st.columns(2)
        c1.metric("Molecular Formula", formula)
        c2.metric("Molecular Weight", f"{weight} g/mol")

        try:
            info = get_pubchem_data(name)

            st.markdown("### Chemical Information")
            st.write(
                "**IUPAC Name:**",
                info.get("IUPACName", "Not available")
            )
            st.write(
                "**Canonical SMILES:**",
                info.get("ConnectivitySMILES", "Not available")
            )

            st.markdown("### 2D Molecular Structure")
            st.image(
                get_structure_image(name),
                caption=f"PubChem structure: {name}",
                use_container_width=True
            )

        except Exception:
            st.warning(
                "Live PubChem information is unavailable. "
                "Showing the built-in compound information."
            )

            st.write("Compound:", name)
            st.write("Formula:", formula)
            st.write("Molecular weight:", weight, "g/mol")

    else:
        st.info("Searching PubChem for your compound...")

        try:
            info = get_pubchem_data(query.strip())

            st.markdown(f"## 🧬 {query.strip()}")

            st.write(
                "**Molecular Formula:**",
                info.get("MolecularFormula", "N/A")
            )
            st.write(
                "**Molecular Weight:**",
                info.get("MolecularWeight", "N/A"),
                "g/mol"
            )
            st.write(
                "**IUPAC Name:**",
                info.get("IUPACName", "N/A")
            )
            st.write(
                "**SMILES:**",
                info.get("ConnectivitySMILES", "N/A")
            )

            st.markdown("### 2D Molecular Structure")
            st.image(
                get_structure_image(query.strip()),
                caption="PubChem molecular structure",
                use_container_width=True
            )

        except Exception:
            st.error(
                "Compound not found or PubChem is unavailable. "
                "Check the spelling and try again."
            )

else:
    st.markdown("### Popular Compounds")

    for name, (formula, weight) in MOLECULES.items():
        with st.expander(name):
            st.write("Formula:", formula)
            st.write("Molecular weight:", weight, "g/mol")

elif page == "Drug Database":
st.title("💊 Drug Molecule Database")

selected = st.selectbox("Select a compound", DRUGS)

formula, weight = MOLECULES[selected]

st.markdown(f"## {selected}")
st.metric("Molecular Formula", formula)
st.metric("Molecular Weight", f"{weight} g/mol")

if st.button("Load Chemical Information"):
    with st.spinner("Connecting to PubChem..."):
        try:
            info = get_pubchem_data(selected)

            st.success("Compound information retrieved!")

            st.write(
                "**IUPAC Name:**",
                info.get("IUPACName", "N/A")
            )
            st.write(
                "**SMILES:**",
                info.get("ConnectivitySMILES", "N/A")
            )

            st.image(
                get_structure_image(selected),
                caption=f"Structure of {selected}",
                use_container_width=True
            )

        except Exception:
            st.error(
                "Unable to retrieve live data. "
                "Please try again later."
            )

st.caption(
    "For educational purposes only. This is not medical advice."
)

elif page == "3D Molecular Lab":
st.title("🧊 3D Molecular Lab")

selected = st.selectbox(
    "Choose a molecule",
    list(MOLECULES.keys())
)

st.write("Selected compound:", selected)

viewer_url = (
    "https://pubchem.ncbi.nlm.nih.gov/compound/"
    f"{requests.utils.quote(selected)}"
)

st.markdown(
    f"[Open molecular visualization on PubChem]({viewer_url})"
)

st.info(
    "This version links to PubChem for molecular visualization. "
    "An embedded interactive 3D viewer can be added in a later version."
)

elif page == "Chemistry Library":
st.title("📚 Chemistry Library")

with st.expander("What is a molecule?"):
    st.write(
        "A molecule is a group of atoms held together by "
        "chemical bonds."
    )

with st.expander("What is molecular formula?"):
    st.write(
        "A molecular formula represents the types and numbers "
        "of atoms in a molecule."
    )

with st.expander("What is molecular weight?"):
    st.write(
        "Molecular weight is the sum of the atomic masses "
        "of the atoms in a molecule."
    )

with st.expander("What is SMILES?"):
    st.write(
        "SMILES is a text-based notation for representing "
        "chemical structures."
    )

with st.expander("What is cheminformatics?"):
    st.write(
        "Cheminformatics combines chemistry and computing "
        "to store, search and analyse molecular information."
    )

elif page == "About":
st.title("About ChemNexa")

st.markdown("### Our Mission")
st.write(
    "ChemNexa is an educational chemistry application "
    "designed to make molecular information easier to explore."
)

st.markdown("### Technology Stack")
st.write("- Python")
st.write("- Streamlit")
st.write("- PubChem PUG REST API")

st.markdown("### Project Highlights")
st.write("- Chemical compound search")
st.write("- Drug compound explorer")
st.write("- Molecular formula and molecular weight")
st.write("- Online 2D molecular structures")
st.write("- Chemistry learning resources")

st.success("Explore Molecules. Discover Chemistry.")

st.caption("ChemNexa | Educational Project | Version 1.0")