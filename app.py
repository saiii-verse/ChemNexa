import streamlit as st
import requests
from urllib.parse import quote

st.set_page_config(
    page_title="ChemNexa | Peach Glow",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -------------------- PASTEL PEACH GLOW THEME --------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');
:root { --pink:#E8759E; --peach:#FFC5A8; --cream:#FFF9F3; --plum:#86556F; }
html, body, [class*="css"] { font-family:'Poppins',sans-serif; }
.stApp {
 background:
 radial-gradient(ellipse at 8% 5%, rgba(255,190,190,.40), transparent 34%),
 radial-gradient(ellipse at 95% 8%, rgba(255,211,169,.45), transparent 35%),
 radial-gradient(ellipse at 50% 100%, rgba(213,194,255,.28), transparent 42%),
 #FFF9F5;
 color:#705565;
}
.block-container {max-width:1250px; padding-top:1.8rem; padding-bottom:3rem;}
h1,h2,h3 {color:#A84F78 !important;}
.hero {
 padding:34px 22px; border-radius:28px; text-align:center;
 background:linear-gradient(135deg,#FFDDCE,#FFF0EF,#EADFFF);
 border:1px solid rgba(255,255,255,.95);
 box-shadow:0 12px 35px rgba(225,139,170,.20),0 0 22px rgba(245,141,181,.12);
 margin-bottom:24px;
}
.hero-title {
 font-size:clamp(36px,6vw,60px); font-weight:800; letter-spacing:-2px;
 background:linear-gradient(90deg,#DB6798,#E99A75,#A18BE5);
 -webkit-background-clip:text; -webkit-text-fill-color:transparent;
}
.hero-subtitle {font-size:16px;color:#805A70;margin-top:8px;}
.badge {display:inline-block;margin-top:14px;padding:7px 16px;border-radius:30px;
 background:rgba(255,255,255,.7);color:#AD5A83;border:1px solid #F4C9DA;font-size:12px;}
.glass-card {
 background:rgba(255,255,255,.78);border:1px solid rgba(255,255,255,.98);
 border-radius:21px;padding:20px;box-shadow:0 8px 26px rgba(183,119,150,.13);
 margin-bottom:14px;transition:all .25s ease;
}
.glass-card:hover {box-shadow:0 12px 30px rgba(231,126,169,.24);transform:translateY(-2px);}
.card-icon {font-size:31px;margin-bottom:8px;}
.card-title {color:#A84F78;font-size:18px;font-weight:700;}
.card-text {color:#826879;font-size:13px;line-height:1.7;}
div.stButton>button {
 width:100%;border-radius:14px;border:1px solid white;
 background:linear-gradient(110deg,#F6A4C3,#FFC5A8);color:#713E58;
 font-weight:600;padding:10px 13px;box-shadow:0 5px 16px rgba(224,123,163,.20);
 transition:all .25s ease;
}
div.stButton>button:hover {color:#713E58;border-color:#E98AB0;
 box-shadow:0 6px 22px rgba(232,117,158,.32);transform:translateY(-2px);}
div[data-testid="stMetric"] {background:rgba(255,255,255,.78);border:1px solid white;
 border-radius:17px;padding:14px;box-shadow:0 5px 18px rgba(200,133,161,.10);}
div[data-testid="stMetricLabel"] {color:#956C84;}
div[data-testid="stMetricValue"] {color:#C45F8A;}
section[data-testid="stSidebar"] {background:linear-gradient(180deg,#FFF0EA,#FFEAF1,#F2ECFF);}
.small-note {background:rgba(255,255,255,.75);border-left:4px solid #E99AB8;
 padding:13px 16px;border-radius:10px;color:#805A70;font-size:13px;}
.footer {text-align:center;color:#A67D91;font-size:12px;padding:25px 0 8px;}
[data-testid="stImage"] img {border-radius:18px;}
@media(max-width:600px){.block-container{padding-left:1rem;padding-right:1rem}.hero{padding:25px 14px}}
</style>
""", unsafe_allow_html=True)

# -------------------- COMPOUND CATALOGUE --------------------
MOLECULES = {
    "Aspirin": ("Drug", "Pain-relief compound"),
    "Paracetamol": ("Drug", "Pain and fever relief"),
    "Ibuprofen": ("Drug", "Anti-inflammatory compound"),
    "Caffeine": ("Natural compound", "Stimulant found in coffee and tea"),
    "Amoxicillin": ("Drug", "Antibiotic"),
    "Penicillin G": ("Drug", "Antibiotic"),
    "Azithromycin": ("Drug", "Antibiotic"),
    "Ciprofloxacin": ("Drug", "Antibiotic"),
    "Metformin": ("Drug", "Antidiabetic medication"),
    "Omeprazole": ("Drug", "Acid-reducing medication"),
    "Cetirizine": ("Drug", "Antihistamine"),
    "Loratadine": ("Drug", "Antihistamine"),
    "Naproxen": ("Drug", "Anti-inflammatory compound"),
    "Diclofenac": ("Drug", "Anti-inflammatory compound"),
    "Lidocaine": ("Drug", "Local anaesthetic"),
    "Atorvastatin": ("Drug", "Cholesterol-lowering medication"),
    "Losartan": ("Drug", "Blood-pressure medication"),
    "Amlodipine": ("Drug", "Blood-pressure medication"),
    "Warfarin": ("Drug", "Anticoagulant"),
    "Fluoxetine": ("Drug", "Antidepressant"),
    "Sertraline": ("Drug", "Antidepressant"),
    "Diazepam": ("Drug", "Benzodiazepine"),
    "Melatonin": ("Biomolecule", "Hormone involved in sleep timing"),
    "Dexamethasone": ("Drug", "Corticosteroid"),
    "Hydrocortisone": ("Drug", "Corticosteroid"),
    "Prednisone": ("Drug", "Corticosteroid"),
    "Furosemide": ("Drug", "Diuretic"),
    "Tramadol": ("Drug", "Pain medication"),
    "Theobromine": ("Natural compound", "Cocoa alkaloid"),
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
    "Glycine": ("Amino acid", "Simplest amino acid"),
    "Alanine": ("Amino acid", "Non-essential amino acid"),
    "Valine": ("Amino acid", "Essential amino acid"),
    "Leucine": ("Amino acid", "Essential amino acid"),
    "Lysine": ("Amino acid", "Essential amino acid"),
    "Tryptophan": ("Amino acid", "Essential amino acid"),
    "Glutamic acid": ("Amino acid", "Acidic amino acid"),
    "Aspartic acid": ("Amino acid", "Acidic amino acid"),
    "Water": ("Common compound", "Universal solvent"),
    "Hydrogen peroxide": ("Common compound", "Oxidising compound"),
    "Ethanol": ("Common compound", "Alcohol"),
    "Methanol": ("Common compound", "Alcohol"),
    "Acetic acid": ("Common compound", "Organic acid"),
    "Citric acid": ("Common compound", "Organic acid"),
    "Lactic acid": ("Common compound", "Organic acid"),
    "Urea": ("Common compound", "Nitrogen compound"),
    "Ammonia": ("Common compound", "Nitrogen compound"),
    "Benzene": ("Organic compound", "Aromatic hydrocarbon"),
    "Toluene": ("Organic compound", "Aromatic hydrocarbon"),
    "Phenol": ("Organic compound", "Aromatic compound"),
    "Aniline": ("Organic compound", "Aromatic amine"),
    "Naphthalene": ("Organic compound", "Aromatic hydrocarbon"),
    "Pyridine": ("Organic compound", "Heterocyclic compound"),
    "Imidazole": ("Organic compound", "Heterocyclic compound"),
    "1,3-Butadiene": ("Organic compound", "Conjugated diene"),
    "Styrene": ("Organic compound", "Aromatic compound"),
    "Formaldehyde": ("Organic compound", "Aldehyde"),
    "Acetone": ("Organic compound", "Ketone"),
    "Ethylene glycol": ("Organic compound", "Diol"),
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
    "Quercetin": ("Natural compound", "Plant flavonoid"),
    "Curcumin": ("Natural compound", "Turmeric compound"),
    "Resveratrol": ("Natural compound", "Plant polyphenol"),
    "Capsaicin": ("Natural compound", "Chilli compound"),
    "Limonene": ("Natural compound", "Terpene"),
    "Vanillin": ("Natural compound", "Vanilla flavour compound"),
    "Menthol": ("Natural compound", "Mint compound"),
    "Linalool": ("Natural compound", "Terpene alcohol"),
    "Oleic acid": ("Biomolecule", "Fatty acid"),
    "Palmitic acid": ("Biomolecule", "Fatty acid"),
    "Stearic acid": ("Biomolecule", "Fatty acid"),
    "Linoleic acid": ("Biomolecule", "Fatty acid"),
    "Glycerol": ("Common compound", "Polyol"),
    "Carbon dioxide": ("Common compound", "Inorganic compound"),
    "Sodium chloride": ("Common compound", "Ionic compound"),
    "Sulfuric acid": ("Common compound", "Mineral acid"),
    "Nitric acid": ("Common compound", "Mineral acid"),
    "Phosphoric acid": ("Common compound", "Mineral acid"),
}

# -------------------- PUBCHEM LOOKUPS --------------------
@st.cache_data(ttl=3600, show_spinner=False)
def get_molecule_data(name):
    encoded = quote(name, safe="")
    url = (
        "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/"
        f"{encoded}/property/MolecularFormula,MolecularWeight,IUPACName,"
        "CanonicalSMILES,XLogP,TPSA,HBondDonorCount,HBondAcceptorCount/JSON"
    )
    try:
        response = requests.get(url, timeout=15)
        if response.status_code != 200:
            return None
        properties = response.json().get("PropertyTable", {}).get("Properties", [])
        return properties[0] if properties else None
    except (requests.RequestException, ValueError, KeyError, IndexError):
        return None

@st.cache_data(ttl=3600, show_spinner=False)
def get_molecule_image(name):
    encoded = quote(name, safe="")
    url = (
        "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/"
        f"{encoded}/PNG?record_type=2d"
    )
    try:
        response = requests.get(url, timeout=15)
        if response.status_code == 200:
            return response.content
    except requests.RequestException:
        pass
    return None

def display_molecule(name):
    category, description = MOLECULES.get(name, ("Compound", "Chemical compound"))
    st.markdown(f"## 🧬 {name}")
    st.markdown(
        f'<div class="glass-card"><div class="card-title">🌸 {name}</div>'
        f'<div class="card-text">Category: {category}<br>{description}</div></div>',
        unsafe_allow_html=True,
    )
    with st.spinner("✨ Fetching molecular information..."):
        data = get_molecule_data(name)
        image_data = get_molecule_image(name)

    if image_data:
        st.subheader("🔬 2D Molecular Structure")
        st.image(image_data, caption=f"2D structure of {name} — PubChem", width=340)
    else:
        st.info("The structure image is unavailable right now. Check your connection or try again.")

    if not data:
        st.warning("Molecular properties are unavailable from PubChem right now.")
        return

    formula = data.get("MolecularFormula", "Not available")
    weight = data.get("MolecularWeight", "Not available")
    iupac = data.get("IUPACName", "Not available")
    smiles = data.get("ConnectivitySMILES", data.get("CanonicalSMILES", "Not available"))
    col1, col2, col3 = st.columns(3)
    col1.metric("🧪 Formula", formula)
    col2.metric("⚖️ Molecular Weight", f"{weight} g/mol")
    col3.metric("🌿 XLogP", str(data.get("XLogP", "N/A")))
    col4, col5, col6 = st.columns(3)
    col4.metric("🫧 TPSA", f'{data.get("TPSA", "N/A")} Å²')
    col5.metric("H-Bond Donors", str(data.get("HBondDonorCount", "N/A")))
    col6.metric("H-Bond Acceptors", str(data.get("HBondAcceptorCount", "N/A")))
    with st.expander("📚 Advanced Molecular Information"):
        st.write("**IUPAC Name**")
        st.write(iupac)
        st.write("**Canonical SMILES**")
        st.code(smiles)
    st.caption("Source: PubChem. Values depend on the compound record.")
    st.markdown(
        '<div class="small-note">💡 Educational information only; not medical advice.</div>',
        unsafe_allow_html=True,
    )

# -------------------- SIDEBAR --------------------
st.sidebar.markdown(
    '<div style="text-align:center;padding:12px 4px;">'
    '<div style="font-size:45px;">🧬</div>'
    '<div style="font-size:25px;font-weight:800;color:#C45F8A;">ChemNexa</div>'
    '<div style="font-size:11px;color:#A57991;letter-spacing:1px;">PEACH GLOW EDITION</div></div>',
    unsafe_allow_html=True,
)
st.sidebar.markdown("---")
page = st.sidebar.radio(
    "🌷 Explore ChemNexa",
    ["🏠 Home", "🧬 Molecule Explorer", "💊 Drug Database", "📚 Chemistry Library", "✨ About ChemNexa"],
)
st.sidebar.markdown("---")
st.sidebar.caption("Explore molecules. Discover chemistry. ✨")

# -------------------- HOME --------------------
if page == "🏠 Home":
    st.markdown(
        '<div class="hero"><div style="font-size:40px;">🌷 🧬 🌷</div>'
        '<div class="hero-title">ChemNexa</div>'
        '<div class="hero-subtitle">Explore Molecules. Discover Chemistry.</div>'
        '<div class="badge">✨ YOUR AESTHETIC MOLECULAR LAB ✨</div></div>',
        unsafe_allow_html=True,
    )
    st.markdown("## 🌸 Welcome to your lab")
    st.write("Explore chemical compounds, molecular structures, and the science behind everyday molecules.")
    c1, c2, c3 = st.columns(3)
    cards = [
        (c1, "🧬", "Molecule Explorer", "Search compounds and explore formulas, structures, and properties."),
        (c2, "💊", "Drug Database", "Explore drug-related compounds and their chemical information."),
        (c3, "🔬", "Chemistry Library", "Discover organic compounds, amino acids, vitamins, and biomolecules."),
    ]
    for col, icon, title, desc in cards:
        with col:
            st.markdown(
                f'<div class="glass-card"><div class="card-icon">{icon}</div>'
                f'<div class="card-title">{title}</div><div class="card-text">{desc}</div></div>',
                unsafe_allow_html=True,
            )
    st.markdown("## ✨ Quick Discover")
    featured = ["Aspirin", "Caffeine", "Glucose", "Vitamin C", "Dopamine", "Benzene"]
    cols = st.columns(3)
    for idx, name in enumerate(featured):
        with cols[idx % 3]:
            st.markdown(
                f'<div class="glass-card"><div class="card-icon">🌸</div>'
                f'<div class="card-title">{name}</div><div class="card-text">Featured compound</div></div>',
                unsafe_allow_html=True,
            )
            if st.button(f"Explore {name} ✨", key=f"home_{name}"):
                st.session_state["selected_molecule"] = name
    if st.session_state.get("selected_molecule") in MOLECULES:
        display_molecule(st.session_state["selected_molecule"])
        if st.button("✖ Close details", key="close_home"):
            st.session_state.pop("selected_molecule", None)
            st.rerun()

# -------------------- MOLECULE EXPLORER --------------------
elif page == "🧬 Molecule Explorer":
    st.markdown(
        '<div class="hero"><div style="font-size:40px;">🧬 🔍 🫧</div>'
        '<div class="hero-title" style="font-size:42px;">Molecule Explorer</div>'
        '<div class="hero-subtitle">Every molecule has a story. Discover yours.</div></div>',
        unsafe_allow_html=True,
    )
    typed_name = st.text_input("🔎 Enter a compound name", placeholder="Try Aspirin, Caffeine, Glucose...")
    choice = st.selectbox("Or choose from the library", ["Choose a molecule..."] + sorted(MOLECULES.keys()))
    if st.button("✨ Explore Molecule", key="explore_button"):
        selected = typed_name.strip() or (choice if choice != "Choose a molecule..." else "")
        if selected:
            st.session_state["explorer_selected"] = selected
        else:
            st.warning("Please enter or select a molecule first.")
    if st.session_state.get("explorer_selected"):
        display_molecule(st.session_state["explorer_selected"])

# -------------------- DRUG DATABASE --------------------
elif page == "💊 Drug Database":
    st.markdown(
        '<div class="hero"><div style="font-size:40px;">💊 🌸 🧪</div>'
        '<div class="hero-title" style="font-size:42px;">Drug Database</div>'
        '<div class="hero-subtitle">Explore the chemistry behind drug compounds.</div></div>',
        unsafe_allow_html=True,
    )
    drug_names = [name for name, info in MOLECULES.items() if info[0] == "Drug"]
    query = st.text_input("🔍 Search drug compounds", placeholder="Enter a drug name...")
    matches = [name for name in drug_names if query.lower() in name.lower()]
    st.write(f"**{len(matches)} compounds found**")
    cols = st.columns(3)
    for idx, name in enumerate(matches):
        with cols[idx % 3]:
            st.markdown(
                f'<div class="glass-card"><div class="card-icon">💊</div>'
                f'<div class="card-title">{name}</div><div class="card-text">{MOLECULES[name][1]}</div></div>',
                unsafe_allow_html=True,
            )
            if st.button("View Details ✨", key=f"drug_{name}"):
                st.session_state["drug_selected"] = name
    if st.session_state.get("drug_selected") in MOLECULES:
        display_molecule(st.session_state["drug_selected"])
    st.markdown(
        '<div class="small-note">📌 Educational use only. This database is not intended for diagnosis, treatment, or medication recommendations.</div>',
        unsafe_allow_html=True,
    )

# -------------------- CHEMISTRY LIBRARY --------------------
elif page == "📚 Chemistry Library":
    st.markdown(
        '<div class="hero"><div style="font-size:40px;">📚 🧪 🌷</div>'
        '<div class="hero-title" style="font-size:42px;">Chemistry Library</div>'
        '<div class="hero-subtitle">A beautiful collection of chemical discoveries.</div></div>',
        unsafe_allow_html=True,
    )
    categories = sorted({details[0] for details in MOLECULES.values()})
    selected_category = st.selectbox("🌸 Choose a category", ["All Categories"] + categories)
    query = st.text_input("🔍 Search library", placeholder="Search by compound name...")
    results = []
    for name, details in MOLECULES.items():
        category, description = details
        if (selected_category == "All Categories" or category == selected_category) and query.lower() in name.lower():
            results.append((name, category, description))
    st.write(f"**{len(results)} compounds available**")
    cols = st.columns(3)
    for idx, (name, category, description) in enumerate(results):
        with cols[idx % 3]:
            st.markdown(
                f'<div class="glass-card"><div class="card-icon">🧬</div>'
                f'<div class="card-title">{name}</div><div class="card-text">{category}<br>{description}</div></div>',
                unsafe_allow_html=True,
            )
            if st.button("Explore ✨", key=f"library_{name}"):
                st.session_state["library_selected"] = name
    selected_library = st.session_state.get("library_selected")
    if selected_library in MOLECULES:
        display_molecule(selected_library)

# -------------------- ABOUT --------------------
elif page == "✨ About ChemNexa":
    st.markdown(
        '<div class="hero"><div style="font-size:45px;">🌸 🧬 🌸</div>'
        '<div class="hero-title">About ChemNexa</div>'
        '<div class="hero-subtitle">Explore Molecules. Discover Chemistry.</div></div>',
        unsafe_allow_html=True,
    )
    about_cards = [
        ("🌷", "Our Mission", "ChemNexa is an educational cheminformatics application designed to make exploring chemical compounds simple, interactive, and visually engaging."),
        ("🔬", "What You Can Explore", "Molecular formulas, molecular weights, 2D structures, drug-related compounds, organic compounds, and biomolecules."),
        ("🌐", "Data Source", "Molecular information and structure images are retrieved from PubChem when available."),
        ("💗", "Designed for Learning", "A pastel peach and pink interface brings chemistry, discovery, and an aesthetic user experience together."),
    ]
    for icon, title, description in about_cards:
        st.markdown(
            f'<div class="glass-card"><div class="card-icon">{icon}</div>'
            f'<div class="card-title">{title}</div>'