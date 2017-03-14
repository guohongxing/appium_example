#encoding=utf-8
from time import sleep;
import unittest,sys,os
sys.path.append('../models');
sys.path.append('../page_obj');
from page_obj.bootPage import bootPage;
from models.myunit import myTest;
from selenium.webdriver.support.ui import WebDriverWait;
from selenium.webdriver.support import expected_conditions as EC;
from selenium.webdriver.common.by import By;

class bootPage_Test(myTest):
	'''引导页测试'''
	firstPage = ('xpath',"//android.support.v4.view.ViewPager/android.widget.ImageView[@index='0']");
	secondPage = ('xpath',"//android.support.v4.view.ViewPager/android.widget.ImageView[@index='1']");
	points = ('xpath','//android.widget.LinearLayout/android.widget.ImageView');
	button =('id','com.laoyuegou.android:id/guide_end_button');
	login = ('id','com.laoyuegou.android:id/btn_login');

	
	def test_a_open_fristPage(self):
		'''引导页打开第一页'''			
		WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.CLASS_NAME,'android.widget.ImageView')))			
		bp=bootPage(self.driver)			
		element = bp.find_element(*self.firstPage);		
		self.assertTrue(element.is_displayed());

	
	def test_b_leftSwipe_firstPage(self):
		'''左滑第一页引导页'''		
		WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.CLASS_NAME,'android.widget.ImageView')));	
		bp = bootPage(self.driver);					
		bp.left_swipe();
		element = bp.find_element(*self.firstPage);			
		self.assertTrue(element.is_displayed());

	
	def test_c_rightSwipe_middlePage(self):
		'''右滑到第二页引导页'''		
		WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.CLASS_NAME,'android.widget.ImageView')));
		bp = bootPage(self.driver);					
		bp.right_swipe();
		element=bp.find_element(*self.secondPage);
		self.assertTrue(element.is_displayed());

	
	def test_d_rightSwipe_lastPage(self):
		'''右滑最后一页引导页 显示按钮'''		
		WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME,'android.widget.ImageView')))
		bp = bootPage(self.driver);	
		elements = bp.find_elements(*self.points);
		index = len(elements)-1;
		for i in range(index):
			bp.right_swipe();
		sleep(2);
		element = bp.find_element(*self.button);
		text= element.get_attribute('text');
		self.assertEqual(text,'立刻体验');

	
	def test_e_clickbutton(self):
		'''进去登陆页面'''
		WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME,'android.widget.ImageView')))
		bp = bootPage(self.driver);	
		elements = bp.find_elements(*self.points);
		index = len(elements)-1;
		for i in range(index):
			bp.right_swipe();
		sleep(2);
		bp.find_element(*self.button).click();
		sleep(2);
		element = bp.find_element(*self.login);
		self.assertTrue(element.is_displayed());	



if __name__ == '__main__':
	unittest.main();


