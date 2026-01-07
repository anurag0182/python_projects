from google import genai

client = genai.Client(
    api_key="AIzaSyBKbSgWGiYHbjFC7DFc-KMZvTZ7gH6BB7g"
)

chat = client.chats.create(
    model="gemini-3-flash-preview"
)

print("Gemini AI chatbot is ready (type 'bye' to exit):\n")

while True:
    user_input = input("Ashish: ").strip()

    if user_input.lower() == "bye":
        print("Anurag: Goodbye!")
        break

    try:
        response = chat.send_message(user_input)
        print("Anurag:", response.text)

    except Exception as err:
        print("Anurag: Error occurred →", err)

