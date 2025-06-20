import streamlit as st
from agents import MyAgent

st.set_page_config(page_title="Flute AI Agent", page_icon="🎵")
st.title("🎵 Balaji Flute AI Assistant")
st.caption("Ask anything about flute scales, prices, or perform math!")

# Initialize agent
agent = MyAgent()

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input prompt
user_input = st.chat_input("Type your query (e.g. 'price of C scale', '2+2', or 'describe E scale')")

if user_input:
    # Display user message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get response from agent
    response = agent.handle(user_input)

    # Display agent response
    st.chat_message("assistant").markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
