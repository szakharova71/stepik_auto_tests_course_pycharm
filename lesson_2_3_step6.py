from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x))))) #function for x

try:
    link = "https://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    flyingbutton = browser.find_element(By.CSS_SELECTOR, "[type=submit]").click() #press flying button

    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window) #switch to 2nd window

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