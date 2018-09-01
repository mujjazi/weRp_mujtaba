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
		self.browser.get('https://www.ounass.ae/')


	def testfacebook(self):

		browser = self.browser

		#Clicking remind me later popup

		self.rem = browser.find_element_by_class_name("remind")
		self.rem.click()

		#Implicit clicking with error handling

		try:
    			self.elem = browser.find_element_by_id("onesignal-popover-cancel-button")
    			self.elem.click()
		except NoSuchElementException:  #spelling error making this code not work as expected
    			pass

		time.sleep(5)

		self.lgn = browser.find_element_by_class_name("login-button")
		self.lgn.click()

		time.sleep(10)


		

		self.algn = browser.find_element_by_class_name("loginWithAmber")
		self.algn.click()
		time.sleep(10)


		
		frame = browser.find_element_by_tag_name('iframe')
		browser.switch_to_frame(frame)
     

		time.sleep(10)

		self.fbbtn = browser.find_element_by_class_name("login_with_facebook")
		self.fbbtn.click()

		time.sleep(10)


		frame = browser.find_element_by_tag_name('iframe')
		browser.switch_to_frame(frame)


		time.sleep(10)


		print browser.window_handles
		print browser.window_handles[1]
		self.child = browser.window_handles[1]
		browser.switch_to_window(self.child) 

		# for handle in driver.window_handles:
  #   			print handle
  #   			#driver.switch_to.window(handle)
	

		self.fblgne = browser.find_element_by_name("email")
		self.fblgne.send_keys('samad@werplay.com')

		self.fblgnp = browser.find_element_by_name("pass")
		self.fblgnp.send_keys('werplayru55')

		self.fblgnb = browser.find_element_by_name("login")
		self.fblgnb.click()


	# def testbag(self):

	# 	browser = self.browser

	# 	self.search = browser.find_element_by_class_name('QuickSearch-textBox')
	# 	self.search.send_keys('Hydration Mask')
	# 	self.search.submit()

	# 	self.prod= browser.find_element_by_class_name('Product-media')
	# 	self.prod.click()

	# 	time.sleep(5)

	# 	self.btn = browser.find_element_by_class_name('PDP-addToBag')
	# 	self.btn.click()


	# 	time.sleep(5)


	# 	#Classic Pumps code

	# 	self.search = browser.find_element_by_class_name('QuickSearch-textBox')
	# 	self.search.send_keys('Zitah Classic Pumps')
	# 	self.search.submit()

	# 	self.prod= browser.find_element_by_class_name('Product-media')
	# 	self.prod.click()

	# 	time.sleep(5)

	# 	self.color =  browser.find_element_by_css_selector("img[alt='color_Pink']")
	# 	self.color.click()
		
	# 	#self.size = browser.find_elements_by_class_name("SizeSelection-option")
	# 	#self.size.click()

	# 	self.el1 = browser.find_elements_by_class_name('SizeSelection-option')
	# 	#print(self.el)

	# 	for self.option in self.el1:
 #    			#print(self.option.text)	
 #    			if self.option.text == '9.5':
 #        			self.option.click() # select() in earlier versions of webdriver
 #        			break

	# 	self.btn = browser.find_element_by_class_name('PDP-addToBag')
	# 	self.btn.click()

	# 	#Sandals code

	# 	self.search = browser.find_element_by_class_name('QuickSearch-textBox')
	# 	self.search.send_keys('Sandals')
	# 	self.search.submit()

	# 	self.prod= browser.find_element_by_class_name('Product-media')
	# 	self.prod.click()

	# 	time.sleep(5)

	# 	self.el = browser.find_elements_by_class_name('SizeSelection-option')
		
	# 	for self.option in self.el:
 #    			#print(self.option.text)	
 #    			if self.option.text == '8':
 #        			self.option.click() # select() in earlier versions of webdriver
 #        			break
		

	# 	self.btn = browser.find_element_by_class_name('PDP-addToBag')
	# 	self.btn.click()
		
	# 	time.sleep(5)

	# 	self.cl = browser.find_element_by_class_name('Popup-notificationBadge').click()
	# 	self.name = browser.find_elements_by_class_name('CartItem-name')
		
	# 	for element in browser.find_elements_by_class_name('CartItem-name'):
 #       			print element.text

	# 	time.sleep(10)

		def tearDown(self):

			self.browser.quit()


		if __name__ == '__main__':
			unittest.main()



