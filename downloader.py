import os
import re
from pytube import YouTube
from tkinter import messagebox, Entry, Button, Label, StringVar

class YoutubeDownloader:
    def __init__(self, root):
        self.root = root
        self.download_folder = os.path.join(os.getcwd(), "Downloads")
        if not os.path.exists(self.download_folder):
            os.makedirs(self.download_folder)

        self.create_widgets()

    def create_widgets(self):
        link_label = Label(self.root, text="URL:", bg="#E8D579")
        link_label.grid(row=1, column=0, pady=5, padx=5)

        self.linkText = StringVar()
        link_entry = Entry(self.root, width=55, textvariable=self.linkText)
        link_entry.grid(row=1, column=1, pady=5, padx=5, columnspan=2)

        download_button = Button(
            self.root, text="Download", command=self.download, width=20, bg="#05E8E0"
        )
        download_button.grid(row=2, column=1, pady=5, padx=5)

    def is_valid_url(self, url):
        # Regex to check if the URL is a valid YouTube URL
        regex = r"(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})"
        return re.match(regex, url) is not None

    def download(self):
        url = self.linkText.get()
        if not self.is_valid_url(url):
            messagebox.showerror("Error", "Invalid YouTube URL")
            return

        try:
            # Check if the file already exists
            video_id = YouTube(url).video_id
            file_name = os.path.join(self.download_folder, f"{video_id}.mp3")
            if os.path.exists(file_name):
                messagebox.showerror("Error", "File with the same name already exists.")
            else:
                self.download_video(url)
                messagebox.showinfo("Success", "File downloaded in \n" + self.download_folder)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def download_video(self, url):
        yt_obj = YouTube(url)
        video = yt_obj.streams.filter(only_audio=True).first()
        out_file = video.download(self.download_folder)
        base, ext = os.path.splitext(out_file)
        new_file = base + ".mp3"
        os.rename(out_file, new_file)
        if os.path.exists(out_file):
            os.remove(out_file)
