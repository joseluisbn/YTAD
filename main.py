import os
import re
from pytube import YouTube
from tkinter import messagebox, Tk, Entry, Button, Label, StringVar, Menu

def is_valid_url(url):
    # Regex to check if the URL is a valid YouTube URL
    regex = r"(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})"
    return re.match(regex, url) is not None

def Widgets():
    link_label = Label(root, text="URL:", bg="#E8D579")
    link_label.grid(row=1, column=0, pady=5, padx=5)

    root.linkText = StringVar()
    link_entry = Entry(root, width=55, textvariable=root.linkText)
    link_entry.grid(row=1, column=1, pady=5, padx=5, columnspan=2)

    download_button = Button(
        root, text="Download", command=Download, width=20, bg="#05E8E0"
    )
    download_button.grid(row=2, column=1, pady=5, padx=5)

def Download():
    url = root.linkText.get()
    if not is_valid_url(url):
        messagebox.showerror("Error", "Invalid YouTube URL")
        return

    out_file = None
    try:
        yt_obj = YouTube(url)
        video = yt_obj.streams.filter(only_audio=True).first()
        out_file = video.download(download_folder)
        base, ext = os.path.splitext(out_file)
        new_file = base + ".mp3"
        os.rename(out_file, new_file)
        messagebox.showinfo("Success", "File downloaded in \n" + download_folder)
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        if out_file and os.path.exists(out_file):
            os.remove(out_file)

def About():
    messagebox.showinfo("About", "YT audio Downloader v0.1.1, by Joselito")

root = Tk()
root.geometry("600x120")
root.resizable(False, False)
root.title("YT audio Downloader v0.1.1")
root.config(background="#000000")

menu = Menu(root)
root.config(menu=menu)
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=About)

download_folder = os.path.join(os.getcwd(), "Downloads")
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

Widgets()
root.mainloop()