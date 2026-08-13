import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import csv
import time
import os
import random

load_dotenv()

CSV_PATH = "emails.csv"
GMAIL_USER = os.getenv("GMAIL_USER")
GMAIL_PASS = os.getenv("GMAIL_PASS")
SUBJECT = "Dedicated link under your pants - Check it out"
BODY = "Hey there! I just wanted to share this dedicated link with you. Check it out when you have a moment! and i hope NETSOL will be happy to see this link and i hope you will like it too. Thanks!"

options = uc.ChromeOptions()
options.add_argument("--start-maximized")
driver = uc.Chrome(options=options, version_main=151)
wait = WebDriverWait(driver, 30)

driver.get("https://mail.google.com")
wait.until(EC.presence_of_element_located((By.ID, "identifierId"))).send_keys(GMAIL_USER)
driver.find_element(By.ID, "identifierNext").click()
time.sleep(random.uniform(2.5, 4))
wait.until(EC.presence_of_element_located((By.NAME, "Passwd"))).send_keys(GMAIL_PASS)
driver.find_element(By.ID, "passwordNext").click()
time.sleep(12)  # extra time for 2FA / loading

emails = []
with open(CSV_PATH, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if row and row[0].strip() and "@" in row[0]:
            emails.append(row[0].strip())

for email in emails:
    compose_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[gh='cm']")))
    compose_btn.click()
    time.sleep(random.uniform(2.5, 4))

    to_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[aria-label='To recipients']")))
    to_field.click()
    time.sleep(random.uniform(0.6, 1.2))
    to_field.send_keys(email)
    time.sleep(random.uniform(0.4, 0.8))
    to_field.send_keys(Keys.ENTER)
    time.sleep(random.uniform(1.0, 1.8))

    subject_field = wait.until(EC.element_to_be_clickable((By.NAME, "subjectbox")))
    subject_field.send_keys(SUBJECT)
    time.sleep(random.uniform(0.8, 1.5))

    body_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[aria-label='Message Body']")))
    body_field.click()
    time.sleep(random.uniform(0.5, 1.0))

    # Type body slowly (more human-like)
    for char in BODY:
        body_field.send_keys(char)
        time.sleep(random.uniform(0.03, 0.09))

    time.sleep(random.uniform(1.5, 2.5))

    send_btn = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@role='button' and contains(@aria-label, 'Send')]")
    ))
    send_btn.click()

    # Longer delay between emails
    time.sleep(random.uniform(8, 14))

print("Done")