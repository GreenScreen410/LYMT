import os


class PromptManager:
    def __init__(self):
        self.prompt_dir = os.path.join(os.path.dirname(__file__), "prompt/templates")

    def list(self):
        """
        List all prompt files in the 'templates' directory.

        Returns:
            list: A list of prompt filenames
        """

        return [f for f in os.listdir(self.prompt_dir) if os.path.isfile(os.path.join(self.prompt_dir, f))]

    def get(self, prompt_name: str):
        """
        Get the content of the prompt file.

        Args:
            prompt_name (str): The name of the prompt file. It should be the filename.

        Returns:
            str: The content of the prompt file
        """

        prompt_path = os.path.join(self.prompt_dir, prompt_name)

        if not os.path.isfile(prompt_path):
            raise FileNotFoundError(f"Prompt file '{prompt_name}' not found in 'prompt' directory.")

        with open(prompt_path, "r", encoding="utf-8") as file:
            return file.read()
