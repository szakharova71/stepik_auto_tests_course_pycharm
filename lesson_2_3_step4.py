from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x))))) #function for x

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    magicbutton = browser.find_element(By.CSS_SELECTOR, "[type=submit]").click()

    confirm=browser.switch_to.alert
    confirm.accept()
    #new page
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text  # read x value
    y = calc(x)  # calculate function for x
    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(y)
    submitbutton = browser.find_element(By.CSS_SELECTOR, ".btn").click()  # press submit


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()


