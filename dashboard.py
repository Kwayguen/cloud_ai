

import streamlit as st
import pandas as pd
import seaborn as sns

st.set_page_config(
    page_title='Streamlit',
    page_icon="🔫",
    layout='wide'
)

@st.cache_data
def load_data():
    return pd.read_csv('https://raw.githubusercontent.com/Quera-fr/Python-Programming/refs/heads/main/data.csv')

try:
    st.sidebar.secrets['API_KEY']
except:
    st.error('pas de clé')

df = load_data()



st.title("Données avec Streamlit")

if st.checkbox('Afficher Données'):
    st.write(df)

with st.form(key='myForm'):
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.title('form')
        profession = st.selectbox('selectionner une profession', df.Profession.unique())
        age_range = st.slider('Selectionner une tranche d\'age: ', df.Age.min(), df.Age.max(), (df.Age.min(),df.Age.max()))
        validate_button = st.form_submit_button(label='Valider')
    with col2:
        st.title('result')
        data_age = df[(df.Profession == profession) & 
                        (df.Age >= age_range[0]) & 
                        (df.Age <= age_range[1])].Age
        if validate_button:
            ax = sns.histplot(data_age, bins=age_range[1]-age_range[0], color="k")
            ax.set_ylabel("Sequential")
            st.pyplot(ax.figure)


    


st.sidebar.image("https://www.macapflag.com/blog/wp-content/uploads/2021/03/Un-logo-facile-a-comprendre.jpg")

st.sidebar.video('https://www.youtube.com/watch?v=8iLduIDZVE4')
