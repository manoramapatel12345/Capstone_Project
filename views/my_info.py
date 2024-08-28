import streamlit as st
from forms.contact import *
from streamlit_lottie import st_lottie
import json
import requests



@st.dialog("Contact Me")
def show_contact_form():
    contact_form()

def load_lottiefile(filepath: str):
    with open(filepath , 'r') as f:
        return json.load(f)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# --- HERO SECTION ---

def my_page():
    col1, col2 = st.columns(2, gap = "small", vertical_alignment="center")

    with col1:
        st.image("assets\profile_pic.png", width=250)
    with col2:
        st.title("Manorama Patel", anchor=False)
        st.write(
            "Aspiring Data Analyst, assisting enterprises by supporting data-driven decision-making."
        )
        if st.button("✉️ contact me"):
            show_contact_form()

    # --- EXPERIENCE & QUALIFICATIONS ---
    colA, colB = st.columns(2, gap = "small", vertical_alignment="top")

    with colA:
        st.write("\n")
        st.subheader("Experience & Qualifications", anchor=False)
        st.write(
            """
            - Real world experience of extracting actionable insights from data
            - Strong hands-on experience and knowledge in Python and Excel
            - Good understanding of statistical principles and their respective applications
            - Excellent team-player and displaying a strong sense of initiative on tasks
            """
        )

        # --- SKILLS ---
        st.write("\n")
        st.subheader("Hard Skills", anchor=False)
        st.write(
            """
            - Programming: Python (Scikit-learn, Pandas), SQL, VBA
            - Data Visualization: PowerBi, MS Excel, Plotly
            - Modeling: Logistic regression, linear regression, decision trees
            - Databases: Postgres, MySQL, ChromaDB
            """
        )

    with colB:
        
        lottie_work = load_lottieurl(st.secrets["Work_url"])
        lottie_skill = load_lottieurl(st.secrets["Skill_url"])
        comedy = load_lottieurl(st.secrets["Comedy"])

        st_lottie(
            lottie_work,
            speed=1,
            reverse=False,
            loop=True,
            quality="low",
            height=210,
            width=None
        )

        st_lottie(lottie_skill, 
            key="hello",
            height = 230,
            width = None
            
        )
    
    st.divider()

# ------------------------------------------------------
st.divider()
my_page()