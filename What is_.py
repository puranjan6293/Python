import requests
import json

question = input("question\n")
question_url = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{question}")
question_ans = question_url.json()
# print(question_ans)
organised_ans = str(question_ans[0]['meanings'][0]['definitions'][0]['definition'])
print(organised_ans)