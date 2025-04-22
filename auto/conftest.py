# File: C:\Users\User\Documents\automation\auto\conftest.py

import sys, os
import pytest
from collections import namedtuple
from selenium import webdriver

# ────────────────────────────────────────────────────────────────────────────────
# 1) הוספת תיקיית auto (שם נמצאים test_survey.py ו־pages/) ל־PYTHONPATH

# ────────────────────────────────────────────────────────────────────────────────



@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser_name = request.param

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


    inst.quit()
