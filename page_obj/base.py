class Page(object):
	def __init__(self,driver):
		self.driver = driver;

	def find_element(self,*loc):
		return self.driver.find_element(*loc);

	def find_elements(self,*loc):
		return self.driver.find_elements(*loc);

	def script(self,src):
		return self.driver.execute_script(src);

	def swipe(self,*loc):
		self.driver.swipe(*loc);

	def get_window_height(self):
		return self.driver.get_window_size()['height'] 

	def get_window_width(self):
		return self.driver.get_window_size()['width']