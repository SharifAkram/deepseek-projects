import requests

# API endpoint for DeepSeek-R1 (replace with your local endpoint)
API_URL = "http://127.0.0.1:11434/v1/chat/completions"

# Request payload
payload = {
    "model": "deepseek-r1:14b",
    "messages": [
        {
            "role": "user",
            "content": "What is the largest city in Florida in terms of square miles?"
        }
    ],
    "stream": False
}

# Send the request to the API
response = requests.post(API_URL, json=payload)

print(response.status_code)
print(response.text)

# Handle the response
if response.status_code == 200:
    answer = response.json()["choices"][0]["message"]["content"]
    print("Answer:", answer)
else:
    print("Error:", response.text)