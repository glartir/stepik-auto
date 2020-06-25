import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1(object):

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.smoke
    @pytest.mark.win10
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")



# pytest.ini:
#
# [pytest]
# markers =
#     smoke: marker for smoke tests
#     regression: marker for regression tests
#     win10


#Чтобы запустить только smoke-тесты для Windows 10, нужно использовать логическое И:
#pytest -s -v -m "smoke and win10" test_fixture81.py
# Для запуска тестов с разными метками можно использовать логическое ИЛИ. Запустим smoke и regression-тесты:
# pytest -s -v -m "smoke or regression" test_fixture8.py


# Чтобы запустить все тесты, не имеющие заданную маркировку, можно использовать инверсию. Для запуска всех тестов, не отмеченных как smoke, нужно выполнить команду:
#
# pytest -s -v -m "not smoke" test_fixture8.py