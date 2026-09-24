import streamlit as st

#Page title
st.title(" Simple Input GUI")
st.write("What is your name?")
name = st.text_input("Enter your name:")

if st.button ("Submit"):
    if name:
        st.write(f" Hello, {name}!  Welcome to Streamlit.")
    else:
        st.warning("Please enter your name.")