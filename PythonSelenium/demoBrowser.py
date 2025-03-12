import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome()
driver.get("http://google.com")
time.sleep(2)

# **** CHROME ****
# from selenium.webdriver.chrome.service import Service
# Chrome driver service
# If you have an old version of Chrome, download Chrome driver and add the root
# service_obj = Service("/Users/myuser/documents/chromediver")
# driver = webdriver.Chrome(service = service_obj)

# **** EDGE ****
# from selenium.webdriver.edge.service import Service
# Edge driver service
# If you have an old version of Edge, download Edge driver and add the root
# service_obj = Service("/Users/myuser/documents/msedgedriver")
# driver = webdriver.Edge(service = service_obj)

# **** FIREFOX ****
# from selenium.webdriver.firefox.service import Service
# Firefox driver service
# If you have an old version of Firefox, download Firefox driver and add the root
# service_obj = Service("/Users/myuser/documents/geckodriver")
# driver = webdriver.Firefox(service = service_obj)