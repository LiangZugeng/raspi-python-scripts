import RPi.GPIO as GPIO
import time

redLightPin = 17
yellowLightPin = 27
greenLightPin = 5

redLightDuration = 3
yellowLightDuration = 1
greenLightDuration = 4

buzzerPin = 21

def print_message():
    print ("|**************************************|")
    print ("|             Traffic Lights           |")
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
    GPIO.setup(buzzerPin, GPIO.OUT, initial=GPIO.LOW)
    turnOffLEDs()

def setLEDState(ledNo, onOffState):
    GPIO.output(ledNo, onOffState)

def setBuzzer(onOffState):
    GPIO.output(buzzerPin, onOffState)

def turnOffLEDs():
    setLEDState(redLightPin, False)
    setLEDState(greenLightPin, False)
    setLEDState(yellowLightPin, False)

def main():
    print_message()
    while True:
        setLEDState(greenLightPin, True)
        time.sleep(greenLightDuration)
        setLEDState(greenLightPin, False)
        setLEDState(yellowLightPin, True)
        time.sleep(yellowLightDuration)
        setLEDState(yellowLightPin, False)
        setLEDState(redLightPin, True)
        time.sleep(redLightDuration)
        setLEDState(redLightPin, False)

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
