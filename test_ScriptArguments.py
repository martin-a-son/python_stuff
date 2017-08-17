#!C:\etc\Python27\python.EXE

# Uebung mit Scriptoptionen

import sys
import getopt

myAuthHash = 'bWFydGluOm15b28xMDA='

def usage():
    print ('Usage:')
	# print ('python myscript.py [-a|--auth <Authentication Hash>] [-h|--help] [-d]')
    print ('python ' + sys.argv[0] + ' [-a|--auth <Authentication Hash>] [-h|--help] [-d]')
    print ('-d: debug mode')

def main(argv):
	# Variablen definieren und initialisieren
	global _debug
	auth = myAuthHash
	_debug = False
	
	try:
		opts, args = getopt.getopt(sys.argv[1:], "ha:d", ["help", "auth="])
	except getopt.GetoptError as err:
		print (err)
		usage()
		sys.exit(2)
	
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			usage()
			sys.exit()
		elif opt == '-d':
			_debug = 1
		elif opt in ("-a", "--auth"):
			auth = arg
		else:
			assert False, "unhandled option"

	if _debug:
		print ('myAuthHash = ' + myAuthHash)
		if auth == "":
			print ('auth = "nix"')	# Da eingangs "auth = myAuthHash" gilt, sollte niemals "nix" ausgegeben werden.
		else:
			print ('auth = ' + auth)

if __name__ == "__main__":
    main(sys.argv[1:])