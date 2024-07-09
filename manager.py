import pytz
import smtplib
from datetime import datetime


def send_notification(email):
    sender = 'omegabi.service@yandex.ru'
    sender_password = 'dajzgyrwwpqbhxyq'
    mail_server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
    mail_server.login(sender, sender_password)

    for i in email:
        msg = 'From: %s <%s>\r\nTo: %s\r\nContent-Type: text/html; charset="utf-8"\r\nSubject: %s\r\n\r\n' % (
            'OmegaBI', sender, i, f'Отчет о тестировании OmegaBI')
        msg += f'Тестирование завершено {report_time}🥳. Отчет доступен по ссылке: https://annk11.github.io/automation_testing/'
        mail_server.sendmail(sender, i, msg.encode('utf8'))
    mail_server.quit()


timezone = pytz.timezone('Europe/Moscow')
current_time = datetime.now()
report_time = current_time.astimezone(timezone).strftime("%d.%m.%Y %H:%M")

send_notification({'nikia@omegafuture.ru'})
