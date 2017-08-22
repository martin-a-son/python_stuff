#!C:\etc\Python27\python.EXE
# -*- mode: Python; tab-width: 4; indent-tabs-mode: nil; -*-
# ex: set tabstop=4 :
# Please do not change the two lines above. See PEP 8, PEP 263.
#

import sys
import pexpect
import re
import os
import socket

def replaceString(filename, old_string, new_string):

                # Open Source file as Input
        with open(filename) as fin:
                s = fin.read()
                if old_string not in s:
                        print '"{old_string}" not found in {filename}.'
                        return

                # Open Destination file as Output
        with open(filename +'_new', 'w') as fout:
                s = s.replace(old_string, new_string)
                fout.write(s)
                fout.close()

def main():

	myHostname = socket.gethostname()
	
	myReplaceValue = 'NEW_VALUE'
	
	if myReplaceValue == "Nothing":
		sys.exit(1)
    else:
		replaceString('/tmp/myfile', 'REPLACE_ME', myReplaceValue)
                
if __name__ == "__main__":
		main()

