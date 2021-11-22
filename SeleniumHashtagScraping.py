from selenium import webdriver
import time

USERNAME = "riyadahmedcsnea@gmail.com"
PASSWORD = "uGPZ6agPF5zTu3"

driverPath = "C:\\Users\\riyad\\Documents\\GitHub\\CSNEA2022\\chromedriver.exe"
driver = webdriver.Chrome(driverPath)
driver.get("http://www.instagram.com")

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

cookiesaccept = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Accept All")]'))).click()
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

username.clear()
username.send_keys(USERNAME)
password.clear()
password.send_keys(PASSWORD)
Login_button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
time.sleep(10)
not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()

#continue from here
#<button class="aOOlW  bIiDR  " tabindex="0">Accept All</button>
#<button class="sqdOP yWX7d    y3zKF     " type="button">Not now</button>
