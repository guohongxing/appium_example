#encoding=utf-8
import os,sys
from base import Page
sys.path.append('../models')
from loginPage import loginPage
from models.operateYaml import getYam
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), p)
)
def get_devices():
    return getYam(PATH("yaml/android/forgetpasswordPage.yaml"))
fp = get_devices()

class forgetpassword(Page):
	def prefixa_condition(self):
		ga = getYam(PATH("yaml/android/loginPage.yaml"))
		username = (ga[5].get('element-type'),ga[5].get('element-info'))
		lp = loginPage(self.driver)
		lp.prefixa_condition()		
		element = lp.img_display(*username)
		index = lp.username_input(element,'10000000100')
		if index == 2:
			fp_button =  (ga[13].get('element-type'),ga[13].get('element-info'))			
			lp.button_click(*fp_button)
			return 'True'
		else:
			return 'False'
	#输入验证码
	def input_code(self,message=' '):
		code = None
		for i in range(len(fp)):
			if fp[i].get('name') == 'code_text':
				code = (fp[i].get('element-type'),fp[i].get('element-info'))
				break		
		element = self.find_element(*code)
		sleep(2)		
		element.send_keys(message)
	#输入密码
	def input_password(self,message=' '):
		code = None
		for i in range(len(fp)):
			if fp[i].get('name') == 'password':
				code = (fp[i].get('element-type'),fp[i].get('element-info'))
				break
		element = self.find_element(*code)		
		element.send_keys(message)
	#验证输入的验证码是否正确
	def validate_codetext(self,code='',message1=''):
		self.input_code(code)
		self.input_password('8430251')
		self.finish_click()
		message = '//*[@text=\'{}\']'.format(message1)	
		element = None
		try:
			element= WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,message)))
			return element
		except BaseException:
			return element
		
	#验证输入的密码合法性
	def validate_password(self,code='',message1=''):
		self.input_code('120110')
		self.input_password(code)
		self.finish_click()
		message = '//*[@text=\'{}\']'.format(message1)
		element = None
		try:
			element= WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,message)))
			return element
		except BaseException:
			return element

	#显示隐藏密码
	def Show_hidden_password(self,password=''):
		self.input_password(password)
		code = None
		for i in range(len(fp)):
			if fp[i].get('name') == 'show_password':
				code = (fp[i].get('element-type'),fp[i].get('element-info'))
				break
		element = self.find_element(*code)		
		text = element.get_attribute('text')
		return text

	#点击完成按钮
	def finish_click(self):
		code = None
		for i in range(len(fp)):
			if fp[i].get('name') == 'finish_button':
				code = (fp[i].get('element-type'),fp[i].get('element-info'))
				break
		self.find_element(*code).click()

	#点击发送验证码
	def code_button_click(self,message1=''):
		code = None
		for i in range(len(fp)):
			if fp[i].get('name') == 'getcode':
				code = (fp[i].get('element-type'),fp[i].get('element-info'))
				break
		self.find_element(*code).click()
		message = '//*[@text=\'{}\']'.format(message1)
		element = None			
		try:
			element= WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,message)))
			return element
		except BaseException:
			return element
	#获取语音验证码
	def get_voice_click(self,message1=''):
		code = None
		for i in range(len(fp)):
			if fp[i].get('name') == 'get_voice':
				code = (fp[i].get('element-type'),fp[i].get('element-info'))
				break
		self.find_element(*code).click()
		message = '//*[@text=\'{}\']'.format(message1)	
		element= None		
		try:
			element= WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,message)))
			return element
		except BaseException:
			return element















		

