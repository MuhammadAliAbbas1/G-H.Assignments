# 03_fahrenheit_to_celsius.md

import streamlit as st

def main():

    degrees_fahrenheit = st.number_input("Enter temperature in Fahrenheit:")

    degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0

    if degrees_fahrenheit:
      st.markdown(f"Temperature: {degrees_fahrenheit} = {degrees_celsius}C")

main()