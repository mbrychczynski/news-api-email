import requests
import os
from send_email import send_email

api_key = os.getenv("news_api_email_API_KEY")

topic = "apple"

url = f"https://newsapi.org/v2/everything?q={topic}&from=2024-07-21&sortBy=publishedAt&apiKey={api_key}&language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
message = "Subject: Today's news" + "\n"
for article in content['articles'][:20]:
    if article["title"] is not None and article["description"] is not None:
        message = (message + "Title: " + article["title"] + "\n" + "Description: " + article["description"]
                   + "\n" + article["url"] + 2*"\n")

message = message.encode("utf-8")
send_email(message)
print("Good")
