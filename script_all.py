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


def run(ape_active, disable_flash, file_name):
	chop = webdriver.ChromeOptions()
	cookies = []

	if ape_active:
		chop.add_argument("--load-extension=" + "../ext") # This adds extension

	if disable_flash:
		chop.add_argument("--disable-bundled-ppapi-flash")
		chop.add_argument("--disable-internal-flash")
		chop.add_argument("--disable-plugins")

	# Start chromedriver
	if os.uname()[0] == "Darwin":
		driver = webdriver.Chrome('../chromedriver', chrome_options = chop)

	f = open("alexa-top-10000-global.txt", 'r')

	for i in range(0,99):
		try:
			driver.get("http://www." + f.readline().strip())
		except:
			pass
		time.sleep(10)
		cookies.append(driver.get_cookies())

	with open(file_name, 'w') as f:
		f.write(json.dumps(cookies))


if __name__=="__main__":
	# run(False, False, "output/2-cookies_100_flash_1.txt")
	# run(False, False, "output/2-cookies_100_flash_2.txt")
	# run(False, False, "output/3-cookies_100_flash_1.txt")
	# run(False, False, "output/3-cookies_100_flash_2.txt")
	# run(False, False, "output/4-cookies_100_flash_1.txt")
	# run(False, False, "output/4-cookies_100_flash_2.txt")
	# run(False, False, "output/5-cookies_100_flash_1.txt")
	# run(False, False, "output/5-cookies_100_flash_2.txt")

	#run(True, True, "output/2-cookies_100_noflash_APE_1.txt")
	#run(True, True, "output/2-cookies_100_noflash_APE_2.txt")
	#run(True, True, "output/3-cookies_100_noflash_APE_1.txt")
	#run(True, True, "output/3-cookies_100_noflash_APE_2.txt")
	#run(True, True, "output/4-cookies_100_noflash_APE_1.txt")
	#run(True, True, "output/4-cookies_100_noflash_APE_2.txt")
	#run(True, True, "output/5-cookies_100_noflash_APE_1.txt")
	#run(True, True, "output/5-cookies_100_noflash_APE_2.txt")

	# run(False, True, "output/2-cookies_100_noflash_1.txt")
	# run(False, True, "output/2-cookies_100_noflash_2.txt")
	# run(False, True, "output/3-cookies_100_noflash_1.txt")
	# run(False, True, "output/3-cookies_100_noflash_2.txt")
	# run(False, True, "output/4-cookies_100_noflash_1.txt")
	# run(False, True, "output/4-cookies_100_noflash_2.txt")
	# run(False, True, "output/5-cookies_100_noflash_1.txt")
	# run(False, True, "output/5-cookies_100_noflash_2.txt")

	# run(False, False, "output/6-cookies_100_flash_1.txt")
	# run(False, False, "output/6-cookies_100_flash_2.txt")
	# run(False, False, "output/7-cookies_100_flash_1.txt")
	# run(False, False, "output/7-cookies_100_flash_2.txt")
	# run(False, False, "output/8-cookies_100_flash_1.txt")
	# run(False, False, "output/8-cookies_100_flash_2.txt")
	# run(False, False, "output/9-cookies_100_flash_1.txt")
	# run(False, False, "output/9-cookies_100_flash_2.txt")

	# run(True, True, "output/6-cookies_100_noflash_APE_1.txt")
	# run(True, True, "output/6-cookies_100_noflash_APE_2.txt")
	# run(True, True, "output/7-cookies_100_noflash_APE_1.txt")
	# run(True, True, "output/7-cookies_100_noflash_APE_2.txt")
	# run(True, True, "output/8-cookies_100_noflash_APE_1.txt")
	# run(True, True, "output/8-cookies_100_noflash_APE_2.txt")

	#run(True, True, "output/9-cookies_100_noflash_APE_1.txt")
	#run(True, True, "output/9-cookies_100_noflash_APE_2.txt") 

	# run(False, True, "output/6-cookies_100_noflash_1.txt")
	# run(False, True, "output/6-cookies_100_noflash_2.txt")
	# run(False, True, "output/7-cookies_100_noflash_1.txt")
	# run(False, True, "output/7-cookies_100_noflash_2.txt")
	# run(False, True, "output/8-cookies_100_noflash_1.txt")
	# run(False, True, "output/8-cookies_100_noflash_2.txt")

	#run(False, True, "output/9-cookies_100_noflash_1.txt") 
	#run(False, True, "output/9-cookies_100_noflash_2.txt") 

	run(False, False, "output/10-cookies_100_flash_1.txt") 
	run(False, False, "output/10-cookies_100_flash_2.txt") 

	# run(False, True, "output/10-cookies_100_noflash_1.txt") # todo
	# run(False, True, "output/10-cookies_100_noflash_2.txt") # todo

	# run(True, False, "output/10-cookies_100_flash_APE_1.txt") # todo
	# run(True, False, "output/10-cookies_100_flash_APE_2.txt") # todo
  
	#run(True, True, "output/10-cookies_100_noflash_APE_1.txt") 
	#run(True, True, "output/10-cookies_100_noflash_APE_2.txt") 


	

