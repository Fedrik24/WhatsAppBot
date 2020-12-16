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
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.get("http://web.whatsapp.com")
    sleep(10) #wait time to scan the code in second

    def send_whatsapp_msg(self,phone_no,text):
        driver.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no))
        try:
            driver.switch_to_alert().accept()
        except Exception as e:
            pass

        try:
            element_presence(self,By.XPATH,'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]',30)
            txt_box=driver.find_element(By.XPATH , '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            global no_of_message
            for x in range(no_of_message):
                txt_box.send_keys(text)
                txt_box.send_keys("\n")

        except Exception as e:
            print("invailid phone no :"+str(phone_no))
    for moblie_no in moblie_no_list:
        try:
            self,send_whatsapp_msg(moblie_no,message_text)

        except Exception as e:
            sleep(10)
            self.is_connected()


class User:

    def UserSingleNo(self):
        print("Enter Single Phone Number Here!")
        user = input("Enter Phone Number : ")
        print(62,int(user))
        BotTime()

    def UserMultipleNo(self,**args):
        print("Enter Multiple Phone Number Here!")
        print("Under Control!")


######################## USER COMMAND ##########################
    def User_Choice(self):
        print(""" 1.Single Number \n 2.Multiple Number""")
        c = input("Enter Number ")
        while c not in ['q','quit']:
            if c == '1':
                self.UserSingleNo()
            elif c == '2':
                self.UserMultipleNo()
            else:
                print('Bye~')
                sys.exit()
            break



if __name__ == "__main__":
    U = User()
    U.User_Choice()
