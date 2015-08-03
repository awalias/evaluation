import json

with open("compare_100_flash_output.txt") as f:
	x = json.loads(f.read())

for key, value in x.iteritems():
    for cookie in value['c1']:
    	for cookie2 in value['c2']:
    		if cookie['name'] == cookie2['name']:
    			if cookie['value'] == cookie2['value']:
    				print key, cookie['name']
    				print "\t" + cookie['value']
    		