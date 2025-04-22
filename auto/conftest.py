# File: C:\Users\User\Documents\automation\auto\conftest.py

import sys, os
import pytest
from collections import namedtuple
from selenium import webdriver

DriverWithName = namedtuple('DriverWithName', ['driver', 'browser_name'])

@pytest.fixture
def driver(request):
    browser_name = request.param  # יבוא מבחוץ! לא מוגדר פה.

    if browser_name == "chrome":
        opts = webdriver.ChromeOptions()
        opts.add_argument("--headless")
        opts.add_argument("--disable-gpu")
        inst = webdriver.Chrome(options=opts)

    elif browser_name == "firefox":
        opts = webdriver.FirefoxOptions()
        opts.add_argument("--headless")
        inst = webdriver.Firefox(options=opts)

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    yield DriverWithName(inst, browser_name)
    inst.quit()
