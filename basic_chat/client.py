"""Thin wrapper around Ollama's HTTP chat API."""

import json
import requests


class OllamaClient:
    """Talks to a local Ollama server's /api/chat endpoint."""

    def __init__(self, model: str, base_url: str = "http://localhost:11434"):
        self.model = model
        self.chat_url = f"{base_url}/api/chat"

    def stream_chat(self, messages: list[dict]):
        """Yield reply text chunks as they arrive from the model."""
        response = requests.post(
            self.chat_url,
            json={"model": self.model, "messages": messages, "stream": True},
            stream=True,
            timeout=300,
        )
        response.raise_for_status()

        for line in response.iter_lines():
            if not line:
                continue
            chunk = json.loads(line)
            yield chunk.get("message", {}).get("content", "")
            if chunk.get("done"):
                return
