import streamlit as st
import pandas as pd

def show_itinerary(filtered_df):
    st.header("Travel Itinerary Generator")

    df = pd.read_excel("countrydataset.xlsx")
    st.write("Test dataset loaded")

    #userchoice
import streamlit as st
import pandas as pd

def show_itinerary(df):
    st.header("Daily Itinerary Builder")

    location = st.selectbox("Where are you heading?", df["Location"].unique())
    loc_df = df[df["Location"] == location]
    
    morn_opt = loc_df[loc_df["Time"] == "Morning"]["Activity"].tolist()
    after_opt = loc_df[loc_df["Time"] == "Afternoon"]["Activity"].tolist()
    even_opt = loc_df[loc_df["Time"] == "Evening"]["Activity"].tolist()
    food_opt = loc_df[loc_df["Time"] == "Food"]["Activity"].tolist()

    m = st.selectbox("Morning Activity", ["None"] + morn_opt)
    a = st.selectbox("Afternoon Activity", ["None"] + after_opt)
    e = st.selectbox("Evening Activity", ["None"] + even_opt)
    f = st.selectbox("Food Option", ["None"] + food_opt)

    final_itinerary = f"Trip to {location}\n"
    if m != "None": final_itinerary += f"- Morning: {m}\n"
    if a != "None": final_itinerary += f"- Afternoon: {a}\n"
    if e != "None": final_itinerary += f"- Evening: {e}\n"
    if f != "None": final_itinerary += f"- Food Option: {f}\n"

    # SAVE itinerary to session state
    st.session_state['itinerary_summary'] = final_itinerary

    st.success("Itinerary saved!")

    # Optional download (you can keep or remove)
    st.download_button(
        label="Download Itinerary Only",
        data=final_itinerary,
        file_name="itinerary.txt"
    )
