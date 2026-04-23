import streamlit as st 
from backend_chatbot import build_chatbot
from langchain_core.messages import HumanMessage
import uuid

# ******************* utility functions *******************
def generate_thread_id():
    return str(uuid.uuid4())

def reset_thread():
    st.session_state['thread_id'] = generate_thread_id()
    add_thread(st.session_state['thread_id'])
    st.session_state['message_history'] = []

def add_thread(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)

def load_conversation(thread_id):
    # Placeholder for loading conversation logic
    # In a real implementation, this would fetch messages from a database or file based on thread_id
    state = chatbot.get_state(config={"configurable": {"thread_id": thread_id}})
    return state.values.get('messages', [])

# ******************* session state initialization *******************
if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = []

add_thread(st.session_state['thread_id'])

# ******************* Streamlit UI *******************
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

if st.sidebar.button("New Chat"):
    reset_thread()

st.sidebar.header("My Conversations")
for thread in st.session_state['chat_threads']:
    if st.sidebar.button(str(thread)):
        st.session_state['thread_id'] = thread
        messages = load_conversation(thread)
        temp_msgs = []
        for msg in messages:
            if isinstance(msg, HumanMessage):
                role = 'user'
            else:
                role = 'assistant'
            temp_msgs.append({'role': role, 'content': msg.content})
        st.session_state['message_history'] = temp_msgs


# message_history = []
CONFIG = {"configurable": {"thread_id": st.session_state['thread_id']}}


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