from openai import OpenAI
import tiktoken

client = OpenAI(
    api_key="sk-proj-PMHh4g6ufP5nPLpjFZyCZeuQ"
)


def generate_text_with_openai(model, system_promt, user_prompt):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system", "content": system_promt
            },
            {
                "role": "user", "content": user_prompt
            }
        ],
        temperature=0.7,
        max_tokens=128,
        top_p=0
    )
    return response.choices[0].message.content


def count_token(prompt, model):
    encoding = tiktoken.encoding_for_model(model)
    num_tokens = encoding.encode(prompt)
    return len(num_tokens)
