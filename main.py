import os
from flask import Flask, jsonify, render_template, request
import yt_dlp

app = Flask(__name__)


@app.route("/")
def index():
  return render_template("index.html")


@app.route("/download", methods=["POST"])
def download():
  data = request.get_json()
  url = data.get("url")

  if not url:
    return jsonify({"status": "error", "message": "URL missing"})

  try:
    # Cloud server par temporary folder use karna zaroori hai
    download_path = "/tmp"
    os.makedirs(download_path, exist_ok=True)

    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "outtmpl": os.path.join(download_path, "%(title)s.%(ext)s"),
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
      info = ydl.extract_info(url, download=True)
      filename = ydl.prepare_filename(info)

    return jsonify({
        "status": "success",
        "message": "Download complete on cloud server!",
    })
  except Exception as e:
    return jsonify({"status": "error", "message": str(e)})


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)
