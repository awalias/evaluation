import time
import os
import subprocess
import unittest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def cleanup():
	grepCmd = "ps -aef | grep -E 'chromedriver|Chrome'"
	grepResults = subprocess.check_output([grepCmd], shell=True).split()

	for i in range(1,len(grepResults)):
		pid = grepResults[i]
		killPidCmd = "kill -9 " + pid
		subprocess.call([killPidCmd], shell=True)


def run():
	chop = webdriver.ChromeOptions()
	#chop.add_argument("--load-extension=" + "../ext"); # This adds extension

	# Start chromedriver
	if os.uname()[0] == "Darwin":
		driver = webdriver.Chrome('../chromedriver', chrome_options = chop)

	f = open("alexa-top-10000-global.txt", 'r')

	for i in range(0,100):
		driver.get("http://www." + f.readline().strip());
		time.sleep(10)
		print driver.get_cookies()

if __name__=="__main__":
	run()
	#cleanup() # required, driver.quit is buggy


	


	
