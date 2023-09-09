import openai
import streamlit as st

st.title('Welcome to my first Streamlit app.')
st.header('This is a header')
temp=0.7

if temp:=st.slider('Temperature', 0.0, 1.0, 0.7):

    if api_key:=st.text_input("Enter API Key","st-"):
        openai.api_key=api_key
        if system_prompt:=st.text_input("Enter  your system prompt:","You are a helpful assistant."):
            if prompt:=st.text_area("Enter  your prompt:",""):
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": prompt},
                    ],temperature=temp
                )
                st.markdown(response['choices'][0]['message']['content'])
