from openai import OpenAI

# Initialize client
client = OpenAI(api_key="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")

# Initialize conversation history
messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

print("ChatGPT Console Chat (type 'quit' to exit)")
print("-" * 50)

while True:
    # Get user input
    user_input = input("You: ")

    # Exit condition
    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    # Add user message to history
    messages.append({"role": "user", "content": user_input})

    # Get AI response
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    # Extract response
    assistant_message = completion.choices[0].message.content

    # Add assistant response to history
    messages.append({"role": "assistant", "content": assistant_message})

    # Display response
    print(f"AI: {assistant_message}\n")