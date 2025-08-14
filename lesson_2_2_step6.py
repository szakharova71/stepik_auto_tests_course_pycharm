from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text  # read x value
    y = calc(x)  # calculate function for x

    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer) #scroll to answer
    answer.send_keys(y)  # enter answer

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button) #scroll to button

    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()  # check robot checkbox
    robot_radiobutton = browser.find_element(By.ID, "robotsRule").click()  # check robot rule radiobutton
    button.click()  # press submit

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()