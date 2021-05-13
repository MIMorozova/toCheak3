import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--user_language', action='store', default="ru", help="Choose language: ru, en, es, fr, etc ...")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("user_language")
    
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    
    yield browser
    print("\nquit browser..")
    browser.quit()