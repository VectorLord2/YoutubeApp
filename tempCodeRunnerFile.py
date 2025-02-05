import tkinter 
import customtkinter 
from pytube import YouTube


def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        music = ytObject.streams.get_audio_only()

        title.configure(text=ytObject.title, text_color="orange")
        finishLabel.configure(text="")
        music.download()
        finishLabel.configure(text="Downloaded", text_color="green")
    except:
        finishLabel.configure(text="Download Error", text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completetion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completetion))
    pPercentage.configure(text=per + "%")
    pPercentage.update

    # Update the Progress bar
    progressBar.set(float(percentage_of_completetion) / 100)


# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
# App Frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# Adding UI Elements
title= customtkinter.CTkLabel(app, text ="Insert a youtube link")
title.pack(padx=10, pady=10)

# link Input

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Download Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)
 
# Finished Downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Progress Percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack(padx=10, pady=10)
progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)


# Run App
app.mainloop()