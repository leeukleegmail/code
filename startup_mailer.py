import smtplib
from email.mime.text import MIMEText
import datetime
from netifaces import interfaces, ifaddresses, AF_INET
from credentails import RECIPIENT, GMAIL_ACCOUNT, GMAIL_PASSWORD

# Change to your own account information
# Account Information

to = RECIPIENT # Email to send to.
gmail_user = GMAIL_ACCOUNT # Email to send from. (MUST BE GMAIL)
gmail_password = GMAIL_PASSWORD # Gmail password.

smtpserver = smtplib.SMTP('smtp.gmail.com', 587) # Server to use.

smtpserver.ehlo()  # Says 'hello' to the server
smtpserver.starttls()  # Start TLS encryption
smtpserver.ehlo()
smtpserver.login(gmail_user, gmail_password)  # Log in to server
today = datetime.date.today()  # Get current time/date

for ifaceName in interfaces():
    addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
    if 'wlan0' in ifaceName:
        my_ip_a = '%s: %s' % (ifaceName, ', '.join(addresses))
    elif 'eth0' in ifaceName:
        my_ip_b = '%s: %s' % (ifaceName, ', '.join(addresses))
    elif 'lo' in ifaceName:    
        my_ip_c = '%s: %s' % (ifaceName, ', '.join(addresses))

# Creates the text, subject, 'from', and 'to' of the message.
msg = MIMEText(my_ip_a + "\n" + my_ip_b + "\n" + my_ip_c)
msg['Subject'] = 'IPs For RaspberryPi on %s' % today.strftime('%b %d %Y')
msg['From'] = gmail_user
msg['To'] = to
smtpserver.sendmail(gmail_user, [to], msg.as_string())
smtpserver.quit()
