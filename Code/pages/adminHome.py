import streamlit as st
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

if st.session_state != {'admin', 'superAdmin'}:
    st.title("Town House Food Management System")
    # Checks permissions, only admins can see this page
    
    if st.button("View Orders", use_container_width=True):
        st.switch_page("pages/viewOrders.py")
    
    if st.button("View Suggestions", use_container_width=True):
        st.switch_page("pages/viewSuggestions.py")

    if st.button("Add/Modify Food", use_container_width=True):
        st.switch_page("pages/addOrEditFood.py")

    # Three buttons for normal admin features

    if st.session_state['permissions'] == 'superAdmin':
        if st.button("Manage Users (Special Super Admin Feature)", use_container_width=True):
            st.switch_page("pages/manageUsers.py")

    # Manage users option for convenience of developing

    if st.button("Log out", use_container_width=True):
        st.session_state['permissions'] = 'none'
        st.session_state['userID'] = 'none'
        st.session_state['name'] = 'none'
        st.switch_page("pages/login.py")
        # Log out button, clears session state and switches to login
else:
    st.warning("No permissions")