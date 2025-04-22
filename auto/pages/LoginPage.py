# pages/login_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.NAME, "login")
        self.password_input = (By.NAME, "password")

    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username_input)
        ).send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.password_input)
        ).send_keys(password)

    def submit_login(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.password_input)
        ).send_keys(Keys.RETURN)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.submit_login()
