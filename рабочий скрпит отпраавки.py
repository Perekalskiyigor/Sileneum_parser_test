import smtplib
import os
from email.mime.text import MIMEText


def send_email(message):
    sender = "perekalskiy.igor@gmail.com"
    password = "uwhwbcfrconlitnu"
    # password = os.getenv("EMAIL_PASSWORD")
    sender1 = 'perekalskiy_igor@mail.ru'

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg["Subject"] = "CLICK ME PLEASE!"
        server.sendmail(sender, sender1, msg.as_string())

        # server.sendmail(sender, sender, f"Subject: CLICK ME PLEASE!\n{message}")

        return "The message was sent successfully!"
    except Exception as _ex:
        return f"{_ex}\nCheck your login or password please!"


def main():
    message = input("Type your message: ")
    print(send_email(message=message))


if __name__ == "__main__":
    main()