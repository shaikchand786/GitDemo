import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
# @pytest.mark.usefixtures("setup")
from PageObjects.CheckoutPage import CheckOutPage
from PageObjects.HomePage import HomePage
from Utilities.BaseClass import BaseClass

class Testcase1(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        # driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        homePage = HomePage(self.driver)
        #When you call "shopItems() method, it returns object of your next class & creating object for next class
        checkOutPage = homePage.shopItems()  # click() is Internally handled in "shopItems" method only
        log.info("Getting all the card titles")
#        checkOutPage = CheckOutPage(self.driver)   --> just skipping due to adding this in previous page itself

        cards = checkOutPage.getCardTitles()   # get from CheckoutPage.py
        i = -1
        # Searching 'Blackberry' text & clicking on Add button
        #p_names = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            #item_name = p_name.find_element(By.XPATH, "div/h4/a").text
            #MobileList.append(item_name)
            if cardText == "Blackberry":
                checkOutPage.getCardFooter()[i].click()  # get from CheckoutPage.py
                #p_name.find_element(By.XPATH, "div/button").click()

        # click on 'Checkout' button
        #self.driver.find_element(By.CSS_SELECTOR, "a[class*='nav-link btn btn-primary']").click()
        checkOutPage.checkOutItems1().click()

        # Click on final 'checkout' button
        #self.driver.find_element(By.CSS_SELECTOR, "button[class*='btn-success']").click()
        confirmPage = checkOutPage.checkOutItems()
        log.info("Entering country name as Ind")
        self.driver.find_element(By.CSS_SELECTOR, "input[class*='filter-input']").send_keys("Ind")

        # External wait time especially for required element which we want
            # entered below code in BaseClass.py & get it from there as simple pass
        #wait = WebDriverWait(self.driver, 10)
        #wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

        self.verifyLinkPresents("India")

        self.driver.find_element(By.LINK_TEXT, "India").click()

        #self.driver.find_element(By.CSS_SELECTOR, "label[for='checkbox2']").click()
        checkOutPage.checkBoxMark().click()

        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        message = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        log.info("Test received from application is "+message)

        assert "Thank you!" in message

        # Assert is exception handler, test is present in input then it passes otherwise it shows error