from dotenv import load_dotenv
import gradio as gd
from langchain_openai import ChatOpenAI
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory


#load api_key
load_dotenv()
#AI obj
model=ChatOpenAI()

#store
store={}
#creat session
def get_session_history(session_id):

    if session_id not in store:
        store[session_id]=InMemoryChatMessageHistory()

    return store[session_id]



chain=RunnableWithMessageHistory(
    model,get_session_history
)


#create chat function
def chat(message,history): 
    responce=chain.invoke(
        message,
        config={"configurable":{"session_id":"user1"}}
    )

    return responce.content


demo=gd.ChatInterface(
    fn=chat,
    title="Memory Chatboat"
)

demo.launch()