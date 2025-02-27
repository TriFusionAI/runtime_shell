import getpass
import os
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph

# Memory Saver for conversation history
memory = MemorySaver()

class Model:
    def __init__(self, onlineStat, model_name):
        self.online = onlineStat
        self.model_name = model_name
        self.model = None

        if self.online:
            try:
                self.model = init_chat_model(model_name, model_provider="groq")
            except Exception as e:
                print(f"An API Related Error Occurred: {e}")

    def llmInterface(self, prompt):
        if self.online and self.model:
            response = self.model.invoke([HumanMessage(content=prompt)])
            return response.content
        return "Offline Mode: No response generated."


workflow = StateGraph(state_schema=MessagesState)

def call_model(state: MessagesState):
    messages = state["messages"]
    last_prompt = messages[-1].content

    model_instance = Model(onlineStat=True, model_name="llama3-70b-8192")
    response = model_instance.llmInterface(last_prompt)

    return {"messages": messages + [HumanMessage(content=response)]}

# Define the workflow
workflow.add_node("model", call_model)
workflow.add_edge(START, "model")

app = workflow.compile(checkpointer=memory)


def interact_with_llm(user_input, thread_id="default_thread"):
    input_messages = [HumanMessage(user_input)]
    config = {"configurable": {"thread_id": thread_id}}

    output = app.invoke({"messages": input_messages}, config)
    return output["messages"][-1].content

def clear_memory():
    global memory
    memory = MemorySaver()
    print("Memory has been cleared.")