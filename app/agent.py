from langchain.agents import create_structured_chat_agent, AgentExecutor
from langchain_ollama import ChatOllama
from langchain_core.runnables.history import RunnableWithMessageHistory

from app.config import AgentConfig
from app.session_manager import get_session
from app.tools import tools
from app.core.prompt import prompt
from app.core.logger import logger

def create_agent():
    try:
        config = AgentConfig()
        llm = ChatOllama(
            model=config.model_name,
            temperature=config.temperature,
            base_url=config.host,
            timeout=config.timeout
        )

        agent = create_structured_chat_agent(llm, tools, prompt)

        executor = AgentExecutor(
            agent=agent,
            tools=tools,
            verbose=True,
            max_iterations=config.max_iterations,
            handle_parsing_errors=True,
            return_intermediate_steps=True
        )

        return RunnableWithMessageHistory(
            executor,
            get_session,
            input_messages_key="input",
            history_messages_key="chat_history"
        )
    except Exception as e:
        logger.error(f"Error creating agent: {str(e)}")
        raise