import streamlit as st
from app.agent import create_agent

agent = create_agent()

st.title("LangChain Ollama Conversational Agent")
if st.button("🛑 Reset Conversation"):
    st.session_state.chat_history = []
    st.session_state.last_steps = []
    st.experimental_rerun()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Say something...")

if user_input:
    # Save user message
    st.session_state.chat_history.append({"type": "human", "content": user_input})

    # Run agent with message
    response = agent.invoke(
        {"input": user_input},
        config={"configurable": {"session_id": "default"}}
    )

    final_answer = response.get("output", "")
    steps = response.get("intermediate_steps", [])

    # Save AI message
    st.session_state.chat_history.append({"type": "ai", "content": final_answer})

    # Store trace in session for sidebar display (optional: keep full trace history)
    st.session_state.last_steps = steps

# Display full chat
for msg in st.session_state.chat_history:
    st.chat_message(msg["type"]).write(msg["content"])

# Show reasoning trace in the sidebar
with st.sidebar:
    st.subheader("🧠 Agent Trace")

    if "last_steps" in st.session_state and st.session_state.last_steps:
        for i, (action, observation) in enumerate(st.session_state.last_steps):
            st.markdown(f"**Step {i+1}**")
            st.markdown(f"- **Thought**: {action.log.strip()}")
            st.markdown(f"- **Action**: `{action.tool}`")
            st.markdown(f"- **Input**: `{action.tool_input}`")
            st.markdown(f"- **Observation**: {observation}")
            st.markdown("---")
    else:
        st.info("Run a query to view agent reasoning.")
