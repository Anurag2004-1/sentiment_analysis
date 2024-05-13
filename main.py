# main.py
import streamlit as st
import time

st.set_page_config(page_title="analyse your sentiment", page_icon="🧊")
st.markdown('<link rel="stylesheet" href="styles.css">', unsafe_allow_html=True)
# from streamlit_option_menu_bar

st.title("*welcome* to :blue[SENTIMETRIC]")
time.sleep(2)
st.switch_page("pages/signin.py")
