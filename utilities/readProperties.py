import configparser

config=configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class Config:

    @staticmethod
    def readurl():
        baseurl=config.read('credentials','baseurl')
        return baseurl

    @staticmethod
    def readusername():
        user=config.read('credentials','username')
        return user

    @staticmethod
    def readpassword():
        password=config.read('credentials','password')
        return password
