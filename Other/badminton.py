import selenium
from selenium import webdriver

import time
import datetime

#define variable username to hold username
userName = "amanp3"
#define password to be ppassword read from txt file
with open('C:/Users/Aman/Desktop/School/seleniumPass.txt', 'r') as f:
    password = f.read()


#define driver to be chrome webdriver
driver = webdriver.Chrome()

#open arc website
driver.get('https://active.illinois.edu/booking/2696dd2e-efa5-4598-b3b8-b7cf601c7e29')

#delay to allow page to load
time.sleep(1)

#find login button and click it
login_button = driver.find_element_by_xpath('//*[@id="divLoginOptions"]/div[2]/div[2]/div/button')
login_button.click()

#find and input username in user name box
usernameInput = driver.find_element_by_id('j_username')
usernameInput.send_keys(userName)

#find and input password in password box
passwordInput = driver.find_element_by_id('j_password')
passwordInput.send_keys(password)

#delay to allow page to load
time.sleep(1)

#subit login credentials
submit_button = driver.find_element_by_xpath('//*[@id="submit_button"]/input')
submit_button.click()

#choose correct day
day_button = driver.find_element_by_xpath('//*[@id="divBookingDateSelector"]/div[2]/div[2]/button[4]')
day_button.click()

#choose correct court number
court_button = driver.find_element_by_xpath('//*[@id="tabBookingFacilities"]/button[2]/span')
court_button.click()