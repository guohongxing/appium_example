#encoding=utf-8
__auth__='guohongxing'
from selenium.webdriver.common.by import By
from base import Page

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), p)
)

class bootPage(Page):
	'''引导页'''

	def left_swipe(self):
		width = self.get_window_width()
		height =self.get_window_height()
		self.swipe(width/6,height/2,width-10,height/2,500)

	def right_swipe(self):
		width = self.get_window_width()
		height =self.get_window_height()
		self.swipe(width-10,height/2,width/6,height/2,500)



