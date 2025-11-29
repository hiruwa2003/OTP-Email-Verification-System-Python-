import random
import smtplib
from email.message import EmailMessage


otp = ""
for i in range(6):
    otp += str(random.randint(0,9))

#print(otp)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

from_mail = 'youremail@gmail.com'
server.login(from_mail, 'password')
to_mail = input("Enter your email address: ")
print("OTP has been sent to your email address.")

msg = EmailMessage()
msg['Subject'] = 'Your One Time Password (OTP)'
msg['From'] = from_mail
msg['To'] = to_mail
msg.set_content('Your OTP is:' +otp)
server.send_message(msg)

input_otp = input("Enter the OTP sent to your email: ")
if input_otp == otp:
    print("OTP is valid.")
else:
    print("OTP is invalid.")
server.quit()

