from core.llm_interface import Model, interact_with_llm, clear_memory
import os
import getpass

# Ensure API Key is set
if not os.environ.get("GROQ_API_KEY"):
    os.environ["GROQ_API_KEY"] = getpass.getpass("Enter API key for Groq[OnlineMode]: ")


# Initialize Model instance
model_instance = Model(onlineStat=True, model_name="llama3-70b-8192")

# Example: Direct interaction
while True:
    user_input = input("Enter a prompt: ")
    thread_id = "session_123"
    response_with_memory = interact_with_llm(user_input, thread_id)
    print("Response with Memory:", response_with_memory)

# Clear memory externally
clear_choice = input("Do you want to clear memory? (yes/no): ").strip().lower()
if clear_choice == "yes":
    clear_memory()
