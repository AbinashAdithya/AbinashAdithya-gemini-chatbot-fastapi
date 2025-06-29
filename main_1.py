import google.generativeai as genai
import os

# Set your Gemini API key here
genai.configure(api_key="AIzaSyAAP0lrg1QFSMsYCE6TQPaW6t0maX-2-Oc")

# Create a model instance
model = genai.GenerativeModel("gemini-2.5-flash")  # or "gemini-2.5-pro"

# Start a chat session
chat = model.start_chat()

# Chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    response = chat.send_message(user_input)
    print("Tara:", response.text)
