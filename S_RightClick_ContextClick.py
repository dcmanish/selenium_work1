import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome(executable_path="C:\\Users\\admin\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/context_menu")
act=ActionChains(driver)
# Right Click
act.context_click(driver.find_element(By.XPATH,"//div[@id='hot-spot']")).perform()

# DoubleClick
act.double_click(driver.find_element(By.XPATH,"//div[@id='hot-spot']")).perform()