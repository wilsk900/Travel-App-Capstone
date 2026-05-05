import streamlit as st
from authentication import initialize_database, register_user, login_user
import pandas as pd
from itinerary import show_itinerary
from mileage_tracker import mileage
from budget_manager import money_manage
import io

initialize_database()

st.title("Travel Planner App\n______________________")

try:
    df = pd.read_excel("countrydataset.xlsx")
    filtered_df = df # Replace this with your actual filtering logic
except:
    st.error("Could not find the data file!")
    filtered_df = pd.DataFrame()
#sessionstate
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
#main menu setup 
if st.session_state.logged_in:
    #only show when logged in
    st.success("You are logged in!")
    menu = st.sidebar.selectbox("Menu", ["Travel Itinerary Generator", "Mileage Tracker", "Trip Budget Planner", "Logout"])
else: 
    #only show when logged out
    menu = st.sidebar.selectbox("Menu", ["Login", "Register"])
#for each menu option when logged out
if not st.session_state.logged_in:
    if menu == "Register":

        st.subheader("Create Account")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Register"):

            if register_user(username, password):
                st.success("Account created!")
            else:
                st.error("Username already exists")

    elif menu == "Login":

        st.subheader("Login")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):

            if login_user(username, password):
                st.session_state.logged_in = True
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Invalid login")

else:
    #for each menu option when logged in
    if menu == "Logout":
        st.session_state.logged_in = False
        st.rerun()

    elif menu == "Travel Itinerary Generator":
        show_itinerary(filtered_df)

    elif menu == "Mileage Tracker":
        mileage()

    elif menu == "Trip Budget Planner":
        money_manage()

st.sidebar.header("Download Full Trip Plan")

if st.sidebar.button("Download Complete Trip File"):

    itinerary = st.session_state.get('itinerary_summary', "No itinerary created")
    mileage = st.session_state.get('mileage_summary', "No mileage data")
    budget = st.session_state.get('budget_summary', "No budget data")

    data = {
        "Category": ["Itinerary", "Mileage", "Budget"],
        "Details": [itinerary, mileage, budget]
    }

    df = pd.DataFrame(data)

    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name="Trip Summary")

    excel_data = output.getvalue()

    st.sidebar.download_button(
        label="Download Trip Summary (Excel)",
        data=excel_data,
        file_name="Trip_Summary.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
