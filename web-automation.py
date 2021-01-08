from selenium import webdriver
#Imports wendriver from Selenium
import time
# Imports time module


driver = webdriver.Chrome()
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
doNotChallengeCheckBox = driver.find_element_by_xpath('//*[@id="okta-sign-in"]/div[2]/div/div/span[2]/div/label').click()
