from utils.driver_factory import DriverFactory
from pages.login_page import LoginPage


def test_login():

    driver = DriverFactory.get_driver()

    driver.get("https://www.saucedemo.com")

    login_page = LoginPage(driver)

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    assert "inventory" in driver.current_url

    driver.quit()