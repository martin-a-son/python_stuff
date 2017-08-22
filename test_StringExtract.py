
import os
import sys
import re

def _read_file(file):
        f = open(file, 'r')
        lines = list(line for line in (l.strip() for l in f) if line)
        return lines
		
def main():
	# File oratab has been created manually for testing.
    lines = _read_file('C:\etc\oratab')
    for line in lines:
		if line.startswith("+ASM"):
			asmvalue = re.search(r'(\+ASM[\d]?)', line, re.M | re.I)
			# using just asmvalue for print will show the match object only
			print "Match Object for asmvalue = ",asmvalue
			# to get the value of the matching object
			print "Value for asmvalue = ",asmvalue.group(1)
			sid = asmvalue.group(1)
			print "Value for sid = ",sid
	

if __name__ == "__main__":
	main()
