from openai import OpenAI

# Initialize the OpenAI client with your API key
client = OpenAI(api_key="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")

# Make a simple API call
completion = client.chat.completions.create(
model="gpt-4o-mini",
messages=[
{"role": "system", "content": "You are a helpful assistant."},
{"role": "user", "content": "Hello! What is AI?"}
]
)

# Print the response
print(completion.choices[0].message.content)