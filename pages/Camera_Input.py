import streamlit as st

st.set_page_config(
    page_title='Streamlit',
    page_icon="🔫",
    layout='wide'
)

enable = st.checkbox("Enable camera")
picture = st.camera_input("Take a picture", disabled=not enable)

if picture:
    st.image(picture)