import requests
import os

api_key = os.getenv("news_api_email_API_KEY")
url = f"https://newsapi.org/v2/everything?q=tesla&from=2024-07-20&sortBy=publishedAt&apiKey={api_key}"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content['articles']:
    print(article["title"])
    print(article["description"])
