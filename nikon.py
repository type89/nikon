import subprocess
import time
import datetime

for i in range (3):
    now = datetime.datetime.today()
    strdate = str(now.date()) + "_" + str(now.time())
    cmd ="gphoto2 --capture-image-and-download --filename /home/pi/nikon/D40_" + strdate + ".jpg"
    subprocess.call(cmd.split())
    time.sleep(5)
