from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class Login:
    textbox_email="Email"
    textbox_password="Password"
    button_login="/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"
    logout_btn="//*[@id='navbarText']/ul/li[3]/a"

    def __init__(self,driver):
        self.driver=driver

    def username(self,username):
        self.driver.find_element(By.ID,self.textbox_email).clear()
        self.driver.find_element(By.ID,self.textbox_email).send_keys(username)

    def password(self,password):
        self.driver.find_element(By.ID,self.textbox_password).clear()
        self.driver.find_element(By.ID,self.textbox_password).send_keys(password)

    def logging(self):
        self.driver.find_element(By.XPATH,self.button_login).click()

    def logout(self):
        self.driver.find_element(By.XPATH,self.logout_btn).click()