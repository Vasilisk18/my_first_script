import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


chromeOptions = webdriver.ChromeOptions()

chromeOptions.binary_location = 'C:/Users/User/AppData/Local/Yandex/YandexBrowser/Application/browser.exe'
service = Service(executable_path=r"C:/yandexdriver/yandexdriver.exe")
browser = webdriver.Chrome(service=service, options=chromeOptions)

try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "$100"))
    button = browser.find_element(By.CSS_SELECTOR, "#book")
    button.click()

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)

    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

    print(browser.switch_to.alert.text.split(': ')[-1])

finally:
    time.sleep(30)
    browser.quit()
