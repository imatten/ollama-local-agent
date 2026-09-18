"""Interactive terminal chat session, built with LangChain."""
# pylint: disable=duplicate-code
# The REPL loop intentionally mirrors basic_chat/session.py for comparison.

from langchain_core.messages import AIMessage, HumanMessage
from langchain_ollama import ChatOllama


class ChatSession:
    """Keeps conversation history and drives the terminal REPL."""

    def __init__(self, model: ChatOllama):
        self.model = model
        self.history: list = []

    def send(self, user_input: str) -> str:
        """Send one user message, print the streamed reply, and record both."""
        self.history.append(HumanMessage(user_input))

        reply = ""
        for chunk in self.model.stream(self.history):
            print(chunk.content, end="", flush=True)
            reply += chunk.content
        print()

        self.history.append(AIMessage(reply))
        return reply

    def run(self):
        """Run the terminal chat loop until the user types exit/quit."""
        print(f"Chatting with {self.model.model} (via LangChain). Type 'exit' to quit.\n")
        while True:
            user_input = input("You: ")
            if user_input.strip().lower() in ("exit", "quit"):
                break
            print("AI: ", end="")
            self.send(user_input)
