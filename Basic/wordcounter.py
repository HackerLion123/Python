import sys
from profiler import profile


@profile
def wordcount(fname):
	file = open(fname,"r")
	line = 0 
	word =[]
	for i in file:
		line += 1
		for a in i.split():
			word.append(a.lower())
	return line,word

def main():
	# lines,words = wordcount(sys.argv[1])
	lines,words = wordcount("wordcounter.py")
	print(words)

if __name__ == '__main__':
	main()