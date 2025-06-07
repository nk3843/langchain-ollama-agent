from langchain_core.messages import BaseMessage

_session_store = {}

class SimpleMessageHistory:
    def __init__(self, session_id: str):
        self.session_id = session_id
        if session_id not in _session_store:
            _session_store[session_id] = []

    @property
    def messages(self) -> list[BaseMessage]:
        return _session_store[self.session_id]

    def add_message(self, message: BaseMessage):
        _session_store[self.session_id].append(message)

    def add_messages(self, messages: list[BaseMessage]):  # ✅ This fixes the error
        _session_store[self.session_id].extend(messages)

def get_session(session_id: str) -> SimpleMessageHistory:
    return SimpleMessageHistory(session_id)
