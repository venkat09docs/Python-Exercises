import helper
import llm
import prompts

service_name = "OpenAI"
model_name = "gpt-3.5-turbo"
# system_prompt = "give me only youtube questions related answers"
# user_prompt = "Generate 5 Youtube video titles for the following content [AWS engineer]"

# -----------------------------------------------------------------------------------------
# LinkedIn Post Generation
# -----------------------------------------------------------------------------------------

system_prompt = prompts.system_prompt_media.format(media="linkedin")
user_prompt = prompts.linkedin_post_generator_prompt.format(topic="Prompt Engineering Tips")

output = llm.llm_generate_text(service_name, model_name, system_prompt, user_prompt)
# output = llm.generate_text_with_openai("gpt-3.5-turbo", system_prompt, user_prompt)

print(output)

# -----------------------------------------------------------------------------------------
# Blog Summary Generation
# -----------------------------------------------------------------------------------------

system_prompt = prompts.system_prompt_media.format(media="blog")
user_prompt = prompts.blog_bullet_summary_prompt.format(MaxPoints="10", MinPoints="5", InputText=output)


output = llm.llm_generate_text(service_name, model_name, system_prompt, user_prompt)
# output = llm.generate_text_with_openai("gpt-3.5-turbo", system_prompt, user_prompt)

print(output)

input_tokens_count = helper.count_token(system_prompt + user_prompt, model_name)
output_tokens_count = helper.count_token(output, model_name)

print(f"Total Input Tokens {input_tokens_count}")
print(f"Total Output Tokens {output_tokens_count}")

estimated_cost = helper.estimate_input_tokens_cost(model_name, input_tokens_count)

print(f"Total estimated cost for Input Tokens - {estimated_cost}")

helper.retrive_openai_llm_models()
