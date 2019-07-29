"""
This code is written by Ashirwad Vyawahare
"""

import os

def findText(strText, data):
    count=0
    for word in data.split():
        #print(word)
        if word == strText:
            count+=1
    return count

	
def readFile(strFileName):
    #Check if file exists
    if not os.path.exists(strFileName):
        return None

    with open(strFileName, 'r') as fh:
        return fh.read()


def mainFunction():
    strFileName = 'SampleFile.txt'
    strText = 'Test'
 
    data = readFile(strFileName)

    count = findText(strText, data)
    print(count)
	

mainFunction()