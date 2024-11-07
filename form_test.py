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

# Kiểm tra chức năng NỘP BIỂU MẪU
# TC10: Kiểm thử nộp biểu mẫu liên hệ với thông tin hợp lệ
def test_valid_form_submission_contact_us(driver):
    driver.get("http://localhost/upload//")
    # Chờ và nhấp vào "fa-solid fa-phone"
    phone_icon = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "fa-phone"))
    )
    phone_icon.click()
    assert "http://localhost/upload/index.php?route=information/contact&language=en-gb" in driver.current_url
    # Nhập Your Name vào trường nhập liệu, ở đây là "Van Phu Tung"
    driver.find_element(By.ID, "input-name").send_keys("sdav")
    # Nhập email vào trường nhập liệu, ở đây là "DCT121C5user1@gmail.com"
    driver.find_element(By.ID, "input-email").send_keys("sdav@gmail.com")
    # Nhập Enquiry vào trường nhập liệu, ở đây là "Your product is very good!"
    driver.find_element(By.ID, "input-enquiry").send_keys("Your product is very good!")
    # Nhấp vào nút "Submit"
    submit_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='submit' and @class='btn btn-primary' and text()='Submit']"))
    )
    # Cuộn đến vị trí của nút "Submit" để đảm bảo nó hiển thị đầy đủ
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    time.sleep(1)  # Đợi một chút sau khi cuộn
    submit_button.click()
    time.sleep(3)
    assert "http://localhost/upload/index.php?route=information/contact.success&language=en-gb" in driver.current_url

def test_invalid_form_submission_contact_us(driver):
    driver.get("http://localhost/upload//")
    # Chờ và nhấp vào "fa-solid fa-phone"
    phone_icon = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "fa-phone"))
    )
    phone_icon.click()
    assert "http://localhost/upload/index.php?route=information/contact&language=en-gb" in driver.current_url
    # Nhập Your Name vào trường nhập liệu, ở đây là "VanTung"
    driver.find_element(By.ID, "input-name").send_keys("sdav")
    # Nhập email không hợp lệ vào trường nhập liệu, ở đây là "DCT121C5user1@gma*il.com"
    driver.find_element(By.ID, "input-email").send_keys("sdav@gma*il.com")
    # Nhập Enquiry không hợp lệ (nằm ngoài 10-3000 ký tự) vào trường nhập liệu, ở đây là "alo123@"
    driver.find_element(By.ID, "input-enquiry").send_keys("alo123@")
    # Nhấp vào nút "Submit"
    submit_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='submit' and @class='btn btn-primary' and text()='Submit']"))
    )
    # Cuộn đến vị trí của nút "Submit" để đảm bảo nó hiển thị đầy đủ
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    time.sleep(1)  # Đợi một chút sau khi cuộn
    submit_button.click()
    time.sleep(3)
    # Thông báo lỗi xuất hiện
    # Xác nhận tính chính xác của thông báo lỗi
    error_message = driver.find_element(By.ID, "error-email").text
    assert "E-Mail Address does not appear to be valid!" in error_message
    error_message = driver.find_element(By.ID, "error-enquiry").text
    assert "Enquiry must be between 10 and 3000 characters!" in error_message

def test_form_submission_contact_us_with_empty_informationform(driver):
    driver.get("http://localhost/upload//")
    # Chờ và nhấp vào "fa-solid fa-phone"
    phone_icon = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "fa-phone"))
    )
    phone_icon.click()
    assert "http://localhost/upload/index.php?route=information/contact&language=en-gb" in driver.current_url
    # Để trống Your Name
    driver.find_element(By.ID, "input-name").clear()
    # Để trống địa chỉ email
    driver.find_element(By.ID, "input-email").clear()
    # Để trống Enquiry
    driver.find_element(By.ID, "input-enquiry").clear()
    # Nhấp vào nút "Submit"
    submit_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='submit' and @class='btn btn-primary' and text()='Submit']"))
    )
    # Cuộn đến vị trí của nút "Submit" để đảm bảo nó hiển thị đầy đủ
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    time.sleep(1)  # Đợi một chút sau khi cuộn
    submit_button.click()
    time.sleep(3)
    # Thông báo lỗi xuất hiện
    # Xác nhận tính chính xác của thông báo lỗi
    error_message = driver.find_element(By.ID, "error-name").text
    assert "Name must be between 3 and 32 characters!" in error_message
    error_message = driver.find_element(By.ID, "error-email").text
    assert "E-Mail Address does not appear to be valid!" in error_message
    error_message = driver.find_element(By.ID, "error-enquiry").text
    assert "Enquiry must be between 10 and 3000 characters!" in error_message