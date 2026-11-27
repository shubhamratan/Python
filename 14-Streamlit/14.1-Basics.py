import streamlit as st

st.title("My First Streamlit App")
st.header("Learning Streamlit")
st.text("Welcome to your first interactive app")
st.write("Hello! Welcome to my first app.")

sports = st.selectbox("Choose your fav sports", ["Cricket", "Football", "Tennis", "Hockey"])
st.write(f"Your favorite sport is {sports}")
st.success("You selected a valid sport")