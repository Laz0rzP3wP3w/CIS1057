import RPi.GPIO as GPIO
import smtplib

GPIO.setmode(GPIO.BOARD)
channel = 26 #whatever pin we use
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)

TOADDR = "" #fill in to address
FROMADDR = "" #fill in from address
LOGIN = FROMADDR
PASSWORD = "" #fill in password
msg = "Door has been opened."

def send_email(TOADDR, LOGIN, PASSWORD, FROMADDR, msg):
	smtpObj = smtplib.SMTP('smtp.gmail.com' , 587)
	smtpObj.set_debuglevel(1)
	smtpObj.ehlo()
	smtpObj.starttls()
	smtpObj.login(LOGIN, PASSWORD)
	smtpObj.sendmail(FROMADDR, TOADDRS, msg)
	smtpObj.quit()
	print('Email Sent')

		
def isOpen(channel):
    if GPIO.input(channel):
	    return 0
	else:
	    return 1
		
while True:
    value = isOpen(channel)
	if value:
	    send_email(TOADDR, LOGIN, PASSWORD, FROMADDR, msg)
		value = 0 #after it sends email, reset value to 0 so it stops sending emails until closed again?
	else:
	    print "All clear"
