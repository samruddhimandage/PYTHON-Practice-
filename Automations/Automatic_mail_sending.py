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


def main():
    
    sender_email = "samruddhimandage3@gmail.com"

    app_password = "____________________________"   # password is private hence it is not written here

    receiver_email = "vikrantsp.2808@gmail.com"
    
    subject = "Mail through automated script using Python"
    
    body = """Hi Vikrant,

Regards,
Samruddhi Mandage"""
    
    send_email(
        sender_email,
        app_password,
        receiver_email,
        subject,
        body
    )
    
    print("Mail sent successfully")


if __name__ == "__main__":
    main()