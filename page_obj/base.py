from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class Page(object):
	def __init__(self,driver):
		self.driver = driver;

	def find_element(self,*loc):
		element = None
		type1 = None		
		if loc[0] == 'id':
			type1 = By.ID
		elif loc[0] == 'xpath':
			type1 = By.XPATH
		else:
			type1 = By.NAME
		try:
			element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((type1,loc[1])))
			return element
		except BaseException:
			print 'element no found %s'%str(loc)
			return element 	

	def find_elements(self,*loc):
		elements = None		
		try:
			elements = self.driver.find_elements(*loc)
			return elements
		except BaseException:
			print 'elements no found %s'%str(loc)
			return elements		

	def script(self,src):
		return self.driver.execute_script(src);

	def swipe(self,*loc):
		self.driver.swipe(*loc);

	def get_window_height(self):		
		return self.driver.get_window_size()['height'] 

	def get_window_width(self):
		return self.driver.get_window_size()['width']

	