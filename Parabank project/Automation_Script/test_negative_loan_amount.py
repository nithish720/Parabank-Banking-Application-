#TC_RL_02
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service


serv_obj = Service(r"D:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://parabank.parasoft.com")

# Login
driver.find_element(By.NAME, "username").send_keys("yourUsername")
driver.find_element(By.NAME, "password").send_keys("yourPassword")
driver.find_element(By.XPATH, "//input[@value='Log In']").click()
time.sleep(2)

driver.find_element(By.LINK_TEXT, "Request Loan").click()
driver.find_element(By.ID, "amount").send_keys("-1000")
driver.find_element(By.ID, "downPayment").send_keys("100")
driver.find_element(By.XPATH, "//input[@value='Apply Now']").click()

assert "invalid" in driver.page_source.lower() or "error" in driver.page_source.lower()
driver.quit()
