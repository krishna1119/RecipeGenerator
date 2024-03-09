import streamlit as st

st.header("Let's Make some Food!")
st.subheader("Enter your Ingredients (separated by commas)")
ingredients = st.text_input("Enter ingredients")

st.subheader("Enter your cooking time (in minutes)")
cooking_time = st.text_input("Enter cooking time")

st.subheader("Enter your preferences")
preferences = st.text_input("Enter preferences")

# Button to submit inputs
if st.button("Submit"):
    # Add logic here to process user inputs
    st.success("Inputs submitted successfully!")






