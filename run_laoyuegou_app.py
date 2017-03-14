#encoding=utf-8;
import unittest;
from HTMLTestRunner import HTMLTestRunner;
import time,sys;
import os
reload(sys)
sys.setdefaultencoding('utf-8');
if __name__ == '__main__':	
	now = time.strftime('%y-%m-%d %H_%M_%S');
	filename = os.path.dirname(__file__)+'\\report\\'+now+'result.html';
	fp = open(filename,'wb');
	runner = HTMLTestRunner(stream=fp,title='捞月狗app测试',description='环境：windows 10');

	discover = unittest.defaultTestLoader.discover(os.path.dirname(__file__)+'\\testcase\\',pattern='*_sta.py');

	runner.run(discover);
	fp.close();
