import requests

api_key = "ec289aae73864afd9ca30d22a390e8f5"
Title = input("Enter the title of the news article:")
url = f"https://newsapi.org/v2/everything?q={Title}&from=2026-05-19&sortBy=publishedAt&apiKey={api_key}"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(f"Total Results: {data['totalResults']}")

    for article in data['articles']:
        print(f"Title: {article['title']}")
        print(f"Description: {article['description']}")
        print(f"URL: {article['url']}")
        print("-" * 50)