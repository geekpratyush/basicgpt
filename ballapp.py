import openai
import streamlit as st

st.title('Welcome to my first Streamlit app.')
st.header('This is a header')

openai.api_key='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'

if system_prompt:=st.text_input("Enter  your system prompt:","You are a helpful assistant."):
    if prompt:=st.text_area("Enter  your prompt:",""):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
            ]
        )
        st.markdown(response['choices'][0]['message']['content'])
