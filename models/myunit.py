from appium import webdriver;
import unittest

class myTest(unittest.TestCase):
	def setUp(self):
		desired_caps={}
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '4.2'
		desired_caps['deviceName'] = 'Android Emulator'
		desired_caps['app'] = 'F:\\laoyuegou\\img\\laoyuegou_2.4.9_009_qa.apk'
		desired_caps['noReset'] = 'true'
		self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps);		
	def tearDown(self):
		self.driver.quit();
				
