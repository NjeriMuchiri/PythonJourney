import openai
openai.my_api_key = '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'

messages = [{"role": "system", "content": "You are a intelligent assistant"}]

while True:
    query = input("User: ")
    if query:
        messages.append(
            {"role": "user", "content": query},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})