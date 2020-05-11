# Python's version used: 3.8.2 64 bit
# Before launching the script you need to activate the less secure apps' access of Gmail from:
# https://myaccount.google.com/lesssecureapps
import smtplib
from email.message import EmailMessage
import os

# Creting attachment (a simple .txt file)
contenuto = "Prova."
file = open("Prova.txt", "w")
file.write(contenuto)
file.close()

# Creating mail with attachment
msg = EmailMessage()
# Sender
msg["From"] = "renzodefrancesco@gmail.com"
# Subject
msg["Subject"] = "Prova"
# Receiver
msg["To"] = "renzo1.defrancesco@libero.it"
# Body of the mail
msg.set_content("Questo è un messaggio di prova")
# Attachment
msg.add_attachment(open("Prova.txt", "r").read(), filename="Prova.txt")

# Creating connection
email = smtplib.SMTP('smtp.gmail.com:587')
email.ehlo()
email.starttls()

# Login for the sender
# Replace "password_email" with the current password of the account
email.login("renzodefrancesco@gmail.com", "password_email")

# Sending the mail
email.send_message(msg)

# Deleting the attachment from the local filesystem
file_path = 'Prova.txt'
os.remove(file_path)

# Closing connection
email.quit()