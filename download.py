import sys
import yt_dlp

def download_video(url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'outtmpl': '%(title)s.%(ext)s',
    }
    
    try:
        print("\n[+] Downloading highest quality streams...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\n[SUCCESS] Download complete!\n")
    except Exception as e:
        print(f"\n[ERROR] {e}\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        video_url = sys.argv[1]
    else:
        video_url = input("Enter YouTube Link: ").strip()
    
    if video_url:
        download_video(video_url)