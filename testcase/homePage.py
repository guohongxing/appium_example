import unittest
import sys,os
sys.path.append('../models')
sys.path.append('../page_obj')
from page_obj.homePage import homePage
from models.myunit import myTest
from models.operateYaml import getYam

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
def get_devices():
    return getYam(PATH("yaml/android/bootPage.yaml"))
ga = get_devices()


class homePage_Test(unittest.TestCase):
	'''主页面测试'''
	image = (ga[0].get('element-type'),ga[0].get('element-info'));
	login = (ga[1].get('element-type'),ga[1].get('element-info'));
	register = (ga[2].get('element-type'),ga[2].get('element-info'));
	wechat = (ga[3].get('element-type'),ga[3].get('element-info'));
	qq = (ga[4].get('element-type'),ga[4].get('element-info'));
	weibo = (ga[5].get('element-type'),ga[5].get('element-info'));


	def test_a_image_display(self):
		'''显示捞月狗图标'''
		hp = homePage(self.driver);
		index = hp.button_display(*self.image);
		self.assertTrue(index);

	def test_b_login_display(self):
		'''显示登录按钮'''
		hp = homePage(self.driver)
		index = hp.button_display(*self.login);
		self.assertTrue(index)

	def test_c_register_display(self):
		'''显示注册按钮'''
		hp = homePage(self.driver)
		index = hp.button_display(*self.register)
		self.assertTrue(index)

	def test_d_wechat_display(self):
		'''显示微信图标'''
		hp = homePage(self.driver)
		index = hp.button_display(*self.wechat)
		self.assertTrue(index)

	def test_e_qq_display(self):
		'''显示qq登录图标'''
		hp = homePage(self.driver)
		index = hp.button_display(*self.qq)
		self.assertTrue(index)

	def test_f_weibo_display(self):
		'''显示微博登录图标'''
		hp = homePage(self.driver)
		index = hp.button_display(*self.weibo)
		self.assertTrue(index)

	#def test_g_login_click(self):
		'''点击登录 进入登录界面'''






if __name__ == '__main__':
	unittest.main();

