import streamlit as st 
from backend_chatbot import chatbot
from langchain_core.messages import HumanMessage
# st.title("Chatbot Interface")

# message_history = []
CONFIG = {"configurable": {"thread_id": "thread-1"}}

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

# loading old messages
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

# {'role': 'user', 'content': 'What is the capital of France?'}
# {'role': 'assistant', 'content': 'The capital of France is Paris.'}

user_input = st.chat_input("Type your message here...")

if user_input:

    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message("user"):
        st.text(user_input)

    # Simulate assistant response (replace with actual chatbot logic)
    assistant_response = chatbot.invoke({'messages': [HumanMessage(content=user_input)]}, config = CONFIG)
    ai_response = assistant_response['messages'][-1].content

    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_response})
    with st.chat_message("assistant"):
        st.text(ai_response)