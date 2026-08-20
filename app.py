import threading
import tkinter as tk
from tkinter import messagebox
import yt_dlp


def run_download(url, status_label):
  ydl_opts = {
      'format': 'bestvideo+bestaudio/best',
      'merge_output_format': 'mp4',
      'outtmpl': '%(title)s.%(ext)s',
  }
  try:
    status_label.config(text='Downloading highest quality...', fg='orange')
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
      ydl.download([url])
    status_label.config(text='Download Complete!', fg='green')
    messagebox.showinfo('Success', 'Video downloaded successfully!')
  except Exception as e:
    status_label.config(text='Error occurred!', fg='red')
    messagebox.showerror('Error', str(e))


def start_thread():
  url = entry_url.get().strip()
  if not url:
    messagebox.showwarning('Warning', 'Please enter a YouTube link.')
    return
  # Run in a separate thread so the app window doesn't freeze while downloading
  threading.Thread(target=run_download, args=(url, lbl_status)).start()


# Create the main window
root = tk.Tk()
root.title('YouTube High-Quality Downloader')
root.geometry('450x220')
root.resizable(False, False)

# UI Elements
tk.Label(
    root, text='Paste YouTube Link:', font=('Arial', 11, 'bold')
).pack(pady=10)

entry_url = tk.Entry(root, width=50, font=('Arial', 10))
entry_url.pack(pady=5)

btn_download = tk.Button(
    root,
    text='Download Video',
    command=start_thread,
    bg='#28a745',
    fg='white',
    font=('Arial', 10, 'bold'),
    padx=10,
    pady=5,
)
btn_download.pack(pady=15)

lbl_status = tk.Label(root, text='Ready', font=('Arial', 10))
lbl_status.pack(pady=5)

root.mainloop()