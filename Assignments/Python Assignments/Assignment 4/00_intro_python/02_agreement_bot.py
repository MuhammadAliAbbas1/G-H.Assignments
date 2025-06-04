# 02_agreement_bot.md

import streamlit as st

def main():
    user_input = st.text_input("What's your favorite animal? ")

    if user_input:
        st.markdown(f"My favorite animal is also ***{user_input}***!")

main()