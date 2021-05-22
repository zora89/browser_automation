#automating nike purchase for Sankalp
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep as sl

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
x1 = webdriver.Chrome(PATH)

driver.get('https://google.com')
print(driver.title)

email = driver.find_element_by_name("q")
email.send_keys("Covid Vaccine")
email.send_keys(Keys.RETURN)

sl(10)

# Load new page 
x1.get('https://google.com')
email = x1.find_element_by_name("q")
email.send_keys("Andaman News")
email.send_keys(Keys.RETURN)



