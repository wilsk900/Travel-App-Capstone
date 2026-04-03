import streamlit as st
import pandas as pd
from datetime import date

username = "test_user" #will get rid of when auth connected

create_trip(username)

DESTINATIONS = ["Thailand", "Jamaica", "Miami"]

def create_trip(username):

 st.header("Create a New Trip")

    destination = st.selectbox(
        "Choose Destination",
        DESTINATIONS)
    )

    start_date = st.date_input("Start Date", date.today())
    end_date = st.date_input("End Date", date.today())

    budget = st.number_input(
        "Budget ($)",
        min_value=0,
        step=100
    )

    notes = st.text_area("Trip Notes")

    if st.button("Save Trip"):

        new_trip = pd.DataFrame([{
            "username": username,
            "destination": destination,
            "start_date": start_date,
            "end_date": end_date,
            "budget": budget,
            "notes": notes
        }])

        try:
            trips = pd.read_excel("trips.xlsx")
            trips = pd.concat([trips, new_trip], ignore_index=True)
        except:
            trips = new_trip

        trips.to_excel("trips.xlsx", index=False)

        st.success("Trip saved successfully!")
