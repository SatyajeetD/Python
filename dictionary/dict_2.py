#create a disctionary
new_dict={}
new_dict['Name']='Satya'
new_dict['Age']=33
print new_dict
#Edit value of Key-> Age
new_dict['Age']=34
print "New dictionary with edited values"
print new_dict
#print length of dictionary
print len(new_dict)
#Print all keys in dictionary
print "All keys in the dictionary"
for keys in new_dict.keys():
	print keys
#Print all values in dictionary

print "All values in the dictionary"
for values in new_dict.values():
	print values
#Print a key and values from the dictionary

print "All keys and values in the dictionary"
for keys,values in new_dict.items():
	print keys
	print values
