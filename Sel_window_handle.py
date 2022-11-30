from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

import time
driver=webdriver.Chrome(executable_path="C:\\Users\\admin\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://www.hyrtutorials.com/p/window-handles-practice.html")
current=driver.current_window_handle
driver.find_element(By.ID,"newWindowBtn").click()
window1=driver.window_handles[1]
driver.switch_to.window(current)
driver.find_element(By.CLASS_NAME,"whButtons").click()