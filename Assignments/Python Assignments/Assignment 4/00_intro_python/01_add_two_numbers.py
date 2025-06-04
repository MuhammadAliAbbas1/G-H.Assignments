#01_add_two_numbers.md

import streamlit as st

def main():
    st.title("🔢 Sum Calculator")

    num1 = st.number_input("Enter the first number:", step=1)
    num2 = st.number_input("Enter the second number:", step=1)

    if st.button("Calculate Sum"):
        total = num1 + num2
        st.success(f"The sum of {num1} and {num2} is: {total}")

main()

