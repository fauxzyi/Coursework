import streamlit as st
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
from submission import *

if not st.session_state['permissions'] == 'user':
    st.warning("No permissions")
    # Checks permissions, users only
else:
    st.title("Packed Lunch Order")
    
    dateInput = st.date_input("What date do you need it?")
    # Shown to the user as a calendar input
    time = st.selectbox("What time do you need it?", ("Make Selection", "Before School (8 AM)", "Break (10:10/10:30 AM)"))
    main = st.selectbox("What is your choice for the main?", ("Make Selection", "Ham Sandwich", "Cheese Sandwich"))
    side = st.selectbox("What is your choice for the side?", ("Make Selection", "Ready Salted Crisps", "Apple"))
    drink = st.selectbox("What is your choice for the drink?", ("Make Selection", "No Drink", "Water Bottle"))
    # Takes the inputs from the user as multiple choice dropdowns, make Selection is the default option
    userID = st.session_state['userID']

    if st.button("Submit", use_container_width=True):
        if time == "Make Selection" or main == "Make Selection" or side == "Make Selection" or drink == "Make Selection":
            st.warning("Please make a selection for all options")
            # Ensures that the user has selected an option for each of the dropdowns
        else:
            submitOrder(dateInput, time, main, side, drink, userID)
            st.switch_page("pages/userHome.py")
            # Adds the order to the database and sends the user home

    if st.button("Back", use_container_width=True):
        st.switch_page("pages/userHome.py")