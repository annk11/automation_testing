import os
import glob
import json
import psycopg2
from datetime import datetime

conn = psycopg2.connect(
    dbname="ml_result",
    user="postgres",
    password="postgres",
    host="bi-dev-01",
    port="5447"
)

def parse_json_data(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    tests_total = data["run"]["stats"]["tests"]["total"]
    tests_pending = data["run"]["stats"]["tests"]["pending"]
    tests_failed = data["run"]["stats"]["tests"]["failed"]
    assertions_total = data["run"]["stats"]["assertions"]["total"]
    assertions_pending = data["run"]["stats"]["assertions"]["pending"]
    assertions_failed = data["run"]["stats"]["assertions"]["failed"]

    return (tests_total, tests_pending, tests_failed, assertions_total, assertions_pending,
            assertions_failed)


def create_allure_report_table(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS allure_report (
                        id SERIAL PRIMARY KEY,
                        date TIMESTAMP,
                        tests_total INTEGER,
                        tests_pending INTEGER,
                        tests_failed INTEGER,
                        assertions_total INTEGER,
                        assertions_pending INTEGER,
                        assertions_failed INTEGER
                    )''')
    conn.commit()

def insert_data_to_allure_report(conn, tests_total, tests_pending, tests_failed, assertions_total,
                                 assertions_pending, assertions_failed):
    cursor = conn.cursor()
    date = datetime.now()
    cursor.execute('''INSERT INTO allure_report (date, tests_total, tests_pending, tests_failed, assertions_total, 
    assertions_pending, assertions_failed) VALUES (%s, %s, %s, %s, %s, %s, %s)''', (date,) + (tests_total,
                                                                                              tests_pending,
                                                                                              tests_failed,
                                                                                              assertions_total,
                                                                                              assertions_pending,
                                                                                              assertions_failed))
    conn.commit()

# Parse json report
report_path = "."
half_name = 'newman'
json_file = max(glob.glob(os.path.join(report_path, f'*{half_name}*.json')), key=os.path.getctime)

(tests_total, tests_pending, tests_failed, assertions_total, assertions_pending,
 assertions_failed) = parse_json_data(json_file)

# Save data
create_allure_report_table(conn)

insert_data_to_allure_report(conn, tests_total, tests_pending, tests_failed, assertions_total,
                             assertions_pending, assertions_failed)

conn.close()