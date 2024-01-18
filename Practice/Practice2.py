# Print user name along with the user role if the role is ESS...

import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Selenim\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10) # seconds  # implicit wait


driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()

# To login
driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()

driver.find_element(By.XPATH,"//li[1]//a[1]//span[1]").click()


#total rows n a table
rows=len(driver.find_elements(By.XPATH,"(//div[@role='row'])"))
print("total number of rows in a table:",rows)


for raw in range(1,rows):
    user_name=driver.find_element(By.XPATH,"//div[@role='rowgroup']//div["+str(raw)+"]//div[1]//div[2]").text
    user_role=driver.find_element(By.XPATH,"//div[@role='rowgroup']//div["+str(raw)+"]//div[1]//div[3]").text
    if user_role == "ESS":
        print(user_name,user_role )

    

