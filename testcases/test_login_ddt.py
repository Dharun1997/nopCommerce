
import sys
import time

sys.path.append("C:/Users/DHARUN R/PycharmProjects/nopCommerce/pageObjects")
sys.path.append("C:/Users/DHARUN R/PycharmProjects/nopCommerce/utilities")

import LoginPage
import readProperties
import customLogger
import ddt_excel

class Test_002_Login:
    baseurl= "https://admin-demo.nopcommerce.com/"
    logger=customLogger.LogGen.loggen()
    path = ".//testData/sample.xlsx"

    def test_login_exddt(self,setup):
        self.driver=setup
        self.driver.get(self.baseurl)
        self.logger.info("*****************Test case 1 Started***************")
        self.lp=LoginPage.Login(self.driver)

        self.rows=ddt_excel.rowcount(self.path,"Sheet2")
        self.actual=[]
        self.expected=[]
        for r in range(2,self.rows+1):
            self.username=ddt_excel.readData(self.path,"Sheet2",r,1)
            self.password=ddt_excel.readData(self.path,"Sheet2",r,2)
            self.exp=ddt_excel.readData(self.path,"Sheet2",r,3)
            self.lp.username(self.username)
            self.lp.password(self.password)
            self.lp.logging()
            time.sleep(5)

            if self.driver.title=="Dashboard / nopCommerce administration":
                self.actual.append("pass")
                self.expected.append(self.exp)
                self.lp.logout()
            else:
                self.actual.append("fail")
                self.expected.append(self.exp)

        self.driver.close()
        if self.actual==self.expected:
            print("Test passed successfully")
            assert True
        else:
            print("Test failed")
            assert False


















