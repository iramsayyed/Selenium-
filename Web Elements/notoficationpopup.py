from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notificatins")

serv_obj=Service("C:\Selenim\chromedriver-win64\chromedriver-win64\chromedriver.exe")

driver=webdriver.Chrome(service=serv_obj,options=ops)

driver.get("https://whatmylocation.com/")
driver.maximize_window()