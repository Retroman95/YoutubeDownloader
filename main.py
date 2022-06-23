import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog



def Widgets():
    head_label = Label(root, text="Загрузчик видео с YouTube",
                       padx=15,
                       pady=15,
                       font="SegoeUI 14",
                       #bg="blue",
                       fg="red")
    head_label.grid(row=1,
                    column=1,
                    pady=10,
                    padx=5,
                    columnspan=3)

    link_label = Label(root,
                       text="YouTube ссылка :",
                       bg="salmon",
                       pady=5,
                       padx=5)
    link_label.grid(row=2,
                    column=0,
                    pady=5,
                    padx=5)

    root.linkText = Entry(root,
                          width=35,
                          textvariable=video_Link,
                          font="Arial 14")
    root.linkText.grid(row=2,
                       column=1,
                       pady=5,
                       padx=5,
                       columnspan=2)

    destination_label = Label(root,
                              text="Путь скачивания :",
                              bg="salmon",
                              pady=5,
                              padx=9)
    destination_label.grid(row=3,
                           column=0,
                           pady=5,
                           padx=5)

    root.destinationText = Entry(root,
                                 width=27,
                                 textvariable=download_Path,
                                 font="Arial 14")
    root.destinationText.grid(row=3,
                              column=1,
                              pady=5,
                              padx=5)

    browse_B = Button(root,
                      text="Указать",
                      command=Browse,
                      width=10,
                      bg="bisque",
                      relief=GROOVE)
    browse_B.grid(row=3,
                  column=2,
                  pady=1,
                  padx=1)

    Download_B = Button(root,
                        text="Скачать видео",
                        command=Download,
                        width=20,
                        bg="thistle1",
                        pady=10,
                        padx=15,
                        relief=GROOVE,
                        font="Georgia, 13")
    Download_B.grid(row=4,
                    column=1,
                    pady=20,
                    padx=20)


# Defining Browse() to select a
# destination folder to save the video

def Browse():

    download_Directory = filedialog.askdirectory(
        initialdir="YOUR DIRECTORY PATH", title="Save Video")


    download_Path.set(download_Directory)





def Download():
    # подготовка введённой пользователем ссылки
    Youtube_link = video_Link.get()

    # выбор директории для сохранения файла
    download_Folder = download_Path.get()

    # создание объекта YouTube()
    getVideo = YouTube(Youtube_link)

    # Подготовка видео к загрузке
    videoStream = getVideo.streams.get_highest_resolution() #Для скачивания в самом высоком качестве

    # Загрузка видео в указанную директорию
    videoStream.download(download_Folder)

    # показ сообщения об окончании загрузки
    messagebox.showinfo("Успешно",
                        "Видео успешно загружено и сохранено\n"
                        + download_Folder)


root = tk.Tk()

root.geometry("540x280")
root.resizable(False, False)
root.title("YouTube Video Downloader")
#root.config(background="Blue")

video_Link = StringVar()
download_Path = StringVar()

Widgets()

root.mainloop()
