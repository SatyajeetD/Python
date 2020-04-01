import json
import ast
f=open('test.json','r')
data=json.load(f).decode('utf-8')
f.close()
#print type(data)
data=ast.literal_eval(data)
#print type(data)
#print data.keys()
print len(data)
#for item in range(0,10):
#	if "Trump" or "trump" in data[item]:
#		print data[item]
#	if "covid" or "Covid" in data[item]:
#		print data[item]	
#	print type(data[item][0])
#	print data[item][0]
#	print data[item]
#	for k,v in item:
#		print k
#d = ast.literal_eval("{'code1':1,'code2':1}")
