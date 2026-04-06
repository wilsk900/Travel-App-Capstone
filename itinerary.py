import streamlit as st
import pandas as pd

def show_itinerary(filtered_df):
    st.header("Travel Itinerary Generator")

    df = pd.read_excel("countrydataset.xlsx")
    st.write("Test dataset loaded")

    #userchoice
    location = st.selectbox("Choose a location:", df["Location"].unique())
    activity_type = st.selectbox("Choose an activity type:", df["Category"].unique())
    time = st.selectbox("Choose a time of day:", df["Time"].unique())

    filtered_df = df[
        (df["Location"] == location) &
        (df["Category"] == activity_type) &
        (df["Time"] == time)
        ]


    itinerary = []

    if not filtered_df.empty:
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

        itinerary_df = pd.DataFrame(itinerary)

    else:
        st.warning("No activites category found for this entry. Try a different category")