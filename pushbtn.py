import RPi.GPIO as GPIO
import time

redLightPin = 17
yellowLightPin = 27
greenLightPin = 5

button1Pin = 18
button2Pin = 23
button3Pin = 24

buzzerPin = 21

btn1On = False
btn1StateChanged = False
btn2On = False
btn2StateChanged = False
btn3On = False
btn3StateChanged = False

def print_message():
    print ("|**************************************|")
    print ("|  Push Button w/ LED & Active Buzzer  |")
    print ("|**************************************|\n")
    print 'Program is running...'
    print ('\n')
    print 'Please press Ctrl+C to end the program...'

def setup():
    # Set the GPIO modes to BCM Numbering
    GPIO.setmode(GPIO.BCM)

    # Setup GPIO pins here
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(redLightPin, GPIO.OUT)
    GPIO.setup(yellowLightPin, GPIO.OUT)
    GPIO.setup(greenLightPin, GPIO.OUT)
    GPIO.setup(button1Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(button2Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(button3Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(buzzerPin, GPIO.OUT, initial=GPIO.LOW)

def setLEDState(ledNo, onOffState):
    GPIO.output(ledNo, onOffState)

def setBuzzer(onOffState):
    GPIO.output(buzzerPin, onOffState)

def turnOffLEDs():
    setLEDState(redLightPin, False)
    setLEDState(greenLightPin, False)
    setLEDState(yellowLightPin, False)

def main():
    global btn1On
    global btn2On
    global btn3On
    global btn1StateChanged
    global btn2StateChanged
    global btn3StateChanged
    print_message()
    while True:
        btn1Pressed = not GPIO.input(button1Pin)
        btn2Pressed = not GPIO.input(button2Pin)
        btn3Pressed = not GPIO.input(button3Pin)

        # the button 1 has to be pressed & hold to light the LED and make noise from buzzer
        # release the button 1 will turn off the light and silient the buzzer
        if btn1Pressed != btn1On:
            btn1StateChanged = True
        # the button 2 has to be pressed & hold to light the LED
        # release the button 2 will turn off the light
        if btn2Pressed != btn2On:
            btn2StateChanged = True
        # the button 3 has to be pressed & hold to light the LED
        # release the button 3 will turn off the light
        if btn3Pressed != btn3On:
            btn3StateChanged = True

        # the button 1 is used as a switch, press it will turn on the LED, press it again will turn off the LED
        #if btn1Pressed == True:
        #    btn1StateChanged = True
        # the button 2 is used as a switch, press it will turn on the LED, press it again will turn off the LED
        #if btn2Pressed == True:
        #    btn2StateChanged = True
        # the button 3 is used as a switch, press it will turn on the LED, press it again will turn off the LED
        #if btn3Pressed == True:
        #    btn3StateChanged = True

        if btn1StateChanged == True:
            print('btn1StateChanged, old: ' + str(btn1On))
            btn1On = not btn1On
            setLEDState(greenLightPin, btn1On)
            setBuzzer(btn1On)
            btn1StateChanged = False

        if btn2StateChanged == True:
            print('btn2StateChanged, old: ' + str(btn2On))
            btn2On = not btn2On
            setLEDState(yellowLightPin, btn2On)
            btn2StateChanged = False

        if btn3StateChanged == True:
            print('btn3StateChanged, old: ' + str(btn3On))
            btn3On = not btn3On
            setLEDState(redLightPin, btn3On)
            btn3StateChanged = False

        time.sleep(0.1)

def destroy():
    # Any custom clean up code goes here
    turnOffLEDs()

    # Release resource
    GPIO.cleanup()    

# If run this script directly, do:
if __name__ == '__main__':
    setup()
    try:
        main()
    # When 'Ctrl+C' is pressed, the child program 
    # destroy() will be  executed.
    except KeyboardInterrupt:
        destroy()
