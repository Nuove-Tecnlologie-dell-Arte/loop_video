import os
from playvideo import *
import subprocess
subprocess.Popen(["python", "dwtelegram.py"])
while True:
    follength = len([f for f in os.listdir("vid/")if os.path.isfile(os.path.join("vid/", f))])
   # contatore = 1
    for contatore in range(int(follength)):
        video_captuire(contatore +1)