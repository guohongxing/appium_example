import threading,os
import subprocess
from multiprocessing import Process
import urllib2
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
class AppiumServer():
	def __init__(self,l_devices):
		self.l_devices = l_devices
	def start_server(self):			
		for i in range(0,len(self.l_devices['appium'])):
			t1 = RunServer(self.l_devices["appium"][i]["config"])
			t1.run()			

	def stop_server(self):
		
		os.system('killall node')

	def re_start_server(self):
		self.stop_server()
		self.start_server()

	def is_runnnig(self):
		response = None
		for i in range(0, len(self.l_devices["appium"])):
			url = " http://127.0.0.1:"+str(self.l_devices["appium"][i]["port"])+"/wd/hub"+"/status"
			request = urllib2.Request(url)
			try:
				response=urllib2.urlopen(request)
				if str(response.getcode()).startswith("2"):
					return True
				else:
					return False
			except urllib2.URLError:
				return False
			finally:
				if response:
					response.close()

class RunServer():
	def __init__(self,cmd):			
		self.cmd = cmd

	def run(self):
		subprocess.Popen(self.cmd,shell='true')

