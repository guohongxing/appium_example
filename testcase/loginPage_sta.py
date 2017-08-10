#encoding=utf-8
import sys,os
sys.path.append('../models')
sys.path.append('../page_obj')
from models.myunit import myTest
from models.operateYaml import getYam
from page_obj.loginPage import loginPage
from time import sleep
import unittest

reload(sys)
sys.setdefaultencoding('utf-8')
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), p)
)
def get_devices():
    return getYam(PATH("yaml/android/loginPage.yaml"))
ga = get_devices()

class loginPage_Test(myTest):
	'''登录模块测试'''
	title = (ga[0].get('element-type'),ga[0].get('element-info'))
	returnButton = (ga[1].get('element-type'),ga[1].get('element-info'))
	phoneImage = (ga[2].get('element-type'),ga[2].get('element-info'))
	code = (ga[3].get('element-type'),ga[3].get('element-info'))
	iconSelect = (ga[4].get('element-type'),ga[4].get('element-info'))
	username = (ga[5].get('element-type'),ga[5].get('element-info'))
	finishButton = (ga[6].get('element-type'),ga[6].get('element-info'))	
	suggest_cancel = (ga[10].get('element-type'),ga[10].get('element-info'))
	suggest = (ga[8].get('element-type'),ga[8].get('element-info'))
	suggest_register = (ga[11].get('element-type'),ga[11].get('element-info'))
	input_password = (ga[12].get('element-type'),ga[12].get('element-info'))
	fp_button =  (ga[13].get('element-type'),ga[13].get('element-info'))
	fp_page =  (ga[14].get('element-type'),ga[14].get('element-info'))

	@unittest.skip('1')
	def test_a_title_display(self):
		'''展示标题'''
		lp = loginPage(self.driver)
		isfound = lp.prefixa_condition()
		if isfound:
			text = lp.getbutton_text(*self.title)
			self.assertEqual(text,u'登录')
		else:
			self.assertTrue(isfound)
	@unittest.skip('2')
	def test_b_button_return(self):
		'''点击返回按钮 返回首页'''
		lp = loginPage(self.driver)
		isfound = lp.prefixa_condition()
		if isfound:
			lp.button_click(*self.returnButton)
			sleep(2)
			ha = getYam(PATH('yaml/android/homePage.yaml'))
			index = lp.img_display(ha[7].get('element-type'),ha[7].get('element-info'))
			self.assertTrue(index)
		else:
			self.assertTrue(isfound)
	@unittest.skip('3')
	def test_c_phone_display(self):
		'''手机图标按钮显示'''
		lp = loginPage(self.driver)
		isfound = lp.prefixa_condition()
		if isfound:
			index = lp.img_display(*self.phoneImage)
			self.assertTrue(index)
		else:
			self.assertTrue(isfound)
	@unittest.skip('4')
	def test_d_code_number(self):
		'''显示默认区号'''
		lp = loginPage(self.driver)
		isfound = lp.prefixa_condition()
		if isfound:
			text = lp.getbutton_text(*self.code)
			self.assertEqual(text,'+86')
		else:
			self.assertTrue(isfound)
	@unittest.skip('5')
	def test_e_code_select(self):
		'''点击区号，进入区号界面'''

		lp = loginPage(self.driver)
		isfound = lp.prefixa_condition() 
		if isfound:
			lp.button_click(*self.iconSelect)
			sleep(2)
			index = lp.img_display(*self.title)
			self.assertTrue(index)
		else:
			self.assertTrue(isfound)
	@unittest.skip('1')
	def test_f_codeSelete_return(self):
		'''进入区号页面，点击返回按钮，返回登录页面'''
		lp = loginPage(self.driver)
		isfound = lp.prefixa_condition()
		if isfound:
			lp.button_click(*self.iconSelect)
			sleep(2)
			lp.button_click(*self.returnButton)
			sleep(2)
			ha = getYam(PATH('yaml/android/homePage.yaml'))
			index = lp.img_display(ha[6].get('element-type'),ha[6].get('element-info'))
			self.assertTrue(index)
		else:
			self.assertTrue(isfound)
	
	def test_g_username_display(self):
		'''账户名输入框默认显示'''
		lp = loginPage(self.driver)
		isfound = lp.prefixa_condition()
		if isfound:
			lp.find_element(*self.username).clear()
			text = lp.getbutton_text(*self.username)
			print text
			self.assertEqual(text,u'请输入您的手机号')
		else:
			self.assertTrue(isfound)
	
	@unittest.skip('1')
	def test_i_login_username(self):
		'''账户名为空'''
		lp = loginPage(self.driver)
		isfound = lp.prefixa_condition()
		if isfound:
			lp.button_click(*self.username)
			sleep(2)
			element = lp.img_display(*self.username)
			index = lp.username_input(element,'11')
			self.assertEqual(index,3)
		else:
			self.assertTrue(isfound)
	@unittest.skip('1')
	def test_j_login_username(self):
		'''注册过的账户名'''
		lp = loginPage(self.driver)
		isfound = lp.prefixa_condition()
		if isfound:
			lp.button_click(*self.username)
			sleep(2)
			element = lp.img_display(*self.username)
			index = lp.username_input(element,'10000000100')
			self.assertEqual(index,2)
		else:
			self.assertTrue(isfound) 
	@unittest.skip('1')
	def test_k_login_username(self):
		'''未注册过的账户名'''
		lp = loginPage(self.driver)
		isfound = lp.prefixa_condition()
		if isfound:
			lp.button_click(*self.username)
			sleep(2)
			element = lp.img_display(*self.username)
			index = lp.username_input(element,'10000001400')
			self.assertEqual(index,1)
		else:
			self.assertTrue(isfound) 
	@unittest.skip('1')
	def test_l_login_username(self):
		'''输入账户长度超过11位'''
		user = '1000000183212513'
		lp = loginPage(self.driver)
		isfound = lp.prefixa_condition()
		if isfound:			
			element = lp.img_display(*self.username)			
			element.send_keys(user)
			text = element.get_attribute('text')
			text2 = user[0:11]			
			self.assertEqual(str(text),text2)
		else:
			self.assertTrue(isfound) 
	@unittest.skip('1')
	def test_m_prompt_box(self):
		#提示框点击取消，关闭提示框
		lp = loginPage(self.driver)
		isfound = lp.prefixa_condition()
		if isfound:
			lp.button_click(*self.username)
			sleep(2)
			element = lp.img_display(*self.username)
			index = lp.username_input(element,'10000001400')
			if index == 1:
				sleep(2)
				lp.button_click(*self.suggest_cancel)
				sleep(2)
				self.assertFalse(lp.img_display(*self.suggest))
		else:
			self.assertTrue(isfound)
	@unittest.skip('1')
	def test_n_prompt_box(self):
		#提示框点击去注册，跳转首页
		lp = loginPage(self.driver)
		isfound = lp.prefixa_condition()
		if isfound:
			lp.button_click(*self.username)
			sleep(2)
			element = lp.img_display(*self.username)
			index = lp.username_input(element,'10000001400')
			if index == 1:
				sleep(2)
				lp.button_click(*self.suggest_register)	
				ha = getYam(PATH('yaml/android/homePage.yaml'))			
				self.assertTrue(lp.img_display(ha[7].get('element-type'),ha[7].get('element-info')))
		else:
			self.assertTrue(isfound)
	@unittest.skip('8')
	def test_o_passworderror(self):
		'''密码输入错误'''
		lp = loginPage(self.driver)
		isfound = lp.prefixa_condition()
		if isfound:
			lp.button_click(*self.username)
			sleep(2)
			element = lp.img_display(*self.username)
			lp.username_input(element,'10000000011')
			sleep(2)
			message = '登录密码错误，请重试'
			index = lp.password_input(2,message,*self.finishButton)
			self.assertIsNotNone(index)	
		else:
			self.assertTrue(isfound)		
	@unittest.skip('8')
	def test_p_passwordErr(self):
		'''密码频繁输入错误'''
		lp = loginPage(self.driver)
		isfound = lp.prefixa_condition()
		if isfound:
			lp.button_click(*self.username)
			sleep(2)
			element = lp.img_display(*self.username)
			lp.username_input(element,'10000000100')
			sleep(2)
			message = '尝试登录太频繁，请一小时后重试'
			index = lp.password_input(1,message,*self.finishButton)
			self.assertIsNotNone(index)
		else:
			self.assertTrue(isfound)
	@unittest.skip('1')
	def test_q_fp_button(self):
		'''点击忘记密码，进入设置密码页面'''
		lp = loginPage(self.driver)
		isfound = lp.prefixa_condition()
		if isfound:
			lp.button_click(*self.username)
			sleep(2)
			element = lp.img_display(*self.username)
			index = lp.username_input(element,'10000000100')
			if index == 2:
				lp.button_click(*self.fp_button)
				element = lp.img_display(*self.fp_page)				
				self.assertTrue(element)
			else:
				print 'username no register'
				self.assertTrue(0)
		else:
			self.assertTrue(isfound)
	@unittest.skip('1')
	def test_q_passwordringht(self):
		'''密码输入正确'''
		lp = loginPage(self.driver)
		isfound = lp.prefixa_condition()
		if isfound:
			lp.button_click(*self.username)
			sleep(2)
			element = lp.img_display(*self.username)
			lp.username_input(element,'10000000100')
			lp.find_element(*self.input_password).send_keys('120110')
			lp.button_click(*self.finishButton)
			sleep(3)
			mp = getYam(PATH("yaml/android/messagePage.yaml"))
			self.assertTrue(lp.img_display(mp[0].get('element-type'),mp[0].get('element-info')))
		else:
			self.assertTrue(isfound)





		





	


