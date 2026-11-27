import streamlit as st

st.title("Coffee Taste Poll")

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Espresso")
    st.image("https://i.shgcdn.com/f7ed9fd1-70f6-41ce-a8c2-be8092ddb063/-/format/auto/-/preview/3000x3000/-/quality/lighter/", width=200)
    vote1=st.button("Vote Espresso")

with col2:
    st.header("Latte")
    st.image("https://coffeebros.com/cdn/shop/articles/unnamed_be2775a1-186d-40c1-b094-488fa5fa4050.png?v=1675965693",width=200)
    vote2=st.button("Vote Latte")

with col3:
    st.header("Cappuccino")
    st.image("https://www.alisonspantry.com/uploads/new-products/1328-2.jpg",width=200)
    vote3=st.button("Vote Cappuccino")

if vote1:
    st.success("Thank you for voting for Espresso")
elif vote2:
    st.success("Thank you for voting for Latte")
elif vote3:
    st.success("Thank you for voting for Cappuccino")

name = st.sidebar.text_input("Enter your name : ")
coffee = st.sidebar.selectbox("Choose your coffee", ["Espresso","Latte","Cappuccino"])
st.write(f"Welcome {name} and your {coffee} is getting ready")

with st.expander("Show coffee Making Instructions"):
    st.write("""
      1. Grind Coffee beans
      2. Boil Water
      3. Add Coffee
      4. Add milk
      5. Steam
      6. Serve
    """)

    st.markdown('### Welome to Coffee Making APP')
    st.markdown('> Here you will learn how to make coffee')