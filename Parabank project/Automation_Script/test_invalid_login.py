#TC_LG_03
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


serv_obj = Service(r"D:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC")

driver.find_element(By.NAME, "username").send_keys("Simple1")
driver.find_element(By.NAME, "password").send_keys("123")
driver.find_element(By.XPATH, "//input[@value='Log In']").click()

time.sleep(5)
assert "error" in driver.page_source.lower() or "invalid" in driver.page_source.lower()
driver.quit()
