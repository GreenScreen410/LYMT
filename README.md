# LYMT: Let Your Model Think

Maximize the model's thinking process.

> This project was inspired by the [Thinking-Claude](https://github.com/richards199999/Thinking-Claude) project by richards199999 to **maximize the thought process of various LLM models.** Also he's developing Chrome Extension. If you're interested, please visit that repository. **Thank you for the good prompt.**
<!-- -->
> **A super quick reminder:** This project is NOT aimed for benchmarks or huge leaps in math or something, since those are pre-determined by the base model. I only want to explore how further we could reach with LLM's "deep mindset". That said, when using it in your daily tasks, you will find LLM's inner monolog (thinking process) very very fun and interesting. - *A slight modification of the introduction to richards199999's Thinking-Claude project.*

## Benefits

**This is an EXPERIMENTAL project!** I DO NOT recommend using it for real service. Please use it for research purposes.

- 🐛 Minimize hallucinations and errors
- 🌟 Maximize your model's thought process
- 🧪 Can solve complex problems (sometimes)
- 🤝 Slightly modified from the code you were using
- 💪 Lightweight models also allow for deep thought processes

## How is this working?

When I looked at the thinking process of the o1 model, I thought, 'Why don't I try implementing this myself?' According to the official presentation data of o1, I saw that the thinking process involves re-entering the previously answered questions and answers, and **I defined this as a 're-question' process.**

I've implemented this myself, and through this process, **I was wondering how small models think about complex problems, and also if small models can have good performance if they go through this process.**  

First, store answers in a place called thinking_chain to save thinking process, and use the message object to continuously store and communicate responses and answers. Finally, return the last element of thinking_chain to get the final response.

## Benchmarks

| Model | Repeat | Question | Response | Is it correct? |
|---|---|---|---|---|
| Llama3.2-1B | 0 | 3.90 - 3.11 = x, solve for x | 3.90 - 3.11 = -0.21 | ❌ |
| Llama3.2-1B | 5 | 3.90 - 3.11 = x, solve for x | The final answer is: $\boxed{0.79}$ | ⭕ |
| Llama3.2-1B | 3 | 384724 + 129375 | Therefore, the correct answer is **13,322,334.** | ❌ |
| Llama-3.1-405B-Instruct | 10 | 384724 + 129375 | 384724 + 129375 = 514099 | ⭕ |
| Llama-3.1-405B-Instruct | 0 | 384724 + 129375 | The answer is 514089. | ❌ |

## Supporting Models

- OpenAI
- Ollama
- Anthropic
- Anything that uses `base_url` in the `openai` library (like [glhf.chat](https://glhf.chat/users/settings/api))

## Install

`pip install lymt`  

## Examples

### OpenAI models (or base_url models)

```python
from lymt.models.openai_model import OpenAIModel

lymt = OpenAIModel(api_key="api_key")

response = lymt.chat.create(
    model="gpt-4o-mini-2024-07-18",
    prompt_name="o1-heavy.txt", # Check print(lymt.prompt.list())
    content="3.90 - 3.11 = x, solve for x",
    repeat=10, # Adjust how much thinking process the model will have.
)

print(response)
```

### Ollama models

```python
from lymt.models.ollama_model import OllamaModel

lymt = OllamaModel()

response = lymt.chat.create(
    model="llama3.2:1b",
    prompt_name="o1-heavy.txt", # Check print(lymt.prompt.list())
    content="3.90 - 3.11 = x, solve for x",
    repeat=5, # Adjust how much thinking process the model will have.
)

print(response)
```

## Contributing

Contributions are welcome! Feel free to:

- Submit bug reports
- Propose new features
- Create pull requests

## License

MIT License - feel free to use and modify as needed.

## Acknowledgments

Special thanks to @richards199999
