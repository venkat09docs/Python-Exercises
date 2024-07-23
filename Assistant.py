from openai import OpenAI

client = OpenAI(
    api_key=""
)

# Step 1: Create an Assistant

assistant = client.beta.assistants.create(
  name="Math Tutor",
  instructions="You are a personal math tutor. Write and run code to answer math questions.",
  tools=[{"type": "code_interpreter"}],
  model="gpt-4o",
)

# print(assistant)

# Step 2: Create a Thread

thread = client.beta.threads.create()

# print(thread)

# Step 3: Add a Message to the Thread

message = client.beta.threads.messages.create(
  thread_id=thread.id,
  role="user",
  content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
)

# Step 4: Create a Run

run = client.beta.threads.runs.create_and_poll(
  thread_id=thread.id,
  assistant_id=assistant.id,
  instructions="Please address the user as RNS. The user has a premium account."
)

# print(run.status)

# if run.status == 'completed':
#   messages = client.beta.threads.messages.list(
#     thread_id=thread.id
#   )
#   print(messages)
# else:
#   print(run.status)

while True:
    run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
    if run.status == "completed":
        messages = client.beta.threads.messages.list(thread_id=thread.id)
        latest_message = messages.data[0]
        text = latest_message.content[0].text.value
        print(text)
        break;