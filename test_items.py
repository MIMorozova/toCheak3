import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_existance(browser):
    browser.get(link)
    # time.sleep(30)
    # button_element = browser.find_element_by_css_selector("button.btn.btn-lg.btn-primary.btn-add-to-basket")
    button_element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")))
    print()
    assert button_element.tag_name == 'button'