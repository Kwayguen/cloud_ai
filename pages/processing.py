
import streamlit as st
import pandas as pd
import seaborn as sns
import os

st.set_page_config(
    page_title='Streamlit',
    page_icon="🔫",
    layout='wide'
)

# upload file
uploaded_file = st.file_uploader("Choose a file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, delimiter=";")
    selected_columns = st.multiselect("Selectionner les colonnes du dataframe", df.columns)
    edited_df = st.data_editor(df[selected_columns])
    st.download_button(
        label="download data as csv",
        data=edited_df.to_csv(),
        file_name="df.csv",
        mime="text/csv"
    )
