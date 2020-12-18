from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import socket
import sys
import platform

user = ""
machine = platform.machine()
if machine == "armv7l":
    driver = webdriver.Chrome()
    driver.get("http://web.whatsapp.com")
else:
    driver = webdriver.Firefox()
    driver.get("http://web.whatsapp.com")

input("klik enter jika sudah scan qr")

class BotTime:
    global user
    message_text='text' # message you want to send
    no_of_message=10 # no. of time you want the message to be send
    moblie_no_list= user # list of phone number can be of any length

    def element_presence(self,by,xpath,time):
        element_present = EC.presence_of_element_located((By.XPATH, xpath))
        WebDriverWait(driver, time).until(element_present)

    def is_connected(self):
        try:
            # connect to the host -- tells us if the host is actually
            # reachable
            socket.create_connection(("www.google.com", 80))
            return True
        except :
            self.is_connected()

    def send_whatsapp_msg(self,phone_no,text):
        driver.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no))
        try:
            driver.switch_to_alert().accept()
        except Exception as e:
            pass

        try:
            element_presence(By.XPATH,'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]',30)
            txt_box=driver.find_element(By.XPATH , '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            global no_of_message
            for x in range(no_of_message):
                txt_box.send_keys(text)
                txt_box.send_keys("\n")

        except Exception as e:
            print("invailid phone no :"+str(phone_no))
    for moblie_no in moblie_no_list:
        try:
            self.send_whatsapp_msg(moblie_no,message_text)

        except Exception as e:
            sleep(10)
            self.is_connected()


class User:

    def UserSingleNo(self):
        print("Enter Single Phone Number Here!")
        global user
        user = input("Enter Phone Number : ")
        text = input("input Text : ")
        # print(62,int(user))
        BotTime.is_connected(self)
        BotTime.send_whatsapp_msg(self, user, text)

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
