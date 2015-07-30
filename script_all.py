import time
import os
import subprocess
import unittest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import json


def cleanup():
	grepCmd = "ps -aef | grep -E 'chromedriver|Chrome'"
	grepResults = subprocess.check_output([grepCmd], shell=True).split()

	for i in range(1,len(grepResults)):
		pid = grepResults[i]
		killPidCmd = "kill -9 " + pid
		subprocess.call([killPidCmd], shell=True)


def run(ape_active, file_name):
	chop = webdriver.ChromeOptions()
	cookies = []

	if ape_active:
		chop.add_argument("--load-extension=" + "../ext") # This adds extension

	# Start chromedriver
	if os.uname()[0] == "Darwin":
		driver = webdriver.Chrome('../chromedriver', chrome_options = chop)

	f = open("alexa-top-10000-global.txt", 'r')

	for i in range(0,1):
		try:
			driver.get("http://www." + f.readline().strip())
		except:
			pass
		time.sleep(10)
		cookies.append(driver.get_cookies())

	with open(file_name, 'w') as f:
		f.write(json.dumps(cookies))


def compare(a, b):
	c = json.loads(a.replace("[]","").replace("], [",",").replace("]]","]").replace("[, ",""))
	c2 = json.loads(b.replace("[]","").replace("], [",",").replace("]]","]").replace("[, ",""))

	c3 = {}

	for cookie in c:
		if cookie["domain"] in c3:
			c3[cookie["domain"]]["c1"].append({'name': cookie['name'], 'value' : cookie["value"]})
		else:
			c3[cookie["domain"]] = {'c1' : [{'name': cookie['name'], 'value' : cookie["value"]}], 'c2' : []}

	for cookie in c2:
		if cookie["domain"] in c3:
			c3[cookie["domain"]]["c2"].append({'name': cookie['name'], 'value' : cookie["value"]})
		else:
			c3[cookie["domain"]] = {'c1': [], "c2" : [{'name': cookie['name'], 'value' : cookie["value"]}]}

	return json.dumps(c3, sort_keys=True, indent=4)


def reduction(c):
	x = json.loads(c)

	for key, value in x.iteritems():
	    for cookie in value['c1']:
	    	for cookie2 in value['c2']:
	    		if cookie['name'] == cookie2['name']:
	    			if cookie['value'] == cookie2['value']:
	    				print key, cookie['name']
	    				print "\t" + cookie['value']


if __name__=="__main__":
	run(True, "output/test.txt")
	run(True, "output/test.txt")
	run(False, "output/test.txt")
	run(False, "output/test.txt")

	# run(False, "output/2-cookies_100_flash_1.txt")
	# run(False, "output/2-cookies_100_flash_2.txt")
	# run(False, "output/3-cookies_100_flash_1.txt")
	# run(False, "output/3-cookies_100_flash_2.txt")
	# run(False, "output/4-cookies_100_flash_1.txt")
	# run(False, "output/4-cookies_100_flash_2.txt")
	# run(False, "output/5-cookies_100_flash_1.txt")
	# run(False, "output/5-cookies_100_flash_2.txt")


	

