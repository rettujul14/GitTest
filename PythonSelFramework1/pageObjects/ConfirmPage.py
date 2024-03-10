from selenium.webdriver.common.by import By

class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    checkOutButton = (By.XPATH, "//button[@class='btn btn-success']")
    LocationTextBox = (By.ID,"country")
    LocText = (By.LINK_TEXT,"India")
    CheckBoxButton = (By.XPATH,"//div[@class='checkbox checkbox-primary']")
    SubmitButton = (By.CSS_SELECTOR,"[type='submit']")
    SuccessText = (By.CLASS_NAME,"alert-success")
    def getFinalCheckout(self):
        return self.driver.find_element(*ConfirmPage.checkOutButton)

    def getLocation(self):
        return self.driver.find_element(*ConfirmPage.LocationTextBox)

    def clickLocation(self):
        return self.driver.find_element(*ConfirmPage.LocText)

    def getCheckbox(self):
        return self.driver.find_element(*ConfirmPage.CheckBoxButton)

    def getSubmit(self):
        return self.driver.find_element(*ConfirmPage.SubmitButton)

    def getSuccess(self):
        return self.driver.find_element(*ConfirmPage.SuccessText)