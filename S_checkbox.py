import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\\Users\\admin\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(checkboxes))
for cb in checkboxes:
    if cb==checkboxes[1]:
        pass
    else:
        cb.click()