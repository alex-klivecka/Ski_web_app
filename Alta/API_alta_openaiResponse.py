import json


with open('data.json', 'r') as json_file:
    openai_response = json.load(json_file)

print(openai_response.choices)