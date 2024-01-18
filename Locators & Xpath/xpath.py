from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


# To Open chrome
serv_obj=Service("C:\Selenim\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get('https://mesta.studentkare.com')
driver.maximize_window()
time.sleep(2)

driver.find_element(By.XPATH,"//a[normalize-space()='Login / Register']").click()
time.sleep(5)

driver.find_element(By.XPATH,"//input[@type='text']").send_keys(" ")
time.sleep(5)

driver.find_element(By.XPATH,"//input[@type='password']").send_keys("ritvi007@")
time.sleep(2)

driver.find_element(By.XPATH,"//a[@id='button1']").click()
time.sleep(5)





