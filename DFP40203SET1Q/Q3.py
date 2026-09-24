import streamlit as st

st.title("Cinema Package Calculator")

package_prices = {
    "Standard": 12.00,
    "VIP": 30.00,
    "Family": 50.00,
}

discounts = {
    "Regular": 0,
    "Students": 20,
    "Senior": 15,
}

st.write("Cinema Package:")
option_package = st.selectbox(
    "Select a package",
    ["Select a package", "Standard", "VIP", "Family"],
)

st.write("Customer Type:")
option_type = st.selectbox(
    "Select Customer Type",
    ["Regular", "Students", "Senior"],
)

if st.button("Calculate Total Payment"):
    if option_package == "Select a package":
        st.warning("Please choose a cinema package first.")
    else:
        base_price = package_prices[option_package]
        discount_percent = discounts[option_type]
        total_payment = base_price * (1 - discount_percent / 100)

        st.write(f"Total payment: RM {total_payment:.2f}")