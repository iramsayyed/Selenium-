from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Selenim\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

#opens alert window
driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(5)

alertwindow=driver.switch_to.alert

print(alertwindow.text)
alertwindow.send_keys("Iram Sayyed")


alertwindow.accept() #close alert window by using OK button
# alertwindow.dismiss() #close alert window by using Cancel button
time.sleep(5)