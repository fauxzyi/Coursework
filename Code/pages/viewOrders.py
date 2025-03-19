import streamlit as st
import pandas as pd
import datetime as dt
from submission import *
from authentication import getName
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
dateNow = dt.datetime.now().date()

if st.session_state != {'admin', 'superAdmin'}:
    st.title("Submitted Orders")
    
    orders = getOrders()
    # Runs a funcion to put all the orders in a list

    if len(orders) == 0:
        st.write("No orders have been submitted yet")
        # If there are no orders, display a message
    else:
        dates = [order[0] for order in orders]
        times = [order[1] for order in orders]
        mains = [order[2] for order in orders]
        sides = [order[3] for order in orders]
        drinks = [order[4] for order in orders]
        names = []
        for i in range(0,len(orders)):
            names.append(getName(orders[i][5]))
        # Creates a list for each of the items in every order

        df = pd.DataFrame(
        {
            "Name": names,
            "Date Needed": dates,
            "Time Needed": times,
            "Main": mains,
            "Side": sides,
            "Drink": drinks
        })
        # Creates a datafram with columns for each of the items

        df = df.sort_values(by='Date Needed')
        df.index.name = 'ID'
        st.dataframe(df)
        # Sorts and displays the dataframe

    if st.button("Remove old orders", use_container_width=True):
        removeOldOrders(dateNow)
        st.rerun()
        # Button which removes every order that was due before the current date

    if st.button("Back", use_container_width=True):
        st.switch_page("pages/adminHome.py")
else:
    st.warning("No permissions")