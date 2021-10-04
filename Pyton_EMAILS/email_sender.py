import smtplib
from email.message import EmailMessage

email = EmailMessage()
#choosing sender, recipient and subject od the message
email['from'] = 'klaudyna631@wp.pl'
email['to'] = 'klaudia.szczepanska.x@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'

#message to sent
email.set_content('I am a Python Master!')

#connection configuration
with smtplib.SMTP(host='smtp.wp.pl', port=587) as smtp:
    smtp.ehlo()         #hello message - obligatory
    smtp.starttls()     #mechanism that connect securely to the serwer
    smtp.login('klaudyna631@wp.pl', 'Malgorzata712')
    smtp.send_message(email)
    print('all good boss')