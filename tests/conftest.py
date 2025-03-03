import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope = "function", autouse = True)
def init_browser():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/119.0.0.0 Safari/537.36")
    options.add_argument("--window-size=1920,1080")
    # options.add_argument('--headless')
    browser.config.base_url = 'https://github.com'
    browser.config.driver_options = options
    yield
    browser.quit()