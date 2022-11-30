import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome(executable_path="C:\\Users\\admin\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.get("https://chercher.tech/practice/implicit-wait-example")
asd="//div[@id='q']//input[1]"
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//div[@id='q']//input[1]")))
driver.find_element(By.XPATH,"//div[@id='q']//input[1]").click()

