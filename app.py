import streamlit as st

st.set_page_config(
page_title="ChemNexa | Chemistry Explorer",
page_icon="🧪",
layout="wide"
)

st.markdown("""

<style>
.stApp {
    background: linear-gradient(135deg, #08111f, #10243a);
    color: #f1f5f9;
}
[data-testid="stSidebar"] {
    background-color: #101d30;
}
h1, h2, h3 {
    color: #54e6c1 !important;
}
p, label, li {
    color: #e2e8f0;
}
div[data-testid="stMetric"] {
    background-color: #14283d;
    padding: 16px;
    border-radius: 12px;
    border: 1px solid #28516a;
}
div.stButton > button {
    background-color: #54e6c1;
    color: #08111f;
    border-radius: 10px;
    border: none;
    font-weight: bold;
}
div[data-testid="stExpander"] {
    background-color: #112238;
    border-radius: 10px;
}
</style>""", unsafe_allow_html=True)

MOLECULES = {
"Aspirin": {
"formula": "C9H8O4",
"weight": 180.16,
"smiles": "CC(=O)OC1=CC=CC=C1C(=O)O",
"category": "Drug compound",
"description": "A compound commonly used for pain relief and fever reduction."
},
"Paracetamol": {
"formula": "C8H9NO2",
"weight": 151.16,
"smiles": "CC(=O)NC1=CC=C(O)C=C1",
"category": "Drug compound",
"description": "A compound used in medicines for pain and fever."
},
"Ibuprofen": {
"formula": "C13H18O2",
"weight": 206.28,
"smiles": "CC(C)CC1=CC=C(C=C1)C(C)C(=O)O",
"category": "Drug compound",
"description": "A nonsteroidal anti-inflammatory drug compound."
},
"Caffeine": {
"formula": "C8H10N4O2",
"weight": 194.19,
"smiles": "Cn1c(=O)c2c(ncn2C)n(C)c1=O",
"category": "Natural compound",
"description": "A naturally occurring stimulant found in coffee and tea."
},
"Glucose": {
"formula": "C6H12O6",
"weight": 180.16,
"smiles": "C([C@@H]1"C@H" ([C@@H]([C@H](C(O1)O)O)O)O)O",
"category": "Carbohydrate",
"description": "A simple sugar used by cells as an energy source."
},
"Benzene": {
"formula": "C6H6",
"weight": 78.11,
"smiles": "C1=CC=CC=C1",
"category": "Aromatic hydrocarbon",
"description": "An aromatic hydrocarbon containing a six-membered carbon ring."
},
"Ethanol": {
"formula": "C2H6O",
"weight": 46.07,
"smiles": "CCO",
"category": "Alcohol",
"description": "A two-carbon alcohol used in laboratories and industry."
},
"Methane": {
"formula": "CH4",
"weight": 16.04,
"smiles": "C",
"category": "Hydrocarbon",
"description": "The simplest hydrocarbon."
},
"Urea": {
"formula": "CH4N2O",
"weight": 60.06,
"smiles": "C(=O)(N)N",
"category": "Organic compound",
"description": "An organic compound involved in nitrogen metabolism."
},
"Citric Acid": {
"formula": "C6H8O7",
"weight": 192.12,
"smiles": "C(C(=O)O)C(CC(=O)O)(C(=O)O)O",
"category": "Organic acid",
"description": "An organic acid found naturally in citrus fruits."
},
"Lactic Acid": {
"formula": "C3H6O3",
"weight": 90.08,
"smiles": "CC(O)C(=O)O",
"category": "Organic acid",
"description": "An organic acid produced during several biological processes."
},
"Glycine": {
"formula": "C2H5NO2",
"weight": 75.07,
"smiles": "NCC(=O)O",
"category": "Amino acid",
"description": "The simplest amino acid found in proteins."
},
"Alanine": {
"formula": "C3H7NO2",
"weight": 89.09,
"smiles": "CC(N)C(=O)O",
"category": "Amino acid",
"description": "An amino acid used in protein synthesis."
},
"Uric Acid": {
"formula": "C5H4N4O3",
"weight": 168.11,
"smiles": "O=C1NC(=O)C2=C(N1)NC=N2",
"category": "Biological compound",
"description": "A compound formed during purine breakdown."
},
"Nicotinamide": {
"formula": "C6H6N2O",
"weight": 122.12,
"smiles": "NC(=O)C1=CC=CN=C1",
"category": "Vitamin-related compound",
"description": "A form of vitamin B3."
},
"Lidocaine": {
"formula": "C14H22N2O",
"weight": 234.34,
"smiles": "CCN(CC)CC(=O)NC1=C(C)C=CC=C1C",
"category": "Drug compound",
"description": "A local anaesthetic compound."
},
"Amoxicillin": {
"formula": "C16H19N3O5S",
"weight": 365.40,
"smiles": "CC1(C(N2C(S1)C(C2=O)NC(=O)C(C3=CC=C(C=C3)O)N)C(=O)O)C",
"category": "Drug compound",
"description": "A penicillin-class antibiotic compound."
},
"Metformin": {
"formula": "C4H11N5",
"weight": 129.16,
"smiles": "CN(C)C(=N)NC(=N)N",
"category": "Drug compound",
"description": "A medicine compound used in the management of type 2 diabetes."
},
"Naproxen": {
"formula": "C14H14O3",
"weight": 230.26,
"smiles": "COC1=CC2=C(C=C1)C=CC(C2)C(=O)O",
"category": "Drug compound",
"description": "A nonsteroidal anti-inflammatory drug compound."
},
"Cholesterol": {
"formula": "C27H46O",
"weight": 386.65,
"smiles": "CC(C)CCCC(C)C1CCC2C1(CCC3C2CCC4(C3CCC4O)C)C",
"category": "Lipid",
"description": "A sterol important in cell membranes."
},
"Vitamin C": {
"formula": "C6H8O6",
"weight": 176.12,
"smiles": "C([C@@H]1OC(=O)C(=C(O)[C@H]1O)O)O",
"category": "Vitamin",
"description": "An essential vitamin also known as ascorbic acid."
},
"Benzamide": {
"formula": "C7H7NO",
"weight": 121.14,
"smiles": "C1=CC=C(C=C1)C(=O)N",
"category": "Organic compound",
"description": "An aromatic compound containing an amide group."
},
"Acetic Acid": {
"formula": "C2H4O2",
"weight": 60.05,
"smiles": "CC(=O)O",
"category": "Organic acid",
"description": "The main acid responsible for the sour taste of vinegar."
},
"Formaldehyde": {
"formula": "CH2O",
"weight": 30.03,
"smiles": "C=O",
"category": "Aldehyde",
"description": "A simple aldehyde used in industrial chemistry."
},
"Propane": {
"formula": "C3H8",
"weight": 44.10,
"smiles": "CCC",
"category": "Hydrocarbon",
"description": "A three-carbon alkane."
}
}

