import json
import os
import sys
import time

import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PageObjects.login import LoginPage

test_data_path = '../Data/test_e2eTestFramework.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]


@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(browserInstance, test_list_item):
    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    login_page = LoginPage(driver)
    shop_page = login_page.login(test_list_item["userEmail"], test_list_item["userPassword"])

    shop_page.add_product_to_cart(test_list_item["productName"])
    checkout_confirmation = shop_page.go_to_cart()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("ind")
    checkout_confirmation.validate_order()

    time.sleep(5)