import os
from playvideo import *

while True:
    follength = len([f for f in os.listdir("vid/")if os.path.isfile(os.path.join("vid/", f))])
    print(follength)
   # contatore = 1
    for contatore in range(int(follength)):
        mammt(contatore +1)