from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj=Service("C:\Selenim\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")

print(driver.title)  #OrangeHRM
print(driver.current_url) #https://opensource-demo.orangehrmlive.com/
print(driver.page_source)

driver.quit()