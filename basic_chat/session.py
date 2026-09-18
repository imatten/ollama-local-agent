"""Interactive terminal chat session."""

from basic_chat.client import OllamaClient


class ChatSession:
    """Keeps conversation history and drives the terminal REPL."""

    def __init__(self, client: OllamaClient):
        self.client = client
        self.history: list[dict] = []

    def send(self, user_input: str) -> str:
        """Send one user message, print the streamed reply, and record both."""
        self.history.append({"role": "user", "content": user_input})

        reply = ""
        for piece in self.client.stream_chat(self.history):
            print(piece, end="", flush=True)
            reply += piece
        print()

        self.history.append({"role": "assistant", "content": reply})
        return reply

    def run(self):
        """Run the terminal chat loop until the user types exit/quit."""
        print(f"Chatting with {self.client.model}. Type 'exit' to quit.\n")
        while True:
            user_input = input("You: ")
            if user_input.strip().lower() in ("exit", "quit"):
                break
            print("AI: ", end="")
            self.send(user_input)
