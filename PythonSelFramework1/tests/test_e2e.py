from lib2to3.pgen2 import driver

from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import  HomePage

from utilities.BaseClass import BaseClass

class TestOne(BaseClass):

    def test_e2e(self):

        log = self.getLogger()
        #  //a[contains(@href,'shop')]    a[href*='shop']
        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()
        log.info("getting all the card titles")
        #checkOutPage = CheckOutPage(self.driver)
        products = checkOutPage.getCardTitle()
        #products = self.driver.find_elements(By.XPATH,"//div[@class='card h-100']")

        for product in products :
            productName = product.find_element(By.XPATH, "div/h4/a").text
            log.info(productName)
            if productName == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()

        #self.driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
        checkOutPage.getCardCheckout().click()
        #self.driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
        confirmPage = ConfirmPage(self.driver)
        confirmPage.getFinalCheckout().click()
        log.info("Entering Country Name as ind")

        #self.driver.find_element(By.ID,"country").send_keys("ind")
        finalPage = ConfirmPage(self.driver)
        finalPage.getLocation().send_keys("Ind")
        self.verifyLinkPresence("India")
        #self.driver.find_element(By.LINK_TEXT,"India").click()
        finalPage.clickLocation().click()
        #self.driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
        finalPage.getCheckbox().click()
        #self.driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()
        finalPage.getSubmit().click()
        #successText = self.driver.find_element(By.CLASS_NAME,"alert-success").text
        successText = finalPage.getSuccess().text
        log.info("Text received from application is "+successText)
        assert "Success! Thank you!" in successText

