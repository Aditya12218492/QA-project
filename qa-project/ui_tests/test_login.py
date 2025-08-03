from selenium import webdriver
from ui_tests.pages.login_page import LoginPage

def test_login_valid():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("user", "pass")
    assert login_page.is_logged_in()
    driver.quit()
