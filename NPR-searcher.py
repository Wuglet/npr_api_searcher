import nltk
import re
from urllib import urlopen
import time
smileResults = []

#smile searcher
def smileFinder():
    smileWords = ["smile", "smiling"]
    smileWordsbare = ['smile', 'smiling']
    nonsmileWords = ["%22not%20smile%22", "%22doesn%27t%20smile%22", "%22don%27t%20smile%22", "%22didn%27t%20smile%22", "%22no%20smile%22", "%22won%27t%20smile%22", "%22can't%20smile%22", "%22not%20able%20to%20smile%22", "%22never%20smile%22", "%22never%20smiles%22"]
    nonsmileWordsbare = ["notsmile", "doesntsmile", "dontsmile", "didntsmile", "nosmile", "wontsmile", "cantsmile", "notabletosmile", "neversmile", "neversmiles"]
    print "Hello."
    print "I am smileFinder"
    print "I will find and record all the smile words on the NPR transcript server."

#http://api.npr.org/query?fields=title,text,audio,transcript&requiredAssets=text,audio&searchTerm=doesn%27t%20smile&startNum=0&output=NPRML&numResults=20&searchType=fullContent&apiKey=MDA3MjY5MjE5MDEzMDE5MjY1NTczMzYzMA001

    #smileWords
    x = -1
    while x < len(smileWords)-1:
        x = x+1
        count = 0
        while count < 200:
            limits = (count + 20)
            time.sleep(2)
            countString = str(count)
            print countString + " to " + str(limits)
            smileFile = urlopen("http://api.npr.org/query?fields=title,text,audio,transcript&requiredAssets=text,audio&searchTerm=" + smileWords[x] + "&startNum=" + countString + "&output=NPRML&numResults=20&searchType=fullContent&apiKey=MDA3MjY5MjE5MDEzMDE5MjY1NTczMzYzMA001")
            output = smileFile.read()
            words = output.split()
            count = count + 20
            title = smileWordsbare[x]
            logfile = open('NPRsearch' + title + '.log', "a")
            logfile.write(output)
            logfile.close()
            
    #nonsmileWords        
    x = -1
    while x < len(nonsmileWords)-1:
        x = x+1
        count = 0
        while count < 200:
            limits = (count + 20)
            time.sleep(2)
            countString = str(count)
            print countString + " to " + str(limits)
            smileFile = urlopen("http://api.npr.org/query?fields=title,text,audio,transcript&requiredAssets=text,audio&searchTerm=" + nonsmileWords[x] + "&startNum=" + countString + "&output=NPRML&numResults=20&searchType=fullContent&apiKey=MDA3MjY5MjE5MDEzMDE5MjY1NTczMzYzMA001")
            output = smileFile.read()
            nonsmileResults = []
            count = count + 20
            title = nonsmileWordsbare[x]
            logfile = open('NPRsearch' + title + '.log', "a")
            logfile.write(output)
            logfile.close()
