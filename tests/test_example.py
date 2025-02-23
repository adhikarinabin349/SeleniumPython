import pytest
from selenium import webdriver
from pages.login_page import LoginPage
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pages')))

from pages.login_page import LoginPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://example.com/login")  # Replace with actual URL
    yield driver
    driver.quit()

def test_login(driver):
    login_page = LoginPage(driver)
    login_page.enter_username("testuser")
    login_page.enter_password("password123")
    login_page.click_login()
    assert "dashboard" in driver.current_url