st.sidebar.markdown("# 🧪 ChemNexa")
st.sidebar.caption("Chemistry Discovery Platform")

page = st.sidebar.radio(
"NAVIGATION",
[
"Home",
"Molecule Explorer",
"Drug Database",
"Chemistry Library",
"About"
]
)

st.sidebar.divider()
st.sidebar.caption("Educational chemistry project")

if page == "Home":
st.title("🧪 ChemNexa")
st.subheader("Explore Molecules. Discover Chemistry.")
st.write(
"A modern platform to explore chemical compounds, "
"molecular formulas, structures and scientific information."
)

st.divider()

col1, col2, col3 = st.columns(3)
col1.metric("Compounds", len(MOLECULES))
col2.metric(
    "Drug Compounds",
    sum(
        1 for m in MOLECULES.values()
        if m["category"] == "Drug compound"
    )
)
col3.metric("Explorer", "Available")

st.markdown("## ✨ Featured Molecules")

featured = ["Aspirin", "Caffeine", "Glucose", "Benzene"]

cols = st.columns(2)

for i, name in enumerate(featured):
    with cols[i % 2]:
        mol = MOLECULES[name]
        st.markdown(f"### 🧬 {name}")
        st.write(f"**Formula:** {mol['formula']}")
        st.write(f"**Molecular Weight:** {mol['weight']} g/mol")
        st.caption(mol["category"])
        st.divider()

