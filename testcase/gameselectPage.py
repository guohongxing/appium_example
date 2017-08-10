#encoding=utf-8
import unittest,os,sys
sys.path.append('../models')
from models.myunit import myTest
sys.path.append('../page_obj')
from time import sleep
from page_obj.gameselectPage import selectGame
class gameselectPage_Test(myTest):
	@unittest.skip(1)
	def test_a_return(self):
		'''点击返回，返回登录注册页面'''
		sg = selectGame(self.driver)
		isfound = sg.prefixa_condition()
		if isfound:
			element = sg.return_click()
			self.assertIsNotNone(element)
		else:
			self.assertTrue(isfound)
	@unittest.skip(1)
	def test_b_title(self):
		'''标题显示'''
		sg = selectGame(self.driver)
		isfound = sg.prefixa_condition()
		if isfound:
			text = sg.title_display()
			self.assertEqual(text,'选择游戏')
		else:
			self.assertTrue(isfound)
	@unittest.skip(1)
	def test_c_skip(self):
		'''点击跳转，跳转到注册页面'''
		sg = selectGame(self.driver)
		isfound = sg.prefixa_condition()
		if isfound:
			element = sg.skip_display()
			self.assertTrue(element)
		else:
			self.assertTrue(isfound)

	def test_d_wip(self):
		'''点击任意游戏，进入对应游戏页面'''
		sg = selectGame(self.driver)
		isfound = sg.prefixa_condition()
		sleep(2)
		if isfound:
			'''isRight = sg.enter_game('英雄联盟','游戏页面')'''
			'''self.assertIsNotNone(isRight)'''			
		else:
			self.assertTrue(isfound)




