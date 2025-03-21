import pytest

from selenium import webdriver

# Example:
# pytest .\test_e2eTestFramework.py --browser_name chrome
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="firefox",
        help="browser selection"
    )

@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()

    driver.implicitly_wait(5)  # 5 seconds is max time out

    yield driver    # before your test function execution

    driver.close()  # post your test function execution