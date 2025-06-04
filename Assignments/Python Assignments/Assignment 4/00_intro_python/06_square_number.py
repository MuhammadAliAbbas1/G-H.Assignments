# 06_square_number.md

import streamlit as st

def main():

  number = st.number_input("Type a number to see its square:")

  squared = number ** 2

  if number:
    st.write(f"The square of {number} is {squared}")


main()