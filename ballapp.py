import openai
import streamlit as st

st.title('Welcome to my first Streamlit app.')
st.header('This is a header')
temp=0.7

if model := st.selectbox(
    'GPT Model',
    ('gpt-3.5-turbo', 'code-davinci-002 (Legacy)', 'gpt-3.5-turbo-16k', 'gpt-3.5-turbo-0613', 'gpt-3.5-turbo-16k-0613', 'gpt-3.5-turbo-0301', 'text-davinci-003', 'text-davinci-002', 'babbage-002', 'davinci-002', 'text-davinci-003', 'text-davinci-002', 'davinci, curie', 'babbage', 'ada')):
    if temp:=st.slider('Temperature', 0.0, 1.0, 0.7):

        if api_key:=st.text_input("Enter API Key","qhOkd68l0oS7icaNaR8YT3BlbkFJUXbBLv8AqrX0a57T4ax6"):
            openai.api_key=api_key
            if system_prompt:=st.text_input("Enter  your system prompt:","YYou are a java developer."):
                if prompt:=st.text_area("Enter  your prompt:","""Use the Prowide-core, prowide-iso20022. 
                                        Use just these opensource dependencies from Maven.
                                        Write some Java methods to translate the Pacs.008 to MT103."""):
                    response = openai.ChatCompletion.create(
                        model=model,
                        messages=[
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": prompt},
                        ],temperature=temp
                    )
                    st.markdown(response['choices'][0]['message']['content'])

def process():
    return "Hello, World!!!"

if st.button(‘Process request.’):
    st.markdown(process())
