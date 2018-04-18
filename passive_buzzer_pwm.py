import RPi.GPIO as GPIO
import time

# variables to be defined here
buzzerPin = 20

def print_message():
    print ("|**************************************|")
    print ("|         Passive Buzzer PWM           |")
    print ("|**************************************|\n")
    print 'Program is running...'
    print ('\n')
    print 'Please press Ctrl+C to end the program...'

def setup():
    # Set the GPIO modes to BCM Numbering
    GPIO.setmode(GPIO.BCM)

    # Setup GPIO pins here
    GPIO.setup(buzzerPin, GPIO.OUT, initial=GPIO.LOW)

    global p
    # Start the PWM
    p = GPIO.PWM(buzzerPin, 880)
    p.start(50)

def main():
    print_message()
    while True:
        time.sleep(1)


def destroy():
    # Stop the PWM
    p.stop()

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