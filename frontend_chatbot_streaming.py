import streamlit as st 
from backend_chatbot import build_chatbot
from langchain_core.messages import HumanMessage

st.set_page_config(page_title="Dynamic Chatbot")

# st.title("🤖 Chatbot with Custom API Key")
st.markdown("<h4>🤖 Chatbot with Custom API Key</h4>", unsafe_allow_html=True)


# 🔑 Sidebar inputs
st.sidebar.header("Configuration")
api_key = st.sidebar.text_input("Enter OpenAI API Key", type="password")
model = st.sidebar.selectbox(
    "Select Model",
    ["gpt-4o-mini", "gpt-4o", "gpt-3.5-turbo"]
)

# Build chatbot only when key is provided
if api_key:
    chatbot = build_chatbot(api_key, model)
else:
    st.warning("Please enter API key to start")
    st.stop()

# message_history = []
CONFIG = {"configurable": {"thread_id": "thread-1"}}

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

# loading old messages
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

# older message format to be stored in session state
# {'role': 'user', 'content': 'What is the capital of France?'}
# {'role': 'assistant', 'content': 'The capital of France is Paris.'}

user_input = st.chat_input("Type your message here...")

if user_input:

    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message("user"):
        st.text(user_input)

    # Simulate assistant response (replace with actual chatbot logic)
    # assistant_response = chatbot.invoke({'messages': [HumanMessage(content=user_input)]}, config = CONFIG)
    # ai_response = assistant_response['messages'][-1].content


    # st.session_state['message_history'].append({'role': 'assistant', 'content': ai_response})
    with st.chat_message("assistant"):
        ai_message = st.write_stream(
            message_chunk.content for message_chunk, metadata in chatbot.stream(
                {'messages': [HumanMessage(content=user_input)]},
                config = CONFIG,
                stream_mode = 'messages'
            )
        )
    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})