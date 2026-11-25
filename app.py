
import streamlit as st
import ollama

# Page settings
st.set_page_config(
    page_title="Local AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.stApp {
    background-color: #101114;
    color: white;
}

[data-testid="stSidebar"] {
    background-color: #191a20;
}

.stChatMessage {
    border-radius: 12px;
}

h1 {
    color: #ffffff;
}

</style>
""", unsafe_allow_html=True)

# Title
st.title("🤖 Local AI Assistant")
st.caption("Powered by Python | Ollama | Llama 3.2")

# Sidebar
with st.sidebar:
    st.title("⚡ Local AI")
    st.write("Your personal AI chatbot")

    st.divider()

    st.write("**Model:** Llama 3.2")
    st.write("**Status:** Running locally")

    if st.button("🗑️ Clear Conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.divider()
    st.caption("Built with Python and Ollama")

# Initialize messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display conversation
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
prompt = st.chat_input("Message your AI assistant...")

if prompt:

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("AI is thinking..."):

            try:
                response = ollama.chat(
                    model="llama3.2",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a helpful AI assistant. "
                            "Give clear, accurate and friendly answers."
                        },
                        *st.session_state.messages
                    ]
                )

                answer = response.message.content

                st.markdown(answer)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })

            except Exception as error:
                st.error("Unable to connect to Ollama.")
                st.write(error)
