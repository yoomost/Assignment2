import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# Register
def test_valid_register(driver):
    driver.get("http://localhost/upload/index.php?route=account/register&language=en-gb")
    driver.find_element(By.ID, "input-firstname").send_keys("zxcv")
    driver.find_element(By.ID, "input-lastname").send_keys("zxcv")
    driver.find_element(By.ID, "input-email").send_keys("zxcv@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("123456")
    time.sleep(3)
    agree_btn = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "input[name='agree']"))
    )
    agree_btn.click()
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    time.sleep(3)
    assert "index.php?route=account/success" in driver.current_url

# Login
def test_valid_login(driver):
    driver.get("http://localhost/upload/index.php?route=account/login&language=en-gb")
    driver.find_element(By.ID, "input-email").send_keys("sdav@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("123456")
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    time.sleep(3)
    assert "index.php?route=account/account&language=en-gb" in driver.current_url

# Logout
def test_valid_logout(driver):
    driver.get("http://localhost/upload/index.php?route=account/login&language=en-gb")
    driver.find_element(By.ID, "input-email").send_keys("sdav@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("123456")
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    time.sleep(2)
    dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@class, 'dropdown-toggle') and contains(span, 'My Account')]"))
    )
    dropdown.click()
    time.sleep(1)
    logout = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='dropdown-item' and text()='Logout']"))
    )
    logout.click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "a.btn.btn-primary").click()
    assert "index.php?route=common/home&language=en-gb" in driver.current_url
    time.sleep(3)