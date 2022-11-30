import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome(executable_path="C:\\Users\\admin\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='courses-iframe']"))
driver.find_element(By.XPATH,"//a[@href='consulting']").click()
