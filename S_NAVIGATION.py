import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\\Users\\admin\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.get("https://en.wikipedia.org/wiki/Yo_(app)")
time.sleep(3)
driver.back()
time.sleep(3)
driver.forward()