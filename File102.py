import logging
logging.basicConfig(level= logging.DEBUG,filename='C:\Users\pdadmin\Documents\study\TestLog.txt', format= '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
def open_file():
    try:
        fp=open('C:\Users\pdadmin\Documents\study\\test_log.txt','r')
        return fp
    except:
        logging.exception("File not present")
#for line in fp.readlines():
#    print "Printing from within the loop"
#    print line
#print fp.readlines()
line_feed=[]
text_to_search=[]
def more_input():
    t=raw_input('Enter the choice as below \n1 to add a search string \n 0 to exit\n')
    if t=='1':
        return True
    else:
        return False
def user_input():
    t=raw_input("Enter the text you want to search\n")
    text_to_search.append(t)
    return text_to_search

def write_file(line):
    filep=open('C:\Users\pdadmin\Documents\study\\new.txt','a')
    filep.write(line)
    filep.close()
def print_lines(res):
    for item in res:
        fp=open_file()
        for line in fp.readlines():
            if item in line:
                write_file(line)
                #print line
                #return line_feed

while more_input():
    res=user_input()

print res
line_feed=print_lines(res)

#print line_feed

