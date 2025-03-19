import streamlit as st
from submission import *
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

if not st.session_state['permissions'] == 'user':
    st.warning("No permissions")
    # Check permissions, users only
else:
    st.title("Make a suggestion")
    suggestion = st.text_area("What is your suggestion?")

    # Text input varaible for suggestion

    if st.button("Submit", use_container_width=True):
        if suggestion == "":
            st.error("Please type your suggestion")
            # Checks if anything has been entered
        else:
            submitSuggestion(suggestion, st.session_state['userID'])
            st.switch_page("pages/userHome.py")
            # Adds suggestion to the database, sends the user home
    if st.button("Back", use_container_width=True):
        st.switch_page("pages/userHome.py")