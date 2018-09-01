import time
import lxml
import string, random
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains



class TestOunass(unittest.TestCase):

	def setUp(self):
		
		self.browser = webdriver.Chrome()
		self.browser.get('https://www.nisnass.ae/')


	def testregister(self):

		browser = self.browser

		#Clicking on the Account button to Sign up

		self.account = browser.find_element_by_class_name('Popup-button')
		self.account.click()

		#Clicking the Sign Up button to open the registration form

		self.signup = browser.find_element_by_class_name('SignInForm-signUpButton')
		self.signup.click()

		#Filling the registration Form

		self.fn = browser.find_element_by_name('firstName')
		self.fn.send_keys('Mujtaba')

		self.ln = browser.find_element_by_name('lastName')
		self.ln.send_keys('Mehdi')

		#Generating Random Email everytime otherwise user is unable to register with same email
		rndem = ''.join(random.sample(string.ascii_lowercase, 6)) + '@gmail.com'
		
		self.em = browser.find_element_by_name('email')
		self.em.send_keys(rndem)

		self.num = browser.find_element_by_name('password')
		self.num.send_keys('LaMadrid.1')

		self.dist = browser.find_element_by_name('phoneNumber')
		self.dist.send_keys('098901234')

		self.addr = browser.find_element_by_class_name('Profile-signUpButton')
		self.addr.click()
		

		time.sleep(10)

		#Navigating to the Account page to validate whether correct details have been stored

		browser.get('https://www.nisnass.ae/customer')

		time.sleep(10)

		#Clicking the Edit button to view and verify the details

		self.edit = browser.find_element_by_class_name('MyAccountPage-link')
		self.edit.click()

		#Storing the Email element to later verify that it is not editable

		self.emailn = browser.find_element_by_name('email')
		
		time.sleep(10)
		
		self.assertEqual(self.emailn.is_enabled(),False)
		self.assertEquals(self.emailn.get_attribute('value'),rndem +' (not editable)')

		print(self.emailn.get_attribute('value'))

		time.sleep(10)
	
		self.phn = browser.find_element_by_name('phoneNumber')
		self.phn.clear()
		self.phn.send_keys('97167324238')

		self.phnu = browser.find_element_by_class_name('Profile-phoneNumber')
		self.assertEquals(self.phnu.get_attribute('value'),'97167324238')
		print(self.phnu.get_attribute('value'))

		#Clicking on the update button to update the details

		self.upd = browser.find_element_by_class_name('Profile-updateDetailsButton')

		time.sleep(10)

	
	def testbag(self):

		browser = self.browser

		self.search = browser.find_element_by_class_name('QuickSearch-textBox')
		self.search.send_keys('Hydration Mask')
		self.search.submit()

		self.prod= browser.find_element_by_class_name('Product-media')
		self.prod.click()

		time.sleep(5)

		self.btn = browser.find_element_by_class_name('PDP-addToBag')
		self.btn.click()


		time.sleep(5)


		#Classic Pumps code

		self.search = browser.find_element_by_class_name('QuickSearch-textBox')
		self.search.send_keys('Zitah Classic Pumps')
		self.search.submit()

		self.prod= browser.find_element_by_class_name('Product-media')
		self.prod.click()

		time.sleep(5)

		self.color =  browser.find_element_by_css_selector("img[alt='color_Pink']")
		self.color.click()
		
		#self.size = browser.find_elements_by_class_name("SizeSelection-option")
		#self.size.click()

		self.el1 = browser.find_elements_by_class_name('SizeSelection-option')
		#print(self.el)

		for self.option in self.el1:
    			#print(self.option.text)	
    			if self.option.text == '9.5':
        			self.option.click() # select() in earlier versions of webdriver
        			break

		self.btn = browser.find_element_by_class_name('PDP-addToBag')
		self.btn.click()

		#Sandals code

		self.search = browser.find_element_by_class_name('QuickSearch-textBox')
		self.search.send_keys('Sandals')
		self.search.submit()

		self.prod= browser.find_element_by_class_name('Product-media')
		self.prod.click()

		time.sleep(5)

		self.el = browser.find_elements_by_class_name('SizeSelection-option')
		
		for self.option in self.el:
    			#print(self.option.text)	
    			if self.option.text == '8':
        			self.option.click() # select() in earlier versions of webdriver
        			break
		

		self.btn = browser.find_element_by_class_name('PDP-addToBag')
		self.btn.click()
		
		time.sleep(5)

		self.cl = browser.find_element_by_class_name('Popup-notificationBadge').click()
		self.name = browser.find_elements_by_class_name('CartItem-name')
		
		for element in browser.find_elements_by_class_name('CartItem-name'):
       			print element.text

		time.sleep(10)

	def tearDown(self):

		self.browser.quit()


		if __name__ == '__main__':
			unittest.main()



