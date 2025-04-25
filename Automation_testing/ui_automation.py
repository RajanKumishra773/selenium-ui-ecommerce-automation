import time
import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import (
    NoSuchElementException, TimeoutException, ElementClickInterceptedException,
    ElementNotInteractableException, WebDriverException
)
from webdriver_manager.chrome import ChromeDriverManager


def setup_driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://practice.automationtesting.in/")
    return driver


def register_user(driver, email, password):
    try:
        driver.find_element(By.LINK_TEXT, "My Account").click()
        time.sleep(2)
        driver.find_element(By.ID, "reg_email").clear()
        driver.find_element(By.ID, "reg_password").clear()
        driver.find_element(By.ID, "reg_email").send_keys(email)
        driver.find_element(By.ID, "reg_password").send_keys(password)
        driver.find_element(By.NAME, "register").click()
        time.sleep(3)

        if "An account is already registered" in driver.page_source:
            print("⚠️ Already registered, logging in instead...")
            driver.find_element(By.ID, "username").clear()
            driver.find_element(By.ID, "password").clear()
            driver.find_element(By.ID, "username").send_keys(email)
            driver.find_element(By.ID, "password").send_keys(password)
            driver.find_element(By.NAME, "login").click()
            time.sleep(3)
        else:
            print("✅ Registration successful")

    except Exception as e:
        print("❗ Registration/Login Error:", e)
        traceback.print_exc()


def clear_cart(driver):
    driver.find_element(By.CLASS_NAME, "wpmenucart-contents").click()
    time.sleep(2)
    while True:
        try:
            remove_buttons = driver.find_elements(By.CLASS_NAME, "remove")
            if not remove_buttons:
                break
            remove_buttons[0].click()
            time.sleep(2)
        except NoSuchElementException:
            break
    try:
        if "Your cart is currently empty" in driver.page_source:
            print("🧹 Cart cleared successfully before test run.")
    except Exception:
        print("⚠️ Could not verify cart status.")


def add_product_to_cart(driver, product_index=0):
    driver.find_element(By.LINK_TEXT, "Shop").click()
    time.sleep(2)
    driver.find_elements(By.CSS_SELECTOR, ".products .button")[product_index].click()
    time.sleep(2)
    print(f"🛒 Product {product_index + 1} added to cart")


def remove_product_from_cart(driver):
    driver.find_element(By.CLASS_NAME, "wpmenucart-contents").click()
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "remove").click()
    time.sleep(3)
    try:
        empty_cart = driver.find_element(By.CSS_SELECTOR, ".cart-empty")
        if "Your cart is currently empty" in empty_cart.text:
            print("🧹 Cart is empty after removing product")
    except NoSuchElementException:
        print("❌ Could not verify empty cart")


def checkout(driver, email):
    driver.find_element(By.CLASS_NAME, "wpmenucart-contents").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".checkout-button.button.alt.wc-forward").click()
    time.sleep(2)
    driver.find_element(By.ID, "billing_first_name").send_keys("Rajan")
    driver.find_element(By.ID, "billing_last_name").send_keys("Mishra")
    driver.find_element(By.ID, "billing_address_1").send_keys("123 Test Street")
    driver.find_element(By.ID, "billing_city").send_keys("Test City")
    driver.find_element(By.ID, "billing_postcode").send_keys("12345")
    driver.find_element(By.ID, "billing_phone").send_keys("1234567890")
    driver.find_element(By.ID, "billing_email").send_keys(email)
    time.sleep(2)
    driver.find_element(By.ID, "place_order").click()
    time.sleep(3)
    print("✅ Order placed successfully")


if __name__ == '__main__':
    email = "test_Rajan123456@gmail.com"
    password = "P123a456@word"

    try:
        driver = setup_driver()

        print("--- Positive Test Flow ---")
        register_user(driver, email, password)
        clear_cart(driver)
        add_product_to_cart(driver, 0)
        remove_product_from_cart(driver)
        add_product_to_cart(driver, 1)
        checkout(driver, email)

    except NoSuchElementException as e:
        print("❌ Element not found:", e)
    except TimeoutException as e:
        print("⏳ Timeout occurred:", e)
    except ElementClickInterceptedException as e:
        print("🚫 Element click intercepted:", e)
    except ElementNotInteractableException as e:
        print("🛑 Element not interactable:", e)
    except WebDriverException as e:
        print("⚠️ WebDriver error:", e)
    except Exception as e:
        print("❗ Unexpected error occurred:", e)
        traceback.print_exc()
    finally:
        driver.quit()
        print("🚪 Browser closed")
