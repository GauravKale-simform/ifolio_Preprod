import pytest
# from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from pageObject.preprod.User_Login_Page import User_Login
from pageObject.preprod.Login_Page import Login
from pageObject.preprod.Manager_flow import Manager
from utilities.excel_reader import read_preprod_test_data, read_preprod_account_test_data


# load_dotenv()

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption("--browser")

def get_driver(browser):
    if browser == 'chrome':
        return webdriver.Chrome()
    elif browser == 'firefox':
        return webdriver.Firefox()
    elif browser == 'edge':
        return webdriver.Edge()
    else:
        return webdriver.Chrome()

@pytest.fixture(scope='session')
def preprod_setup(browser, request,preprod_test_data):
    driver = get_driver(browser)
    driver.maximize_window()
    driver.get("https://admin.preprod.ifolio.cloud/login")
    request.addfinalizer(driver.quit)
    lp = Login(driver)
    lp.enter_email(preprod_test_data['email'])
    lp.enter_password(preprod_test_data['password'])
    lp.click_on_signin_button()
    return driver

@pytest.fixture(scope='session')
def preprod_user_setup(browser, request, preprod_test_data):
    driver = get_driver(browser)
    driver.maximize_window()
    driver.get("https://preprod.ifolio.cloud/signin")
    request.addfinalizer(driver.quit)
    ulp = User_Login(driver)
    ulp.enter_email(preprod_test_data['user_email'])
    ulp.enter_password(preprod_test_data['user_password'])
    ulp.click_on_signin_button()
    return driver


@pytest.fixture
def manager_flow(preprod_setup):
    driver = preprod_setup
    mg = Manager(driver)
    mg.select_account('Simform')
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    mg.wait_for_progress_to_disappear()
    mg.owner_with_login()
    mg.close_toast_message()
    return mg

@pytest.fixture(scope='session')
def preprod_test_data():
    return read_preprod_test_data()

@pytest.fixture(scope='session')
def preprod_account_test_data():
    return read_preprod_account_test_data()