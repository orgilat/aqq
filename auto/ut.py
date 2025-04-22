import pytest
import allure
from selenium.webdriver.ie.options import Options as IeOptions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
import time


import sys
import os

def close_alert_if_present(driver):
    try:
        alert = Alert(driver)
        alert.accept()
    except:
        pass

def click_and_wait(driver, xpath, wait_time=10):
    element = WebDriverWait(driver, wait_time).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    element.click()
    time.sleep(0.5)

def navigate_back(driver):
    driver.back()
    time.sleep(0.5)