import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.implicitly_wait(2)   # 2 seconds is max time out

# Click on column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

# collect all veggie names
veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")

browserSortedVeggies = []
for ele in veggieWebElements:
    browserSortedVeggies.append(ele.text)

originalBrowserSortedList = browserSortedVeggies.copy()

# sort this browserSortedVeggies list
browserSortedVeggies.sort()

assert browserSortedVeggies == originalBrowserSortedList

time.sleep(5)