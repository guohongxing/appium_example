
#encoding=utf-8
from time import sleep
import unittest
import sys,os
sys.path.append('../models')
sys.path.append('../page_obj')
from page_obj.homePage import homePage
from models.myunit import myTest
from models.operateYaml import getYam
from selenium.webdriver.common.by import By

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), p)
)
def get_devices():
    return getYam(PATH("yaml/android/homePage.yaml"))
ga = get_devices()


class homePage_Test(myTest):
	'''主页面测试'''

	image = (ga[0].get('element-type'),ga[0].get('element-info'))
	login = (ga[1].get('element-type'),ga[1].get('element-info'))
	register = (ga[2].get('element-type'),ga[2].get('element-info'))
	wechat = (ga[3].get('element-type'),ga[3].get('element-info'))
	qq = (ga[4].get('element-type'),ga[4].get('element-info'))
	weibo = (ga[5].get('element-type'),ga[5].get('element-info'))
	#登录界面
	loginPage = (ga[6].get('element-type'),ga[6].get('element-info'))
	#注册--游戏选择界面
	gameSwitch = (ga[8].get('element-type'),ga[8].get('element-info'))

	home = (By.ID,ga[1].get('element-info'))

	
	
	def test_a_image_display(self):
		'''显示捞月狗图标'''		
		hp = homePage(self.driver)
		isfound = hp.prefixa_condition(*self.home)
		if isfound:
			index = hp.button_display(*self.image)
			self.assertTrue(index)
		else:
			self.assertTrue(isfound)				
	
	def test_b_login_display(self):
		'''显示登录按钮'''
		hp = homePage(self.driver)
		isfound = hp.prefixa_condition(*self.home)
		if isfound:
			index = hp.button_display(*self.login);
			self.assertTrue(index)
		else:
			self.assertTrue(isfound)
	
	def test_c_register_display(self):
		'''显示注册按钮'''		
		hp = homePage(self.driver)
		isfound = hp.prefixa_condition(*self.home)
		if isfound:
			index = hp.button_display(*self.register)
			self.assertTrue(index)
		else:
			self.assertTrue(isfound)
	
	def test_d_wechat_display(self):
		'''显示微信图标'''		
		hp = homePage(self.driver)
		isfound = hp.prefixa_condition(*self.home)	
		if isfound:
			index = hp.button_display(*self.wechat)
			self.assertTrue(index)
		else:
			self.assertTrue(isfound)

	
	def test_e_qq_display(self):
		'''显示qq登录图标'''		
		hp = homePage(self.driver)
		isfound = hp.prefixa_condition(*self.home)	
		if isfound:
			index = hp.button_display(*self.qq)
			self.assertTrue(index)
		else:
			self.assertTrue(isfound)
	
	def test_f_weibo_display(self):
		'''显示微博登录图标'''		
		hp = homePage(self.driver)
		isfound = hp.prefixa_condition(*self.home)	
		if isfound:
			index = hp.button_display(*self.weibo)
			self.assertTrue(index)
		else:
			self.assertTrue(isfound)
	
	def test_g_register_click(self):
		'''点击注册 进入注册页面'''		
		hp = homePage(self.driver)
		isfound = hp.prefixa_condition(*self.home)	
		if isfound:
			hp.button_click(*self.register)
			sleep(2)
			element = hp.find_element(*self.gameSwitch)
			self.assertTrue(element)
		else:
			self.assertTrue(isfound)
	
	def test_h_login_click(self):
		'''点击登录 进入登录界面'''		
		hp = homePage(self.driver)
		isfound = hp.prefixa_condition(*self.home)
		if isfound:
			hp.button_click(*self.login)
			sleep(2)
			element = hp.find_element(*self.loginPage)		
			self.assertTrue(element)
		else:
			self.assertTrue(isfound)

if __name__ == '__main__':
	unittest.main();

