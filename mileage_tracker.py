import streamlit as st
from itinerary import show_itinerary

def mileage():
    st.header("Mileage Tracker")
    
    # Get speed and travel time from the user
    speed = st.number_input('What is the average speed of the vehicle (mph)?', min_value=0)
    time_traveled = st.number_input('How many hours will you be traveling?', min_value=1)
    
    # Display for chart
    st.write('\nHour by Hour Breakdown')
    st.write('__________________________')
    
    # Calculations
    total_dist = speed * time_traveled
    st.success(f"--Total Estimated Distance: {total_dist} miles--")
    
    breakdown = []
    for hour in range(1, time_traveled + 1):
        distance = hour * speed
        breakdown.append({"Hour": hour, "Distance Traveled (miles)": distance})
    
    st.table(breakdown)
    
    summary = f"""
------------------------------
Transportation Summary
Total Distance: {total_dist} miles
Average Speed: {speed} mph
Travel Time: {time_traveled} hours
------------------------------
"""
    
    st.session_state['mileage_summary'] = summary
    st.write("Summary saved!")
    st.text(summary)

    #save mileage summary
    st.session_state['mileage_summary'] = summary
    st.success("Mileage saved!")
    
