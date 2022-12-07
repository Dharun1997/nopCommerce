import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def setup():
    serv_obj = Service("C:\\Driver\\\chromedriver_win32\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj)
    return driver

###########Pytest HTML report#####

#It is a hook for adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name']  = 'Customers'
    config._metadata['Tester']       =  'Tharun'

#It is a hook for delete/modify information to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


