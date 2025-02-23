# SeleniumPython
Scalable Selenium Test Repository using Python. This repository contains a reusable and maintainable test framework for web applications using Selenium and Python. It’s designed for automated browser testing with easy integration with GitHub Actions for continuous integration (CI). The structure of this repository allows you to add tests for any web application and scale as necessary.

## Overview

This framework uses Selenium WebDriver to automate web browser actions and pytest for running and organizing tests. The framework is built with scalability in mind, which means that as your test suite grows, the framework remains easy to extend and maintain.

## Key Features:
	•	Selenium WebDriver: Automates browsers to interact with web applications.
	•	pytest: Test runner for easy execution, reporting, and organizing tests.
	•	Reusable Code: Structure designed for reusability (e.g., page object model).
	•	Continuous Integration: GitHub Actions integration for CI pipelines.
	•	Modular Design: Easy to add new tests and extend functionality.

## Clone the Repository
     git clone repo

# Installation
 - Install Python
 - Then:  touch requirements.txt
 - echo "selenium" >> requirements.txt
    echo "pytest" >> requirements.txt
    echo "pytest-html" >> requirements.txt
 - python3 -m pip install -r requirements.txt

 ## Set Up Python Environment
 	1.	Ensure you have Python 3.9+ installed. You can check your Python version with: python --version
    2. Create a Virtual Environment:
        In the root folder of the project, create and activate a virtual environment:
        python3 -m venv venv
        source venv/bin/activate   # On macOS/Linux
        venv\Scripts\activate      # On Windows
    3.	Install Dependencies:
        Run: pip install -r requirements.txt



## WebDriver Installation

To run the tests with Selenium, you need to install a WebDriver (e.g., ChromeDriver for Google Chrome):
	1.	Download the correct version of ChromeDriver:
	•	ChromeDriver download link
	2.	Ensure it’s in your system PATH, or specify the path directly in your tests.

## How to Write Tests
	1.	Page Object Model: All page-related actions should be encapsulated inside classes located in the pages/ folder. This keeps your test code organized and reusable.

# Test Example 
- Inside tests folder
import pytest
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # Or another browser of your choice
    driver.get("https://example.com/login")
    yield driver
    driver.quit()

def test_login(driver):
    login_page = LoginPage(driver)
    login_page.enter_username("testuser")
    login_page.enter_password("password123")
    login_page.click_login()
    assert "dashboard" in driver.current_url

# Run the test using: pytest

## Scaling the Framework

As your application and test coverage grow, you can easily scale this framework:
	1.	Add More Page Objects: For every page of your application, create a new class inside the pages/ folder. Each page should represent actions that can be performed on that page (e.g., filling out a form, clicking a button).
	2.	Add More Tests: Add more test files in the tests/ folder. Each file can focus on testing a specific feature of the web application.
	3.	Data-Driven Testing: Use external data (e.g., from a CSV or Excel file) to drive tests. This allows you to test the same functionality with different inputs.
	4.	Parallel Test Execution: You can integrate pytest-xdist to run tests in parallel to speed up the test execution time as your test suite grows.
	5.	Cross-Browser Testing: For cross-browser testing, you can extend the WebDriver setup to use different browsers like Firefox, Edge, etc.

## Integration with GitHub Actions

You can easily set up continuous integration (CI) with GitHub Actions to automatically run tests on every push and pull request. Follow these steps:
	- Create a .github/workflows/ci.yml file 

## Useful Document to google
	•	Selenium Documentation
	•	pytest Documentation
	•	ChromeDriver Downloads
	•	GitHub Actions Documentation


## Why This Framework Is Useful

1. Reusability and Maintainability:

The Page Object Model (POM) design pattern ensures that you can reuse code and separate concerns (test logic and page actions). As your test suite grows, the codebase remains organized and maintainable.

2. Scalable:

You can scale the framework by adding more test cases and page objects without worrying about performance or complexity. The modular design ensures you can add more tests as your application grows.

3. Integration with CI/CD:

By integrating with GitHub Actions, you can automate the process of running tests with every code push or pull request. This ensures your application is always tested and verified before merging any changes.

4. Cross-Browser Testing:

The framework is built to support different browsers. By adding a few configurations, you can test your application across multiple browsers such as Chrome, Firefox, Safari, and Edge.

5. Error Reports:

With the integration of pytest-html, you can generate detailed HTML reports for your tests, making it easier to understand test results, identify failures, and get insight into test execution times.

# For any suggestions Please reach out to nabin.adhikari349@gmail.com (atroverse.com)