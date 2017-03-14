import unittest;
import sys;
sys.path.append('../models');
sys.path.append('../page_obj');
from page_obj.homePage import homePage;
from models.myunit import myTest;


class homePage_Test(unittest.TestCase):
	'''主页面测试'''
	image = ('id','com.laoyuegou.android:id/iv_logo');
	login = ('id','com.laoyuegou.android:id/btn_login');
	register = ('id','com.laoyuegou.android:id/btn_regist');
	wechat = ('id','com.laoyuegou.android:id/weixinBtn');
	qq = ('id','com.laoyuegou.android:id/QQBtn');
	weibo = ('id','com.laoyuegou.android:id/weiboBtn');


	def test_a_image_display(self):
		'''显示捞月狗图标'''
		hp = homePage(self.driver);
		index = hp.button_display(*self.image);
		self.assertTrue(index);

	def test_b_login_display(self):
		'''显示登录按钮'''
		hp = homePage(self.driver);
		index = hp.button_display(*self.login);
		self.assertTrue(index);

	def test_c_register_display(self):
		'''显示注册按钮'''
		hp = homePage(self.driver);
		index = hp.button_display(*self.register);
		self.assertTrue(index);

	def test_d_wechat_display(self):
		'''显示微信图标'''
		hp = homePage(self.driver);
		index = hp.button_display(*self.wechat);
		self.assertTrue(index);

	def test_e_qq_display(self):
		'''显示qq登录图标'''
		hp = homePage(self.driver);
		index = hp.button_display(*self.qq);
		self.assertTrue(index);

	def test_f_weibo_display(self):
		'''显示微博登录图标'''
		hp = homePage(self.driver);
		index = hp.button_display(*self.weibo);
		self.assertTrue(index);

	#def test_g_login_click(self):
		'''点击登录 进入登录界面'''






if __name__ == '__main__':
	unittest.main();

