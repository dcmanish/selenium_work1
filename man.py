from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
driver=webdriver.Chrome(executable_path="C:\\Users\\admin\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
homepage=driver.window_handles[0]
driver.find_element(By.XPATH,"//a[@id='opentab']").click()
tab=driver.window_handles[1]
driver.switch_to(homepage)
driver.find_element(By.XPATH,"//button[id='openwindow']").click()
# window2=driver.window_handles[2]
# driver.switch_to.window(tab)
# driver.find_element(By.LINK_TEXT,'JavaScript SDET- Automation Testing Package').click()
