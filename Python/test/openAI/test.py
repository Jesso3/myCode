import os
import openai
openai.api_key = os.getenv("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")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Tell the world about the ChatGPT API in the style of a pirate."}
  ]
)

print(completion.choices[0].message.content)