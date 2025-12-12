from typing import List, Dict
from openai import OpenAI


class AIAssistant:
    """Wrapper around OpenAI Chat API."""

    def __init__(self, api_key: str, system_prompt: str = "You are a helpful assistant."):
        self._client = OpenAI(api_key=api_key)
        self._system_prompt = system_prompt
        self._history: List[Dict[str, str]] = [
            {"role": "system", "content": system_prompt}
        ]

    def set_system_prompt(self, prompt: str) -> None:
        self._system_prompt = prompt
        self.clear_history()

    def send_message(self, user_message: str, model: str = "gpt-4o-mini") -> str:
        self._history.append({"role": "user", "content": user_message})

        completion = self._client.chat.completions.create(
            model=model,
            messages=self._history,
        )

        reply = completion.choices[0].message.content
        self._history.append({"role": "assistant", "content": reply})
        return reply

    def clear_history(self) -> None:
        self._history = [{"role": "system", "content": self._system_prompt}]