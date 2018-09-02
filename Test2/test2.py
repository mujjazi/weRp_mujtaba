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
	

		self.fblgne = browser.find_element_by_name("email")
		self.fblgne.send_keys('samad@werplay.com')

		self.fblgnp = browser.find_element_by_name("pass")
		self.fblgnp.send_keys('werplayru55')

		self.fblgnb = browser.find_element_by_name("login")
		self.fblgnb.click()


	def testproducts(self):

		browser = self.browser
		browser.get('https://www.ounass.ae/clothing/')

		try:
    			self.elem = browser.find_element_by_id("onesignal-popover-cancel-button")
    			self.elem.click()
		except NoSuchElementException:  #spelling error making this code not work as expected
    			pass

		time.sleep(5)

		items = browser.find_elements_by_class_name('product-item-wrapper')

		

		time.sleep(10)


		elcon = browser.find_element_by_class_name('load-more')

		hover = ActionChains(browser).move_to_element(elcon)
		hover.perform()
		time.sleep(10)

		self.uitems = browser.find_elements_by_class_name('product-item-wrapper')

		countbefore = len(self.uitems)

		time.sleep(10)

		elcon.click()



		time.sleep(10)
		
		self.unitems = browser.find_elements_by_class_name('product-item-wrapper')


		print(len(self.unitems))

		countafter = len(self.unitems)

		self.assertNotEquals(countbefore,countafter,'Erro! New items does not load')

		def tearDown(self):

			self.browser.quit()


		if __name__ == '__main__':
			unittest.main()



