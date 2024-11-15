import openai
import your_api_key

openai.api_key = your_api_key.your_api_key
client = openai.OpenAI(api_key=your_api_key.your_api_key)

# ------------------------------------------------------------

# New chat object
class newChat:
    def __init__(self, prompt, length=50):
        self.system_prompt = prompt
        self.length = length
        self.chat = []

    def send(self, user_input):

        # Add user_input to the communication log
        user_message = {"role": "user", "content": user_input}
        system_prom = {"role": "system", "content": self.system_prompt}
        self.chat.append(system_prom)
        self.chat.append(user_message)

        # Send the communication log
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=self.chat
        )

        # Save the response in the log
        assistant_message = response.choices[0].message.content
        self.chat.append({"role": "assistant", "content": assistant_message})

        # Limit the chat log length (to save tokens)
        if len(self.chat) > self.length:
            self.chat.pop(0)

        # Print the response
        print(assistant_message)

# ------------------------------------------------------------
