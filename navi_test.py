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

# Navigation w/o login
def test_navigation_top_not_login(driver):
    driver.get("http://localhost/upload//")
    time.sleep(2)
    phone_icon = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "fa-phone"))
    )
    phone_icon.click()
    time.sleep(2)
    assert "http://localhost/upload/index.php?route=information/contact&language=en-gb" in driver.current_url
    dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@class, 'dropdown-toggle') and contains(span, 'My Account')]"))
    )
    dropdown.click()
    time.sleep(2)
    register_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='dropdown-item' and text()='Register']"))
    )
    register_link.click()
    time.sleep(2)
    assert "http://localhost/upload/index.php?route=account/register&language=en-gb" in driver.current_url
    dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@class, 'dropdown-toggle') and contains(span, 'My Account')]"))
    )
    dropdown.click()
    time.sleep(2)
    login_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='dropdown-item' and text()='Login']"))
    )
    login_link.click()
    time.sleep(2)
    assert "http://localhost/upload/index.php?route=account/login&language=en-gb" in driver.current_url
    wish_list_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "wishlist-total"))
    )
    wish_list_link.click()
    time.sleep(2)
    assert "http://localhost/upload/index.php?route=account/login&language=en-gb" in driver.current_url
    shopping_cart_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='Shopping Cart']"))
    )
    shopping_cart_link.click()
    time.sleep(2)
    assert "http://localhost/upload/index.php?route=checkout/cart&language=en-gb" in driver.current_url
    checkout_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='Checkout']"))
    )
    checkout_link.click()
    time.sleep(2)
    assert "http://localhost/upload/index.php?route=checkout/cart&language=en-gb" in driver.current_url

# Login Navigation
def test_navigation_top_login(driver):
    driver.get("http://localhost/upload//")
    time.sleep(2)

    dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@class, 'dropdown-toggle') and contains(span, 'My Account')]"))
    )
    dropdown.click()

    login_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='dropdown-item' and text()='Login']"))
    )
    login_link.click()
    assert "http://localhost/upload/index.php?route=account/login&language=en-gb" in driver.current_url
    
    driver.find_element(By.ID, "input-email").send_keys("sdav@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("123456")
    driver.find_element(By.XPATH, "//button[contains(@class, 'btn btn-primary') and text()='Login']").click()
    time.sleep(3)
    assert "http://localhost/upload/index.php?route=account/account&language=en-gb" in driver.current_url

    # Contact Us
    phone_icon = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "fa-phone"))
    )
    phone_icon.click()
    time.sleep(2)
    assert "http://localhost/upload/index.php?route=information/contact&language=en-gb" in driver.current_url

    # My Account
    dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@class, 'dropdown-toggle') and contains(span, 'My Account')]"))
    )
    dropdown.click()
    time.sleep(2)

    account_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='dropdown-item' and text()='My Account']"))
    )
    account_link.click()
    time.sleep(2)
    assert "http://localhost/upload/index.php?route=account/account&language=en-gb" in driver.current_url

    # Order History
    dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@class, 'dropdown-toggle') and contains(span, 'My Account')]"))
    )
    dropdown.click()
    time.sleep(2)

    order_history_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='dropdown-item' and text()='Order History']"))
    )
    order_history_link.click()
    time.sleep(2)
    assert "http://localhost/upload/index.php?route=account/order&language=en-gb" in driver.current_url

    # Transactions
    dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@class, 'dropdown-toggle') and contains(span, 'My Account')]"))
    )
    dropdown.click()
    time.sleep(2)

    transactions_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='dropdown-item' and text()='Transactions']"))
    )
    transactions_link.click()
    time.sleep(2)
    assert "http://localhost/upload/index.php?route=account/transaction&language=en-gb" in driver.current_url

    # Downloads
    dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@class, 'dropdown-toggle') and contains(span, 'My Account')]"))
    )
    dropdown.click()
    time.sleep(2)

    downloads_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='dropdown-item' and text()='Downloads']"))
    )
    downloads_link.click()
    time.sleep(2)
    assert "http://localhost/upload/index.php?route=account/download&language=en-gb" in driver.current_url

    # Wishlist
    wish_list_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "wishlist-total"))
    )
    wish_list_link.click()
    time.sleep(2)
    assert "http://localhost/upload/index.php?route=account/wishlist&language=en-gb" in driver.current_url

    # Shopping Cart
    shopping_cart_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='Shopping Cart']"))
    )
    shopping_cart_link.click()
    time.sleep(2)
    assert "http://localhost/upload/index.php?route=checkout/cart&language=en-gb" in driver.current_url

    # Checkout
    image_element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//img[@title='Your Store']"))
    )
    image_element.click()

    add_to_cart_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='submit' and @title='Add to Cart']")
        )
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart_button)
    time.sleep(1)

    add_to_cart_button.click()

    checkout_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='Checkout']"))
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", checkout_link)
    time.sleep(5)  

    checkout_link.click()
    time.sleep(2)
    assert "http://localhost/upload/index.php?route=checkout/checkout&language=en-gb" in driver.current_url

