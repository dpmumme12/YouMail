import pathlib
import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = 'grab dinner'
msg['From'] = 'dpmumme12@gmail.com'
msg['To'] = 'dpmumme12@gmail.com'
msg.set_content('That Works!')

# Replace file name with file you wish to send
with open('test.pdf', 'rb') as f:
    file_data = f.read()
    file_type = pathlib.Path(f.name).suffix
    file_name = f.name


msg.add_attachment(file_data, maintype = 'application', subtype = file_type, filename = file_name)
    
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login('dpmumme12@gmail.com', 'heciuecbuvjisaeg')

    smtp.send_message(msg)
