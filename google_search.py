#automating nike purchase for Sankalp
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep as sl

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://google.com')
print(driver.title)
sl(3)

email = driver.find_element_by_name("q")
email.send_keys("Covid Vaccine")
email.send_keys(Keys.RETURN)


#sl(10)
#driver.quit()
