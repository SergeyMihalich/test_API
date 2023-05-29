from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import requests

from resources.data import select_button as sb


class BaseClass:

    def get_request(self, URL):
        return requests.get(URL)

    def post_request(self, URL, payload):
        return requests.post(URL, json=payload)

    def put_request(self, URL, payload):
        return requests.put(URL, json=payload)

    def del_request(self, URL):
        return requests.delete(URL)

    def patch_request(self, URL, payload):
        return requests.patch(URL, json=payload)


class WebPage:

    def compare_with_page(self, URL, browser, select):
        browser.get(URL)
        button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, sb[select])))
        browser.execute_script("arguments[0].scrollIntoView();", button)
        button.click()
        sleep(2)
        res_code = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, sb['res_code'])))
        browser.execute_script("arguments[0].scrollIntoView();", res_code)
        res_body = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, sb['res_body'])))
        return int(res_code.text), res_body.text
