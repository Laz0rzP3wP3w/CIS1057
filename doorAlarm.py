import RPi.GPIO as GPIO
import smtplib
import time

GPIO.setmode(GPIO.BOARD)
channel = 26 #whatever pin we use
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)

TOADDR = "" # fill in to address (gmail only)
FROMADDR = "" #fill in from address
LOGIN = FROMADDR
PASSWORD = "" #fill in password
msg = "Door has been opened."

def send_email(TOADDR, LOGIN, PASSWORD, FROMADDR, msg):
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.set_debuglevel(1)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(LOGIN, PASSWORD)
    smtpObj.sendmail(FROMADDR, TOADDR, msg)
    smtpObj.quit()
    print "--Email sent--"

		
def isOpen(channel):
    if GPIO.input(channel):
        return 0
    else:
        return 1

initial_run = 0
count = 0
print "...Checking for open door..."

while True:
    value = isOpen(channel)
    if value:
	initial_run=1
        if (initial_run == 1):
            count += 1
            if count > 10:
                send_email(TOADDR, LOGIN, PASSWORD, FROMADDR, msg)
                count = 0
                initial_run = 0
                print "10 seconds until next check"
                time.sleep(10)
                print "...Checking for open door..."

    
GPIO.cleanup()
