import os

"""
	Note: Do not run this twice on a single folder.
"""

	
if __name__ == '__main__':
	count = 0

	for f in os.listdir("."):	
		if not ".py" in f and not f[0:-4].isdigit():
			count += 1
			os.renames(f,str(count)+f[-4:])
