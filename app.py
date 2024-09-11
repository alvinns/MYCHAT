import google.generativeai as genai
import streamlit as st

genai.configure(api_key="AIzaSyD_hS7CZeAj01uBur9IemKkcf1sSR8rOLY")

def generate_content(prompt):
    try:
        response = genai.generate_text(
            model="models/gemini-1.5-flash",
            prompt=prompt
        )
        return response.generations[0].text if response.generations else "No response generated."
    except Exception as e:
        return f"Error: {str(e)}"

prompt = st.chat_input("Enter your prompt")
if prompt:
    response = generate_content(prompt)
    st.write(response)
