import streamlit as st
import time

st.snow()
st.title("Snack Bar Ordering System")
st.write("Items order list:")
popcorn_qty = st.number_input(
    "Popcorn (RM 8.50)", value=0, min_value=0, step=1, key="popcorn"
)

hotdog_qty = st.number_input(
    "Hotdog (RM 7.00)", value=0, min_value=0, step=1, key="hotdog"
)

nachos_qty = st.number_input(
    "Nachos (RM 6.50)", value=0, min_value=0, step=1, key="nachos"
)

soft_drink_qty = st.number_input(
    "Soft Drink (RM 5.00)", value=0, min_value=0, step=1, key="soft_drink"
)

p_qty = popcorn_qty if popcorn_qty is not None else 0
h_qty = hotdog_qty if hotdog_qty is not None else 0
n_qty = nachos_qty if nachos_qty is not None else 0
s_qty = soft_drink_qty if soft_drink_qty is not None else 0
st.write("")

if st.button("Calculate total", type="primary"):
    with st.spinner("Wait for it...", show_time=True):
        time.sleep(3)  
    total_cost = (p_qty * 8.50) + (h_qty * 7.00) + (n_qty * 6.50) + (s_qty * 5.00)
    
    st.success("Success!")
    st.divider()
    
    st.write(f"Total cost: RM {round(total_cost, 2)}")

    if total_cost >= 50:
        discount = total_cost * 0.05
        final_amount = total_cost - discount
        
        st.write(f"Discount applied (5%): RM {round(discount, 2)}")
        st.write(f"### Final amount to pay: RM {round(final_amount, 2)}")
    else:
        st.write(f"### Final amount to pay: RM {round(total_cost, 2)}")

st.write("") 
st.button("Clear all", on_click=lambda: st.session_state.update({"popcorn": 0, "hotdog": 0, "nachos": 0, "soft_drink": 0}))

sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")