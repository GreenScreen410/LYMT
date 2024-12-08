import ollama


class OllamaChatManager:
    def __init__(self, prompt, **kwargs):
        self.client = ollama.Client(**kwargs)
        self.prompt = prompt

    def create(self, model: str, prompt_name: str, content: str, repeat: int = 0, **kwargs):
        """
        Get the response from the Ollama chat model.

        Args:
            model (str): The model name
            prompt_name (str): The name of the prompt file
            content (str): The content of the prompt
            repeat (int): The number of times to repeat the conversation
            **kwargs: Additional keyword arguments
        """

        if kwargs.get("stream"):
            raise ValueError("Streaming is not supported at this time. Please set 'stream' parameter to False.")

        prompt_content = self.prompt.get(prompt_name)
        messages = [
            {"role": "system", "content": prompt_content},
            {"role": "user", "content": content},
        ]

        if repeat <= 0:
            response = self.client.chat(model=model, messages=messages, **kwargs)
            return response["message"]["content"]

        else:
            thinking_chain = [f"<original_question>{content}</original_question>"]

            for i in range(repeat):
                response = self.client.chat(model=model, messages=messages, **kwargs)
                response_content = response["message"]["content"]

                messages.append(
                    {
                        "role": "user",
                        "content": f"<original_question>{content}</original_question>\n<requestion_{i+1}>{response_content}</requestion_{i+1}>",
                    }
                )
                thinking_chain.append(response_content)

            return thinking_chain[-1]
