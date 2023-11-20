from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from testCases.conftest import setup
from utilities import randomeString
import os
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_AccountReg:
    baseURL = ReadConfig.getApplicationURL()
    logger=LogGen.loggen()
    def test_account_reg(self,setup):
        self.logger.debug("no")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp=HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickRegister()
        self.logger.info("on")
        self.regpage=AccountRegistrationPage(self.driver)
        self.regpage.setFirstName("John")
        self.regpage.setLastName("khan")
        self.email=randomeString.random_string_generator()+'@gmail.com'
        self.regpage.setEmail(self.email)
        self.regpage.setPassword("abcxyz34324")
        self.regpage.setPrivacyPolicy()
        self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_account_reg.png")
        # self.regpage.clickContinue()
        # self.confmsg=self.regpage.getconfirmationmsg()
        # if self.confmsg=="Your Account Has Been Created!":
        #     assert True
        #     self.driver.close()
        # else:
        #     self.driver.save_screenshot("..\\screenshots\\" + "test_account_reg.png")
        #     self.driver.close()
        #     assert False
