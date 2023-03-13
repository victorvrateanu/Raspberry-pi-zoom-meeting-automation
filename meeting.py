import webbrowser
import datetime
import time
import subprocess

# Replace the placeholders with your actual meeting ID and password
meeting_id = "123456789"
password = "password123"

# Open the Zoom web URL with the meeting ID and password as query parameters
zoom_url = f"https://zoom.us/wc/{meeting_id}/join?pwd={password}"
chrome_path = "/usr/bin/chromium-browser" # Replace with the actual path to Chromium on your system
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open_new(zoom_url)

# Continuously check the current time and exit Zoom if it is 4:00 AM
while True:
    now = datetime.datetime.now()
    if now.hour == 4 and now.minute == 0:
        # Use the 'pkill' command to kill all instances of Chromium and Zoom
        subprocess.run(['pkill', '-9', 'chromium-browser'])
        subprocess.run(['pkill', '-9', 'zoom'])
        # Sleep for 5 seconds to allow time for the processes to exit
        time.sleep(5)
        # Run the 'meeting.py' script again
        subprocess.run(['python3', '/home/pi/Desktop/meeting.py'])
        break
    # Sleep for 60 seconds before checking the time again
    time.sleep(60)
