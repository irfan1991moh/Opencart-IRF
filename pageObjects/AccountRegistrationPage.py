from selenium.webdriver.common.by import By

class AccountRegistrationPage():
    # locators
    txt_firstname_name = "//input[@name='firstname']"
    txt_lastname_name = "//input[@name='lastname']"
    txt_email_name = "//input[@name='email']"
    txt_password_name = "//input[@name='password']"
    chk_policy_name = "//input[@name='agree']"
    btn_cont_xpath="//button[@type='submit']"
    # text_msg_conf_xpath="//h1[normalize-space()='Your Account Has Been Created!']"
    # Constructor
    def __init__(self, driver):
        self.driver = driver
    # Actions Methods
    def setFirstName(self,fname):
      self.driver.find_element(By.XPATH,self.txt_firstname_name).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.XPATH,self.txt_lastname_name).send_keys(lname)

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txt_email_name).send_keys(email)

    def setPassword(self,pwd):
        self.driver.find_element(By.XPATH,self.txt_password_name).send_keys(pwd)

    def setPrivacyPolicy(self):
        self.driver.find_element(By.XPATH,self.chk_policy_name).click()

    def clickContinue(self):
        self.driver.find_element(By.XPATH,self.btn_cont_xpath).click()

    # def getconfirmationmsg(self):
    #     try:
    #         return  self.driver.find_element(By.XPATH,self.text_msg_conf_xpath).text
    #     except:
    #         None