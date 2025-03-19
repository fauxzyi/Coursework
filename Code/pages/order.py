import streamlit as st
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
from submission import *

if not st.session_state['permissions'] == 'user':
    st.warning("No permissions")
    # Checks permissions, users only
else:
    st.title("Packed Lunch Order")
    
    mains = getMains()
    sides = getSides()
    drinks = getDrinks()
    #Functions get the items from the database

    # If the lst of items returned by the functions is empty, the lines below will cause the code to crash
    mains = [x[0] for x in mains]
    sides = [x[0] for x in sides]
    drinks = [x[0] for x in drinks]
    # The above lines convert the list of tuples into a list of strings
    
    mains.insert(0, "Make Selection")
    sides.insert(0, "Make Selection")
    drinks.insert(0, "Make Selection")
    # Inserts "Make Selection" at the beginning of each list
    
    dateInput = st.date_input("What date do you need it?")
    # Shown to the user as a calendar input
    time = st.selectbox("What time do you need it?", ("Make Selection", "Before School (8 AM)", "Break (10:10/10:30 AM)"))
    main = st.selectbox("What is your choice for the main?", mains)
    side = st.selectbox("What is your choice for the side?", sides)
    drink = st.selectbox("What is your choice for the drink?", drinks)
    # Takes the inputs from the user as multiple choice dropdowns, make Selection is the default option
    userID = st.session_state['userID']

    if st.button("Submit", use_container_width=True):
        if time == "Make Selection" or main == "Make Selection" or side == "Make Selection" or drink == "Make Selection":
            st.error("Please make a selection for all options")
            # Ensures that the user has selected an option for each of the dropdowns
        else:
            submitOrder(dateInput, time, main, side, drink, userID)
            st.switch_page("pages/userHome.py")
            # Adds the order to the database and sends the user home

    if st.button("Submit 1000 times", use_container_width=True):
        if time == "Make Selection" or main == "Make Selection" or side == "Make Selection" or drink == "Make Selection":
            st.error("Please make a selection for all options")
        else:
            for i in range(0,1000):
                submitOrder(dateInput, time, main, side, drink, userID)
            st.switch_page("pages/userHome.py")

    if st.button("Back", use_container_width=True):
        st.switch_page("pages/userHome.py")