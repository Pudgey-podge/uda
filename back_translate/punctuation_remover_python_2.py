#!/Users/johncosnett/opt/anaconda3/envs/py27/bin/python

import string

inputfile = './back_trans_data/forward_gen/file_0_of_1.txt'
outputfile = 'french_with_no_punctuation.txt'

file = open(inputfile, 'rt')
text = file.read()
file.close()

cleaned_text = text.translate(None, string.punctuation)

f = open(outputfile, "w+")

f
f.write(cleaned_text)
f.close()



#checking that it worked and printing contents
f = open(outputfile, 'rt')
check = f.read()
print check


