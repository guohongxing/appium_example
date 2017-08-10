#encoding=utf-8
__auth__='guohongxing'
import os,sys 
from base import Page
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
sys.path.append('../models')
from bootPage import bootPage
from models.operateYaml import getYam
from selenium.webdriver.common.by import By

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), p)
)

def get_devices():
    return getYam(PATH("yaml/android/bootPage.yaml"))
ga = get_devices()

class loginPage(Page):
	'''主页面'''
	def img_display(self,*loc):
		element = self.find_element(*loc)
		return element

	def button_click(self,*loc):
		element = self.find_element(*loc)
		if element:
			element.click()

	def getbutton_text(self,*loc):
		element = self.find_element(*loc)
		if element:				
			text = element.get_attribute('text')
			return text

	#进入登录界面前置条件	
	def prefixa_condition(self):
		try:
			hp = getYam(PATH("yaml/android/homePage.yaml"))
			WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.ID,hp[7].get('element-info'))))
			self.button_click(hp[1].get('element-type'),hp[1].get('element-info'))
			sleep(2)
			return 1						
		except BaseException:			
			if self.find_element(ga[0].get('element-type'),ga[0].get('element-info')):
				bp = bootPage(self.driver)
				elements = bp.find_elements(ga[2].get('element-type'),ga[2].get('element-info'))
				index = len(elements)-1
				for i in range(index):
					bp.right_swipe()
				sleep(2)
				bp.find_element(ga[3].get('element-type'),ga[3].get('element-info')).click()
				self.button_click(hp[1].get('element-type'),hp[1].get('element-info'))
				sleep(2)
				return 1
			else:
				print 'element no found,element:%s'%str(hp[7].get('element-info'))
				return 0
	'''
	登录框输入账户名信息是否正确 
	return 1:跳出提示框 2：跳入下一步 3：账户信息输入错误 
	'''		
	def isSuccessful_username(self):
		lp = getYam(PATH("yaml/android/loginPage.yaml"))
		self.button_click(lp[6].get('element-type'),lp[6].get('element-info'))
		sleep(2)
		#提示框是否显示
		isDisplay = self.img_display(lp[8].get('element-type'),lp[8].get('element-info'))
		#是否跳入下一步
		isEnterNext = self.img_display(lp[9].get('element-type'),lp[9].get('element-info'))
		if isDisplay:
			return 1
		if isEnterNext:
			return 2
		if (not isDisplay) and (not isEnterNext):
			return 3

	def username_input(self,element,username):		
		element.send_keys(username)		
		index = self.isSuccessful_username()
		return index

	def password_input(self,index,message1,*loc):
		lp = getYam(PATH("yaml/android/loginPage.yaml"))
		self.find_element(lp[12].get('element-type'),lp[12].get('element-info')).send_keys('125125')
		sleep(2)
		if index == 1:
			size = 0
			while size <= 5 :
				self.button_click(*loc)	
				size = size+1
		else:
			self.button_click(*loc)	
		message = '//*[@text=\'{}\']'.format(message1)	
		element= WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,message)))
		return element
		
        
	



