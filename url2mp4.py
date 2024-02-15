import subprocess

ytURL = "URL"

process = subprocess.Popen(['yt-dlp', '-f', 'bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]', ytURL], \
                           shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

while True:
    output = process.stdout.readline()
    if output == '' and process.poll() is not None:
        break
    if output:
        print(output.strip(), "\n")

input("Press Enter to finish.")
