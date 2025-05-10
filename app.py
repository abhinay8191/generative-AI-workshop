import streamlit as st
from langchain_groq import ChatGroq
apikey="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"

st.title("chat with Groq")
st.write("This is a simple app to chat with Groq using the langchain library,")

llm = ChatGroq(
    model="llama-3.1-8b-instant", api_key=apikey
)


user = st.chat_input("what do you want to ask")

if user:
    with st.spinner("Thinking..."):
        response = llm.invoke(user)
        st.write(response.content)