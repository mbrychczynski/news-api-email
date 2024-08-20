import requests
import os
from send_email import send_email

api_key = os.getenv("news_api_email_API_KEY")
url = f"https://newsapi.org/v2/everything?q=tesla&from=2024-07-20&sortBy=publishedAt&apiKey={api_key}"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
message = ""
for article in content['articles']:
    if article["title"] is not None and article["description"] is not None:
        message = message + "Title: " + article["title"] + "\n" + "Description: " + article["description"] + 2*"\n"

message = message.encode("utf-8")
send_email(message)
print("Good")