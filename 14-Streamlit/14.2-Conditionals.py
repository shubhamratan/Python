import streamlit as st
from datetime import date

st.title("Coffee Maker App")
st.subheader("Make your coffee")
if st.button("Make Coffee"):
    st.success("Here is your coffee")

add_milk = st.checkbox("Add milk")
add_sugar = st.checkbox("Add sugar")
if add_milk:
    st.write("Milk added to your coffee")
if add_sugar:
    st.write("Sugar added to your coffee")

coffee_type = st.radio("Select coffee type : ", ["Espresso", "Latte", "Cappuccino"])

st.write(f"You selected {coffee_type} coffee")

flavour =st.selectbox("Select flavour : ", ["Vanilla", "Chocolate", "Strawberry"])

st.write(f"You selected {flavour} flavour")

coffee_size = st.select_slider("Select coffee size : ", ["Small", "Medium", "Large"])

st.write(f"You selected {coffee_size} size")

sugar_amount = st.slider("Select sugar spoons : ", 0, 3, 1)

st.write(f"You selected {sugar_amount} spoons of sugar")

cups = st.number_input("How many coffees do you want to make? : ", min_value=1, max_value=10, value=1, step=1)

st.write(f"You selected {cups} cups of coffee") 

name = st.text_input("Enter your name : ")

if name:
    st.write(f"Hello {name}! Welcome! Your coffee is on the way")

dob = st.date_input("Enter your date of birth : ", min_value=date(1900, 1, 1),
    max_value=date.today(),
)
today = date.today()
age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

st.write(f"You are {age} years old")
