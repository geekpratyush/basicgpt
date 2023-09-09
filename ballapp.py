import openai
import streamlit as st

st.title('Welcome to my first custom prompt processor. :flag-in:')
temp=0.7

model = st.selectbox(
    'GPT Model',
    ('gpt-3.5-turbo', 'davinci', 'code-davinci-002 (Legacy)', 'gpt-3.5-turbo-16k', 'gpt-3.5-turbo-0613', 'gpt-3.5-turbo-16k-0613', 'gpt-3.5-turbo-0301', 'text-davinci-003', 'text-davinci-002', 'babbage-002', 'davinci-002', 'text-davinci-003', 'text-davinci-002', 'davinci, curie', 'babbage', 'ada'))
temp=st.slider('Temperature', 0.0, 1.0, 0.7)
api_key=st.text_input("Enter API Key","qhOkd68l0oS7icaNaR8YT3BlbkFJUXbBLv8AqrX0a57T4ax6",type="password")
openai.api_key=api_key
system_prompt=st.text_input("Enter  your system prompt:","You are a java developer.")
prompt=st.text_area("Enter  your prompt:","""Use the Prowide-core, prowide-iso20022. 
Use just these opensource dependencies from Maven.
Write some Java methods to translate the Pacs.008 to MT103.""")

def process():
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],temperature=temp
    )
    st.markdown(response['choices'][0]['message']['content'])



if st.button('Process Prompt...👈'):
    st.markdown(process())
