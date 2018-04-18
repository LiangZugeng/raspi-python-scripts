from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.resolution = (3280, 2464)
camera.iso = 100
camera.shutter_speed = 400000
#camera.exposure_mode = 'off'
camera.start_preview()
sleep(2)
camera.capture('/home/pi/Desktop/image1.jpg', 'jpeg', quality=85)
camera.stop_preview()
