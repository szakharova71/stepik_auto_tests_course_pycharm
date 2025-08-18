from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def test_login(browser):
    link="https://stepik.org/lesson/236895/step/1"
    browser.get(link)
    login=os.getenv("stepik_login")
    pw=os.getenv("stepik_pw")
    loginbutton = browser.find_element(By.CSS_SELECTOR, ".navbar__auth_login").click()
    loginelement=browser.find_element(By.NAME,"login")
    pwelement=browser.find_element(By.NAME,"password")
    loginelement.send_keys(login)
    pwelement.send_keys(pw)
    submitbth=WebDriverWait(browser,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"[type=submit]")))
    submitbth.click()
    #make sure user is logged in
    assert WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,\
                                            ".navbar__profile-img"))),"profile image not visible"
    time.sleep(2)