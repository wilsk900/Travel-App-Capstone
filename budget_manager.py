import streamlit as st
import pandas as pd
import plotly.express as px
from mileage_tracker import mileage

def money_manage():
    st.header("Trip Budget Planner")
    st.write("Enter your total budget to see the recommended spending breakdown.")

    total_budget = st.number_input("Total Trip Budget ($):", min_value=0.0)

    if total_budget > 0:
        housing = total_budget * 0.50
        food = total_budget * 0.20
        activities = total_budget * 0.20
        gas = total_budget * 0.10

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Housing (50%)", f"${housing:,.2f}")
        col2.metric("Food (20%)", f"${food:,.2f}")
        col3.metric("Activities (20%)", f"${activities:,.2f}")
        col4.metric("Gas (10%)", f"${gas:,.2f}")

#for pie chart
        data = {
            "Category": ["Housing", "Food", "Activities", "Gas"],
            "Amount": [housing, food, activities, gas]
        }
        df = pd.DataFrame(data)

        fig = px.pie(
            df,
            values='Amount',
            names='Category',
            title=f"Budget Breakdown: ${total_budget:,.2f}",
            color_discrete_sequence=px.colors.sequential.RdBu
        )

        st.plotly_chart(fig)

        if st.button("Save Budget to Itinerary"):
            summary = f"Budget Breakdown: Housing: ${housing}, Food: ${food}, Activities: ${activities}, Gas: ${gas}"
            st.session_state['budget_summary'] = summary
            st.success("Budget saved!")
    else:
        st.warning("Please enter a budget amount greater than 0.")
