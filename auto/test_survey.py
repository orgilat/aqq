import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time


def get_driver():
    options = Options()
    # אם ברצונך לראות את ההתנהגות הגראפית של הדפדפן
    # options.add_argument("--headless=new")  # לבטל את ה‑headless
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(options=options)


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


@allure.epic("Survey Management System")
@allure.feature("UI Testing")
@allure.story("Button Functionality")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("CI", "Headless", "Automation")
def test_survey_buttons():
    driver = get_driver()
    passed, failed = 0, 0

    buttons = [
        {"name": "ניהול הסקר", "xpath": "//a[contains(text(), 'ניהול הסקר')]"},
        {"name": "ניהול סוציומטרי", "xpath": "//a[contains(text(), 'ניהול סוציומטרי')]"},
        {"name": "עונות", "xpath": "//input[contains(@value, 'עונות')]"},
        {"name": "שאלות חובה", "xpath": "//input[contains(@value, 'שאלות חובה')]"},
        {"name": "חוקים לבדיקת שאלונים חריגים", "xpath": "//input[contains(@value, 'חוקים לבדיקת שאלונים חריגים')]"},
        {"name": "חוקים על שאלות", "xpath": "//input[contains(@value, 'חוקים על שאלות')]"},
        {"name": "כללי השתתפות לפי סוג יחידה", "xpath": "//input[contains(@value, 'כללי השתתפות לפי סוג יחידה')]"},
        {"name": "הגדרת השדות שיופיעו בטבלאות", "xpath": "//input[contains(@value, 'הגדרת השדות שיופיעו בטבלאות')]"},
        {"name": "אופציות לסוציומטרי", "xpath": "//input[contains(@value, 'אופציות לסוציומטרי')]"},
        {"name": "הגדרה וניהול סטטוסים לאירועים", "xpath": "//input[contains(@value, 'הגדרה וניהול סטטוסים לאירועים')]"},
        {"name": "סיבות להוספת או הסרת משתתפים באירוע", "xpath": "//input[contains(@value, 'סיבות להוספת או הסרת משתתפים באירוע')]"},
        {"name": "הגדרת שאלונים בהם מותר למחוק נתונים", "xpath": "//input[contains(@value, 'הגדרת שאלונים בהם מותר למחוק נתונים')]"},
        {"name": "רשימת אשכולות לאיגוד קבוצות של היגדים", "xpath": "//input[contains(@value, 'רשימת אשכולות לאיגוד קבוצות של היגדים')]"},
        {"name": "העברת משיבים ממאגר", "xpath": "//input[contains(@value, 'העברת משיבים ממאגר')]"},
        {"name": "ניהול הרשאות משתמשים", "xpath": "//input[contains(@value, 'ניהול הרשאות משתמשים')]"},
        {"name": "של פוטנציאל המשתתפים בסוציומטרי", "xpath": "//input[contains(@value, 'של פוטנציאל המשתתפים בסוציומטרי')]"},
        {"name": "הגדרת חוקי העתקה של נתונים מחושבים לשאלון העזר", "xpath": "//input[contains(@value, 'הגדרת חוקי העתקה של נתונים מחושבים לשאלון העזר')]"},
        {"name": "הגדרת כללים לחוקות חישוב", "xpath": "//input[contains(@value, 'הגדרת כללים לחוקות חישוב')]"},
        {"name": "עריכה שדות במאגר המשיבים", "xpath": "//input[contains(@value, 'עריכה שדות במאגר המשיבים')]"},
        {"name": "ייצוא דוחות אישיים", "xpath": "//input[contains(@value, 'ייצוא דוחות אישיים')]"},
        {"name": "שיוך יחידות לאשכול", "xpath": "//input[contains(@value, 'שיוך יחידות לאשכול')]"},
        {"name": "פלט אישי בתיקיית עובד", "xpath": "//input[contains(@value, 'פלט אישי בתיקיית עובד')]"},
        {"name": "ניהול אירועים", "xpath": "//input[contains(@value, 'ניהול אירועים')]"}
    ]

    try:
        with allure.step("Login to the system"):
            driver.get("https://www.survey.co.il/pms/MMDANEW/default.asp")
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "login")))
            driver.find_element(By.NAME, "login").send_keys("MARINAS")
            driver.find_element(By.NAME, "password").send_keys("Ms123456", Keys.RETURN)

        with allure.step("Navigate to main management page"):
            close_alert_if_present(driver)
            click_and_wait(driver, buttons[0]["xpath"])
            close_alert_if_present(driver)
            click_and_wait(driver, buttons[1]["xpath"])

        for button in buttons[2:23]:
            with allure.step(f"Testing button: {button['name']}"):
                try:
                    close_alert_if_present(driver)
                    click_and_wait(driver, button["xpath"])
                    passed += 1
                    navigate_back(driver)
                except Exception as e:
                    allure.attach(str(e), name=f"Error on button {button['name']}", attachment_type=allure.attachment_type.TEXT)
                    failed += 1
        for button in buttons[23:]:
            if button["name"] == "ניהול אירועים":
                with allure.step("בדיקות פנימיות עבור 'ניהול אירועים'"):
                    close_alert_if_present(driver)
                    events_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, button["xpath"]))
                    )
                    events_button.click()
                    time.sleep(0.5)
                    passed += 1

                with allure.step("לחיצה על 'להקמת אירוע חדש'"):
                    add_event_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(.//span[contains(@class, 'block')])='להקמת אירוע חדש']"))
                    )
                    driver.execute_script("arguments[0].scrollIntoView(true);", add_event_button)
                    time.sleep(1)
                    add_event_button.click()
                    time.sleep(25)
                    passed += 1

                with allure.step("מילוי שם האירוע"):
                    event_name_input = WebDriverWait(driver, 20).until(
                        EC.visibility_of_element_located((By.XPATH, "//div[@class='field floating-label' and @label='שם האירוע']//input"))
                    )
                    event_name_input.send_keys("אירוע לדוגמה")
                    time.sleep(5.5)
                    passed += 1

                with allure.step("בחירת עונת הערכה"):
                    dropdown_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//div[@class='dropdown dropdown-select' and @label='בחר עונת הערכה']//div[contains(@class, 'dropdown-btn')]"))
                    )
                    dropdown_button.click()
                    time.sleep(3)

                    season_option = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//div[@class='dropdown-list']//li//div[@class='list-item']/span[text()='עונת 1']"))
                    )
                    season_option.click()
                    passed += 1
                    time.sleep(3)

                with allure.step("בחירת תאריך התחלה - 18"):
                    calendar_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'dx-dropdowneditor-button') and @aria-label='Select']"))
                    )
                    calendar_button.click()
                    passed += 1
                    time.sleep(1)

                    date_18 = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//td[contains(@class, 'dx-calendar-cell') and not(contains(@class, 'dx-calendar-other-view'))]//span[text()='18']"))
                    )
                    date_18.click()
                    passed += 1
                    time.sleep(2)

                with allure.step("בחירת תאריך סיום - 26"):
                    calendar_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'dx-datebox') and .//span[contains(., 'תאריך סיום')]]//div[contains(@class, 'dx-dropdowneditor-button') and @aria-label='Select']"))
                    )
                    calendar_button.click()
                    passed += 1

                    date_input = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'dx-datebox') and .//span[contains(., 'תאריך סיום')]]//input[@type='text']"))
                    )
                    date_input.send_keys("18-03-2025" + Keys.ENTER)
                    passed += 1
                    time.sleep(6)

                with allure.step("בחירת סוג יחידה - 'מטה'"):
                    unit_dropdown_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//div[@class='dropdown dropdown-select' and @label='הגדרת סוג היחידה לאירוע ']/div[contains(@class, 'dropdown-btn')]"))
                    )
                    unit_dropdown_button.click()

                    unit_option_mathe = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//div[@class='dropdown-list']//li//div[contains(@class, 'list-item')]//span[normalize-space(text())='מטה']"))
                    )
                    unit_option_mathe.click()
                    passed += 2
                    time.sleep(3)

                with allure.step("לחיצה פנימית על הריבוע ליד 'פיקוד 2'"):
                    checkbox_pikud2 = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//li[@data-item-id='249']//div[contains(@class, 'dx-checkbox-container')]"))
                    )
                    checkbox_pikud2.click()
                    passed += 1
                    time.sleep(11)



    finally:
        driver.quit()

    with allure.step(f"Test Summary - Passed: {passed}, Failed: {failed}"):
        assert failed == 0, f"Some tests failed. Passed: {passed}, Failed: {failed}"