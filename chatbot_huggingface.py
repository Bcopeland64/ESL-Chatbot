import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

@st.cache(allow_output_mutation=True)
def load_model():
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    tokenizer.pad_token = tokenizer.eos_token
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    return tokenizer, model

tokenizer, model = load_model()

def generate_response(user_input, temperature):
    encoded_input = tokenizer.encode_plus(
        user_input, 
        return_tensors='pt', 
        max_length=512, 
        truncation=True, 
        padding=True
    )
    input_ids = encoded_input['input_ids']
    attention_mask = encoded_input['attention_mask']

    with torch.no_grad():
        output = model.generate(
            input_ids, 
            attention_mask=attention_mask, 
            max_new_tokens=50,
            num_return_sequences=1,
            temperature=temperature  # Set the temperature parameter
        )
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

def main():
    st.title("GPT-2 Chatbot")
    user_input = st.text_input("You: ", "")
    temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7, step=0.05)

    if user_input:
        response = generate_response(user_input, temperature)
        st.text_area("GPT-2:", value=response, height=100, disabled=True)

if __name__ == "__main__":
    main()
