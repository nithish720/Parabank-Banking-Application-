
#TC_FT_07
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

serv_obj = Service(r"D:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://parabank.parasoft.com")

# Login
driver.find_element(By.NAME, "username").send_keys("yourUsername")
driver.find_element(By.NAME, "password").send_keys("yourPassword")
driver.find_element(By.XPATH, "//input[@value='Log In']").click()
time.sleep(2)

driver.find_element(By.LINK_TEXT, "Find Transactions").click()
driver.find_element(By.ID, "criteria.fromDate").send_keys("07-01-2025")
driver.find_element(By.ID, "criteria.toDate").send_keys("07-28-2025")
driver.find_element(By.XPATH, "//button[contains(text(),'Find Transactions')]").click()
time.sleep(2)

assert "transaction" in driver.page_source.lower()
driver.quit()
