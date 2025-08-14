from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x))))) #function for x

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    expectedpriceis100= WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID, "price"),'$100'))
    bookbutton=browser.find_element(By.ID, "book").click()

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text  # read x value
    y = calc(x)  # calculate function for x
    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(y)
    submitbutton = browser.find_element(By.ID, "solve").click()  # press submit
    #browser.execute_script("return arguments[0].scrollIntoView(true);", submitbutton)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()