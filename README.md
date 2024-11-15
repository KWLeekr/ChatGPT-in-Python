# ChatGPT-in-Python

Thank you for visiting my first project!

It’s a code that makes it easy to call OpenAI's REST API using Python.

By using the object in this code, you can:  
1. Easily send and receive messages with GPT.  
2. Maintain GPT’s chat memory.  
3. Effortlessly define and categorize multiple chats.  
4. Add a system prompt to the chat object.  
5. Set a length limitation for memory, making it easy to manage tokens.  

---------------------------------------

# How to use

Before using, enter API KEY in `your_api_key.py`
```your_api_key.py
my_api_key = "YOUR_API_KEY"
```

example code
```main.py
import chatgpt

# make a new chat object
chat = chatgpt.newChat("This is a system prompt")

# get user's message
user_input = input("Message : ")

# send message & print reply
chat.send(user_input)
```

if you like to set memory(data type : array) limitation to save your token,
you can follow the example below

```python
chat = chatgpt.newChat(system_prompt1, length=10)
```
default value of length is 50

---------------------------------------

Since this is my first project, I would love to receive plenty of feedback!

Sincerely, Gyungwook Lee
