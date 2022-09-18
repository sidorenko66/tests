import configparser
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


config = configparser.ConfigParser()
config.read("settings.ini")
yandex_login = config["Yandex"]["yandex_login"]
yandex_password = config["Yandex"]["yandex_password"]


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://passport.yandex.ru/auth")
        sleep(3)
        self.assertIn("Авторизация", driver.title)
        elem = driver.find_element("name", "login")
        elem.send_keys(yandex_login)
        sleep(1)
        elem.send_keys(Keys.RETURN)
        sleep(3)
        self.assertIn("Авторизация", driver.title)
        elem = driver.find_element("name", "passwd")
        elem.send_keys(yandex_password)
        sleep(1)
        elem.send_keys(Keys.RETURN)
        sleep(3)
        h1 = driver.find_element(By.TAG_NAME, "h1")
        self.assertIn("Безопасный вход", h1.text)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
