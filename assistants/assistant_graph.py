from openai import OpenAI

client = OpenAI(
    api_key=""
)

# Upload a file with an "assistants" purpose
file = client.files.create(
    file=open("users_data.csv", "rb"),
    purpose='assistants'
)

# Step 1: Create an Assistant

assistant = client.beta.assistants.create(
    name="Data Visualizer",
    instructions="You are a great at creating beautiful data visualizations. You analyze the data in .csv files, understand the data and share a brief summary of the trends.",
    tools=[{"type": "code_interpreter"}],
    model="gpt-3.5-turbo",
    tool_resources={
        "code_interpreter": {
            "file_ids": [file.id]
        }
    }
)

thread = client.beta.threads.create(
  messages=[
    {
      "role": "user",
      "content": "Create 3 Data Visualizations based on the trend from this file",
      "attachments": [
        {
          "file_id": file.id,
          "tools": [{"type": "code_interpreter"}]
        }
      ]
    }
  ]
)

run = client.beta.threads.runs.create_and_poll(
  thread_id=thread.id,
  assistant_id=assistant.id,
  instructions="Please address the user as RNS. The user has a premium account."
)

print(run.status)

output_file="users_graph.png"
while True:
    run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
    if run.status == "completed":
        messages = client.beta.threads.messages.list(thread_id=thread.id)
        print(messages)
        latest_message = messages.data[0]
        file_id = latest_message.content[0].image_file.file_id
        file_name = client.files.with_raw_response.retrieve_content(file_id)
        with open(output_file, "wb") as file:
            file.write(file_name.content)
        break
