filenames = ["2_cookies_100_flash_APE_2.text",
			 "3_cookies_100_flash_APE_1.text",
			 "3_cookies_100_flash_APE_2.text",
			 "4_cookies_100_flash_APE_1.text",
			 "4_cookies_100_flash_APE_2.text",
			 "5_cookies_100_flash_APE_1.text",
			 "5_cookies_100_flash_APE_2.text",
			 "6_cookies_100_flash_APE_1.text",
			 "6_cookies_100_flash_APE_2.text",
			 "7_cookies_100_flash_APE_1.text",
			 "7_cookies_100_flash_APE_2.text",
			 "8_cookies_100_flash_APE_1.text",
			 "8_cookies_100_flash_APE_2.text",
			 "9_cookies_100_flash_APE_1.text",
			 "9_cookies_100_flash_APE_2.text"]

for filename in filenames:
	f = open(filename, 'r+')
	text = f.read()
	text = text.replace("[[], ","").replace("]]","").replace(" [], ","").replace("],[",",")
	f.seek(0)
	f.write(text)
	f.truncate()
	f.close()