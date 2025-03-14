# Send a message list to the model and await the response.
from autogen_core.models import UserMessage

# Send a message list to the model and await the response.
messages = [
    UserMessage(content="What is the capital of France?", source="user"),
]
response = await model_client.create(messages=messages)

# Print the response
print(response.content)

# Print the response
print(response.content)

