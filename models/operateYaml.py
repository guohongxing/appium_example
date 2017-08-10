__author__ = 'guohongxing'
#coding='utf-8'
import yaml

def getYam(homeyaml):
	try:
		f = open(homeyaml,'r')
		x = yaml.load(f)		
		return x
	except IOError:
		print "yaml file not found %s"%homeyaml




