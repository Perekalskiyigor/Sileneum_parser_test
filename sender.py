import smtplib
import os
from email.mime.text import MIMEText
import openpyxl


def send_email(message, email):
    sender = 'perekalskiy.igor@gmail.com'
    # your password = "your password"
    password = 'cooezvzfyeoadjwa'

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg["Subject"] = "Диктант побды"
        server.sendmail(sender, email, msg.as_string())

        # server.sendmail(sender, sender, f"Subject: CLICK ME PLEASE!\n{message}")

        return "The message was sent successfully!"
    except Exception as _ex:
        return f"{_ex}\nCheck your login or password please!"


def main():
    # Чтение таблицы Excel и создание списка получателей и текста письма
    wb = openpyxl.load_workbook('emails.xlsx')
    ws = wb.active
    send_to = []
    body = []
    for row in ws.iter_rows(min_row=2, values_only=True):
        send_to.append(row[0])
        body.append(row[1])
        send_email(message=row[1], email = row[1])
        print(row[0])
        print(row[1])
        input()
        # message = input("Type your message: ")
        
        # print(send_email(message=message))


if __name__ == "__main__":
    main()