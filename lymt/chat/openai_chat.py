from openai import OpenAI


class OpenAIChatManager:
    def __init__(self, api_key, prompt, **kwargs):
        self.client = OpenAI(api_key=api_key, **kwargs)
        self.prompt = prompt

    def create(self, model: str, prompt_name: str, content: str, repeat: int = 0, **kwargs):
        """
        Get the response from the OpenAI chat model.

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
            response = self.client.chat.completions.create(model=model, messages=messages, **kwargs)
            return "".join(choice.message.content for choice in response.choices)

        else:
            thinking_chain = [f"<original_question>{content}</original_question>"]

            for i in range(repeat):
                response = self.client.chat.completions.create(model=model, messages=messages, **kwargs)
                response_content = "".join(choice.message.content for choice in response.choices)

                messages.append(
                    {
                        "role": "user",
                        "content": f"<original_question>{content}</original_question>\n<requestion_{i+1}>{response_content}</requestion_{i+1}>",
                    }
                )
                thinking_chain.append(response_content)

            return thinking_chain[-1]
