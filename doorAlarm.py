import RPi.GPIO as GPIO
import smtplib

GPIO.setmode(GPIO.BOARD)
channel = 26 #whatever pin we use
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)

TOADDR = "4848858460@txt.att.net" # fill in to address
FROMADDR = "VWiernicki@gmail.com" #fill in from address
LOGIN = FROMADDR
PASSWORD = "Beetlewmv93" #fill in password
msg = "Door has been opened."

def send_email(TOADDR, LOGIN, PASSWORD, FROMADDR, msg):
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.set_debuglevel(1)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(LOGIN, PASSWORD)
    smtpObj.sendmail(FROMADDR, TOADDR, msg)
    smtpObj.quit()
    print('Email Sent')

		
def isOpen(channel):
    if GPIO.input(channel):
        return 0
    else:
        return 1

initial_run = 0
count = 0
sentEmailCount = 0		
while True:
    value = isOpen(channel)
    if value:
	initial_run=1
        if (initial_run == 1): #switch is now closed.
            count += 1
            if count > 10:
     		if sentEmailCount == 0:
                    send_email(TOADDR, LOGIN, PASSWORD, FROMADDR, msg)
                    sentEmailCount = 1
                    count = 0
                    initial_run = 0
    
GPIO.cleanup()            	
#value = 0 after it sends email, reset value to 0 so it stops sending emails until closed again?
   # else:
    #    print "All clear"
