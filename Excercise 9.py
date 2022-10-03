#EXCERCISE 9
import requests
import json
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("Sir wait a minute, I am finding top news for you.")
    url = "https://newsapi.org/v2/everything?q=tesla&from=2022-05-28&sortBy=publishedAt&apiKey=166cf40956434d289c251173d7e36715"
    news = requests.get(url).text
    news_dict = json.loads(news)
    print(news_dict["articles"])
    arts = news_dict['articles']
    for article in arts:
        speak(article['title'])
        speak("Next news..")

