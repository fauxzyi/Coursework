import streamlit as st
from submission import *
from authentication import *
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

if not st.session_state['permissions'] == 'superAdmin':
    st.warning("No permissions")
else:
    st.title("Manage Users")
    st.write("Current Users")
    users = []
    permissions = []
    for i in getUsers():
        users.append(i[0])
        permissions.append(i[1])
    for i, (user, permission) in enumerate(zip(users, permissions), start=1):
        col1, col2, col3 = st.columns([4, 3, 2])
        col1.markdown(f"* {user}")
        col2.markdown(permissions[i-1])
        if user == st.session_state['name']:
            col3.markdown("Do not delete, this is you")
        else:
            if col3.button("Delete", key=f"delete_{i}"):
                deleteAccount(user)
                st.rerun()

    if st.button("Back", use_container_width=True):
        st.switch_page("pages/adminHome.py")