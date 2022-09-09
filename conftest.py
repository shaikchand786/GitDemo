
import pytest
from selenium import webdriver
driver = None
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Images\chromedriver.exe")
        # service_obj = Service(r"C:\Users\HP\Desktop\Images\chromedriver.exe")
        # driver = webdriver.Chrome(service=service_obj)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path=r"C:\Users\HP\Desktop\Images\geckodriver.exe")
    elif browser_name == "edge":
        driver = webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Images\msedgedriver.exe")

    driver.get("https://www.rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()


# We have to declare it, where we declaring driver object.
# When your test fails, first most it comes to 'pytest_runtest_makereport()' method & it will inform to report that
#   test is failed. And it will have all the properties to give file_name of that test case.
#   The screenshot will generate with file_name. If your test case is failed (xfail) then it creates the file_name
#   by pulling-out the method name (replace()) & giving .png (whichever method got failed).
#   Thereafter we are calling '_capture_screenshot()' selenium method.
#   'if file_name:' --> This code to attach screenshot in your report (by tweaking the HTML)

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
     Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
     :param item:
     """
    pytest_html = item.config.pluginmanager.getplugin('html')   # report
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    #properties to give file_name
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"   # Screenshot will create with it (file_name.png)
            _capture_screenshot(file_name)
            #to attach screenshot in your report
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;"' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)