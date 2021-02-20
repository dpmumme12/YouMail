import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = 'grab dinner'
msg['From'] = 'dpmumme12@gmail.com'
msg['To'] = 'dpmumme12@gmail.com'
msg.set_content('That Works!')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login('dpmumme12@gmail.com', 'heciuecbuvjisaeg')

    smtp.send_message(msg)
