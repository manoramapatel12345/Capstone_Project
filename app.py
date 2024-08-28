import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit.components.v1 as components
from streamlit_extras.dataframe_explorer import dataframe_explorer
from streamlit_lottie import st_lottie

# --- PAGE SETUP ---

st.set_page_config(page_title="Capstone Project",
                   layout="wide",
                   page_icon=":material/developer_board:")


# --- Heading ---

st.markdown(
    """
    <style>
        .heading-container {
            background: linear-gradient(135deg, #6e45e2, #88d3ce);
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            color: white;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            margin-bottom: 20px;
        }
        .heading-container h1 {
            font-size: 36px;
            font-family: 'Helvetica', sans-serif;
            margin: 0;
        }
        .heading-container p {
            font-size: 18px;
            font-family: 'Helvetica', sans-serif;
            margin-top: 5px;
        }
    </style>
    <div class="heading-container">
        <h1>Welcome to the Car Price Prediction App</h1>
        <p>Utilize cutting-edge machine learning models to predict car prices with ease.</p>
    </div>
    """,
    unsafe_allow_html=True
)





# ---

project = st.Page(
    page = 'views/prediction.py',
    title = "Model Prediction",
    icon = ":material/smart_toy:",
    # default = True
)

Data_des = st.Page(
    page = 'views/data_info.py',
    title = "Data info",
    icon = ":material/account_circle:",
)

Visualization = st.Page(
    page = 'views/Visualization.py',
    title = "Visualization",
    icon = ":material/monitoring:",
)

about_me = st.Page(
    page = 'views/my_info.py',
    title = "About me",
    icon = ":material/person:",
)




# ---- NAVIGATION SETUP [WITHOUT SECTIONS] ---

pg = st.navigation(
    {
        "Prediction": [project],
        "Extras": [Data_des, Visualization, about_me],
    }
)

# --- SHARED ON ALL THE PAGES ---

st.logo("https://i.postimg.cc/wv9MyGT4/database-management.png",)


# ---- RUN NAVIGATION ----

pg.run()

# st.sidebar.caption("This is a string that explains something above.")
st.sidebar.caption("Accurate car price predictions with cutting-edge ML models. :car: :rocket:")

st.sidebar.caption(
    "Like this? [Hire me!](https://www.linkedin.com/in/analyst-gaurav-yadav/)"
)

st.sidebar.text("Built with ❤️ by Manorama Patel")

# st.sidebar.caption(
#     "Built by [Gaurav yadav](https://www.linkedin.com/in/analyst-gaurav-yadav/). Like this? [Hire me!](https://www.linkedin.com/in/analyst-gaurav-yadav/)"
# )


linkedin = "https://img.icons8.com/fluency/48/linkedin.png"
topmate = "https://img.icons8.com/cute-clipart/64/chat.png"
email = "https://img.icons8.com/doodle/48/new-post.png"
newsletter = (
    "https://raw.githubusercontent.com/sahirmaharaj/exifa/main/img/newsletter.gif"
)
share = "https://img.icons8.com/officel/80/github.png"

uptime = "https://uptime.betterstack.com/status-badges/v1/monitor/196o6.svg"

st.sidebar.caption(
    f"""
        <div style='display: flex; align-items: center;'>
            <a href = 'https://www.linkedin.com/in/analyst-gaurav-yadav/'><img src='{linkedin}' style='width: 35px; height: 35px; margin-right: 25px;'></a>
            <a href = ''><img width="24" height="24" src='{topmate}' style='width: 32px; height: 32px; margin-right: 25px;'></a>
            <a href = 'mailto:Gaurav7869@outlook.com'><img src='{email}' style='width: 28px; height: 28px; margin-right: 25px;'></a>
            <a href = 'https://www.linkedin.com'><img src='{newsletter}' style='width: 28px; height: 28px; margin-right: 25px;'></a>
            <a href = 'https://www.kaggle.com/gaurav86451'><img src='{share}' style='width: 28px; height: 28px; margin-right: 25px;'></a>
            
        </div>
        <br>
        <a href = ''><img src='{uptime}'></a>
        
        """,
    unsafe_allow_html=True,
)
