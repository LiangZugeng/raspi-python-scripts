import RPi.GPIO as GPIO
import time

buzzerPin = 20

def print_message():
    print ("|**************************************|")
    print ("|            Passive Buzzer            |")
    print ("|**************************************|\n")
    print 'Program is running...'
    print ('\n')
    print 'Please press Ctrl+C to end the program...'

def setup():
    # Set the GPIO modes to BCM Numbering
    GPIO.setmode(GPIO.BCM)

    # Setup GPIO pins here
    GPIO.setup(buzzerPin, GPIO.OUT)

def buzz(frequency, length):     #create the function "buzz" and feed it the pitch and duration)

    if(frequency==0):
        time.sleep(length)
        return
    period = 1.0 / frequency          #in physics, the period (sec/cyc) is the inverse of the frequency (cyc/sec)
    delayValue = period / 2         #calcuate the time for half of the wave
    numCycles = int(length * frequency)     #the number of waves to produce is the duration times the frequency
    
    for i in range(numCycles):        #start a loop from 0 to the variable "cycles" calculated above
        GPIO.output(buzzerPin, True)     #set buzzerPin to high
        time.sleep(delayValue)        #wait with buzzerPin high
        GPIO.output(buzzerPin, False)        #set buzzerPin to low
        time.sleep(delayValue)        #wait with buzzerPin low

def main():
    print_message()
    while True:
        buzz(220, 2)
        time.sleep(0.5)
        buzz(440, 2)
        time.sleep(0.5)
        buzz(880, 2)
        time.sleep(0.5)
        buzz(1760, 2)
        time.sleep(0.5)


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