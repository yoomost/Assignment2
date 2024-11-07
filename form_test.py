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

#Form Submission
def test_valid_form_submission(driver):
    driver.get("http://localhost/upload//")

    phone_icon = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "fa-phone"))
    )
    phone_icon.click()
    assert "http://localhost/upload/index.php?route=information/contact&language=en-gb" in driver.current_url

    driver.find_element(By.ID, "input-name").send_keys("sdav")
    driver.find_element(By.ID, "input-email").send_keys("sdav@gmail.com")
    driver.find_element(By.ID, "input-enquiry").send_keys("Your product is very good!")

    submit_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='submit' and @class='btn btn-primary' and text()='Submit']"))
    )
    # Cuộn đến vị trí của nút "Submit" để đảm bảo nó hiển thị đầy đủ
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    time.sleep(1)
    submit_button.click()
    time.sleep(3)
    assert "http://localhost/upload/index.php?route=information/contact.success&language=en-gb" in driver.current_url

#Form submission invalid
def test_invalid_form_submission(driver):
    driver.get("http://localhost/upload//")

    phone_icon = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "fa-phone"))
    )
    phone_icon.click()
    assert "http://localhost/upload/index.php?route=information/contact&language=en-gb" in driver.current_url

    driver.find_element(By.ID, "input-name").send_keys("sdav")
    # Nhập email không hợp lệ
    driver.find_element(By.ID, "input-email").send_keys("sdav@gma*il.com")
    # Nhập Enquiry không hợp lệ
    driver.find_element(By.ID, "input-enquiry").send_keys("alo123@")
    submit_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='submit' and @class='btn btn-primary' and text()='Submit']"))
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    time.sleep(1) 
    submit_button.click()
    time.sleep(3)

    error_message = driver.find_element(By.ID, "error-email").text
    assert "E-Mail Address does not appear to be valid!" in error_message
    error_message = driver.find_element(By.ID, "error-enquiry").text
    assert "Enquiry must be between 10 and 3000 characters!" in error_message

#Form submission empty
def test_form_submission_empty(driver):
    driver.get("http://localhost/upload//")

    phone_icon = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "fa-phone"))
    )
    phone_icon.click()
    assert "http://localhost/upload/index.php?route=information/contact&language=en-gb" in driver.current_url
    driver.find_element(By.ID, "input-name").clear()
    driver.find_element(By.ID, "input-email").clear()
    driver.find_element(By.ID, "input-enquiry").clear()

    submit_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='submit' and @class='btn btn-primary' and text()='Submit']"))
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    time.sleep(1)
    submit_button.click()
    time.sleep(3)

    error_message = driver.find_element(By.ID, "error-name").text
    assert "Name must be between 3 and 32 characters!" in error_message
    error_message = driver.find_element(By.ID, "error-email").text
    assert "E-Mail Address does not appear to be valid!" in error_message
    error_message = driver.find_element(By.ID, "error-enquiry").text
    assert "Enquiry must be between 10 and 3000 characters!" in error_message