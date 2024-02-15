import subprocess

ytURL = "URL"

result = subprocess.run(['yt-dlp', '-f', 'bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]', ytURL])
print(result)
