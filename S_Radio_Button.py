import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\\Users\\admin\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CLASS_NAME,"radioButton").click()
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='radio-btn-example']/fieldset/label[2]/input").click()
time.sleep(3)
driver.find_element(By.XPATH,"//body/div[1]/div[1]/fieldset[1]/label[3]/input[1]").click()

