import subprocess
import time
import datetime

foldername = "/home/pi/nikon/"

for i in range (3):
    now = datetime.datetime.today()
    strdate = str(now.date()) + "_" + str(now.time())
    filename = "D40_" + strdate + ".jpg"

    cmd ="gphoto2 --capture-image-and-download --filename " + folder + filename
    subprocess.call(cmd.split())
    time.sleep(5)
