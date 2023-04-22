import openpyxl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
# Чтение таблицы Excel и создание списка получателей и текста письма
wb = openpyxl.load_workbook('emails.xlsx')
ws = wb.active
send_to = []
body = []
for row in ws.iter_rows(min_row=2, values_only=True):
    send_to.append(row[0])
    body.append(row[1])
# Настройка параметров подключения к Gmail
EMAIL = "perekalskiy.igor@gmail.com"
PASSWORD = "Fnkfynblf!(*&14"
SERVER = "smtp.gmail.com"
PORT = 587
# Отправка письма
server = smtplib.SMTP(SERVER, PORT)
server.starttls()
server.login(EMAIL, PASSWORD)
for recipient, content in zip(send_to, body):
    message = MIMEMultipart()
    message['From'] = EMAIL
    message['To'] = recipient
    message['Subject'] = 'Тестовое письмо'
    text = MIMEText(content)
    message.attach(text)
    server.sendmail(EMAIL, recipient, message.as_string())
    print(f"Письмо отправлено на {recipient}")
server.quit()