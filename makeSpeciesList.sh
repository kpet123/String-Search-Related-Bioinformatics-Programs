#!/bin/sh

#input: list of names. Output: file with selection of one species per genera from well-formatted input


on_ctrl_c(){
         echo "Ignoring Ctrl-C"
}



echo -n "Enter name of output file"
read output

echo -n "Enter name of library "
read lib
#runs getNames on library

python getNames.py $lib | cut -d " " -f 1 | sort -k 1,1 -u  >> $output