st.info(
    "Select Molecule Explorer from the sidebar "
    "to search the complete built-in compound list."
)

elif page == "Molecule Explorer":
st.title("🔬 Molecule Explorer")
st.write("Search and explore chemical compound information.")

query = st.text_input(
    "🔍 Search by molecule name or formula",
    placeholder="Example: Aspirin, Glucose, C6H6"
)

category = st.selectbox(
    "Filter by category",
    ["All Categories"] +
    sorted(set(m["category"] for m in MOLECULES.values()))
)

results = []

for name, mol in MOLECULES.items():
    matches_query = (
        query.strip().lower() in name.lower()
        or query.strip().lower() in mol["formula"].lower()
    )

    matches_category = (
        category == "All Categories"
        or mol["category"] == category
    )

    if matches_query and matches_category:
        results.append((name, mol))

st.caption(f"{len(results)} compound(s) found")

if not results:
    st.warning("No compounds found. Try another search.")

for name, mol in results:
    with st.expander(f"🧬 {name} — {mol['formula']}"):
        st.write("**Category:**", mol["category"])
        st.write("**Molecular Formula:**", mol["formula"])
        st.write(
            "**Molecular Weight:**",
            f"{mol['weight']:.2f} g/mol"
        )
        st.write("**SMILES:**")
        st.code(mol["smiles"], language="text")
        st.write("**About this molecule:**")
        st.write(mol["description"])

elif page == "Drug Database":
st.title("💊 Drug Compound Database")
st.write(
"Explore selected compounds used in medicines "
"for educational purposes."
)

drug_query = st.text_input(
    "Search drug compounds",
    placeholder="Example: Aspirin"
)

drugs = {
    name: mol
    for name, mol in MOLECULES.items()
    if mol["category"] == "Drug compound"
    and drug_query.lower() in name.lower()
}

if not drugs:
    st.warning("No matching drug compound found.")

for name, mol in drugs.items():
    with st.expander(name):
        st.write("**Formula:**", mol["formula"])
        st.write(
            "**Molecular Weight:**",
            f"{mol['weight']:.2f} g/mol"
        )
        st.write("**SMILES:**")
        st.code(mol["smiles"], language="text")
        st.write(mol["description"])

st.warning(
    "Educational information only. This database does not "
    "provide treatment recommendations or medical advice."
)

elif page == "Chemistry Library":
st.title("📚 Chemistry Library")

st.markdown("### What is a molecule?")
st.write(
    "A molecule is a group of two or more atoms chemically "
    "bonded together."
)

st.markdown("### What is molecular formula?")
st.write(
    "A molecular formula indicates the types and numbers "
    "of atoms in a molecule."
)

st.markdown("### What is molecular weight?")
st.write(
    "Molecular weight is calculated from the atomic masses "
    "of the atoms present in a molecule."
)

st.markdown("### What is SMILES?")
st.write(
    "SMILES is a text notation used to represent molecular "
    "structures in a computer-readable format."
)

st.markdown("### What is cheminformatics?")
st.write(
    "Cheminformatics combines chemistry, information science "
    "and computing to organize and analyse chemical data."
)

elif page == "About":
st.title("About ChemNexa")

st.markdown("### 🧪 Our Mission")
st.write(
    "ChemNexa is a student-oriented chemistry exploration "
    "platform designed to make chemical information accessible."
)

st.markdown("### ⚙️ Technologies")
st.write("- Python")
st.write("- Streamlit")
st.write("- Chemical compound data and SMILES notation")

st.markdown("### 📌 Current Features")
st.write("- Searchable compound library")
st.write("- Chemical formulas and molecular weights")
st.write("- Drug compound information")
st.write("- Chemistry learning section")

st.success("Explore Molecules. Discover Chemistry.")

st.caption(
    "Version 1.0 | Educational use only | ChemNexa"
)