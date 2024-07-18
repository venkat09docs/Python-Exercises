from openai import OpenAI

client = OpenAI(
    api_key="sk-proj-PMHh4g6ufnQe0nPLpjFZyCZeuQ"
)


def llm_generate_text(service, model, system_prompt, user_prompt):
    if service == "OpenAI":
        generate_text = generate_text_with_openai(model, system_prompt, user_prompt)
    else:
        pass
    return generate_text


def generate_text_with_openai(model, system_prompt, user_prompt):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7,
        max_tokens=4092,
        top_p=0
    )
    return response.choices[0].message.content