# Product Navigation
def test_product_navigation_menu(driver):
    driver.get("http://localhost/upload//")
    time.sleep(2)

    # Desktops
    dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='nav-link dropdown-toggle' and contains(text(), 'Desktops')]"))
    )
    dropdown.click()
    time.sleep(2)

    # PCs
    pc_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='nav-link' and contains(@href, 'path=20_26') and contains(text(), 'PC')]"))
    )
    pc_link.click()
    time.sleep(2)
  
    assert "http://localhost/upload/index.php?route=product/category&language=en-gb&path=20_26" in driver.current_url
    ''' Nhấp chọn "Mac" '''

    dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='nav-link dropdown-toggle' and contains(text(), 'Desktops')]"))
    )
    dropdown.click()
    time.sleep(2)

    # Macs
    mac_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='nav-link' and contains(@href, 'path=20_27') and contains(text(), 'Mac')]"))
    )
    mac_link.click()
    time.sleep(2)

    assert "http://localhost/upload/index.php?route=product/category&language=en-gb&path=20_27" in driver.current_url

    dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='nav-link dropdown-toggle' and contains(text(), 'Desktops')]"))
    )
    dropdown.click()
    time.sleep(2)
    
    # Show All Desktops
    show_all_desktops = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='see-all' and contains(@href, 'path=20') "
                       "and contains(text(), 'Show All Desktops')]"))
    )
    show_all_desktops.click()
    time.sleep(2)

    assert "http://localhost/upload/index.php?route=product/category&language=en-gb&path=20" in driver.current_url

    # "Laptops & Notebooks"
    dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='nav-link dropdown-toggle' and contains(text(), 'Laptops & Notebooks')]"))
    )
    dropdown.click()
    time.sleep(2)

    macs_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='nav-link' and contains(@href, 'path=18_46') and contains(text(), 'Macs')]"))
    )
    macs_link.click()
    time.sleep(2)

    assert "http://localhost/upload/index.php?route=product/category&language=en-gb&path=18_46" in driver.current_url
    ''' Nhấp chọn "Windows" '''

    dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='nav-link dropdown-toggle' and contains(text(), 'Laptops & Notebooks')]"))
    )
    dropdown.click()
    time.sleep(2)

    # Windows
    windows_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='nav-link' and contains(@href, 'path=18_45') "
                       "and contains(text(), 'Windows')]"))
    )
    windows_link.click()
    time.sleep(2)

    assert "http://localhost/upload/index.php?route=product/category&language=en-gb&path=18_45" in driver.current_url

    dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='nav-link dropdown-toggle' and contains(text(), 'Laptops & Notebooks')]"))
    )
    dropdown.click()
    time.sleep(2)
    
    # Show All Laptops & Notebooks
    show_all_laptops_notebooks = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='see-all' and contains(@href, 'path=18') "
                       "and contains(text(), 'Show All Laptops & Notebooks')]"))
    )
    show_all_laptops_notebooks.click()
    time.sleep(2)

    assert "http://localhost/upload/index.php?route=product/category&language=en-gb&path=18" in driver.current_url

    # Components
    dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='nav-link dropdown-toggle' and contains(text(), 'Components')]"))
    )
    dropdown.click()
    time.sleep(2)

    show_all_components = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='see-all' and contains(@href, 'path=25') "
                       "and contains(text(), 'Show All Components')]"))
    )
    show_all_components.click()
    time.sleep(2)

    assert "http://localhost/upload/index.php?route=product/category&language=en-gb&path=25" in driver.current_url
    ''' Danh mục Tablets'''
    # Tablets
    tablets_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='nav-link' and contains(@href, 'path=57') "
                       "and contains(text(), 'Tablets')]"))
    )
    tablets_link.click()
    time.sleep(2)
    assert "http://localhost/upload/index.php?route=product/category&language=en-gb&path=57" in driver.current_url
    ''' Danh mục Software'''
    # Software
    software_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='nav-link' and contains(@href, 'path=17') "
                       "and contains(text(), 'Software')]"))
    )
    software_link.click()
    time.sleep(2)
    assert "http://localhost/upload/index.php?route=product/category&language=en-gb&path=17" in driver.current_url
    ''' Danh mục Phones & PDAs'''
    # Phones & PDAs
    phonespdas_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='nav-link' and contains(@href, 'path=24') "
                       "and contains(text(), 'Phones & PDAs')]"))
    )
    phonespdas_link.click()
    time.sleep(2)
    assert "http://localhost/upload/index.php?route=product/category&language=en-gb&path=24" in driver.current_url
    ''' Danh mục Cameras'''
    # Cameras
    cameras_link = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='nav-link' and contains(@href, 'path=33') "
                       "and contains(text(), 'Cameras')]"))
    )
    cameras_link.click()
    time.sleep(2)
    assert "http://localhost/upload/index.php?route=product/category&language=en-gb&path=33" in driver.current_url
    ''' Danh mục MP3 Players'''
    # MP3 Players
    dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='nav-link dropdown-toggle' and contains(text(), 'MP3 Players')]"))
    )
    dropdown.click()
    time.sleep(2)
    # Show All MP3 Players
    show_all_mp3players = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='see-all' and contains(@href, 'path=34') "
                       "and contains(text(), 'Show All MP3 Players')]"))
    )
    show_all_mp3players.click()
    time.sleep(2)

    assert "http://localhost/upload/index.php?route=product/category&language=en-gb&path=34" in driver.current_url
