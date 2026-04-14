import os
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.runnables import RunnableConfig
from dotenv import load_dotenv
load_dotenv()

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

llm = ChatOpenAI(model='gpt-4o-mini',temperature=0, api_key=os.getenv('OPENAI_API_KEY'))

def chat_node(state: ChatState) -> ChatState:
    msg = state['messages']
    response = llm.invoke(state['messages'])
    return {'messages': [response]}

memory = InMemorySaver()
builder = StateGraph(ChatState)
builder.add_node('chat_node', chat_node)

builder.add_edge(START, 'chat_node')
builder.add_edge('chat_node', END)

chatbot = builder.compile(checkpointer = memory)


# initial_state = {
#     'messages': [HumanMessage(content='What is the capital of india')]
# }

# config: RunnableConfig = {"configurable": {"thread_id": "1"}}

# res = chatbot.invoke(initial_state, config=config)['messages'][-1].content
# print(res)