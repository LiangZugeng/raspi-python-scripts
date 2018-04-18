import RPi.GPIO as GPIO
import time

# variables to be defined here
ledPin = 27

def print_message():
    print ("|**************************************|")
    print ("|            Breathing LED             |")
    print ("|**************************************|\n")
    print 'Program is running...'
    print ('\n')
    print 'Please press Ctrl+C to end the program...'

def setup():
    # Set the GPIO modes to BCM Numbering
    GPIO.setmode(GPIO.BCM)

    # Setup GPIO pins here
    GPIO.setup(ledPin, GPIO.OUT, initial=GPIO.LOW)

    global p
    # Start the PWM
    p = GPIO.PWM(ledPin, 1000)
    p.start(0)

def main():
    print_message()
    while True:
        for dc in range(0, 101, 4):   # Increase duty cycle: 0~100
            p.ChangeDutyCycle(dc)     # Change duty cycle
            time.sleep(0.1)
        time.sleep(1)
        for dc in range(100, -1, -4): # Decrease duty cycle: 100~0
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
        time.sleep(1)


def destroy():
    # Stop the PWM
    p.stop()
    # Turn off the LED
    GPIO.output(ledPin, GPIO.HIGH)

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