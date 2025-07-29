#TC_CF_01 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service(r"D:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://parabank.parasoft.com")

driver.find_element(By.LINK_TEXT, "Contact").click()
driver.find_element(By.XPATH, "//input[@value='Send to Customer Care']").click()

assert "required" in driver.page_source.lower() or "error" in driver.page_source.lower()
driver.quit()
