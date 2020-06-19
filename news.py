import requests

api_key = "api key"

query = "Covid"

date = "current date"

url = f"http://newsapi.org/v2/everything?q={query}&from={date}&sortBy=publishedAt&apiKey={api_key}"

try:
    response = requests.get(url).json()
except Exception as e:
    print("Error :" + str(e))

if response["status"] == 'ok':
    articles = response['articles']
    for article in articles:
        source = article["source"]["name"]
        print(f"From: {source}")
        title = article["title"]
        print(f"Title : {title}")
        print("\n")
else:
    print("No news")