import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(executable_path="C:\\Users\\admin\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
Drop_dn=Select(driver.find_element(By.XPATH,"//select[@id='dropdown-class-example']"))
Drop_dn.select_by_index(1)
time.sleep(2)
Drop_dn.select_by_value("option3")
time.sleep(2)
Drop_dn.select_by_visible_text("Option2")