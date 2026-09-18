"""Entry point: uv run langchain_chat.py"""

from langchain_chat.client import build_model
from langchain_chat.session import ChatSession

MODEL = "llama3.2:3b"


def main():
    """Start an interactive LangChain-powered chat session."""
    model = build_model(MODEL)
    session = ChatSession(model)
    session.run()


if __name__ == "__main__":
    main()
