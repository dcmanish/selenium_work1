import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome(executable_path="C:\\Users\\admin\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.google.co.in/")
driver.implicitly_wait(5)
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@name='callout']"))
driver.find_element(By.XPATH,"//*[@class='M6CB1c rr4y5c']").click()
driver.switch_to.parent_frame()
driver.find_element(By.XPATH,"//input[@title='Search']").send_keys("mahaonline")
driver.find_element(By.XPATH,"//div[@class='lJ9FBc']//input[@name='btnK']").click()

