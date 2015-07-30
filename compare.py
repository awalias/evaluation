import json

def compare(a, b):
	c = json.loads(a)
	c2 = json.loads(b)

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

	with open("output/9-cookies_100_flash_APE_1.txt") as f:
		a = f.read()

	with open("output/9-cookies_100_flash_APE_2.txt") as f:
		b = f.read()

	reduction(compare(a,b))