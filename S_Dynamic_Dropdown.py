import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome(executable_path="C:\\Users\\admin\\Downloads\\chromedriver_win32\\chromedriver.exe")
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# var = "India"
# driver.find_element(By.XPATH,"//input[@id='autocomplete']").send_keys(var)
# time.sleep(2)
# s = "//ul[@id='ui-id-1']//li//div[text()='%s']/parent::li"%var
# driver.find_element(By.XPATH,s).click()
# -------new_dynamic_dropdwn-------
driver.get("https://www.cleartrip.com/")
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//*[@class=' c-pointer c-neutral-900']").click()
driver.maximize_window()
