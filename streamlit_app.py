
import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets['GOOGLE_API_KEY'])
model = genai.GenerativeModel('gemini-1.5-flash-latest')

prompt = st.text_area('Enter your prompt')
if st.button('Generate'):
    response = model.generate_content(prompt)
    st.write(response.text)
