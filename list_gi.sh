#!/bin/sh

#input: list of genera. Output: file with all gi numbers sorted by genera


on_ctrl_c(){
         echo "Ignoring Ctrl-C"
}

echo -n "Enter name of file to be searched (a CnaB Library)"
read lib

echo -n "Enter name of output file"
read output


cat $lib | grep ">" | colrm 20 |  sort -u | cut -d "|" -f 2  >> $output
echo "complete"




