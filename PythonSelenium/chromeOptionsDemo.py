import time

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
#ignore certificate error
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(options = chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice")

print(driver.title)

driver.implicitly_wait(2)   # 2 seconds is max time out

