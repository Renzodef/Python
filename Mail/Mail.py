# Python's version used: 3.8.2 64 bit
# Before launching the script you need to activate the less secure apps' access of Gmail from:
# https://myaccount.google.com/lesssecureapps
import smtplib

# Creating mail
oggetto = "Subject: Prova\n\n"
contenuto = "Messaggio di prova."
messaggio = oggetto + contenuto

# Creating connection
email = smtplib.SMTP('smtp.gmail.com:587')
email.ehlo()
email.starttls()

# Login for the sender
# Replace "password_email" with the current password of the account
email.login("renzodefrancesco@gmail.com", "password_email")

# Sending the mail (Sender, Receiver, Mail)
email.sendmail("renzodefrancesco@gmail.com", "renzodefrancesco@gmail.com",
               messaggio)

# Closing connection
email.quit()