import streamlit as st
from authentication import *

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
st.title("Town House Food Management System")
usernameInput = st.text_input("Create username")
passwordInput = st.text_input("Create password", type="password")
passwordInput2 = st.text_input("Confirm password", type="password")
permissions = st.selectbox("Choose Permissions", ("Make Selection", "User", "Admin"))
# All data is inputted by the user and stored in variables

if st.button("Create account", use_container_width=True):
    errors = []
    if usernameInput == "":
        errors.append("No username was entered")
    if accountExists(str(usernameInput)) == True:
        errors.append("Account with this name already exists")
    if len(passwordInput) < 3 or len(passwordInput) > 20:
        errors.append("Password is incorrect length, must be between 3 and 20 characters")
    if passwordInput != passwordInput2:
        errors.append("Passwords do not match")
    if permissions == "Make Selection":
        errors.append("You need to choose permissions")
    # Inputs are validated before being passed to the createAccount function
    if len(errors) == 0:
        permissions = str(permissions).lower()
        if createAccount(str(usernameInput), str(passwordInput), permissions):
            st.switch_page("pages/login.py")
            # Account is added to the database and the user is redirected to the login page
        else:
            st.warning("An error has occured")
            # Shouldn't ever happen due to validation but just in case
    else:
        for i in range(len(errors)):
            st.error(errors[i])

if st.button("Switch to sign in", use_container_width=True):
    st.switch_page("pages/login.py")