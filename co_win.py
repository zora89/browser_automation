#automating co win website
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep as sl
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

print(driver.title)

wait = WebDriverWait(driver,10)
wait.until(EC.element_to_be_clickable((By.ID, 'mat-input-0')))

email = driver.find_element_by_id("mat-input-0")
email.send_keys("122008")
email.send_keys(Keys.RETURN)

