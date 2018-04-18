import RPi.GPIO as GPIO
import time

light1Pin = 27
light2Pin = 17

button1Pin = 18
button2Pin = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(light1Pin, GPIO.OUT)
GPIO.setup(light2Pin, GPIO.OUT)
GPIO.setup(button1Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    btn1_state = GPIO.input(button1Pin)
    btn2_state2 = GPIO.input(button2Pin)
    print(btn1_state)
    if btn1_state == False:
        print('Button 1 Pressed')
        GPIO.output(light1Pin, True)
    else:
        GPIO.output(light1Pin, False)

    print(btn2_state2)
    if btn2_state2 == False:
        print('Button 2 Pressed')
        GPIO.output(light2Pin, True)
    else:
        GPIO.output(light2Pin, False)

    print('')
    time.sleep(0.1)
