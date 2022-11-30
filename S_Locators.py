import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path="C:\\Users\\admin\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.find_element(By.ID,"opentab").click()
# driver.find_element(By.ID,"autocomplete").send_keys("admin")
# content = driver.find_element(By.CLASS_NAME, 'content')
# driver.find_element(By.NAME,"enter-name").send_keys("fgd")
# driver.find_element(By.LINK_TEXT,("Free Access to InterviewQues/ResumeAssistance/Material")).click()
# driver.find_element(By.XPATH,"//input[@id='checkBoxOption2']").click()

# -------CSS_SELECTOR LOCATOR

# driver.find_element(By.CSS_SELECTOR
# driver.find_element(By.CSS_SELECTOR,"input[value='radio2']").click()
driver.find_element(By.CSS_SELECTOR,'#opentab').click()
