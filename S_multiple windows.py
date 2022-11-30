import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\\Users\\admin\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
current=driver.current_window_handle
print(current)
driver.find_element(By.ID,"openwindow").click()
child = driver.window_handles
print(child)
driver.switch_to.window(current)
driver.find_element(By.XPATH,"//input[@value='radio2']").click()



