import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service('F:/Auto_test/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://adminqa.neapro.site/login")
driver.find_element(By.ID, "admin_email").send_keys("moderat@neapro.ru")
driver.find_element(By.ID, "admin_password").send_keys("Aa123456")
driver.find_element(By.NAME, "commit").click()
driver.find_element(By.LINK_TEXT, "Сотрудники").click()
driver.find_element(By.LINK_TEXT, "Администраторы").click()
driver.find_element(By.LINK_TEXT, "Создано").click()
time.sleep(10)
driver.find_element(By.LINK_TEXT, "Создано").click()
driver.find_element(By.XPATH, "//*[@id='admin_1']/td[9]/div/a[1]").click()
