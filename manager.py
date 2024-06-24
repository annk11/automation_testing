import os
import glob
import json
import pytz
import base64
import smtplib
from datetime import datetime
import matplotlib.pyplot as plt


def send_notification(email, txt):
    sender = 'omegabi.service@yandex.ru'
    sender_password = 'dajzgyrwwpqbhxyq'
    mail_server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
    mail_server.login(sender, sender_password)

    for to_item in email:
        msg = 'From: %s\r\nTo: %s\r\nContent-Type: text/html; charset="utf-8"\r\nSubject: %s\r\n\r\n' % (
            sender, to_item, f'Отчет о тестировании API OmegaBI')
        msg += txt
        mail_server.sendmail(sender, to_item, msg.encode('utf8'))
    mail_server.quit()

def create_message(message):
    half_name = 'newman'
    html_file = glob.glob(os.path.join(report_path, f'*{half_name}*.html'))  # html file name
    latest_html_file = max(html_file, key=os.path.getctime)  # fresh html file
    report_file = open(latest_html_file, 'r', encoding='utf-8')
    html = report_file.read()
    json_file = glob.glob(os.path.join(report_path, f'*{half_name}*.json'))  # json file name
    latest_json_file = max(json_file, key=os.path.getctime)  # fresh json file

    # Parsing json
    with open(latest_json_file, 'r') as file:
        data = json.load(file)
    total = data["run"]["stats"]["assertions"]["total"]
    failed = data["run"]["stats"]["assertions"]["failed"]

    return message

# Path to Postman collection/environment
postman_collection = "tests/api/testing.postman_collection.json"
postman_environment = "tests/api/test-stand-ml.postman_environment.json"

# Path to save report
report_path = "."

# Command text
cmd = f"newman run {postman_collection} -e {postman_environment} -r cli,html,json, allure --reporter-html-export " \
      f"{report_path} --reporter-json-export {report_path} --reporter-allure-export {report_path} --delay-request 1000"
cmd_allure = "allure generate allure-results"

process = os.system(cmd)

if process == 0:
    process_allure = os.system(cmd_allure)
    timezone = pytz.timezone('Europe/Moscow')
    current_time = datetime.now()
    report_time = current_time.astimezone(timezone).strftime("%d.%m.%Y %H:%M")
    html_text = f"""\
        <html>
    <head>
        <style>
            .bold-green-text {{
                font-weight: bold;
                font-size: 16px;
                color: ForestGreen;
            }}
        </style>
    </head>
    <body>
        <p class="bold-green-text">Collections run completed at {report_time}. 
        All tests passed successfully!</p>
        <p>More information: https://annk11.github.io/automation_testing/</p>
    </body>
    </html>
    """
    message = create_message(html_text)
    send_notification({'nikia@omegafuture.ru'}, message)
else:
    process_allure = os.system(cmd_allure)
    timezone = pytz.timezone('Europe/Moscow')
    current_time = datetime.now()
    report_time = current_time.astimezone(timezone).strftime("%d.%m.%Y %H:%M")
    html_text = f"""\
            <html>
        <head>
            <style>
                .bold-red-text {{
                    font-weight: bold;
                    font-size: 16px;
                    color: Crimson;
                }}
            </style>
        </head>
        <body>
            <p class="bold-red-text">Collections run completed at {report_time}. 
            An error occurred while executing tests.</p>
            <p>More information: https://annk11.github.io/automation_testing/</p>
        </body>
        </html>
    """
    message = create_message(html_text)
    send_notification({'nikia@omegafuture.ru'}, message)