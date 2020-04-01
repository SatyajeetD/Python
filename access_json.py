import json
fp=open('output.txt','r')
i=fp.read()
print type(i)
fp.close()
#i=list(i)
#j=json.dumps(i)
#print type(j)
#k=json.loads(j).encode('utf8')
#print type(k)
#l=json.loads(k)
#print type(l)
with open('test.json', 'w') as fout:
	json.dump(i , fout)
