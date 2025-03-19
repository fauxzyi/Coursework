import streamlit as st
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
from submission import *

if not st.session_state['permissions'] == 'user':
    st.warning("No permissions")
else:
    st.title("Your Current Orders")
    orders = getYourOrders(st.session_state["userID"])
    # Creates a list of all the orders submitted by the user who is signed in
    if len(orders) == 0:
        st.write("You have not submitted any orders yet.")
    # If there are no orders, display a message
    else:
        st.dataframe(orders)
        # Displays the orders in a dataframe
    if st.button("Back", use_container_width=True):
        st.switch_page("pages/userHome.py")