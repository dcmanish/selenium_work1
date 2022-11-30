import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome(executable_path="C:\\Users\\admin\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
act=ActionChains(driver)
act.move_to_element(driver.find_element(By.XPATH,"//button[@id='mousehover']")).perform()
time.sleep(2)
act.move_to_element(driver.find_element(By.XPATH,"//a[normalize-space()='Top']")).click().perform()