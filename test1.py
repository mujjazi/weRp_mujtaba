import time
import lxml
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


	# def testregister(self):

	# 	browser = self.browser

	# 	self.account = browser.find_element_by_class_name('Popup-button')
	# 	self.account.click()


	# 	self.signup = browser.find_element_by_class_name('SignInForm-signUpButton')
	# 	self.signup.click()


	# 	self.fn = browser.find_element_by_name('firstName')
	# 	self.fn.send_keys('Mujtaba')

	# 	self.ln = browser.find_element_by_name('lastName')
	# 	self.ln.send_keys('Mehdi')

	# 	self.em = browser.find_element_by_name('email')
	# 	self.em.send_keys('random22222d2221322nom@gmail.com')

	# 	self.num = browser.find_element_by_name('password')
	# 	self.num.send_keys('LaMadrid.1')

	# 	self.dist = browser.find_element_by_name('phoneNumber')
	# 	self.dist.send_keys('098901234')

	# 	self.addr = browser.find_element_by_class_name('Profile-signUpButton')
	# 	self.addr.click()
	# 	a= 1
			

		

	# 	time.sleep(10)

	# 	browser.get('https://www.nisnass.ae/customer')

	# 	time.sleep(10)

	# 	self.edit = browser.find_element_by_class_name('MyAccountPage-link')
	# 	self.edit.click()

	# 	self.emailn = browser.find_element_by_name('email')
		
	# 	time.sleep(10)
	# 	self.assertEqual(self.emailn.is_enabled(),False)
	# 	self.assertEquals(self.emailn.get_attribute('value'),'random22222d2221322nom@gmail.com (not editable)')

	# 	print(self.emailn.get_attribute('value'))

	# 	time.sleep(10)
	
	# 	self.phn = browser.find_element_by_name('phoneNumber')
	# 	self.phn.clear()
	# 	self.phn.send_keys('97167324238')

	# 	self.upd = browser.find_element_by_class_name('Profile-updateDetailsButton')

	# 	time.sleep(10)

	# 	#self.assertEquals(self.phn.get_attribute('textContent'),'97167324238')

	
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

		self.el = browser.find_elements_by_class_name('SizeSelection-option')
		#print(self.el)

		for self.option in self.el:
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

		self.el = browser.find_elements_by_class_name('SizeSelection-option')
		self.size = len(self.el)-1
		self.el[self.size].click()

		
		time.sleep(5)

		self.cl = browser.find_element_by_class_name('Popup-iconLink').click()
		self.name = browser.find_elements_by_class_name('CartItem-name')
		print(self.name)

		time.sleep(10)

	def tearDown(self):

		self.browser.quit()


		if __name__ == '__main__':
			unittest.main()



