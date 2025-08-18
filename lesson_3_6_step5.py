from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import os
import pytest
import math

def answer():
    return str(math.log(int(time.time())))

pagelist=[236895,236896,236897,236898,236899,236903,236904,236905]

@pytest.mark.parametrize('pagenumber',pagelist)
def test_login(browser,pagenumber):
    link=f"https://stepik.org/lesson/{pagenumber}/step/1"
    browser.get(link)
    login = os.getenv("stepik_login")
    pw = os.getenv("stepik_pw")
    loginbutton = browser.find_element(By.CSS_SELECTOR, ".navbar__auth_login").click()
    loginelement = browser.find_element(By.NAME, "login")
    pwelement = browser.find_element(By.NAME, "password")
    loginelement.send_keys(login)
    pwelement.send_keys(pw)
    submitbtn=browser.find_element(By.CLASS_NAME, "button_with-loader").click()

    #make sure user is logged in
    assert browser.find_element(By.CSS_SELECTOR,".navbar__profile-img"),"profile image not visible"
    try:
        resetanswerbtn= browser.find_element(By.CSS_SELECTOR,".again-btn").click()
        try:
            confirm = browser.find_element(By.CLASS_NAME, "modal-popup__container")
            confirm_button = confirm.find_element(By.CSS_SELECTOR, "button:first-child").click()
        except NoSuchElementException:
            print('OK button not found')
    except NoSuchElementException:
        print("RESET button not found")
    finally:
        answerelement = browser.find_element(By.CSS_SELECTOR, ".ember-text-area")
        answerelement.clear()
        answerelement.send_keys(answer())
        submitanswerbth = browser.find_element(By.CLASS_NAME, "submit-submission").click()

        feedbackelement=browser.find_element(By.CLASS_NAME,"smart-hints__hint")
        feedbacktext=feedbackelement.text
        assert feedbacktext=="Correct!", f"incorrect answer entered for page {pagenumber}, collecting the text: {feedbacktext}"