import time
import lxml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains



#Running the website using Chrome Drive, Can be done for Firefox and IE too

browser = webdriver.Chrome()
browser.get('https://www.nisnass.ae/')

account = browser.find_element_by_class_name('Popup-button')
account.click()


signup = browser.find_element_by_class_name('SignInForm-signUpButton')
signup.click()

#Closing the popups to ensure elements are visible


#Filling the delivery form

fn = browser.find_element_by_name('firstName')
fn.send_keys('Mujtaba')

ln = browser.find_element_by_name('lastName')
ln.send_keys('Mehdi')

em = browser.find_element_by_name('email')
em.send_keys('muj5@gmail.com')

num = browser.find_element_by_name('password')
num.send_keys('LaMadrid.1')

dist = browser.find_element_by_name('phoneNumber')
dist.send_keys('098901234')

addr = browser.find_element_by_class_name('Profile-signUpButton')
addr.click()



time.sleep(10)

browser.get('https://www.nisnass.ae/customer')

time.sleep(10)

edit = browser.find_element_by_class_name('MyAccountPage-link')
edit.click()

emailn = browser.find_element_by_name('email')

a = emailn.is_enabled()
if (a =='False'):
  print('PASS - Element Disabled ')

else:
  print('FAIL') 


phn = browser.find_element_by_name('phoneNumber')
phn.clear()
phn.send_keys('198901234')

upd = browser.find_element_by_class_name('Profile-updateDetailsButton')

time.sleep(10)




#time.sleep(20)

browser.quit()