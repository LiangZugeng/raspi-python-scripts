import RPi.GPIO as GPIO
import time

buzzerPin = 21

def print_message():
    print ("|**************************************|")
    print ("|            Active Buzzer             |")
    print ("|**************************************|\n")
    print 'Program is running...'
    print ('\n')
    print 'Please press Ctrl+C to end the program...'

def setup():
    # Set the GPIO modes to BCM Numbering
    GPIO.setmode(GPIO.BCM)

    # Setup GPIO pins here
    GPIO.setup(buzzerPin, GPIO.OUT)

def main():
    print_message()
    while True:
        GPIO.output(buzzerPin, False)
        time.sleep(0.2)
        GPIO.output(buzzerPin, True)
        time.sleep(0.2)


def destroy():
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