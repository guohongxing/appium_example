#encoding=utf-8;
import unittest
from HTMLTestRunner import HTMLTestRunner
import time,sys
import os
sys.path.append('./testcase')
from models import appiumServer 
from models import operateYaml
from models import myunit
from multiprocessing import Process
from testcase.bootPage import bootPage_Test
from testcase.homePage import homePage_Test
from testcase.loginPage_sta import loginPage_Test
from testcase.forgetpasswordPage import forgetpasswordPage_Test
from testcase.gameselectPage import gameselectPage_Test
reload(sys)
sys.setdefaultencoding('utf-8')

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
def get_devices():
	return operateYaml.getYam(PATH("devices.yaml"))
ga = get_devices()

def runnePool():
	devices_Pool = []
	for i in range(0,len(ga['appium'])):
		l_pool = []		
		t = {}
		t['devices'] = ga['appium'][i]['devices']
		t['version'] = ga['appium'][i]['version']
		t['port'] = ga['appium'][i]['port']
		t['devicesName'] = ga['appium'][i]['devicesName']
		l_pool.append(t)
		devices_Pool.append(l_pool)	
	p=Process(target=runnerCaseApp,args=devices_Pool)
	p.start()
	p.join()
	#pool = Pool(2) 	
	#pool.map(runnerCaseApp,devices_Pool)

	#pool.join()	

def runnerCaseApp(l_devices):
	now = time.strftime("%y-%m-%d %H_%M_%S")	
	filename = os.path.dirname(__file__)+'/report/'+now+str(l_devices[0]['devicesName'])+'_result.html'
	print filename
	fp = open(filename,'wb')
	description = '手机型号:'+str(l_devices[0]['devicesName'])+'  端口号:'+str(l_devices[0]['port'])
	runner = HTMLTestRunner(stream=fp,title='捞月狗app自动化测试',description=description)
	suite = unittest.TestSuite()
	#suite.addTest(myunit.myTest.parametrize(bootPage_Test,l_devices[0]))
	#suite.addTest(myunit.myTest.parametrize(homePage_Test,l_devices[0]))
	#suite.addTest(myunit.myTest.parametrize(loginPage_Test,l_devices[0]))
	#suite.addTest(myunit.myTest.parametrize(forgetpasswordPage_Test,l_devices[0]))
	suite.addTest(myunit.myTest.parametrize(gameselectPage_Test,l_devices[0]))
	#discover = unittest.defaultTestLoader.discover(os.path.dirname(__file__)+'\\testcase\\',pattern='*_sta.py');
	runner.run(suite)
	#unittest.TextTestRunner(verbosity=2).run(suite)
	fp.close()

if __name__ == '__main__':
	print os.path.dirname(__file__)
	appium_server = appiumServer.AppiumServer(ga)
	appium_server.re_start_server()	
	while not appium_server.is_runnnig():
		time.sleep(2)
	runnePool()



	