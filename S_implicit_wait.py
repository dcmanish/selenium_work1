import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome(executable_path="C:\\Users\\admin\\Downloads\\chromedriver_win32\\chromedriver.exe")
# --------
# driver.get("https://www.makemytrip.com/flights/")
# title="Flight Booking, Flight Tickets Booking at Lowest Airfare | MakeMyTrip"
# assert  title in driver.title


# -------
#setting implicit wait 5 seconds
# driver.implicitly_wait(10)
# to maximize the browser window
# driver.maximize_window()
#get method to launch the URL
# driver.get("https://www.tutorialspoint.com")
# time.sleep(5)
#to refresh the browser
# driver.refresh()
# identifying the link with link_text locator
# driver.find_element(By.LINK_TEXT,"Company").click()
#to close the browser
# driver.quit()


# ---------------

driver.get("https://chercher.tech/practice/implicit-wait-example")
driver.implicitly_wait(30)
driver.find_element(By.XPATH,"//div[@id='q']//input[1]").click()
driver.find_element(By.XPATH,"//div[@id='q']//input[3]").click()