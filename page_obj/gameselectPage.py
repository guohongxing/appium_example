#encoding=utf-8
import os,sys
from base import Page
sys.path.append('../models')
from time import sleep

from bootPage import bootPage
from models.operateYaml import getYam
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), p)
)

def get_devices():
    return getYam(PATH("yaml/android/gameselectPage.yaml"))
gs = get_devices()

class selectGame(Page):

	def button_click(self,*loc):
		element = self.find_element(*loc)
		if element:			
			element.click()
			
	def prefixa_condition(self):
		try:			
			hp = getYam(PATH("yaml/android/homePage.yaml"))
			WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.ID,hp[7].get('element-info'))))
			self.button_click(hp[2].get('element-type'),hp[2].get('element-info'))			
			return 1						
		except BaseException:
			ga1 = getYam(PATH("yaml/android/bootPage.yaml"))
			if self.find_element(ga1[0].get('element-type'),ga1[0].get('element-info')):
				bp = bootPage(self.driver)
				elements = bp.find_elements(ga1[2].get('element-type'),ga1[2].get('element-info'))
				index = len(elements)-1
				for i in range(index):
					bp.right_swipe()
				sleep(2)				
				self.button_click(ga1[3].get('element-type'),ga1[3].get('element-info'))
				self.button_click(hp[2].get('element-type'),hp[2].get('element-info'))				
				return 1
			else:
				print 'element no found,element:%s'%str(hp[7].get('element-info'))
				return 0

	def return_click(self):
		code = None
		code1 = None
		for i in range(len(gs)):
			if gs[i].get('name') == 'return':
				code = (gs[i].get('element-type'),gs[i].get('element-info'))
				break
		self.button_click(*code)
		hp = getYam(PATH("yaml/android/homePage.yaml"))
		for i in range(len(hp)):
			if hp[i].get('name') == 'homeregister-Page':
				code1 = (hp[i].get('element-type'),hp[i].get('element-info'))
				break
		element = self.find_element(*code1)
		return element
	#获取标题
	def title_display(self):
		code = None
		for i in range(len(gs)):
			if gs[i].get('name') == 'title':
				code = (gs[i].get('element-type'),gs[i].get('element-info'))
				break
		element = self.find_element(*code)
		text = element.get_attribute('text')
		return text

	#跳转到注册页面
	def skip_display(self):
		code = None
		for i in range(len(gs)):
			if gs[i].get('name') == 'skip':
				code = (gs[i].get('element-type'),gs[i].get('element-info'))
				break
		self.button_click(*code)
		rp = getYam(PATH("yaml/android/registerPage.yaml"))
		element = self.find_element(rp[0].get('element-type'),rp[0].get('element-info'))
		return element
	
	#向上滑动页面
	def swipe_up(self):
		code = None
		for i in range(len(gs)):
			if gs[i].get('name') == 'game-submit':
				code = (gs[i].get('element-type'),gs[i].get('element-info'))
				break
		swidth = self.get_window_width()
		height = self.get_window_height()
		self.swipe(swidth/2,height/5*4,swidth/2,height/5,500)
		while not self.find_element(*code):
			self.swipe(swidth/2,height/5*4,swidth/2,height/5,500)

	#点击任意游戏，进入该游戏页面	
	def enter_game(self,game='',enterPage=''):
		code = None
		if game == '王者荣耀'or game == '部落冲突' or game == '皇室战争' or game == 'STEAM' or game =='PSN' or game == 'XBOX':
			self.swipe_up()
		for i in range(len(gs)):
			if gs[i].get('describe') == game:
				code = (gs[i].get('element-type'),gs[i].get('element-info'))
				break
		self.find_element(*code).click()
		sleep(2)
		code1 = None
		for i in range(len(gs)):
			if gs[i].get('describe') == enterPage:
				code1 = (gs[i].get('element-type'),gs[i].get('element-info'))
				break
		return self.find_element(*code1)
		










	











