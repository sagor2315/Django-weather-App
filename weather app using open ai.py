import os
import openai


openai.api_key = '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'

def command_prompt(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    output = response.get('choices')[0].get('text').strip()
    return output

write = command_prompt('write anything in just 20 words')
print(write)