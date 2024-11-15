# ------------------------------------------------------------

# Import chatgpt.py
import chatgpt

# How to use
# Chat = chatgpt.newChat("System prompt")
# Chat.send("User input") -> Sends "User input" and outputs the response

# ------------------------------------------------------------

# Set the system prompt
system_prompt = "your name is Tom, you are a helpful assistant."

# Declare a new chat
chat = chatgpt.newChat(system_prompt)

# repeat
while True :
  # Receive user input
  user_input = input("Message: ")
  # Send a message to the chat and display the response
  chat.send(user_input)

# ------------------------------------------------------------
