

import sys

def myfunc(strA, strB):
	x = 'value_' + strA
	y = 'value_' + strB
	return x, y
	
def main(argv):
	print ('argv = ' + str(argv))

	Wert_1, Wert_2 = myfunc(argv[0], argv[1])
	
	print ('Wert 1 = ' + Wert_1)
	print ('Wert 2 = ' + Wert_2)



if __name__ == "__main__":
    main(sys.argv[1:])