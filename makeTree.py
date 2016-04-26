## Creates different tree models and compares on basis of topology (maybe also distace
##This will get piped to HYPHY, so ultimate output is multiple seq alignment and NEXUS tree




from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio import AlignIO
from TreeConstruction import DistanceTreeConstructor
            

def makeDistanceTree():
    aln = AlignIO.read('Tests/TreeConstruction/msa.phy', 'phylip')
    calculator = DistanceCalculator('identity')
    dm = calculator.get_distance(aln)
    constructor = DistanceTreeConstructor(calculator, 'nj')
    tree = constructor.build_tree(aln)




