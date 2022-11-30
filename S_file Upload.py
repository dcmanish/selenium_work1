import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome(executable_path="C:\\Users\\admin\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/upload")
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//input[@id='file-upload']").send_keys("C:\\Users\\admin\\Desktop\\jupyter\\man.txt")
driver.find_element(By.XPATH,"//input[@id='file-submit']").click()