"""Entry point: uv run chat.py"""

from basic_chat.client import OllamaClient
from basic_chat.session import ChatSession

MODEL = "llama3.2:3b"


def main():
    """Start an interactive chat session with the local Ollama model."""
    client = OllamaClient(model=MODEL)
    session = ChatSession(client)
    session.run()


if __name__ == "__main__":
    main()
