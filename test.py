# for testing
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
driver.get('https://oakton.edu')
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/div/header/div[2]/div[4]').click()
username = "vmisyuti9711" 
password = "popcorn888"
usernameElem = driver.find_element(By.ID,"username")
passwordElem= driver.find_element(By.ID,"password")
usernameElem.send_keys(username)
passwordElem.send_keys(password)
signInButton = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div[2]/input[3]').click()
time.sleep(30)

