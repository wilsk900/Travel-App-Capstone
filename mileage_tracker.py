import streamlit as st
import show_itinerary as itinerary

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

    summary = f"""
        ------------------------------
        Transportation Summary
        Total Distance: {total_dist} miles
        Average Speed: {speed} mph
        Travel Time: {time_traveled} hours
        
        Breakdown Table: {st.table(breakdown)}
        ------------------------------

        """
            st.session_state['mileage_summary'] = summary
            st.write("Summary saved)
            

        st.text(summary)
                     

    with open("my_itinerary.txt", "r") as f:
        itinerary_content = f.read()
    combined_data = f"{summary}\n\n{itinerary_content}"
    
    st.download_button(
        label="Add mileage calculations to itinerary",
        data=combined_data,
        file_name="full_travel_plan.txt",
        mime="text/plain"
    )
