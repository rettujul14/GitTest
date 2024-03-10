from selenium.webdriver.common.by import By


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    #driver.find_elements(By.XPATH,"//div[@class='card h-100']")
    cardTitle = (By.XPATH,"//div[@class='card h-100']")
    #driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
    ButtonCheckOut = (By.CSS_SELECTOR,"a[class*='btn-primary']")



    def getCardTitle(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardCheckout(self):
        return self.driver.find_element(*CheckOutPage.ButtonCheckOut)
