# Distributing tests across multiple CPUs to speed up test execution
# pip install pytest-xdist
# pytest -n # //pytest-xdist plugin you need to run in parallel

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


@pytest.mark.smoke      # execute: pytest -m smoke
@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(browserInstance, test_list_item):
    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    login_page = LoginPage(driver)
    print(login_page.get_title())

    shop_page = login_page.login(test_list_item["userEmail"], test_list_item["userPassword"])
    shop_page.add_product_to_cart(test_list_item["productName"])
    print(shop_page.get_title())
    checkout_confirmation = shop_page.go_to_cart()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("ind")
    checkout_confirmation.validate_order()

    time.sleep(5)