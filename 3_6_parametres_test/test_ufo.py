import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import time
import math


@pytest.fixture(scope="function")
def browser():
    #answer = math.log(int(time.time()))
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('lesson', ["236895","236896","236897","236898","236899","236903","236904","236905" ])
def test_ufo_ans(browser, lesson):
    link = f"https://stepik.org/lesson/{lesson}/step/1/"
    browser.get(link)
    browser.implicitly_wait(5)

    input1 = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".textarea"))
    )
    answer = math.log(int(time.time()))
    input1.send_keys(str(answer))

    #button=browser.find_element_by_css_selector("submit-submission")
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
    )
    button.click()
    text=browser.find_element_by_css_selector(".smart-hints__hint").text
    assert text== "Correct!"
#answer = math.log(int(time.time()))