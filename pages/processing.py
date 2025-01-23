
import streamlit as st
import pandas as pd
import seaborn as sns
import os
import matplotlib.pyplot as plt

st.set_page_config(
    page_title='Streamlit',
    page_icon="🔫",
    layout='wide'
)

# upload file
uploaded_file = st.file_uploader("Choose a file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, delimiter=",")
    selected_columns = st.multiselect("Selectionner les colonnes du dataframe", df.columns)
    edited_df = st.data_editor(df[selected_columns])
    
if uploaded_file is not None:
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("col1")
        chart_type = st.selectbox(
            "Choisir le type de graphique a afficher",
            ("Bar Chart", "Line Chart", "Scatter Plot")
        )
        
    
    with col2:
        st.write("col2")
        if st.button("Afficher Graphique"):
            st.write('afficher graphique')
        
        if edited_df is not None:
            st.download_button(
            label="download data as csv",
            data=edited_df.to_csv(),
            file_name="df.csv",
            mime="text/csv"
        )



    






