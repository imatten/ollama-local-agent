"""LangChain's chat model wrapper for a local Ollama model."""

from langchain_ollama import ChatOllama


def build_model(model: str, base_url: str = "http://localhost:11434") -> ChatOllama:
    """Create a LangChain chat model backed by a local Ollama server."""
    return ChatOllama(model=model, base_url=base_url)
