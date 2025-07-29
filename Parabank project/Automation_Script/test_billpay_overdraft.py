#TC_BP_03
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

driver.find_element(By.LINK_TEXT, "Bill Pay").click()
driver.find_element(By.NAME, "payee.name").send_keys("Electricity Board")
driver.find_element(By.NAME, "payee.address.street").send_keys("1 Main St")
driver.find_element(By.NAME, "payee.address.city").send_keys("Hyderabad")
driver.find_element(By.NAME, "payee.address.state").send_keys("TS")
driver.find_element(By.NAME, "payee.address.zipCode").send_keys("500001")
driver.find_element(By.NAME, "payee.phoneNumber").send_keys("9876543210")
driver.find_element(By.NAME, "payee.accountNumber").send_keys("123456")
driver.find_element(By.NAME, "verifyAccount").send_keys("123456")
driver.find_element(By.NAME, "amount").send_keys("99999")  # Intentionally large amount
driver.find_element(By.XPATH, "//input[@value='Send Payment']").click()

assert "insufficient" in driver.page_source.lower() or "error" in driver.page_source.lower()
driver.quit()
