
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
        st.subheader("Configuration du graphique")
        
        chart_type = st.selectbox(
            "Choisir le type de graphique à afficher",
            ("Bar Chart", "Line Chart", "Scatter Plot")
        )

        x_axis = st.selectbox("Sélectionner la colonne pour l'axe X", selected_columns)
        y_axis = st.selectbox("Sélectionner la colonne pour l'axe Y", selected_columns)
        
        
    
    with col2:
        st.subheader("Action")
        if st.button("Afficher le Graphique"):
            st.write("Graphique généré :")
            
            fig, ax = plt.subplots()

            if chart_type == "Bar Chart":
                sns.barplot(
                    data=edited_df, 
                    x=x_axis, 
                    y=y_axis, 
                    ax=ax,
                    errorbar=None
                )
            
            elif chart_type == "Line Chart":
                sns.lineplot(
                    data=edited_df, 
                    x=x_axis, 
                    y=y_axis, 
                    ax=ax
                )
                
            elif chart_type == "Scatter Plot":
                sns.scatterplot(
                    data=edited_df, 
                    x=x_axis, 
                    y=y_axis, 
                    ax=ax
                )
            plt.tight_layout()
            st.pyplot(fig)
        
        if edited_df is not None:
            st.download_button(
            label="download data as csv",
            data=edited_df.to_csv(),
            file_name="df.csv",
            mime="text/csv"
        )









