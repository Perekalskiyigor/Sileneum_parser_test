import smtplib
import os
from email.mime.text import MIMEText
import openpyxl

def send_email(message,sender1):
    sender = "perekalskiy.igor@gmail.com"
    password = "wnnshwomrmtxlsvo"
    # password = os.getenv("EMAIL_PASSWORD")
    

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
    # Чтение таблицы Excel и создание списка получателей и текста письма
    wb = openpyxl.load_workbook('emails.xlsx')
    ws = wb.active
    send_to = []
    body = []
    for row in ws.iter_rows(min_row=2, values_only=True):
         send_to.append(row[0])
         body.append(row[1])
         print(row[0])
         print(row[1])
         print(send_email(message=row[1], sender1 = row[0]))
         input()

    #sender1 = 'perekalskiy_igor@mail.ru'
    #message = input("Type your message: ")
    #print(send_email(message=message, sender1 = sender1))


if __name__ == "__main__":
    main()