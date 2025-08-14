from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class TestRegister(unittest.TestCase):
    def test_checkreg1 (self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        fn = browser.find_element(By.CSS_SELECTOR, ".first[required]")
        fn.send_keys("42")
        ln = browser.find_element(By.CSS_SELECTOR, ".second[required]")
        ln.send_keys("42")
        email = browser.find_element(By.CSS_SELECTOR, ".third[required]")
        email.send_keys("42")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text1 текст из элемента welcome_text_elt
        welcome_text1 = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text1, "Congratulations! You have successfully registered!", "Error message")

    def test_checkreg2 (self): #expected to fail
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        fn = browser.find_element(By.CSS_SELECTOR, ".first[required]")
        fn.send_keys("42")
        ln = browser.find_element(By.CSS_SELECTOR, ".second[required]")
        ln.send_keys("42")
        email = browser.find_element(By.CSS_SELECTOR, ".third[required]")
        email.send_keys("42")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text2 текст из элемента welcome_text_elt
        welcome_text2 = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text2, "Congratulations! You have successfully registered!", "Error message")

if __name__ == '__main__':
    unittest.main()

