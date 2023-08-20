import pytest
from selenium import webdriver
from pages.registration.login_page import LoginPage


@pytest.fixture(scope="function", autouse=True)
def setup_teardown_method():
    print("Method level setup")
    yield
    print("Method level teardown")


@pytest.fixture(scope="class", autouse=True)
def setup_teardown_class(request, browser):
    print("Class level setup")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    driver.implicitly_wait(3)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    request.cls.driver = driver
    yield driver
    print("Class level teardown")
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--os_type")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def os_type(request):
    return request.config.getoption("--os_type")

"""
1. Framework Refactor - Done
2. Add more methods to custom driver - Done
3. BasePage Concept - Done
4. Util Concept - Done
5. Verifying test result - Done
6. Convert test modules to test class - Done
7. Adding logging to framework - Done
8. Data Driven Testing - Done
9. How to run complete automation suite - Done
10. Taking screenshots on failure - Done
11. Utility for assertion (Framework Refactor) - Done
12. Reporting and attaching screenshots to reports - Done
13. GitHub < 1 class- Done
14. Push the framework code to GitHub
15. Jenkins < 1 class (CI / CD) - CircleCI, Bamboo, TeamCity
16. API Testing >= 1 class
17. Performance Testing >=1
18. SQL Testing >=1
"""