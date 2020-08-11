from news import *
from audio import *


# this function start two new threads for news fetching and news reading
def play_news(topic=None):
    t1 = Thread(target=news.fetch, args=(topic,))
    t2 = Thread(target=tta.convert)
    t1.start()
    t2.start()


MAIN_BACKGROUND = '#b2ff59'
suggestions = [
    'Technology', 'Machine\nLearning', 'AI', 'Android', 'Tesla', 'SpaceX', 'Covid-19'
]

# start of tkinter GUI program
window = tk.Tk()
window.geometry("400x600")
window.title("Talking News v1.0")
window.iconbitmap(bitmap='res/News.ico')
window.configure(bg=MAIN_BACKGROUND)

# create two main frames : head frame and body frame
headFrame = tk.Frame(window)
bodyFrame = tk.Frame(window)
bodyFrame.configure(bg=MAIN_BACKGROUND)

# create a suggestions frame which is inside of body frame
suggestionFrame = tk.Frame(bodyFrame, relief=tk.SUNKEN, borderwidth=1)
suggestionFrame.configure(bg=MAIN_BACKGROUND)

# create labels and buttons
titleLabel = tk.Label(headFrame, text="Talking News",
                      bg=MAIN_BACKGROUND, fg="#2c3d94", font='Helvetica 20 bold')
topicLabel = tk.Label(bodyFrame, text="So... About what topic you want news ?",
                      bg=MAIN_BACKGROUND, fg="black", font='Helvetica 14 bold')
topicEntry = tk.Entry(bodyFrame, bg="#99ebdb", fg="black", font='Helvetica 14')
topicButton = tk.Button(bodyFrame, text="Let\'s Hear",
                        bg="#00bfa5", fg="black", font='Helvetica 14 bold',
                        command=lambda: play_news(topic=topicEntry.get()))
suggestionLabel = tk.Label(suggestionFrame, text="Suggestions :",
                           bg=MAIN_BACKGROUND, fg="black", font='Helvetica 12 bold')

# create objects of classes News and TextToAudio
news = News(window=window)
tta = TextToAudio(news=news, window=window)

# pack and grid elements
headFrame.pack(pady=10)
titleLabel.pack()
bodyFrame.pack(pady=10)
topicLabel.grid(row=0, column=0)
topicEntry.grid(row=1, column=0, pady=20)

suggestionFrame.grid(row=3, column=0, columnspan=3)
suggestionLabel.grid(row=0, column=0, sticky="w")
tk.Button(suggestionFrame, width=10, text=suggestions[0], bg="#53dd81", fg="black", font='Helvetica 10 bold',
          command=lambda: play_news(suggestions[0])).grid(row=0, column=1)
tk.Button(suggestionFrame, width=10, text=suggestions[1], bg="#53dd81", fg="black", font='Helvetica 10 bold',
          command=lambda: play_news(suggestions[1])).grid(row=0, column=2)
tk.Button(suggestionFrame, width=10, text=suggestions[2], bg="#53dd81", fg="black", font='Helvetica 10 bold',
          command=lambda: play_news(suggestions[2])).grid(row=0, column=3)
tk.Button(suggestionFrame, width=10, text=suggestions[3], bg="#53dd81", fg="black", font='Helvetica 10 bold',
          command=lambda: play_news(suggestions[3])).grid(row=1, column=1)
tk.Button(suggestionFrame, width=10, text=suggestions[4], bg="#53dd81", fg="black", font='Helvetica 10 bold',
          command=lambda: play_news(suggestions[4])).grid(row=1, column=2)
tk.Button(suggestionFrame, width=10, text=suggestions[5], bg="#53dd81", fg="black", font='Helvetica 10 bold',
          command=lambda: play_news(suggestions[5])).grid(row=1, column=3)
tk.Button(suggestionFrame, width=10, text=suggestions[6], bg="#53dd81", fg="black", font='Helvetica 10 bold',
          command=lambda: play_news(suggestions[6])).grid(row=2, column=1)

topicButton.grid(row=2, pady=20)
window.mainloop()
