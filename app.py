import streamlit as st
from authentication import initialize_database, register_user, login_user
import pandas as pd

initialize_database()

st.title("Travel Planner App")

menu = st.sidebar.selectbox("Menu", ["Login", "Register"])

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in:
    st.success("You are logged in!")

    if st.button("Logout"):
        st.session_state.logged_in = False

else:

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
            else:
                st.error("Invalid login")


travel_menu = st.sidebar.selectbox("Travel Itinerary Generator")

df = pd.read_excel("countrydataset.xlsx")
st.write("Dataset Loaded")

#userchoice
location = st.selectbox("Choose a location:", df["Location"].unique())
activity_type = st.selectbox("Choose an activity type:", df["Category"].unique())

'''
#come back and figure out#
#filter for userchoice
fitlered_df = df[
    (df["Location"] == location)
    (df["Category"] == activity_type)
]

#itinerary file
st.subheader('Your Itinerary')

morning = filtered_df[filtered_df["Time"] == "Morning"]
afternoon = filtered_df[filtered_df["Time"] == "Afternoon"]
evening = filtered_df[filtered_df["Time"] == "Evening"]

if not morning.empty:
    st.write(f"Morning: {morning.iloc[0]['Activity']}")
    itinerary.append({"Time": "Morning", "Activity": morning.iloc[0]["Activity"]})

if not afternoon.empty:
    st.write(f"Afternoon: {afternoon.iloc[0]['Activity']}")
    itinerary.append({"Time": "Afternoon", "Activity": afternoon.iloc[0]["Activity"]})

if not evening.empty:
    st.write(f"Evening: {evening.iloc[0]['Activity']}")
    itinerary.append({"Time": "Evening", "Activity": evening.iloc[0]["Activity"]})

itinerary = []
itinerary_df = pd.DataFrame(itinerary)

'''
