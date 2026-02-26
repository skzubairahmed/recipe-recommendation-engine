import streamlit as st
from engine import get_recommendations

st.title("Flavour Intelligence 👨‍🍳")
st.write("Enter the ingredients you have, adn I'll find the perfect recipe for you.")

user_ingredients = st.text_input("Ingredients(comma separated)", "chicken, garlic, olive oil")

if st.button("Generate Flavour profile"):
    results = get_recommendations(user_ingredients)
    for i, row in results.iterrows():
        st.subheader(f"🍴 {row['cuisine'].capitalize()} Style")
        st.write(f"**Ingredients:** {', '.join(row['ingredients'])}")
        st.divider()
