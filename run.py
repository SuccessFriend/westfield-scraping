import csv
from selenium.webdriver.common.by import By
import time
from seleniumbase import Driver
from selenium.webdriver.support.ui import Select
import random

driver = Driver(uc=True)

header = ["Company Name", "Company Type", "Description"]
with open('result.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(header)

driver.get("https://www.alchemy.com/best/blockchain-auditing-companies")

content_boxs = driver.find_elements(By.XPATH, '/html/body/main/div/div[2]/section/div/ul/li')
for content_box in content_boxs:
    try:
        company_title = content_box.find_elements(By.CLASS_NAME, 'gap-4')[0].text
    except:
        company_title = ""
    print("name : ", company_title)
    try:
        company_types = content_box.find_elements(By.CSS_SELECTOR, 'div.gap-1 span')
        company_type = company_types[len(company_types)-1].text
    except:
        company_type = ""
    try:
        company_desc = content_box.find_elements(By.CLASS_NAME, 'font-paragraph-size-300-medium')[0].text
    except:
        company_desc = ""

    result = [company_title, company_type, company_desc]
    with open('result.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(result)


driver.quit()