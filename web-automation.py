from selenium import webdriver
#Imports webdriver from Selenium
from  selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


import time
# Imports time module
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(chrome_options=chrome_options)
#Using webdriver for chrome
driver.get('https://kaltura.okta.com')
#Will open kaltura.okta.com on chrome
username = driver.find_element_by_xpath('//*[@id="okta-signin-username"]')
password = driver.find_element_by_xpath('//*[@id="okta-signin-password"]')
#assign variables to username and password field of okta. 
username.send_keys('ADM.ChrisS@kaltura.com')
password.send_keys('Goldsmith1992Q')
#sends the username and password to the fields
rememberMe = driver.find_element_by_xpath('//*[@id="form1"]/div[1]/div[2]/div[3]/div/span/div/label').click()
signinButton = driver.find_element_by_xpath('//*[@id="okta-signin-submit"]').click()
#checks the remember me check box and signs in
time.sleep(5)
#waits for 5 sec
sendPushButton = driver.find_element_by_xpath('//*[@id="form8"]/div[2]/input').click()
sendPushCheckBox = driver.find_element_by_xpath('//*[@id="okta-sign-in"]/div[2]/div/div/span/div/label').click()

driver.execute_script("window.open('about:blank', 'tab2');")
driver.switch_to_window("tab2")
driver.get('https://admin.microsoft.com/Adminportal')