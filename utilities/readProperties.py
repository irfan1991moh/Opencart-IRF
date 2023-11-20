import configparser
import os

config=configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+'\\configurations\\config.ini')

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('commonInfo','baseURL')
        return url
    @staticmethod
    def getEmail():
        useremail=config.get('commonInfo','email')
        return useremail
    @staticmethod
    def getPwd():
        password=config.get('commonInfo','password')
        return password

