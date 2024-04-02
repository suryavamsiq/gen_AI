from langchain.llms import GooglePalm
api_key='AIzaSyA-3_o22Y-anWlUzWRfHYBuhmVFO-OUvy8'
llm=GooglePalm(google_api_key=api_key,temperature=0.7)

import streamlit as st
st.set_page_config(page_title="Conversational Q&A Chatbot")
st.header("Hey, Let's type your question")


input=st.text_input("Input: ",key="input")
response=llm(input)

submit=st.button("submit to get your answer")

## If ask button is clicked

if submit:
    st.subheader("The Response is")
    st.write(response)
