from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture
def setup_driver():
    driver=webdriver.Chrome()
    yield driver
    driver.quit()

def test_cookie_clicker(setup_driver):
    setup_driver.get("https://orteil.dashnet.org/cookieclicker/")
    wait = WebDriverWait(setup_driver, 30)
    english_button = wait.until(EC.element_to_be_clickable((By.ID, "langSelect-EN")))
    english_button.click()
    time.sleep(5)
    setup_driver.save_screenshot("language_selected.png")
    big_cookie = wait.until(EC.presence_of_element_located((By.ID, "bigCookie")))
    for i in range(100):
        big_cookie.click()
        time.sleep(0.05)
    time.sleep(10)
    setup_driver.save_screenshot("cookie_clicked.png")
    upgrades = setup_driver.find_elements(By.CLASS_NAME, "crate.upgrade.enabled")
    print(f"Available upgrades: {len(upgrades)}")
    if upgrades:
        upgrades[0].click()
        setup_driver.save_screenshot("screenshots/upgrade_bought.png")
    setup_driver.quit()