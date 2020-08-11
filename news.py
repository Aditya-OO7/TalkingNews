from threading import *
import requests
from load import *


# News class contains methods and data members which help in fetching news from news API
class News:
    def __init__(self, window):
        self.window = window
        self.headings = []
        self.descriptions = []
        self.condition = Condition()
        self.secret = '<your_api_key_goes_here>'
        self.url = 'https://newsapi.org/v2/everything?'
        self.loadAnim = LoaderAnim(self.window)

    # this function fetches news from news API
    def fetch(self, topic):
        # lock the thread
        self.condition.acquire()

        # display loading image
        self.loadAnim.loadingLabel.pack()
        self.window.after(0, self.loadAnim.start_loading, 0)

        # display label for loading content
        progress_label = tk.Label(self.window, text="Fetching News about " + topic,
                                  bg="#b2ff59", font='Helvetica 14 bold')
        progress_label.pack()

        # fetch news
        parameters = {
            'q': topic,
            'pageSize': 2,
            'apiKey': self.secret
        }
        response = requests.get(self.url, params=parameters)

        response_json = response.json()

        for i in response_json['articles']:
            self.headings.append(i['title'])
            self.descriptions.append(i['description'])

        file_handler = open('news.txt', 'w')
        for i, j in zip(self.headings, self.descriptions):
            file_handler.write("Heading : " + i + '\n' + "Description : " + j + '\n')

        file_handler.close()

        # destroy loading image and label
        progress_label.destroy()
        self.loadAnim.stop_loading()

        # release lock and notify to waiting threads
        self.condition.notify()
        self.condition.release()
