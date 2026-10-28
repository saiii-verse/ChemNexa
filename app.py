import streamlit as st

st.set_page_config(
page_title="ChemNexa",
page_icon="🧪",
layout="wide"
)

st.markdown("""

<style>
.stApp {
    background-color: #0b1220;
    color: #f1f5f9;
}
[data-testid="stSidebar"] {
    background-color: #111c30;
}
h1, h2, h3 {
    color: #55e6c1;
}
div.stButton > button {
    background-color: #55e6c1;
    color: #0b1220;
    border-radius: 10px;
    border: none;
    font-weight: bold;
}
</style>""", unsafe_allow_html=True)

st.title("🧪 ChemNexa")
st.subheader("Explore Molecules. Discover Chemistry.")

st.write(
"Your interactive chemistry and molecular exploration platform."
)

page = st.sidebar.selectbox(
"Navigate",
[
"Home",
"Molecule Explorer",
"Drug Database",
"About"
]
)

molecules = {
"Aspirin": {
"formula": "C9H8O4",
"weight": "180.16 g/mol",
"smiles": "CC(=O)OC1=CC=CC=C1C(=O)O"
},
"Paracetamol": {
"formula": "C8H9NO2",
"weight": "151.16 g/mol",
"smiles": "CC(=O)NC1=CC=C(O)C=C1"
},
"Caffeine": {
"formula": "C8H10N4O2",
"weight": "194.19 g/mol",
"smiles": "Cn1c(=O)c2c(ncn2C)n(C)c1=O"
},
"Ibuprofen": {
"formula": "C13H18O2",
"weight": "206.28 g/mol",
"smiles": "CC(C)CC1=CC=C(C=C1)C(C)C(=O)O"
},
"Glucose": {
    "formula": "C6H12O6",
    "weight": "180.16 g/mol",
    "smiles": "C([C@@H]1[C@H]([C@@H]([C@H](C(O1)O)O)O)O)O"
},
"Benzene": {
"formula": "C6H6",
"weight": "78.11 g/mol",
"smiles": "C1=CC=CC=C1"
}
}

if page == "Home":
st.markdown("## Welcome to ChemNexa")
st.write(
"Discover chemical compounds, explore molecular "
"identities, and learn about chemistry."
)

a, b, c = st.columns(3)
a.metric("Compounds", len(molecules))
b.metric("Main Sections", 4)
c.metric("Platform", "Chemistry")

st.markdown("### Featured Molecules")

for name in list(molecules.keys())[:3]:
    st.info(f"🧬 {name} — {molecules[name]['formula']}")

elif page == "Molecule Explorer":
st.header("🔬 Molecule Explorer")

query = st.text_input("Search for a molecule")

matches = [
    name for name in molecules
    if query.lower() in name.lower()
]

if query and not matches:
    st.warning("No matching molecule found.")

for name in matches if query else molecules:
    with st.expander(name):
        st.write("**Formula:**", molecules[name]["formula"])
        st.write("**Molecular Weight:**",
                 molecules[name]["weight"])
        st.write("**SMILES:**", molecules[name]["smiles"])

elif page == "Drug Database":
st.header("💊 Drug Molecule Database")

for name in ["Aspirin", "Paracetamol", "Caffeine", "Ibuprofen"]:
    st.markdown(f"### {name}")
    st.write("Formula:", molecules[name]["formula"])
    st.write("Molecular Weight:", molecules[name]["weight"])
    st.divider()

st.caption(
    "Educational information only. This is not medical advice."
)

elif page == "About":
st.header("About ChemNexa")
st.write(
"ChemNexa is a chemistry learning and molecular "
"exploration project designed to make chemical "
"information easier to explore."
)
st.write("Version: 1.0")
st.write("Technology: Python and Streamlit")
st.success("Explore Molecules. Discover Chemistry.")