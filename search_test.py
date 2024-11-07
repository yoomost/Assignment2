import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Fixture to initialize and close the browser driver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
    
# Valid search
def test_search(driver):
    driver.get("http://localhost/upload/index.php?route=account/login&language=en-gb")
    driver.find_element(By.ID, "input-email").send_keys("sdav@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("123456")
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    
    WebDriverWait(driver, 10).until(
            EC.url_contains("route=account/account")
        )
        
    assert "route=account/account" in driver.current_url
    
    driver.find_element(By.NAME, "search").send_keys("Iphone")
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-light.btn-lg").click()
    
    WebDriverWait(driver, 10).until(
        EC.url_contains("route=product/search")
    )

    assert "route=product/search" in driver.current_url
    time.sleep(10)
    
# Number search
def test_search_num(driver):
    driver.get("http://localhost/upload/index.php?route=account/login&language=en-gb")
    driver.find_element(By.ID, "input-email").send_keys("sdav@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("123456")
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    
    WebDriverWait(driver, 10).until(
            EC.url_contains("route=account/account")
        )
        
    assert "route=account/account" in driver.current_url
    
    driver.find_element(By.NAME, "search").send_keys("123.00")
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-light.btn-lg").click()
    
    message_0 = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h1[text()='Search - 123.00']"))
    )
    assert message_0
    
    message_1 = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[text()='Products meeting the search criteria']"))
    )
    assert message_1 
    
    message_2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'There is no product that matches the search criteria.')]"))
    )
    assert message_2.text
    time.sleep(2)
    
    
# Special characters search
def test_search_special(driver):
    driver.get("http://localhost/upload/index.php?route=account/login&language=en-gb")
    driver.find_element(By.ID, "input-email").send_keys("sdav@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("123456")
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    
    WebDriverWait(driver, 10).until(
            EC.url_contains("route=account/account")
        )
        
    assert "route=account/account" in driver.current_url
    
    driver.find_element(By.NAME, "search").send_keys("@$#%^#$%*")
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-light.btn-lg").click()
    
    message_0 = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h1[text()='Search - @$#%^#$%*']"))
    )
    assert message_0
    
    message_1 = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[text()='Products meeting the search criteria']"))
    )
    assert message_1 
    
    message_2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'There is no product that matches the search criteria.')]"))
    )
    assert message_2.text
    time.sleep(2)
    

# Empty search
def test_search_empty(driver):
    driver.get("http://localhost/upload/index.php?route=account/login&language=en-gb")
    driver.find_element(By.ID, "input-email").send_keys("sdav@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("123456")
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    
    WebDriverWait(driver, 10).until(
            EC.url_contains("route=account/account")
        )
        
    assert "route=account/account" in driver.current_url
    
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-light.btn-lg").click()
    
    message_0 = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h1[text()='Search']"))
    )
    assert message_0
    
    message_1 = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[text()='Products meeting the search criteria']"))
    )
    assert message_1 
    
    message_2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'There is no product that matches the search criteria.')]"))
    )
    assert message_2.text
    time.sleep(2)