from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def Chrome_Browser():
    serv_obj=Service("C:\Selenim\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    driver=webdriver.Chrome(service=serv_obj)
    return driver