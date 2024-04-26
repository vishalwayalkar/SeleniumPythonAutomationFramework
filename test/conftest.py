import pytest
from selenium import webdriver
from test.Profiles.ENTProfile import ENTProfile
@pytest.fixture(scope="class")
def launch_browser(request):
    driver = webdriver.Chrome()
    driver.get(ENTProfile.BASE_URL)
    driver.maximize_window()
    driver.implicitly_wait(ENTProfile.MAX_TIMEOUT)
    request.cls.driver = driver
    yield
    # driver.get_screenshot_as_file("screenshot.png")
    driver.close()

@pytest.mark.usefixtures("launch_browser")
class Base:
    pass
