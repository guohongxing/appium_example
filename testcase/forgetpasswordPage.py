#encoding=utf-8
import unittest,os,sys
sys.path.append('../models')
sys.path.append('../page_obj')
from models.myunit import myTest
from models.operateYaml import getYam
from page_obj.forgetpasswordPage import forgetpassword
from time import sleep

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), p)
)
def get_devices():
    return getYam(PATH("yaml/android/forgetpasswordPage.yaml"))
ga = get_devices()

class forgetpasswordPage_Test(myTest):
	'''忘记密码页面'''
	@unittest.skip(1)
	def test_a_title(self):
		'''标题展示'''
		fp = forgetpassword(self.driver)
		isfound = fp.prefixa_condition()
		if isfound:
			sleep(2)
			title =(ga[0].get('element-type'),ga[0].get('element-info'))
			element = fp.find_element(*title)
			print element				
			text = element.get_attribute('text')
			self.assertEqual(text,'设置密码')
			
		else:
			self.assertTrue(isfound)	
	@unittest.skip(1)
	def test_b_code(self):
		'''输入短信校验码小于6位'''
		fp = forgetpassword(self.driver)
		isfound = fp.prefixa_condition()
		if isfound:
			sleep(2)
			element = fp.validate_codetext('11','验证码错误，请重新输入')
			self.assertIsNotNone(element)
		else:
			self.assertTrue(isfound)
	@unittest.skip(1)
	def test_c_code(self):
		'''输入验证码特殊符号,英文'''
		fp = forgetpassword(self.driver)
		isfound = fp.prefixa_condition()
		if isfound:
			sleep(2)
			element = fp.validate_codetext('dfdsf1','验证码错误，请重新输入')
			self.assertIsNotNone(element) 
		else:
			self.assertTrue(isfound)
	@unittest.skip(1)
	def test_d_password(self):
		'''登录密码为小于6位'''
		fp = forgetpassword(self.driver)
		isfound = fp.prefixa_condition()
		if isfound:
			sleep(2)
			element = fp.validate_password('12')
			self.assertIsNone(element)
		else:
			self.assertTrue(isfound)
	@unittest.skip(1)
	def test_g_password(self):
		'''登录密码为大于6位，小于12位'''
		fp = forgetpassword(self.driver)
		isfound = fp.prefixa_condition()
		if isfound:
			sleep(2)
			fp.validate_password('1234567')
			mp = getYam(PATH("yaml/android/messagePage.yaml"))
			element = fp.find_element(mp[0].get('element-type'),mp[0].get('element-info'))
			self.assertTrue(element)
		else:
			self.assertTrue(isfound)
	
	def test_e_getcode(self):
		'''点击获取校验码'''
		fp = forgetpassword(self.driver)
		isfound = fp.prefixa_condition()
		if isfound:
			sleep(2)
			element = fp.code_button_click('验证码已成功发送，请注意查收')
			self.assertTrue(element)
		else:
			self.assertTrue(isfound)
	
	def test_f_getvoice(self):
		'''点击获取语音'''
		fp = forgetpassword(self.driver)
		isfound = fp.prefixa_condition()
		if isfound:
			sleep(2)
			element = fp.get_voice_click('验证码已成功发送，请注意查收')
			self.assertTrue(element)
		else:
			self.assertTrue(isfound)








	






