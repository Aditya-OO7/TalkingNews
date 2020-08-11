import tkinter as tk


# LoaderAnim class helps to display loading image animation
class LoaderAnim:
    def __init__(self, window):
        self.window = window
        self.frameRange = 12
        self.frames = [tk.PhotoImage(file='res/loading.gif', format='gif -index %i' % i) for i in
                       range(self.frameRange)]
        self.loadingLabel = tk.Label(image=self.frames[0],)
        self.timer_id = None

    # start animation
    def start_loading(self, n=0):
        frame = self.frames[n]
        if n < self.frameRange - 1:
            n += 1
        else:
            n = 0

        self.loadingLabel.configure(image=frame)
        self.timer_id = self.window.after(100, self.start_loading, n)

    # stop animation
    def stop_loading(self):
        if self.timer_id:
            self.window.after_cancel(self.timer_id)
            self.loadingLabel.pack_forget()
