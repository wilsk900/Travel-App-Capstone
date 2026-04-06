import streamlit as st

def mileage():
    st.header("Mileage Tracker")
    
    #get speed and travel time from the user
    speed = st.number_input('What is the average speed of the vehicle (mph)?', min_value=0)
    time_traveled = st.number_input('How many hours will you be traveling?', min_value=1)
    
    #display for chart
    st.write('\nHour by Hour Breakdown')
    st.write('__________________________')
    
    #calculations
    total_dist = speed * time_traveled
    st.success(f"--Total Estimated Distance: {total_dist} miles--")
    
    breakdown=[]
    for hour in range(1, time_traveled +1):
        distance = hour * speed
        breakdown.append({"Hour": hour, "Distance Traveled (miles)": distance})
    
    st.table(breakdown)

    summary = f"Total travel distance at {speed} mph for {time_traveled} hours: {total_dist} miles."
    
    full_itin_mile = f"
    Trip Itinerary\n____________\n{final_itinerary}\n\nTransportation Summary\n___________\n{summary}
    "
    #to save to itinerary file
    if st.download_button("Add mileage calculations to intinerary"):
        data = full_file_content,
        file_namee = "full_trip_plan.txt",
        mime = "text/plain"
