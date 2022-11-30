# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# driver=webdriver.Chrome(executable_path="C:\\Users\\admin\\Downloads\\chromedriver_win32\\chromedriver.exe")
# driver.get("https://www.facebook.com/")
# ele=driver.find_element(By.XPATH,"//input[@id='email']")
# print(ele.is_displayed())
# print(ele.is_enabled())
# print(ele.is_selected())       # returns True/False based on elements

# ------------------------
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path="C:\\Users\\admin\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.XPATH,"//label[@for='radio2']//input").click()
# radio_btn=driver.find_element(By.XPATH,"//label[@for='radio2']//input")
# print(radio_btn.is_selected())