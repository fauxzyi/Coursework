import streamlit as st
from submission import *
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

if st.session_state != {'admin', 'superAdmin'}:
    # Checks permissions, admins only
    st.title("Add or Modify Available Food")
    with st.expander("Mains"):
        # Uses an expander to show mains
        st.write("Current mains:")
        mains = []
        for i in getMains():
            # Returns mains from database
            mains.append(i[0])
        for i, item in enumerate(mains, start=1):
            col1, col2 = st.columns([4, 1])
            col1.markdown(f"* {item}")
            # Creates a bullet point list of mains
            if col2.button("Delete", key=i):
                deleteMain(item)
                st.rerun()
                # Creates a delete button for each main
        mainName = st.text_input("New main")
        if st.button("Add main to database"):
            if mainName != "":
                if mainName in mains:
                    st.error("This main already exists")
                else:
                    newMain(mainName)
                    st.rerun()
                    # Takes input for a new main, adds it to the databse if it doesn't already exist
            else:
                st.warning("Please enter text")

    with st.expander("Sides"):
        # Uses an expander to show sides
        st.write("Current sides:")
        sides = []
        for i in getSides():
            sides.append(i[0])
        for i, item in enumerate(sides, start=1):
            col1, col2 = st.columns([4, 1])
            col1.markdown(f"* {item}")
            # Creates a bullet point list of sides
            if col2.button("Delete", key=f"side_{i}"):
                deleteSide(item)
                st.rerun()
                # Creates a delete button for each side
        sideName = st.text_input("New side")
        if st.button("Add side to database"):
            if sideName != "":
                if sideName in sides:
                    st.error("This side already exists")
                else:
                    newSide(sideName)
                    st.rerun()
                    # Takes input for a new side, adds it to the databse if it doesn't already exist
            else:
                st.warning("Please enter text")

    with st.expander("Drinks"):
        # Uses an expander to show drinks
        st.write("Current drinks:")
        drinks = []
        for i in getDrinks():
            drinks.append(i[0])
        for i, item in enumerate(drinks, start=1):
            col1, col2 = st.columns([4, 1])
            col1.markdown(f"* {item}")
            # Creates a bullet point list of drinks
            if col2.button("Delete", key=f"drink_{i}"):
                deleteDrink(item)
                st.rerun()
                # Creates a delete button for each drink
        drinkName = st.text_input("New drink")
        if st.button("Add drink to database"):
            if drinkName != "":
                if drinkName in drinks:
                    st.error("This drink already exists")
                else:
                    newDrink(drinkName)
                    st.rerun()
                    # Takes input for a new drink, adds it to the databse if it doesn't already exist
            else:
                st.warning("Please enter text")
    if st.button("Back", use_container_width=True):
        st.switch_page("pages/adminHome.py")
else:
    st.warning("No Permissions")