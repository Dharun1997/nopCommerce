
import sys
import time

sys.path.append("C:/Users/DHARUN R/PycharmProjects/nopCommerce/pageObjects")
sys.path.append("C:/Users/DHARUN R/PycharmProjects/nopCommerce/utilities")

import LoginPage
import readProperties
import customLogger

class Test_001_Login:
    baseurl= "https://admin-demo.nopcommerce.com/"
    username= "admin@yourstore.com"
    password= "admin"
    logger=customLogger.LogGen.loggen()

    def test_login(self,setup):
        self.driver=setup
        self.driver.get(self.baseurl)
        self.logger.info("*****************Test case 1 Started***************")
        self.lp=LoginPage.Login(self.driver)
        self.lp.username(self.username)
        self.lp.password(self.password)
        self.lp.logging()
        self.logger.info("*******************Login successful***************")
        act_title=self.driver.title
        self.driver.close()
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.logger.info("*************Test case 1 passed******************")
        else:
            assert False



