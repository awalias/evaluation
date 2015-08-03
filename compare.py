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
	results = ""

	for key, value in x.iteritems():
	    for cookie in value['c1']:
	    	for cookie2 in value['c2']:
	    		if cookie['name'] == cookie2['name']:
	    			if cookie['value'] == cookie2['value']:
	    				results += "\n" + key + " " + cookie['name'] + "\n\t" + cookie['value']

	return results

if __name__=="__main__":
	cases = ["flash", "flash_APE", "noflash", "noflash_APE"]

	for i in range (10,11):
		for case in cases:
			with open("output/%d-cookies_100_%s_1.txt" % (i, case)) as f:
				a = f.read()

			with open("output/%d-cookies_100_%s_2.txt" % (i, case)) as f:
				b = f.read()

			with open("results/%d_%s" % (i,case), "w") as f:
				try:
					f.write(reduction(compare(a,b)))
				except ValueError as e:
					print "error: results/%d_%s" % (i,case)
					print e

			