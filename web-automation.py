#Imports webdriver from Selenium
from selenium import webdriver

from  selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
# Imports time module
import time


chrome_options = webdriver.ChromeOptions()
#Opens chrome in incognito mode
chrome_options.add_argument("--incognito")
#Using webdriver for chrome
driver = webdriver.Chrome(chrome_options=chrome_options)
#Gets Kaltura.okta.com HTTP page
driver.get('https://kaltura.okta.com')

#assign variables to username and password field of okta. 
username = driver.find_element_by_xpath('//*[@id="okta-signin-username"]')
password = driver.find_element_by_xpath('//*[@id="okta-signin-password"]')

#sends the username and password to the respective fields on the web page
username.send_keys('email')
password.send_keys('pass')
#checks the 'remember me' check box and clicks 'Sign In'
rememberMe = driver.find_element_by_xpath('//*[@id="form1"]/div[1]/div[2]/div[3]/div/span/div/label').click()
signinButton = driver.find_element_by_xpath('//*[@id="okta-signin-submit"]').click()
# Waits for page to fully load to proceed
delay = 3
try:
    meElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))
    print ("Page is ready")
except TimeoutException:
    print ("Loading took too much time!")

sendPushButton = driver.find_element_by_xpath('//*[@id="form8"]/div[2]/input').click()
sendPushCheckBox = driver.find_element_by_xpath('//*[@id="okta-sign-in"]/div[2]/div/div/span/div/label').click()
#opens a second tab on chrome
driver.execute_script("window.open('about:blank', 'tab2');")
driver.switch_to_window("tab2")
driver.get('https://admin.microsoft.com/Adminportal')
time.sleep(1)
microsoftEmail = driver.find_element_by_xpath('//*[@id="i0116"]')
microsoftEmail.send_keys('email')
microsoftNext = driver.find_element_by_xpath('//*[@id="idSIButton9"]').click()
delay = 3
try:
    meElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))
    print ("Page is ready")
except TimeoutException:
    print ("Loading took too much time!")
username = driver.find_element_by_xpath('//*[@id="okta-signin-username"]')
username.clear()
username.send_keys('email')
password = driver.find_element_by_xpath('//*[@id="okta-signin-password"]')
password.send_keys('pass')
signinButton = driver.find_element_by_xpath('//*[@id="okta-signin-submit"]').click()
driver.execute_script("window.open('about:blank', 'tab3');")
driver.switch_to_window("tab3")
driver.get('https://github.com')
signInGithub = driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/a[1]').click()
delay = 3
try:
    meElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))
    print ("Page is ready")
except TimeoutException:
    print ("Loading took too much time!")
githubUsername = driver.find_element_by_xpath('//*[@id="login_field"]')
githubUsername.send_keys('email')
githubPassword = driver.find_element_by_xpath('//*[@id="password"]')
githubPassword.send_keys('pass')
githubSignIn = driver.find_element_by_xpath('//*[@id="login"]/div[4]/form/input[14]').click()
