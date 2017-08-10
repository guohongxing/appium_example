#encoding=utf-8
from time import sleep
import unittest,sys,os
sys.path.append('../models')
sys.path.append('../page_obj')
from page_obj.bootPage import bootPage
from models.myunit import myTest
from models.operateYaml import getYam
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), p)
)
def get_devices():
    return getYam(PATH("yaml/android/bootPage.yaml"))
ga = get_devices()

class bootPage_Test(myTest):
	'''引导页测试'''
	firstPage = (ga[0].get('element-type'),ga[0].get('element-info'))
	secondPage = (ga[1].get('element-type'),ga[1].get('element-info'))
	points = (ga[2].get('element-type'),ga[2].get('element-info'))	
	button = (ga[3].get('element-type'),ga[3].get('element-info'))
	login_regist =  (ga[4].get('element-type'),ga[4].get('element-info'))

	
	def test_a_open_fristPage(self):
		'''引导页打开第一页'''
		try:
			WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH,ga[0].get('element-info'))))	
		except BaseException:
			print 'element timeout element:%s'%ga[0].get('element-info')
			self.assertTrue(bool(0))
			return			
		bp = bootPage(self.driver)			
		element = bp.find_element(*self.firstPage)
		self.assertTrue(element)
	
	def test_b_leftSwipe_firstPage(self):
		'''左滑第一页引导页'''		
		try:
			WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH,ga[0].get('element-info'))))	
		except BaseException:
			print 'element timeout element:%s'%ga[0].get('element-info')
			self.assertTrue(bool(0))
			return		
		bp = bootPage(self.driver)				
		bp.left_swipe()
		element = bp.find_element(*self.firstPage)		
		self.assertTrue(element)

	
	def test_c_rightSwipe_middlePage(self):
		'''右滑到第二页引导页'''		
		try:
			WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH,ga[0].get('element-info'))))	
		except BaseException:
			print 'element timeout element:%s'%ga[0].get('element-info')
			self.assertTrue(bool(0))
			return			
		bp = bootPage(self.driver)	
		elements = bp.find_elements(*self.points)
		if elements:
			if len(elements) >= 2:
				bp.right_swipe()
				element=bp.find_element(*self.secondPage)
				self.assertTrue(element)
		else:
			self.assertTrue(elements)	
		
	
	def test_d_rightSwipe_lastPage(self):
		'''最后一页引导页 显示按钮'''		
		try:
			WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH,ga[0].get('element-info'))))	
		except BaseException:
			print 'element timeout element:%s'%ga[0].get('element-info')
			self.assertTrue(bool(0))
			return			
		bp = bootPage(self.driver)	
		elements = bp.find_elements(*self.points)			
		if elements:			
			for i in range(len(elements)-1):
				bp.right_swipe()
			sleep(2)
			element = bp.find_element(*self.button)
			if element:
				text= element.get_attribute('text')
				self.assertEqual(text,u'立刻体验')
			else:
				self.assertTrue(element)
		else:
			self.assertTrue(elements)

	def test_e_clickbutton(self):
		'''进去登陆页面'''
		try:
			WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.XPATH,ga[0].get('element-info'))))	
		except BaseException:
			print 'element timeout element:%s'%ga[0].get('element-info')
			self.assertTrue(bool(0))
			return		
		bp = bootPage(self.driver)	
		elements = bp.find_elements(*self.points)			
		if elements:			
			for i in range(len(elements)-1):
				bp.right_swipe()			
			bp.find_element(*self.button).click()
			loginButton = bp.find_element(*self.login_regist)
			self.assertTrue(loginButton)			
		else:
			self.assertTrue(elements)




if __name__ == '__main__':
	unittest.main();


