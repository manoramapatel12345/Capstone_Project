import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import streamlit as st
import streamlit.components.v1 as components
from streamlit_extras.dataframe_explorer import dataframe_explorer
import pandas as pd
import plotly.express as px

# getting the working directory of the main.py
# working_dir = os.path.dirname(os.path.abspath(__file__))


@st.cache_data
def get_data(path):

    data = pd.read_csv(path)
    return data
    
    
def grouped_data(df, column_name):
  '''
  This function will group the Data
  '''
  df_tmp = df.groupby(column_name).agg({'selling_price':'mean'}).reset_index()
  return df_tmp


def vizual_data():
    with open(f"HTML_Files/pandas_profiling_report.html", "r") as file:
        html_content = file.read()

    components.html(html_content, width=1035, height=1024, scrolling=True)


    # with open(f"{working_dir}/HTML_Files/sales_by_fuel.html", "r", encoding='ISO-8859-1') as file_2:
    #     html_content_2 = file_2.read()

    # components.html(html_content_2, width=1300, height=1024, scrolling=True)    

    # with open(f"{working_dir}/HTML_Files/autoviz_visualization.html", "r", encoding='utf-8') as file_2:
    #     html_content_2 = file_2.read()

    # components.html(html_content_2, width=1300, height=1024, scrolling=True)


    my_df = get_data(f'dataset/CAR_DETAILS_clean.csv')
    filtered_df = dataframe_explorer(my_df, case=False)
    n_data = st.dataframe(
    filtered_df,
    key="car_data",
    on_select="rerun",
    selection_mode=["multi-row", "multi-column"],
    height=300,
    use_container_width=True
    )

    # Graphs and charts

    owner_type = grouped_data(filtered_df, 'owner')
    seller_type = grouped_data(filtered_df, 'seller_type')
    fuel_type = grouped_data(filtered_df, 'fuel')
    sp_year = filtered_df.groupby('year').agg({'selling_price':'mean', 'km_driven': 'mean'}).reset_index()
    

    # Creating two columns for visualization
    col1, col2 = st.columns(2)
    template_style = "plotly_dark"


    with col1:
        st.subheader("fuel wise Prices")

        # Creating a bar chart for CPU brand prices
        fig = px.bar(fuel_type, x='fuel', y='selling_price', 
                    template=template_style,
                    # text=fuel_type['selling_price'].apply(lambda x: '${:,.2f}'.format(x)),
                    color='fuel')

        # fig.update_layout(template=template_style)
        
        fig.update_traces(
        texttemplate='%{y:.2s}',
        textposition='outside',
        hovertemplate='<b>Fuel: %{x}</b><br>Selling Price: %{y}<extra></extra>'
        )
        st.plotly_chart(fig, use_container_width=True)
    

    with col2:
        st.subheader("Owner wise Prices")

        # Creating a bar chart for CPU brand prices
        fig = px.bar(owner_type, x='owner', y='selling_price', 
                    template=template_style,
                    # text=fuel_type['selling_price'].apply(lambda x: '${:,.2f}'.format(x)),
                    color='owner')
        fig.update_traces(
        texttemplate='%{y:.2s}',
        textposition='outside',
        hovertemplate='<b>Owner: %{x}</b><br>Selling Price: %{y}<extra></extra>'
        )
        st.plotly_chart(fig, use_container_width=True)

    with col1:
        with st.expander("Fuel Wise Prices data &#x2935;"):
            st.write(fuel_type.style.background_gradient(cmap="Blues"))
            csv = fuel_type.to_csv(index=False).encode('utf-8')
            st.download_button("Download Data", data=csv, file_name='fuel_type.csv', mime="text/csv", help="Click here to download the CSV file")


    with col2:
        with st.expander("Owner wise Prices &#x2935;"):
            st.write(owner_type.style.background_gradient(cmap="Blues"))
            csv = owner_type.to_csv(index=False).encode('utf-8')
            st.download_button("Download Data", data=csv, file_name='owner_type.csv', mime="text/csv", help="Click here to download the CSV file")



    @st.fragment
    def scatter_select():
        scatter_chart = px.scatter(
        filtered_df,
        x = "km_driven",
        y = "selling_price",
        color = "fuel",
        height = 350
        )

        selected_scatter = st.plotly_chart(
        scatter_chart,
        key="scatter_data",
        on_select="rerun"
        )

        # Check if there is any selection data
        if selected_scatter and 'selection' in selected_scatter:
            selected_indices = selected_scatter['selection'].get('point_indices', [])
            if selected_indices:
                with st.expander("Selected Data Points"):
                    st.dataframe(
                        filtered_df.iloc[selected_indices],
                        height=350,
                        use_container_width=True
                    )
                    csv = filtered_df.iloc[selected_indices].to_csv(index=False).encode('utf-8')
                    st.download_button("Download Data", data=csv, file_name='Selected_datapoints.csv', mime="text/csv", help="Click here to download the CSV file")
            else:
                st.text("No points selected.")
        else:
            st.text("No points selected.")

    scatter_select()

    col1, col2 = st.columns(2)

    with col1:
        avg_dist = filtered_df.groupby('fuel').agg({'km_driven':'mean', 'selling_price': 'mean'}).reset_index()

        # Creating a pie chart for market share
        fig = px.pie(avg_dist, values='km_driven', names='fuel', hole=0.5)
        fig.update_traces(textposition='outside')
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        # st.write(filtered_df.columns)
        brand_share = filtered_df.groupby('Brand').agg({'selling_price': 'mean'}).reset_index()

        # Creating a pie chart for market share
        fig = px.pie(brand_share, values='selling_price', names='Brand', hole=0.5)
        fig.update_traces(textposition='outside')
        st.plotly_chart(fig, use_container_width=True)

    with col1:
        with st.expander("Fuel Wise Travell data &#x2935;"):
            st.write(avg_dist.style.background_gradient(cmap="Blues"))
            csv = avg_dist.to_csv(index=False).encode('utf-8')
            st.download_button("Download Data", data=csv, file_name='avg_dist.csv', mime="text/csv", help="Click here to download the CSV file")


    with col2:
        with st.expander("Market share &#x2935;"):
            st.write(brand_share.style.background_gradient(cmap="Blues"))
            csv = brand_share.to_csv(index=False).encode('utf-8')
            st.download_button("Download Data", data=csv, file_name='brand_share.csv', mime="text/csv", help="Click here to download the CSV file")

    fig = px.line(sp_year,
             x='year',
             y=['selling_price', 'km_driven'],
             title = '<b>Selling Price by Year<B>',
             template = template_style)

    fig.update_traces(
        hovertemplate='<b>Year: %{x}</b><br>Selling Price: %{y}<extra></extra>'
    )

    fig.update_layout(
        xaxis_title='<b>Year</b>',
        yaxis_title='<b>Selling Price</b>',
    )
    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    fuel_type_owner = filtered_df.groupby(['fuel', 'owner']).agg({'selling_price':'mean'}).reset_index()

    # Creating a bar chart for CPU brand prices
    fig = px.bar(fuel_type_owner, x='fuel', y='selling_price', 
                template=template_style,
                # text=fuel_type['selling_price'].apply(lambda x: '${:,.2f}'.format(x)),
                color='owner',
                hover_data=['owner'])
    fig.update_traces(
    texttemplate='%{y:.2s}',
    textposition='outside',
    hovertemplate='<b>Fuel: %{x}</b><br>Selling Price: %{y}<br>Owner: %{customdata[0]}<extra></extra>'
    )
    st.plotly_chart(fig, use_container_width=True)


#------------------------------

vizual_data()

