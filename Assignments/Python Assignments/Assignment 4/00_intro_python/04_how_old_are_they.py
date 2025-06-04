# 04_how_old_are_they

import streamlit as st

def main():

   anton: int = 21
   beth: int = anton + 6
   chen: int = beth + 20
   drew: int = chen + anton
   ethan: int = chen

   st.text(f"Anton is  {anton}")
   st.text(f"Beth is  {beth}")
   st.text(f"Chen is  {chen}")
   st.text(f"Drew is  {drew}")
   st.text(f"Ethan is  {ethan}")

main()