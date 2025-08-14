from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x))))) #function for x

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_image = browser.find_element(By.ID, "treasure")
    x = x_image.get_attribute("valuex") # read x value
    y = calc(x)  # calculate function for x
    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(y)  # enter answer
    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()  # check robot checkbox
    robot_radiobutton = browser.find_element(By.ID, "robotsRule").click()  # check robot rule radiobutton
    submitbutton = browser.find_element(By.CSS_SELECTOR, ".btn").click()  # press submit

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()