
from picamera import PiCamera
import time as time
import os

try:
    os.mkdir("Images")
    print("Image directory made")
except:
    print("")
    
path=os.getcwd()
path=path+"/Images"
os.chdir(path)

y=1
n=0
response=n
while (response==n):
    time_interval=input("Enter the inteval (in sec) between shots:")

    print("Will save a picture ever "+str(time_interval)+" seconds")
    response=input( "\npress y to continue or n to enter a different interval:")

camera = PiCamera()
camera.rotation=180


time.sleep(2)

k=1
while (1):
    a=time.time()
 
    #camera.capture("/home/pi/Pictures/img.jpg")
    camera.capture(str(a)+"img.jpg")
    time.sleep(time_interval-0.48)   
    k=k+1
    b=time.time()
    print("shot "+str(k)+"   "+str(b-a))




