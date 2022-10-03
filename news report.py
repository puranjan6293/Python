import json
import requests
import datetime
datefor = datetime.date.today()
news_about = input("about\n")
news_api = "166cf40956434d289c251173d7e36715"
news_data = requests.get(f"https://newsapi.org/v2/everything?q={news_about}&from={datefor}&sortBy=publishedAt&apiKey={news_api}")
news_report = news_data.json()
print(news_report)
# article = news_report["articles"]
# best_articles = []
# for arti in article:
#     best_articles.append(arti['title'])
# for at in range(5):
#     print(at + 1, best_articles[at])
