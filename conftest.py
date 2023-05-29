import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='session')
def browser():
    chrome_options = options()
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


def options():
    chrome_options = Options()
    chrome_options.add_argument('headless')
    return chrome_options
