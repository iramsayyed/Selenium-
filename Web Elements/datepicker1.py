from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import datetime

serv_obj=Service("C:\Selenim\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)  #switch to frame


today = datetime.date.today()
curent_year = str(today.year)



#driver.find_element(By.XPATH,"//*[@id='datepicker']").send_keys("05/30/2022") #mm/dd/yyyy

year="2019"
month="April"
date="26"

driver.find_element(By.XPATH,"//*[@id='datepicker']").click() # opens datepicker


while True:
    mon=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yr=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

    if mon==month and yr==year:
        break;
    else:
        if  curent_year < year :
   
            driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[2]/span").click()  #Next arrow
        else:
            driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[1]/span").click() # Previous Arrow - old date

#select date

dates=driver.find_elements(By.XPATH,"//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")

for ele in dates:
    if ele.text==date:
        ele.click()
        break



