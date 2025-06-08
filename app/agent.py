# app/agent.py

from langchain.agents import create_structured_chat_agent, AgentExecutor
from langchain.output_parsers.retry import RetryWithErrorOutputParser
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from langchain_core.runnables.history import RunnableWithMessageHistory

from app.config import AgentConfig
from app.session_manager import get_session
from app.tools import tools
from app.core.prompt import prompt  # ← import your prompt
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

        # Retry parser to handle minor LLM output formatting issues
        base_parser = StrOutputParser()
        output_parser = RetryWithErrorOutputParser.from_llm(
            llm=llm,
            parser=base_parser,
            max_retries=2
        )

        # Create structured agent using your custom prompt
        agent = create_structured_chat_agent(
            llm=llm,
            tools=tools,
            prompt=prompt
        )

        executor = AgentExecutor(
            agent=agent,
            tools=tools,
            verbose=True,
            max_iterations=config.max_iterations,
            handle_parsing_errors=True,
            return_intermediate_steps=True,
            output_parser=output_parser
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
