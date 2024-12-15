OPENAI_API_KEY = "Your OpenAI API key"

ANTHROPIC_API_KEY = "Your Anthropic API key"

DASHSCOPE_API_KEY = "Your Dashscope API key"

gpt_batch_request_template = {
    "custom_id": "request-1", 
    "method": "POST", 
    "url": "/v1/chat/completions",
    "body": {"model": "",
            "messages": [
                {"role": "system", "content": ""}, 
                {"role": "user", "content": ""}],
            "max_tokens": 16384}
    }


claude_batch_request_template = {
    "custom_id": "request-1",
    "params": {
        "model": "claude-3-5-sonnet-20241022",
        "max_tokens": 8192,
        "messages": [
                    {
                        "role": "user",
                        "content": "Hey Claude, tell me a short fun fact about video games!",
                    }
                ],
            },
        }

qwen_batch_request_template = {
    "custom_id": "request-1", "method": "POST", "url": "/v1/chat/completions", "body": 
            {"model": "qwen-turbo", "messages": [
                {"role": "system", "content": "You are a helpful assistant."}, 
                {"role": "user", "content": "What is 2+2?"}]
                }
        }
    

import json

def read_jsonl(file: str) -> list[dict[any,any]]:

    with open(file, 'r') as file:
        results = [json.loads(line.strip()) for line in file]

    return results

def extract_result(completion_text):
    start = completion_text.rfind('{')
    end = completion_text.rfind('}')
    if start != -1 and end != -1 and start < end:
        content = completion_text[start + 1:end]
        if "'Result'" in content or '"Result"' in content:
            value_start = content.find(':') + 1
            value = content[value_start:].strip().strip("'\" ")
            return value
    return None

