from pages.LoginPage import LoginPage

import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
import time
from ut import close_alert_if_present, click_and_wait, navigate_back
# הוספת תיקיית הפרויקט ל-Python path






@allure.epic("Survey Management System")
@allure.feature("UI Testing")
@allure.story("Button Functionality")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("CI", "Headless", "Automation")
@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
def test_survey_buttons(driver):
    passed, failed = 0, 0
    browser_name = driver.browser_name  # הוצא את השם
    driver = driver.driver  # הוצא את הדרייבר האמיתי

    # הוספת שם הדפדפן לדינמיקה של Allure
    allure.dynamic.description(f"Test running on {browser_name.capitalize()}")

    allure_results_dir = f"allure-results_{browser_name}"

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
        #{"name": "הגדרת שאלונים בהם מותר למחוק נתונים", "xpath": "//input[contains(@value, 'הגדרת שאלונים בהם מותר למחוק נתונים')]"},
        #{"name": "רשימת אשכולות לאיגוד קבוצות של היגדים", "xpath": "//input[contains(@value, 'רשימת אשכולות לאיגוד קבוצות של היגדים')]"},
        #{"name": "העברת משיבים ממאגר", "xpath": "//input[contains(@value, 'העברת משיבים ממאגר')]"},
        #"name": "ניהול הרשאות משתמשים", "xpath": "//input[contains(@value, 'ניהול הרשאות משתמשים')]"},
        #"name": "של פוטנציאל המשתתפים בסוציומטרי", "xpath": "//input[contains(@value, 'של פוטנציאל המשתתפים בסוציומטרי')]"},
        {"name": "הגדרת חוקי העתקה של נתונים מחושבים לשאלון העזר", "xpath": "//input[contains(@value, 'הגדרת חוקי העתקה של נתונים מחושבים לשאלון העזר')]"},
        {"name": "הגדרת כללים לחוקות חישוב", "xpath": "//input[contains(@value, 'הגדרת כללים לחוקות חישוב')]"},
        {"name": "עריכה שדות במאגר המשיבים", "xpath": "//input[contains(@value, 'עריכה שדות במאגר המשיבים')]"},
        {"name": "ייצוא דוחות אישיים", "xpath": "//input[contains(@value, 'ייצוא דוחות אישיים')]"},
        {"name": "שיוך יחידות לאשכול", "xpath": "//input[contains(@value, 'שיוך יחידות לאשכול')]"},
        {"name": "פלט אישי בתיקיית עובד", "xpath": "//input[contains(@value, 'פלט אישי בתיקיית עובד')]"},
        {"name": "ניהול אירועים", "xpath": "//input[contains(@value, 'ניהול אירועים')]"}
    ]

    try:
        driver.get("https://www.survey.co.il/pms/MMDANEW/default.asp")
        login_page = LoginPage(driver)
        login_page.login("MARINAS", "Ms123456")
        with allure.step(f"Navigate to main management page using {browser_name.capitalize()}"):
            manage_survey_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, buttons[0]["xpath"]))
            )
            ActionChains(driver).move_to_element(manage_survey_button).perform()
            time.sleep(0.5)
            close_alert_if_present(driver)
            click_and_wait(driver, buttons[1]["xpath"])
            allure.attach(driver.current_url, name="כתובת האתר במסך סוציומטרי", attachment_type=allure.attachment_type.TEXT)

        for button in buttons[2:22]:
            with allure.step(f"Testing button: {button['name']} on {browser_name.capitalize()}"):
                try:
                    close_alert_if_present(driver)
                    click_and_wait(driver, button["xpath"])
                    passed += 1
                    navigate_back(driver)
                except Exception as e:
                    allure.attach(str(e), name=f"Error on button {button['name']}", attachment_type=allure.attachment_type.TEXT)
                    failed += 1
              
        with allure.step(f"בדיקות פנימיות עבור 'ניהול אירועים' ב-{browser_name.capitalize()}"):
            close_alert_if_present(driver)
            events_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//input[contains(@value, 'ניהול אירועים')]"))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", events_button)
            events_button.click()
            time.sleep(0.5)
            passed += 1

            with allure.step(f"לחיצה על 'להקמת אירוע חדש' ב-{browser_name.capitalize()}"):
                add_event_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(.//span[contains(@class, 'block')])='להקמת אירוע חדש']"))
                )
                driver.execute_script("arguments[0].scrollIntoView(true);", add_event_button)
                time.sleep(1)
                add_event_button.click()
                time.sleep(25)
                passed += 1

            with allure.step(f"מילוי שם האירוע ב-{browser_name.capitalize()}"):
                    event_name_input = WebDriverWait(driver, 20).until(
                        EC.visibility_of_element_located((By.XPATH, "//div[@class='field floating-label' and @label='שם האירוע']//input"))
                    )
                    event_name_input.send_keys("אירוע לדוגמה")
                    time.sleep(5.5)
                    passed += 1

            with allure.step(f"בחירת עונת הערכה ב-{browser_name.capitalize()}"):
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

            with allure.step(f"בחירת תאריך התחלה - 18 ב-{browser_name.capitalize()}"):
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
                    time.sleep(4)

            with allure.step(f"בחירת תאריך סיום - 26 ב-{browser_name.capitalize()}"):
                    calendar_button = WebDriverWait(driver, 20).until(
                        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'dx-datebox') and .//span[contains(., 'תאריך סיום')]]//div[contains(@class, 'dx-dropdowneditor-button') and @aria-label='Select']"))
                    )
                    calendar_button.click()
                    passed += 1

                    date_input = WebDriverWait(driver, 20).until(
                        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'dx-datebox') and .//span[contains(., 'תאריך סיום')]]//input[@type='text']"))
                    )
                    date_input.send_keys("18-03-2025" + Keys.ENTER)
                    passed += 1
                    time.sleep(6)

            with allure.step(f"בחירת סוג יחידה - 'מטה' ב-{browser_name.capitalize()}"):
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

            with allure.step(f"לחיצה פנימית על הריבוע ליד 'פיקוד 2' ב-{browser_name.capitalize()}"):
                    checkbox_pikud2 = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//li[@data-item-id='249']//div[contains(@class, 'dx-checkbox-container')]"))
                    )
                    checkbox_pikud2.click()
                    passed += 1
                    time.sleep(11)


                    

    finally:
        driver.quit()

    with allure.step(f"Test Summary - Passed: {passed}, Failed: {failed} on {browser_name.capitalize()}"):
        assert failed == 0, f"Some tests failed. Passed: {passed}, Failed: {failed}" if failed > 0 else f"All tests passed! Passed: {passed}, Failed: {failed}"
