import re
lines, blanklines, sentences, words=0,0,0,0

try:
	filename='war_and_peace.txt'
	textf=open(filename, 'r', encoding="utf-8")
	data=textf.read()
except IOError:
	print('cannot open file %s for reading' % filename)
	import sys
	sys.exit(0)
	
i=1
data=data.replace('\n', ' ')
data=data.replace('\t', ' ')	

data=data.replace('"', ' ' )
data=data.replace('*', ' ')
data=data.replace('“', ' ' )
data=data.replace('”', ' ' )
sentences = re.split(r' *[\.\?!,][\'"\)\]]* *', data)	


fdump=open("data\newlines.txt",'w')

 

for i in range(900,len(sentences)-500):
	if(len(sentences[i])>50 and len(sentences[i+1])>50):
		fdump.write("%s\n" % (sentences[i]))

#for line in sentences:


textf.close()