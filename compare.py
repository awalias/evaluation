import json

with open('cookies_100_flash_1.txt') as f:
	c = eval(f.readline())

with open('cookies_100_flash_2.txt') as f:
	c2 = eval(f.readline())

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

print json.dumps(c3, sort_keys=True, indent=4)