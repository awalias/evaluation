filenames = ["2-cookies_100_flash_APE_2.txt",
			 "3-cookies_100_flash_APE_1.txt",
			 "3-cookies_100_flash_APE_2.txt",
			 "4-cookies_100_flash_APE_1.txt",
			 "4-cookies_100_flash_APE_2.txt",
			 "5-cookies_100_flash_APE_1.txt",
			 "5-cookies_100_flash_APE_2.txt",
			 "6-cookies_100_flash_APE_1.txt",
			 "6-cookies_100_flash_APE_2.txt",
			 "7-cookies_100_flash_APE_1.txt",
			 "7-cookies_100_flash_APE_2.txt",
			 "8-cookies_100_flash_APE_1.txt",
			 "8-cookies_100_flash_APE_2.txt",
			 "9-cookies_100_flash_APE_1.txt",
			 "9-cookies_100_flash_APE_2.txt"]

for filename in filenames:
	f = open(filename, 'r+')
	text = f.read()
	text = text.replace("[[], ","").replace("]]","").replace(" [], ","").replace("], [",",")
	f.seek(0)
	f.write(text)
	f.truncate()
	f.close()