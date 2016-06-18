import RPi.GPIO as GPIO

FLOW_METER_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_METER_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def hello_world(pin_number):
    print "flow detected - " + str(pin_number)


GPIO.add_event_detect(FLOW_METER_PIN, GPIO.RISING, callback=hello_world, bouncetime=20)

while True:
    x = 1
