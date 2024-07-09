import os
import glob
import json
import psycopg2
from datetime import datetime

conn = psycopg2.connect(
    dbname="ml_result",
    user="postgres",
    password="postgres",
    host="bi-demo-01",
    port="5447"
)

report_path = "."
half_name = 'newman'
newman_report = max(glob.glob(os.path.join(report_path, f'*{half_name}*.json')), key=os.path.getctime)
allure_report = max(glob.glob(os.path.join(f'{report_path}/allure-report/widgets', 'summary.json')))

with open(newman_report, 'r') as file:
    data = json.load(file)

    api_tests_total = data["run"]["stats"]["tests"]["total"]
    api_tests_pending = data["run"]["stats"]["tests"]["pending"]
    api_tests_failed = data["run"]["stats"]["tests"]["failed"]
    api_tests_passed = api_tests_total - api_tests_pending - api_tests_failed
    api_assertions_total = data["run"]["stats"]["assertions"]["total"]
    api_assertions_pending = data["run"]["stats"]["assertions"]["pending"]
    api_assertions_failed = data["run"]["stats"]["assertions"]["failed"]
    api_assertions_passed = api_assertions_total - api_assertions_pending - api_assertions_failed

with open(allure_report, 'r') as file:
    data = json.load(file)

    ui_tests_total = data["statistic"]["total"]
    ui_tests_broken = data["statistic"]["broken"]
    ui_tests_failed = data["statistic"]["failed"]
    ui_tests_passed = data["statistic"]["passed"]
    ui_tests_unknown = data["statistic"]["unknown"]
    ui_tests_skipped = data["statistic"]["skipped"]

with conn.cursor() as cursor:
    cursor.execute('''CREATE TABLE IF NOT EXISTS allure_report (
                        id SERIAL PRIMARY KEY,
                        date TIMESTAMP,
                        metric_name VARCHAR(50),
                        total INTEGER,
                        pending INTEGER,
                        failed INTEGER,
                        broken INTEGER,
                        passed INTEGER,
                        unknown INTEGER,
                        skipped INTEGER
                    )''')

date = datetime.now()
with conn.cursor() as cursor:
    cursor.execute('''INSERT INTO allure_report (date, metric_name, total, pending, failed, broken, passed, 
    unknown, skipped) 
                      VALUES 
                      (CURRENT_TIMESTAMP, 'api_tests', %s, %s, %s, 0, %s, 0, 0),
                      (CURRENT_TIMESTAMP, 'api_assertions', %s, %s, %s, 0, %s, 0, 0),
                      (CURRENT_TIMESTAMP, 'ui_tests', %s, 0, %s, %s, %s, %s, %s)''',
                   (api_tests_total, api_tests_pending, api_tests_failed, api_tests_passed,
                    api_assertions_total, api_assertions_pending, api_assertions_failed, api_assertions_passed,
                    ui_tests_total, ui_tests_failed, ui_tests_broken, ui_tests_passed, ui_tests_unknown,
                    ui_tests_skipped))

conn.commit()
conn.close()