import streamlit as st
from authentication import initialize_database, register_user, login_user

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
