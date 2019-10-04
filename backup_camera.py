import RPi.GPIO as GPIO
import time
import os

M_pin = 24 #select the pin for reverse signal

def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(M_pin,GPIO.IN)
    pass

def detct():
    #os.system("raspivid -n -ih -t 0 -rot 270 -w 1280 -h 720 -fps 15 -b 1000000 -o - | nc -lkv4 5001")
    lastPinState = GPIO.input(M_pin)
    startCountdown = False
    counter = 0;
    while (1):
        currentPinState = GPIO.input(M_pin)
        if lastPinState != currentPinState :
            if (currentPinState):
                print "Turning WIFI ON"
                os.system("sudo service hostapd start")
                startCountdown = False
                counter = 0
            else :
                startCountdown = True

            lastPinState = currentPinState

        if startCountdown:
            counter = counter + 1
            if (counter > 20):
                print "Turning WIFI OFF"
                os.system("sudo service hostapd stop")
                startCountdown = False


        time.sleep(0.5)

print "Starting"
init()
detct()

GPIO.cleanup()
