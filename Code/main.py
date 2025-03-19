# python -m streamlit run main.py
import streamlit as st

if 'permissions' not in st.session_state:
    st.session_state['permissions'] = 'none'
if 'userID' not in st.session_state:
    st.session_state['userID'] = 'none'
if 'name' not in st.session_state:
    st.session_state['name'] = 'none'

st.switch_page("pages/login.py")