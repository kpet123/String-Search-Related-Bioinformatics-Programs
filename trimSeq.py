#####TRIMS SEQUENCE ACCORDING TO RECOGNIZABLE PATTERN

from Bio.Seq import Seq
from Bio import SeqIO
import sys
PARTITION=3

def main():
    print "hi"
    ##because stdout is piped into a readable .fasta file, all user-related output is printed in standard error (stderr)
    sys.stderr.write("Enter full name of .fasta file to be parsed\n")
    filename=raw_input()
    infile=open(filename, "r")
    sys.stderr.write("Enter all possible delimiting sequenced, separated by a space. NOTE: trimmed output will end before delimeter \n")
    raw_delim=raw_input()
    delim_list=raw_delim.split()## list of possible delimitting sequences, such as stop codons or start codons
    for seq_record in SeqIO.parse(infile, "fasta"):
        reduced_seq=trim(delim_list, seq_record.seq)
        print ">"+seq_record.description
        print reduced_seq
    

def trim(delim_list, seq):
    split_list=[]##holds positions where splits will occur; i.e. whereever a delimeter is found
    split_list.append(0) ##always include 0
    for delim in delim_list:
        delim_indicies=findAllNeedles(delim, seq, PARTITION)#partition is hardcodeded as 3
        split_list+=delim_indicies## append all locations the searched sequence is found to split_list
    split_list.append(len(seq)-1)##beginning and end both are points
    split_list.sort()## should all be numberical, so no need for custom sorting method
    sys.stderr.write("size of split_list is "+str(len(split_list))+"\n")
    options=[]
    index=0
    
    ##Finds where needle sequence starts and adds those points to the list "options"
    while index < (len(split_list)-1):
        options.append(seq[split_list[index]:split_list[index+1]]) ##identifies and prints eachsubstring along split points
        index+=1

    ##Pattern not found
    if options == False:
        sys.stderr.write("Pattern not found")
    
    ##Prints to allow user to choose
    for count, fragment in enumerate(options):
        print count, fragment 
    sys.stderr.write( "\nEnter the number of the sequence you want to use\n")
    usedIndex=raw_input()
    return options[int(usedIndex)]


## returns a list of locations of "needles" (substring) in "haystack"(larger string
def findAllNeedles(needle, haystack, partition): 
    i=0
    needleList=[]
    while i<len(haystack)-3:
        if haystack[i:i+len(needle)]==needle and i%3==0:
            needleList.append(i)
            print i, " is added to split_list"
        i+=1
    return needleList






        
if __name__ == "__main__": main()    
