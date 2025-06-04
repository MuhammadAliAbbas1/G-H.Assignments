# 05_triangle_perimeter.md

import streamlit as st

def main():

    side1 = st.number_input("Length of side 1", min_value=0.0, value=0.0)
    side2 = st.number_input("Length of side 2", min_value=0.0, value=0.0)
    side3 = st.number_input("Length of side 3", min_value=0.0, value=0.0)

    if st.button("Calculate Perimeter"):
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            st.error("All sides must be greater than 0.")
        else:
            perimeter = side1 + side2 + side3
            st.success(f"The perimeter of the triangle is: {perimeter}")

main()