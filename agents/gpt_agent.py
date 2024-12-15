from utils import OPENAI_API_KEY
from openai import OpenAI

def create_message(
        messages: list[dict[str, str]],
        role: str,
        content: str,) -> list[dict[str, str]]:
    messages.append({"role": role, "content": content})
    return messages


def get_completion(
        messages: list[dict[str, str]],
        model: str = "gpt-4o",
        max_tokens: int = 10240,
        temperature: float = 0.0,
        stop: list[str] | None = None,
        seed: int = 42,
        tools: list | None = None,
        logprobs: bool = True, # whether to return log probabilities of the output tokens or not.
        # If true, returns the log probabilities of each output token returned in the content of message.
        top_logprobs: list[dict[str, float]] | None = None,
        verbose: bool = True
) -> tuple[str, list[float]]:
    params = {
        "model": model,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "stop": stop,
        "seed": seed,
        "logprobs": logprobs,
        "top_logprobs": top_logprobs,
    }
    if tools:
        params["tools"] = tools

    try:
        client = OpenAI(
            api_key=OPENAI_API_KEY,
        )
        completion = client.chat.completions.create(**params)
        logprobs = [token.logprob for token in completion.choices[0].logprobs.content]
        return completion.choices[0].message.content, logprobs
    except Exception as e:
        if verbose:
            print(e)

