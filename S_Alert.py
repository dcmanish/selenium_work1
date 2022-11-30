import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\\Users\\admin\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.XPATH,"//input[@id='alertbtn']").click()
driver.switch_to().alert().accept()