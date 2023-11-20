from selenium.webdriver.common.by import By

class HomePage():
    # locators
    lnk_myaccount_xpath = "//span[normalize-space()='My Account']"
    lnk_register_linktext = "//a[normalize-space()='Register']"
    lnk_login_linktext = "//a[normalize-space()='Login']"
    # Constructor
    def __init__(self, driver):
        self.driver = driver
    # Actions Methods
    def clickMyAccount(self):
        self.driver.find_element(By.XPATH, self.lnk_myaccount_xpath).click()
    def clickRegister(self):
        self.driver.find_element(By.XPATH,self.lnk_register_linktext).click()
    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.lnk_login_linktext).click()