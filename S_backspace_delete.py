import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome(executable_path="C:\\Users\\admin\\Downloads\\chromedriver_win32\\chromedriver.exe")
var ="manish"
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.XPATH,"//input[@id='name']").send_keys(var)
act=ActionChains(driver)
# var = driver.find_element(By.XPATH,"//input[@id='name']")
len = len(var);
while(len>=0):
    act.send_keys(Keys.BACK_SPACE).perform()
    time.sleep(1)
    len-=1
act.perform()

