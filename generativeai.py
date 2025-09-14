import google.generativeai as genai
genai.configure(api_key= "AIzaSyBe-V036YcjgiBEwzr1HiKvgqEy4aVRGrs")
model = genai.GenerativeModel("models/gemini-1.5-flash")

chat = model.start_chat()

print("Gemini AI chatbot is ready (type'Bye' to exit):\n")

while True:
    user_input = input("Ashish: ")

    if user_input.lower() == 'bye':
        print("Anurag: Goodbye!")
        break
    elif user_input.lower() == 'who created you':
        print("Anurag: Anurag Master!")
    else:
        print("Anurag: I don't understand that.")

    
    try:
        response = chat.send_message(user_input)
        print("Anurag:", response.text.strip())
    except Exception as err:
        print("Anurag: Error 2201",err)