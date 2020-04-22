import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 


html = Template(Path('test.html').read_text())
email = EmailMessage()
email['from'] = 'Garima Rahangdale'
email['to'] = 'garimarahangdale6@gmail.com'
email['subject'] = 'just checking my program!!'

email.set_content(html.substitute(name = 'Garima'), 'html')                                            

with smtplib.SMTP(host = 'smtp.gmail.com', port = 587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('garimarahangdale6@gmail.com', 'gar2997raha')
	smtp.send_message(email)
	print('Email sent!!')