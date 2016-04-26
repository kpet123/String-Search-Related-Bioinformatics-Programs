from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio.Blast import Record
import Pattern as p
import sys as s



def getNames():
    
    #f=open(filename, "r")
    #print "Input output file name"

    filename=s.argv[-1]
    f=open(filename, "r")
    #make checkRepeat list
    uniqueList=[]
    #iterate through file, each line should be description
    with f as openfileobject:
        for line in openfileobject:
            if line.startswith("gi|"):
                name=p.findEnclosed(line, '[', ']')
                if name!=None:
		    if len(name.split())>=2:
                        p.isRepeat(name+'\n', uniqueList)
    #writeFile(uniqueList) ############ uncomment if writing directly to file
    #f.close()
    for el in uniqueList:
	print el
    return uniqueList
    
	    
def writeFile(list1):
    print "Input output file name"
    output=raw_input()
    o=open(output, "w")
    for el in list1:
	line=el+'\n'
        o.write(line)
    o.close()

def shortName(string):
    elements=string.split()
    return elements[0]
####**********  EXECUTED STUFF
getNames()
