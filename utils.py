import time
import os
from io import BytesIO
import requests
from PIL import Image

def download(url):
    for i in range(3):
        try:
            with requests.get(url) as response:
                return Image.open(BytesIO(response.content))
        except Exception as e:
            print(f"{i}/3 Could not download Image '{url}'...")
            time.sleep(1)

def setBG(p, filename):
    if p == "feh":
        os.system(f"feh --bg-max {filename}")
    elif p == "nitrogen":
        os.system(f"nitrogen {filename}")
    elif p == "gsettings":
        os.system(f"gsettings set org.gnome.desktop.background picture-uri file:{filename}")
        os.system("gsettings set org.gnome.desktop.background picture-options 'scaled'")
    
    #set the Lock screen
    #os.system(f"sudo ./ubuntu-gdm-set-background --image {filename}")