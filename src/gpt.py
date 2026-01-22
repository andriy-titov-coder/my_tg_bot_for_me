"""
Module for interacting with OpenAI's GPT API.
"""
from openai import OpenAI
import httpx


class ChatGPTService:
    """
    Service for managing chat interactions with OpenAI's ChatGPT.
    """
    client: OpenAI = None
    message_list: list = None

    def __init__(self, token):
        """
        Initializes the ChatGPTService with an OpenAI API token and a proxy.
        """
        self.client = OpenAI(
            http_client=httpx.Client(proxy="http://18.199.183.77:49232"),
            api_key=token
        )
        self.message_list = []

    async def send_message_list(self) -> str:
        """
        Sends the current message list to OpenAI and returns the AI's response.
        """
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.message_list,
            max_tokens=3000,
            temperature=0.9
        )
        message = completion.choices[0].message
        self.message_list.append(message)
        return message.content

    def set_prompt(self, prompt_text: str) -> None:
        """
        Sets the system prompt for the conversation, clearing previous history.
        """
        self.message_list.clear()
        self.message_list.append({"role": "system", "content": prompt_text})

    async def add_message(self, message_text: str) -> str:
        """
        Adds a user message to the conversation and gets the AI response.
        """
        self.message_list.append({"role": "user", "content": message_text})
        return await self.send_message_list()

    async def send_question(self, prompt_text: str, message_text: str) -> str:
        """
        Sends a single question with a specific system prompt, clearing previous history.
        """
        self.message_list.clear()
        self.message_list.append({"role": "system", "content": prompt_text})
        self.message_list.append({"role": "user", "content": message_text})
        return await self.send_message_list()
