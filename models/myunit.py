from appium import webdriver
import unittest,os
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), p)
)
def appium_testcase(l_devices):
	desired_caps={}
	desired_caps['platformName'] = 'Android'
	desired_caps['platformVersion'] = l_devices['version']
	desired_caps['deviceName'] = l_devices['devices']
	desired_caps['udid'] = l_devices['devices']
	desired_caps['unicodeKeyboard'] = 'True'
	desired_caps['resetKeyboard'] = 'True'
	desired_caps['app'] = PATH('img/laoyuegou_2.5.0_009_qa.apk')
	desired_caps['noReset'] = 'True'
	desired_caps['noSign'] = 'True'
	desired_caps['newCommandTimeout'] = 60
	desired_caps['automationName'] = 'uiautomator2'	
	remote = 'http://127.0.0.1:'+str(l_devices['port'])+'/wd/hub'	
	driver = webdriver.Remote(remote,desired_caps)
	return driver


class myTest(unittest.TestCase):
	def __init__(self,methodName='runTest',l_devices=None):
		super(myTest,self).__init__(methodName)
		self.l_devices = l_devices

	def setUp(self):		
		self.driver = appium_testcase(self.l_devices)

	def tearDown(self):
		
		self.driver.quit()


	@staticmethod
	def parametrize(testcase_klass,l_devices=None):
		testloader = unittest.TestLoader()
		testnames = testloader.getTestCaseNames(testcase_klass)
		suite = unittest.TestSuite()
		for name in testnames:
			suite.addTest(testcase_klass(name,l_devices=l_devices))
		return suite
				
