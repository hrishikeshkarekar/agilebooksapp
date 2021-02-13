import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

import unittest
import os
import sys
import pytest
import time

class FunctionalTests_SearchGivesResults(unittest.TestCase):

	def setUp(self):
		options = webdriver.ChromeOptions()
		options.add_argument('--no-sandbox')
		self.driver = webdriver.Chrome(chrome_options=options)
		self.driver.implicitly_wait(300)

	def test_selenium(self):
		webAppUrl = pytest.config.getoption('webAppUrl')
		start_timestamp = time.time()
		end_timestamp = start_timestamp + 60*10
		while True:
			try:
				response = self.driver.get(webAppUrl)
				element = self.driver.find_element_by_id("searchterm")
				element.send_keys("kanban")

				element = self.driver.find_element_by_id("searchnowbtn")
				element.send_keys(Keys.RETURN)

				try:
					# Wait as long as required, or maximum of 10 sec for alert to appear
					WebDriverWait(self.driver, 10)
					element = self.driver.find_element_by_id("totalbooksreturned")
					self.assertNotEqual(element.text, "", "Value returned is bad - " + element.text)

				except (TimeoutException) as ex:
					print('"##vso[task.logissue type=error;]Test test_selenium failed with timeout exception: ' + str(ex))
					current_timestamp = time.time()
					if (current_timestamp > end_timestamp):
						raise
					time.sleep(5)

				break
			except Exception as e:
				print('"##vso[task.logissue type=error;]Test test_selenium failed with error: ' + str(e))
				current_timestamp = time.time()
				if(current_timestamp > end_timestamp):
					raise
				time.sleep(5)

	def tearDown(self):
		try:
			self.driver.quit()
		except Exception as e:
			print('tearDown.Error occurred while trying to close the selenium chrome driver: ' + str(e))
