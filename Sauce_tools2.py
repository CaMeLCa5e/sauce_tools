#!/usr/bin/env python

import unittest
from selenium import webdriver

SAUCE_USERNAME = "username_str"
SAUCE_ACCESS_KEY = "your-access-key-str"

class seleniumOnSauce(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Remote(
			desired_capabilities=webdriver.DesiredCapabilities.FIREFOX,
			command_executor="http://%s%s@ondemand.saucelabs.com:80/wd/hub"
			(SAUCE_USERNAME, SAUCE_ACCESS_KEY)
		)

	def test_from_sauce(self):
		self.driver.get('http:saucelabs/test/guinea-pig')
		self.assertEqual('Page Title - Sauce Labs', self.driver.title)
		body = self.driver.find_element_by_css_selector('body')
		self.assertIn('This page is a selenium sandbox', body.text)

	def tearDown(self):
		id = self.driver.session_id
		print 'Link to your jobL www.saucelabs.com/job/%s' %id
		self.driver

if __name__ == '__main__':
	unittest.main()

	