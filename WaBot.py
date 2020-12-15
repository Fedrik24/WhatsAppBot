from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import socket
import sys


class BotTime:
    def Test(self):
        print("testing")

class User:

    def UserSingleNo(self):
        print("Enter Single Phone Number Here!")
        user = input("Enter Phone Number : ")
        print(62,int(user))
        BotTime.Test(self)

    def UserMultipleNo(self):
        print("Enter Multiple Phone Number Here!")
        print("Under Control!")

    def User_Choice(self):
        print(""" 1.Single Number \n 2.Multiple Number""")
        c = input("Enter Number ")
        while c not in ['Null']:
            if c == '1':
                self.UserSingleNo()
            else:
                self.UserMultipleNo()
            break



if __name__ == "__main__":
    U = User()
    U.User_Choice()
