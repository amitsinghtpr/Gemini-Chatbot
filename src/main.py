import streamlit as st
from langchain.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI

# Initialize memory
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory()

# Initialize Gemini (Google Generative AI) LLM
llm = ChatGoogleGenerativeAI(model="gemini-pro")  # Make sure your API key is set in your environment

def main():
    st.title("Gemini Chatbot with Memory")
    st.write("Welcome to the Chatbot! Type your message below:")

    user_input = st.text_input("You:", key="input")

    if user_input:
        # Add user message to memory
        st.session_state.memory.save_context({"input": user_input}, {})
        # Get conversation history
        history = st.session_state.memory.load_memory_variables({})["history"]
        # Generate response
        response = llm.invoke(history + "\nHuman: " + user_input + "\nAI:")
        # Add AI response to memory
        st.session_state.memory.save_context({}, {"output": response})
        st.write("Bot:", response)

if __name__ == "__main__":
    main()