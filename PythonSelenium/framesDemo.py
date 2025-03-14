import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")
driver.implicitly_wait(2)   # 2 seconds is max time out

driver.switch_to.frame("mce_0_ifr")

# Inject & Execute JavaScript to set contentEditable = true
driver.execute_script('''
const element = document.getElementById('tinymce');
element.contentEditable = true;
''')

driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("I am able to automate frames")
driver.switch_to.default_content()

# Confirm that Text in H3 element
h3ElementText = driver.find_element(By.CSS_SELECTOR, "h3").text
print(h3ElementText)
assert "An iFrame containing the TinyMCE WYSIWYG Editor" in h3ElementText



time.sleep(5)