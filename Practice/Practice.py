# write selenium in search and click on search icon
# clcik each and open each and every link
# capture each every open tabs windows id and print title
# close window id on shorts
from selenium.webdriver.common.by import By
from  browser_utils import Chrome_Browser
import time


driver=Chrome_Browser()

# To Open chrome
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
time.sleep(2)

Serach_box=driver.find_element(By.XPATH,"//input[@id='Wikipedia1_wikipedia-search-input']").send_keys("Selenium")
Seech_clcik=driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(3)

Search_results=driver.find_elements(By.XPATH,"//div[@id='Wikipedia1_wikipedia-search-results']//a")


for serach_result in Search_results:
    serach_result.click()
    windowsIDs=driver.window_handles

for windowid in windowsIDs:
    driver.switch_to.window(windowid)
    print("Titile of each page" ,driver.title)
    print("Windows ID of each Page",windowid )


