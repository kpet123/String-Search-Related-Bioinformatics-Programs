####Download data from ncbi
from Bio import Entrez
import time
from Bio import SeqIO

def main():
    ##entrez email here 
    ## promt file name
    print "Type name of input file[gi]"
    f=raw_input()
    inpt=open(f)
    ## make list of input gi
    gi_list=[]
    for line in inpt:
        gi_list.append(line)
    ## Get web environment through Epost
    webenv=getPost(gi_list)
    print "webenv is ", webenv
    ## Download XML with Efetch
    fetchResults(webenv, len(gi_list))
   
    inpt.close()
   

## searches for protein gi's specified in gi_list and stores results in entrez history    
def getPost(gi_list):
    Entrez.email="khp2106@columbia.edu"
    print "pre connect test"
    l=str(",".join(gi_list))
    idstr=l.replace('\n', '').replace('\r', '')
    print idstr
    handle=Entrez.epost(db="nucleotide", rettype="fasta", id=idstr)
    print "post-connect test"
    entrez_results=Entrez.read(handle)
    handle.close()

    ## get session and queryKey from results
    
    webenv=entrez_results["WebEnv"]
    return webenv


def fetchResults(webenv, count):
    print "total proteins to be downloaded is", count
    try: 
        from urllib.error import HTTPError  # for Python 3
    except: 
        from urllib2 import HTTPError  # for Python 2
        import urllib2

    ## read ouput file
    print ("Input name of output file")
    filename=raw_input()
    out_handle=open(filename, "w")
    batch_size=40
    for start in range(0, count, batch_size):
        end=min(count, start+batch_size)
        print("Going to download record %i to %i" % (start+1, end))
        attempt=1
        while attempt <=3:
            try:
                searchURL= "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?&db=nucleotide&rettype=fasta&retmode=text&restart="+str(start)+"&retmax="+str(batch_size)+"&WebEnv="+webenv+"&query_key=1"
                print searchURL
                fetch_handle=urllib2.urlopen(searchURL)
                attempt=4 ##executed sucessfully

               #fetch_handle = Entrez.efetch(db="protein", rettype="fasta", retstart=start, retmax=batch_size, webenv=webenv, query_key=1)
            except HTTPError as err:
                if 500 <= err.code <= 599:
                        print ("Received error from server %s" %err)
                        print ("Attempt %i of 3" % attempt)
                        attempt += 1
                        time.sleep(15)

                else:
                    raise
        data=fetch_handle.read()   
        out_handle.write(data)
        fetch_handle.close()
    out_handle.close()

def matchProtToGene(genbank_file):
    geneList=[]
    for record in SeqIO.parse(genbank_file, "genbank"):
        for feature in record.features:
            if type(feature)=='CDS':
                geneList.append(feature.qualifiers['locus_tag'])
    return geneList
 


if __name__ == "__main__": main()
