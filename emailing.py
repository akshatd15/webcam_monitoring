import smtplib
import imghdr
from email.message import EmailMessage
import os

username = "devinx34@gmail.com"
password = os.getenv("PASSWORD")
receiver = "devinx34@gmail.com"


def send_mail(img_path):
   print("e started")
   email_message = EmailMessage()
   email_message["Subject"] = "Movement detected"
   email_message.set_content("Something came in camera")

   with open(img_path, 'rb') as file:
       content = file.read()
   email_message.add_attachment(content,maintype="image",subtype=imghdr.what(None,content))

   gmail = smtplib.SMTP("smtp.gmail.com",587)
   gmail.ehlo()
   gmail.starttls()
   gmail.login(username, password)
   gmail.sendmail(username, receiver, email_message.as_string())
   gmail.quit()
   print("e ended")


if __name__ == "__main__":
    send_mail()

