#automating nike purchase for Sankalp

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep as sl
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import datetime as dt

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

tg_day = dt.datetime(2021, 5, 22, 21, 32, 0, 1)
print(tg_day)
date = dt.datetime.now()
print(date)

def while_1():
        if tg_day.hour == date.hour and tg_day.minute == date.minute:
            nike_website() # this breaks out of the while loop if it's the right day.
        else:
            print("Waiting a bit longer....")
            sl(1) #wait 1 seconds

def nike_website():

    driver.get('https://gs.nike.com/?checkoutId=47fa2977-c2f4-46ad-bd7d-384fddf2f70c&launchId=e18f55bb-c188-4fab-83c0-cc19107f59e7&skuId=0fef8cb6-f185-5ced-bffd-c09dd2575521&country=IN&locale=en-GB&appId=com.nike.commerce.snkrs.web&returnUrl=https:%2F%2Fwww.nike.com%2Fin%2Flaunch%2Ft%2Flebron-18-low-mimi-plange-higher-learning%2F')
    print(driver.title)

    driver.switch_to.default_content()
    wait = WebDriverWait(driver,10)
    wait.until(EC.element_to_be_clickable((By.NAME, 'emailAddress')))

    email = driver.find_element_by_name("emailAddress")
    email.send_keys("zorawar.purohit@gmail.com")
    email.send_keys(Keys.RETURN)

    password = driver.find_element_by_name("password")
    password.send_keys("123456xZ")
    password.send_keys(Keys.RETURN)

    sl(10)


while True:
    while_1()







