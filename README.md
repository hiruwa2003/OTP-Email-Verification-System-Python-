 OTP Email Verification System (Python)

This project is a simple and secure OTP (One Time Password) verification system built using Python.
It automatically generates a 6-digit OTP, sends it to the user’s email using Gmail SMTP, and verifies the OTP entered by the user.

 Features

-> Generates a random 6-digit OTP

-> Sends OTP to any email using Gmail SMTP

-> Secure TLS connection

-> Email content handled using EmailMessage()

-> Verifies user input OTP

-> Easy to customize & extend

 -> Technologies Used

Python 3

-> smtplib (for sending email)

-> email.message.EmailMessage

-> random module

 How It Works

-> Program generates a random OTP

-> Sends OTP to the email entered by the user

-> User enters the OTP

-> Program checks if OTP is correct

-> Displays success or failure message

 Setup Instructions

-> Install Python 3

-> Enable App Password in Gmail

-> Replace the email and app password in the code

-> Run the script

Enter the target email & verify OTP
 Important

Use a Gmail App Password (NOT your normal password) for security.
