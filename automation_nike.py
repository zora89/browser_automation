#automating nike purchase for a bud

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep as sl
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import datetime as dt

#setting path to driver

PATH = 'C:\Program Files (x86)\chromedriver.exe'

#creating instance of the driver

driver = webdriver.Chrome(PATH)

#target date to be set manually for initiation of get requests

tg_day = dt.datetime(2021, 5, 22, 3, 4, 29, 1)
print(tg_day)



def time_check():
    date = dt.datetime.now()
    print(date)

#match now() to target date then proceeds    

    while tg_day.hour == date.hour and tg_day.minute == date.minute and tg_day.second == date.second:
        print("Activated")
        nike_website() # this breaks out of the while loop if it's the right day.
        print("We did our best!!!!! Better Luck Next Time!!!!!")
        break

    else:
        print("Waiting a bit longer....")
        sl(1)
        time_check()
    

#driver and actionable methods here 

def nike_website():

    driver.get('https://gs.nike.com/?checkoutId=47fa2977-c2f4-46ad-bd7d-384fddf2f70c&launchId=e18f55bb-c188-4fab-83c0-cc19107f59e7&skuId=0fef8cb6-f185-5ced-bffd-c09dd2575521&country=IN&locale=en-GB&appId=com.nike.commerce.snkrs.web&returnUrl=https:%2F%2Fwww.nike.com%2Fin%2Flaunch%2Ft%2Flebron-18-low-mimi-plange-higher-learning%2F')
    print(driver.title)

#critical wait use and clickable delay    

    driver.switch_to.default_content()
    wait = WebDriverWait(driver,10)
    wait.until(EC.element_to_be_clickable((By.NAME, 'emailAddress')))

#finding the element email via name

    email = driver.find_element_by_name("emailAddress")
    email.send_keys("zorawar.purohit@gmail.com")
    email.send_keys(Keys.RETURN)

#finding the element password via name

    password = driver.find_element_by_name("password")
    password.send_keys("123456xZ")
    password.send_keys(Keys.RETURN)


#launch

time_check()







