from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    num1=browser.find_element(By.ID, "num1")#get element
    num2=browser.find_element(By.ID, "num2")
    x=int(num1.text)#get element text as number
    y=int(num2.text)
    sum=str(x+y) #get sun as str
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sum)
    submitbutton = browser.find_element(By.CSS_SELECTOR, ".btn").click()  # press submit

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()