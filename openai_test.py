import helper


system_prompt = "give me only youtube questions related answers"
user_prompt = "Generate 5 Youtube video titles for the following content [AWS engineer]"

output = helper.generate_text_with_openai("gpt-3.5-turbo", system_prompt, user_prompt)

print(output)

input_count = helper.count_token(system_prompt + user_prompt, "gpt-3.5-turbo")
output_tokens_count = helper.count_token(output, "gpt-3.5-turbo")

print(f"Total Input Tokens {input_count}")
print(f"Total Output Tokens {output_tokens_count}")
