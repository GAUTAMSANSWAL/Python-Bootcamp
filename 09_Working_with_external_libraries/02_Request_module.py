import requests

r = requests.get('https://api.github.com/events')

print(r.status_code)

with open('learning_api.txt', 'w') as file:
    file.write(r.text)