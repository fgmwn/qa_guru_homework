import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()   # закроется даже если тест упал

def test_selenium_google(driver):
    url = "https://www.google.com/"
    driver.get(url)
    assert "Google" in driver.title
    assert driver.current_url.rstrip("/") == url.rstrip("/")

def test_selenium_github(driver):
    url = "https://github.com/"
    driver.get(url)
    assert "GitHub" in driver.title
    assert "github.com" in driver.current_url