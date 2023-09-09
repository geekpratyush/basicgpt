import openai
import streamlit as st

st.title('Welcome to my first Streamlit app.')
st.header('This is a header')
temp=0.7

if model := st.selectbox(
    'GPT Model',
    ('gpt-3.5-turbo', 'code-davinci-002', 'gpt-3.5-turbo-16k', 'gpt-3.5-turbo-0613', 'gpt-3.5-turbo-16k-0613', 'gpt-3.5-turbo-0301', 'text-davinci-003', 'text-davinci-002', 'babbage-002', 'davinci-002', 'text-davinci-003', 'text-davinci-002', 'davinci, curie', 'babbage', 'ada')):
    if temp:=st.slider('Temperature', 0.0, 1.0, 0.7):

        if api_key:=st.text_input("Enter API Key","qhOkd68l0oS7icaNaR8YT3BlbkFJUXbBLv8AqrX0a57T4ax6"):
            openai.api_key=api_key
            if system_prompt:=st.text_input("Enter  your system prompt:","You are a helpful assistant."):
                if prompt:=st.text_area("Enter  your prompt:",""):
                    response = openai.ChatCompletion.create(
                        model=model,
                        messages=[
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": prompt},
                        ],temperature=temp
                    )
                    st.markdown(response['choices'][0]['message']['content'])
