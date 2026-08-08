import schedule       
import time           
import datetime
import smtplib
from email.message import EmailMessage


def send_email(sender, app_password, receiver, subject, body):

    msg = EmailMessage()

    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    msg.set_content(body)

    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    smtp.login(sender, app_password)

    smtp.send_message(msg)

    smtp.quit()

    print("Mail sent successfully")


def main():

    sender_email = "samruddhimandage3@gmail.com"

    app_password = "______________________"   # password is private hence it is not written here

    receiver_email = "vikrantsp.2808@gmail.com"

    subject = "Mail through automated script using Python"

    body = """Hi Vikrant,

Regards,
Samruddhi Mandage"""

    # Send email every 10 seconds
    schedule.every(10).seconds.do(
        send_email,
        sender_email,
        app_password,
        receiver_email,
        subject,
        body
    )

    print("Email scheduler started...")

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()