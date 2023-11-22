import os
from tkinter import Tk, Menu, messagebox
from downloader import YoutubeDownloader
from utils import about

if __name__ == "__main__":
    root = Tk()
    root.geometry("600x120")
    root.resizable(False, False)
    root.title("YT audio Downloader v0.1.1")
    root.config(background="grey")

    menu = Menu(root)
    root.config(menu=menu)
    helpmenu = Menu(menu)
    menu.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="About", command=about)

    downloader = YoutubeDownloader(root)

    root.mainloop()
