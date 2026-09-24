import streamlit as st

st.title("Instant Loan")
st.write("If the loan value is less than 3 times the salary, the application is approved.")

loan_value = st.number_input("Loan Value", value=None, key="loan_value")
salary_value = st.number_input("Salary Value", value=None, key="salary_value")

loan_value = loan_value if loan_value is not None else 0
salary_value = salary_value if salary_value is not None else 0  


if st.button("Calculate"):
    if loan_value < 3 * salary_value:
        st.title("Instant Loan")
        st.write("If the loan value is less than 3 times the salary, the application is approved.")
        st.write(f"Loan Value: {st.session_state['loan_value']}")
        st.write(f"Salary Value: {st.session_state['salary_value']}") 
        st.write("Your application approved.")
    else:
        st.title("Instant Loan")
        st.write("If the loan value is less than 3 times the salary, the application is approved.")
        st.write(f"Loan Value: {st.session_state['loan_value']}")
        st.write(f"Salary Value: {st.session_state['salary_value']}")
        st.write("Your application not been approved.")