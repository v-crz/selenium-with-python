import time

from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless") #browser no visible
chrome_options.add_argument("--ignore-certificate-errors")


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/AutomationPractice")
driver.implicitly_wait(2)   # 2 seconds is max time out

driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
time.sleep(2)
driver.get_screenshot_as_file("screen.png")

time.sleep(5)