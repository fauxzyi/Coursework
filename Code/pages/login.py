import streamlit as st
from authentication import *

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
st.title("Town House Food Management System")
usernameInput = st.text_input("Username")
passwordInput = st.text_input("Password", type="password")
# Takes text inputs from the user, assigns them to variables

if st.button("Sign In", use_container_width=True):
    if usernameInput == "":
        st.error("No username was entered")
    elif passwordInput == "":
        st.error("No password was entered")
    # Tests if the user has entered a username and password
    else:
        if authenticateLogin(str(usernameInput), str(passwordInput)) == True:
            userID = getID(usernameInput)
            st.session_state['permissions'] = checkPerms(str(usernameInput))
            if str(st.session_state['permissions']) == "admin" or str(st.session_state['permissions']) == "superAdmin":
                st.session_state['userID'] = userID
                st.session_state['name'] = usernameInput
                st.switch_page("pages/adminHome.py")
                # Adds userID and username to session state
                # Switch to the admin home page
            else:
                st.session_state['userID'] = userID
                st.session_state['name'] = usernameInput
                st.switch_page("pages/userHome.py")
                # Adds userID and username to session state to be used later
                # Switch to the user home page
        else:
            st.error("Username or password is incorrect (Both are Case-Sensitive)")

if st.button("Forgot password", use_container_width=True):
    st.switch_page("pages/forgotPassword.py")

if st.button("Switch to create account", use_container_width=True):
    st.switch_page("pages/createAccount.py")