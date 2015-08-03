filenames = ["10-cookies_100_flash_1.txt",
"10-cookies_100_flash_2.txt",
"10-cookies_100_noflash_1.txt",
"10-cookies_100_noflash_2.txt",
"10-cookies_100_noflash_APE_1.txt",
"10-cookies_100_noflash_APE_2.txt",
"10-cookies_100_flash_APE_1.txt",
"10-cookies_100_flash_APE_2.txt"]

for filename in filenames:
	f = open(filename, 'r+')
	text = f.read()
	text = text.replace("[[], ","").replace("]]","]").replace(" [], ","").replace("],[",",").replace("], [",",")
	f.seek(0)
	f.write(text)
	f.truncate()
	f.close()