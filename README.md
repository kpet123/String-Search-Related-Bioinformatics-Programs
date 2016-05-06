# String-Search-Related-Bioinformatics-Programs
Programs in Python and BASH related to homology comparison and bioinformatics-related functions involving string searches. Formats used: FASTA, NEXUS, and Clustal aln. Python code requires Biopython package.


Note: almost all have dependencies in Pattern.py and Bioptyhon


1. download_data.py
Currently: Prompts for list of gi numbers and returns file with full ncbi information for each protein. 
Under construction: return nucleotide seqence for each protein sequence that has associated nucleotide sequence.

2. getNames.py
Prompts for library, outputs list of organism names (name defined as enclosed by [])

3. list_gi.sh
Prompts for library and output file name, then will write to the output file gi numbers of all records in library.
Note: this is a BASH script, so to my knowlege, only works with UNIX-like system. Also make sure to make it executable with chmod + program_name

4. makeLibrary_oo.py
Creates library from 2 hard-coded file dependencies: FASTA file of subunit sequences (in this case CnaBs), and another file of the location of the motif in each sequence of the FASTA file (in this case the ebox)


5. makeSpeciesList.sh
Creates list of species names from library. Under the hood: cleans up output from getNames.py
Note: see #3 for note about .sh files

6. makeTree.py
creates tree with Biopython, under construction

7. makePrimer.py
Given FASTA file with 1 protein sequence followed by it's DNA sequence (forward, 5'-3') and given defined starts of the forward and reverse primer, will output a bunch of potential primers, their AT content, and their estimated melting temperature

8. trimSeq.py
Used to parse proteins in large chunks of DNA sequence. Currently can use start and stop codons as delimeters. 

