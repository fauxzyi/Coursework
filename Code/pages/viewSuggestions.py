import streamlit as st
from submission import *
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

if st.session_state != {'admin', 'superAdmin'}:
    st.title("Submitted Suggestions")

    st.subheader("From oldest to newest")

    suggestions = []
    # An array to store all the suggestions

    for i in getSuggestions():
        suggestions.append(i[0])
    # Calls a function to get the suggestions and adds them to the list

    if suggestions == []:
        st.write("No suggestions have been submitted")
    # If there are no suggestions, display a message

    for i, item in enumerate(suggestions, start=1):
        st.markdown(f"{i}. {item}")
    # Displays all the suggestions in numbered list

    if st.button("Clear Suggestions", use_container_width=True):
        clearSuggestions()
        st.rerun()
    # Button to clear all the suggestions

    if st.button("Back", use_container_width=True):
        st.switch_page("pages/adminHome.py")
else:
    st.warning("No permissions")
