#encoding=utf-8
from base import Page
from time import sleep
import os,sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
sys.path.append('../models')
from models.operateYaml import getYam
from bootPage import bootPage

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), p)
)

def get_devices():
    return getYam(PATH("yaml/android/bootPage.yaml"))
ga = get_devices()

class homePage(Page):
	points = (ga[2].get('element-type'),ga[2].get('element-info'))	
	button = (ga[3].get('element-type'),ga[3].get('element-info'))
	'''主页面'''
	def button_display(self,*loc):
		element = self.find_element(*loc)		
		return element	

	#点击按钮
	def button_click(self,*loc):
		element = self.find_element(*loc)
		if element:
			element.click()
			

	#进入主页前置条件	
	def prefixa_condition(self,*loc):
		try:
			WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc))
			return 1			
		except BaseException:			
			if self.find_element(ga[0].get('element-type'),ga[0].get('element-info')):
				bp = bootPage(self.driver)
				elements = bp.find_elements(*self.points)
				index = len(elements)-1
				for i in range(index):
					bp.right_swipe()
				sleep(2)
				bp.find_element(*self.button).click()
				return 1				
			else:
				print 'no found element,element:%s'%str(loc)
				return 0
	
	
		



		

				
			


