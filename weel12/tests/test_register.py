import os
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = os.getenv("APP_URL", "http://127.0.0.1:5000")


@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()


def test_registration_page_opens(browser):
    browser.get(BASE_URL)

    assert browser.title == "Register"

    assert browser.find_element(
        By.ID, "submit"
    ).is_displayed()


def test_empty_username(browser):
    browser.get(BASE_URL)

    browser.find_element(
        By.ID, "password"
    ).send_keys("test123")

    browser.find_element(
        By.ID, "submit"
    ).click()

    alert = WebDriverWait(browser, 5).until(
        EC.alert_is_present()
    )

    assert alert.text == "Username cannot be empty"
    alert.accept()


def test_empty_password(browser):
    browser.get(BASE_URL)

    browser.find_element(
        By.ID, "name"
    ).send_keys("Ranjitha")

    browser.find_element(
        By.ID, "submit"
    ).click()

    alert = WebDriverWait(browser, 5).until(
        EC.alert_is_present()
    )

    assert alert.text == "Password cannot be empty"
    alert.accept()


def test_valid_registration(browser):
    browser.get(BASE_URL)

    browser.find_element(
        By.ID, "name"
    ).send_keys("Ranjitha")

    browser.find_element(
        By.ID, "password"
    ).send_keys("test123")

    browser.find_element(
        By.ID, "submit"
    ).click()

    WebDriverWait(browser, 5).until(
        EC.title_contains("Registration Successful")
    )

    message = browser.find_element(
        By.ID, "success-message"
    ).text

    assert "Registration successful for Ranjitha" in message