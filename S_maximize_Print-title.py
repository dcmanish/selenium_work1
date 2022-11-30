from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:\\Users\\admin\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.title)
driver.maximize_window()
print (driver.current_url)