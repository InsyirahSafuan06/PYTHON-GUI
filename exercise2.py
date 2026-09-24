import streamlit as st

#Page title
st.title("Sample Quiz")

#Introduction
st.write("Answer the question below:")

#Question
st.subheader("Question 1")
st.write("What is the capital city of Malaysia?")

#Answer choices
answer = st.radio("Choose your answer:",
                ["Kuala Lumpur", "Penang", "Johor Bahru", "Malacca"])

#Button
if st.button("Submit Answer"):
    if answer == "Kuala Lumpur":
        st.success("Correct! Kuala Lumpur is the capital city of Malaysia.")
    else:
        st.error("Incorrect. The correct answer is Kuala Lumpur.")