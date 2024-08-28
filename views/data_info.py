import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd




def autoviz_html(file_name, width = 1000, height = 500):
    with open(f"AutoViz_Plots/AutoViz/{file_name}.html", "r", encoding='ISO-8859-1') as file:
        html_content = file.read()

    components.html(html_content, width=width, height=height, scrolling=True)


def descprit_data(df):

    with st.expander('descriptions'):
         # Create multiple check box in row
        col_name, col_dtype, col_data = st.columns(3)

        # Create a checkbox to get the summary.
        # with veiw_summary:
        if st.checkbox("View Summary"):
            st.dataframe(df.describe(), use_container_width=True)

        # Create multiple check box in row

       

        # Show name of all dataframe
        with col_name:
            if st.checkbox("Column Names"):
                st.dataframe(df.columns, use_container_width=True)

        # Show datatype of all columns 
        with col_dtype:
            if st.checkbox("Columns data types"):
                dtypes = df.dtypes.apply(lambda x: x.name)
                st.dataframe(dtypes, use_container_width=True)
        
        # Show data for each columns
        with col_data: 
            if st.checkbox("Columns Data"):
                col = st.selectbox("Column Name", list(df.columns))
                st.dataframe(df[col].head(8), use_container_width=True)


def Data_page():
    st.title("Data Info page", anchor=False)


    st.markdown(
        """
        ## 📊 **Dataset Overview**

        The dataset contains various features related to used cars. Here’s a detailed description:

        - **`name`**: 
            - **Type**: :blue[Object]
            - **Missing Values**: :green[0%]
            - **Unique Values**: :orange[41]
            - **Range**: :grey[N/A]
            - **DQ Issue**: :green[No data quality issues.]

        - **`year`**: 
            - **Type**: :blue[Integer]
            - **Missing Values**: :green[0%]
            - **Unique Values**: :orange[0]
            - **Range**: :grey[1992 to 2020]
            - **DQ Issue**: :red[Potential date-time column; consider transforming it before modeling.]

        - **`selling_price`**: 
            - **Type**: :blue[Integer]
            - **Missing Values**: :green[0%]
            - **Unique Values**: :orange[12]
            - **Range**: :grey[20,000 to 8,900,000]
            - **DQ Issue**: :red[Contains 170 outliers. Consider capping or removing these outliers to improve accuracy.]

        - **`km_driven`**: 
            - **Type**: :blue[Integer]
            - **Missing Values**: :green[0%]
            - **Unique Values**: :orange[21]
            - **Range**: :grey[1 to 806,599]
            - **DQ Issue**: :red[Contains 106 outliers. Cap or remove these outliers to ensure reliable predictions.]

        - **`fuel`**: 
            - **Type**: :blue[Object]
            - **Missing Values**: :green[0%]
            - **Unique Values**: :orange[2 rare categories: `LPG`, `Electric`]
            - **DQ Issue**: :orange[Group rare categories into a single category or drop them to simplify the analysis.]

        - **`seller_type`**: 
            - **Type**: :blue[Object]
            - **Missing Values**: :green[0%]
            - **Unique Values**: :orange[1 rare category: `Trustmark Dealer`]
            - **DQ Issue**: :orange[Group rare categories into a single category or drop them to avoid potential bias.]

        - **`transmission`**: 
            - **Type**: :blue[Object]
            - **Missing Values**: :green[0%]
            - **Unique Values**: :orange[No issue]
            
        - **`owner`**: 
            - **Type**: :blue[Object]
            - **Missing Values**: :green[0%]
            - **Unique Values**: :orange[1 rare category: `Test Drive Car`]
            - **DQ Issue**: :orange[Group rare categories into a single category or drop them to ensure consistency.]

        **Notes**: Address outliers and handle rare categories appropriately to enhance the dataset’s quality and improve model performance. 🚗🔍
        """,
        unsafe_allow_html=True
    )

    with st.expander("View Raw data"):
            df = pd.read_csv(f'dataset/CAR DETAILS.csv')
            st.dataframe(df)
            st.subheader("This is Raw Dataset Befor Preprocessing")

    with st.expander("View Clean data"):
            df = pd.read_csv(f'dataset/CAR_DETAILS_clean.csv')
            st.dataframe(df)
            st.subheader("This is Raw Dataset Befor Preprocessing")

    descprit_data(df)

    chart_list = ["Cat Plot", "Displot", "Heatmap", "Scatter Plot", "Time Series", "Violin Plot"]
    default_file = "violinplots"

    chart_mapping = {
        "Cat Plot": "cat_var_plots",
        "Displot": "distplots_nums",
        "Heatmap": "heatmaps",
        "Scatter Plot": "pair_scatters",
        "Time Series": "timeseries_plots",
    }

    with st.expander("More info", expanded=True):
        selected_charts = st.multiselect("", chart_list, placeholder="Choose your chart...")

        with st.spinner("Generating Charts..."):
            if selected_charts:
                for chart in selected_charts:
                    file_name = chart_mapping.get(chart, default_file)
                    autoviz_html(file_name)
            else:
                autoviz_html(default_file)
#-----------------------------------------------------------------------------

Data_page()




