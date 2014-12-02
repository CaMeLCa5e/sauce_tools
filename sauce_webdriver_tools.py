#webdriver tools
#/usr/bin/env python

from selenium import webdriver

SAUCE_USERNAME = "username-string"
SAUCE_ACCESS_KEY = "access-key-string"

driver = webdriver.Remote(
	webdriver.get.FIREFOX,
	command_executor = "http://%s:%s@ondemand.saucelabs.com:80/wd/hub"
	(SAUCE_USERNAME, SAUCE_ACCESS_KEY)
)
driver.get('www.saucelabs/test/guinea-pig')
id = self.driver.session_id
print "link to your job: www.saucelabs.com/jobs/%s" % id
driver.quit