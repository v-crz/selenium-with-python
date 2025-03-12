import time
from selenium import webdriver

# Edge driver - msedgedriver
# driver = webdriver.Edge()

# Firefox driver - geckodriver
# driver = webdriver.Firefox()

driver = webdriver.Chrome()
driver.get("http://google.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
