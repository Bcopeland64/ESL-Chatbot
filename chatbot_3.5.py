import os
import openai
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key
api_key = os.getenv('OPENAI_API_KEY')

def generate_response(user_input, api_key):
    openai.api_key = api_key
    response = openai.Completion.create(
        model="gpt-3.5-turbo",  # Use the latest available model
        prompt=user_input,
        temperature=0.7,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def main():
    st.title("Chatbot Assistant")

    api_key = os.getenv('OPENAI_API_KEY')
    user_input = st.text_area("Your message:", height=150)

    if st.button("Send"):
        if user_input and api_key:
            try:
                response = generate_response(user_input, api_key)
                st.text_area("Response:", value=response, height=150, disabled=True)
            except openai.error.RateLimitError:
                st.error("Rate limit exceeded. Please try again later.")
        else:
            st.warning("Please enter a message and make sure your API key is set.")

if __name__ == "__main__":
    main()
