import google.generativeai as genai
import streamlit as st

genai.configure(api_key="AIzaSyD_hS7CZeAj01uBur9IemKkcf1sSR8rOLY")
genai.GenerativeModel("gemini-1.5-flash")

prompt=st.chat_input("Enter your prompt")
if prompt: 
  response = generate_content(prompt)
  st.write(response)

