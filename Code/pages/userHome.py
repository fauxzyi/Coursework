import streamlit as st
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

if not st.session_state['permissions'] == 'user':
    st.warning("No permissions")
    # Checks permissions before loading the page, only signed-in users can see this page
else:
    st.title("Town House Food Management System")

    if st.button("Order a Packed Lunch", use_container_width=True):
        st.switch_page("pages/order.py")

    if st.button("Submit a Suggestion", use_container_width=True):
        st.switch_page("pages/suggestion.py")

    if st.button("View Your Orders", use_container_width=True):
        st.switch_page("pages/getYourOrders.py")

    # Three buttons for each of the three pages

    if st.button("Log out", use_container_width=True):
        st.session_state['permissions'] = 'none'
        st.session_state['userID'] = 'none'
        st.session_state['name'] = 'none'
        st.switch_page("pages/login.py")
    # Log out button, clears everythin stored in the session state, and switches to login