import pytest

from PageData.HomePageData import HomePageData
from PageObjects.HomePage import HomePage
from Utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_formSubmission(self, getData):
        log = self.getLogger()
        #driver.find_element(By.NAME, "name").send_keys("Chand")
        homePage = HomePage(self.driver)
        log.info("Firstname is "+getData["firstname"])
        homePage.getName().send_keys(getData["firstname"])
        # driver.find_element_by_name("email").send_keys("Shaik")
        log.info("Mail ID is"+getData["mailID"])
        homePage.getEmail().send_keys(getData["mailID"])
        #driver.find_element_by_id("examplecheck1").click()
        homePage.getCheck().click()

        #driver.find_element(By.CSS_SELECTOR, 'input[type="password"]').send_keys(143143786)
        homePage.getPassword().send_keys(getData["password"])

        #sel = Select(driver.find_element_by_id("exampleFormControlSelect1"))
        #Reuse below two line by placing these in 'BaseClass' as a utility because 'Select' dropdown is helping to
            # identify that dropdown with visible text 'Male'
        # sel = Select(HomePage.getGender())
        # sel.select_by_visible_text("Male")
        log.info("Gender: "+getData["gender"])
        self.selectOptionsByText(homePage.getGender(), getData["gender"])

        # Reuse below lines by placing these in 'BaseClass' as a utility.
        # radios = HomePage.clickButton()
        # for radio in radios:
        #     if radio.get_attribute("ID") == "inlineRadio2":
        #         radio.click()
        #         assert radio.is_selected()  # if radio button is clicked in browser then it will not give error, just passes.
        #         break
        self.selectOptionsByButton(homePage.clickButton(), getData["working"])

        #driver.find_element_by_xpath("//input[@value='Submit']").click()
        homePage.clickSubmit().click()

        #message = driver.find_element_by_css_selector("[class*='alert-success']").text
        message = homePage.getSuccessMessage().text
        log.info("Test received from application is "+message)
        assert ("Success" in message)
        self.driver.refresh()

        #Success message will be print if test case will pass!

    #How to run "test_formSubmission" testcase in multiple data base in the form of Tuples '()' & Dictionary '{ : }'
    #       In test case, we have to give 'getData[index_value]' to get data from tuple_lists.
    #@pytest.fixture(params=[("chand", "chandshaik321@gmail.com", "143143786", "Male", "inlineRadio2"), ("nazira", "shaiknazira4@gmail.com", "143143143", "Female", "inlineRadio2")])
    # How to run "test_formSubmission" testcase in multiple data base in the form of Dictionary '{key:value}'.
    #       In test case, we have to give 'getData[key]' to get values.

    #    Moving below data '[{ }]' to 'HomePageData.py' file in PageData package
    #@pytest.fixture(params=[{"firstname":"chand", "mailID":"chandshaik321@gmail.com", "password":"143143786", "gender":"Male", "working":"inlineRadio2"}, {"firstname":"nazira", "mailID":"shaiknazira4@gmail.com", "password":"143143143", "gender":"Female", "working":"inlineRadio2"}])
#    @pytest.fixture(params=HomePageData.test_HomePage_data)
    @pytest.fixture(params=HomePageData.getTestData("Testcase2")) # get details through Excel file
    def getData(self, request):
        return request.param


#Notes: How to set_up Framework?
    #   In every test case,you think you need data to drive have one variable pass either touples or dictionary & carefully
    #   send that format at runtime to 'getData' fixture of your test case. This 'getData' fixture will load all your
    #   test data before your test 'test_formSubmission' started executing. So make sure you pass fixture through your
    #   test case 'test_formSubmission(self, getData)' so that before execution starts it will load all data required to
    #   test data file and then it will run. This is how you need to set_up framework.
#Notes: How & what the principles of Framework work needs?
    #   For data you have separate package('PageData'); for test cases you have separate package('pytestpractiseproject');
    #   for Page Objects you have separate package ('PageObjects'); for Utilities all to invoke browser & to some reusable methods you have separate package ('Utilities').
    #   So you have to segregate all into proper places and then pull everything into your test.
