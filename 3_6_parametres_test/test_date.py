import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import time
import math
try:
    link = "https://stepik.org/lesson/236895/step/1"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)


    #time.sleep(5)
    #input1 = browser.find_element_by_css_selector('.textarea')
    input1= WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".textarea"))
    )

    answer = math.log(int(time.time()))
    input1.send_keys(str(answer))


    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
    )
    button.click()
    text = browser.find_element_by_css_selector(".smart-hints__hint").text
    assert text == "Correct!"



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()