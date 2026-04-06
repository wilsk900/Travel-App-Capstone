import streamlit as st

st.header("Mileage Tracker")

#get speed and travel time from the user
speed = st.number_input('What is the average speed of the vehicle (mph)?', min_value=0, value=60))
time_traveled = st.number_input('How many hours will you be traveling?', min_value=1, value=1))

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

#to save to itinerary file
if st.button("Add mileage calculations to intinerary"):
    summary = f"Total travel distance at {speed} mph for {time_traveled} hours: {total_distance} miles."
    st.session_state['mileage_summary'] = summary
    st.write("Summary saved!")
