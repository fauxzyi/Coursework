import streamlit as st
from authentication import *

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
st.title("Town House Food Management System")

usernameInput = st.text_input("What is your username")
if st.button("Tell me my password", use_container_width=True):
    if accountExists(usernameInput):
        password = getPassword(usernameInput)
        st.write("Your password is '" + password + "'")
        if password == 'password':
            st.write("Thats pretty stupid isn't it?")
    else:
        st.write("Account does not exist")

if st.button("Back to login", use_container_width=True):
    st.switch_page("pages/login.py")