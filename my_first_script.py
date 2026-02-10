import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import math
from faker import Faker

fake = Faker()
chromeOptions = webdriver.ChromeOptions()

chromeOptions.binary_location = 'C:/Users/User/AppData/Local/Yandex/YandexBrowser/Application/browser.exe'
service = Service(executable_path=r"C:/yandexdriver/yandexdriver.exe")
browser = webdriver.Chrome(service=service, options=chromeOptions)

browser.get("http://suninjuly.github.io/huge_form.html")

try:
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        word = fake.word()
        element.send_keys(word)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
