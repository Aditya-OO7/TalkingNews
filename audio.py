from gtts import gTTS
import os
from load import *


# TextToAudio class contains methods and data members which help in converting fetched news into audio file (.mp3)
class TextToAudio:
    def __init__(self, news=None, window=None):
        self.news = news
        self.window = window
        self.loadAnim = LoaderAnim(self.window)

    # convert fetched news into audio file
    def convert(self):
        # wait for news fetching thread to complete it's task
        self.news.condition.acquire()
        self.news.condition.wait(timeout=0)
        self.news.condition.release()

        # display loading image
        self.loadAnim.loadingLabel.pack()
        self.window.after(0, self.loadAnim.start_loading, 0)

        # display label for loading content
        progress_label = tk.Label(self.window, text="Reading news for you!!! ",
                                  bg="#b2ff59", font='Helvetica 14 bold')
        progress_label.pack()

        # convert to audio file
        file_handler = open('news.txt', 'r')
        news = file_handler.read()
        file_handler.close()
        language = 'en'
        output = gTTS(text=news, lang=language, slow=False)
        output.save('output.mp3')
        os.system("start output.mp3")

        # destroy loading image and label
        progress_label.destroy()
        self.loadAnim.stop_loading()
