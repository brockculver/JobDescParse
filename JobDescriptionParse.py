import nltk
from nltk import corpus
import docx
import time
import edReqs
import os


def main():
    DocName="JDTest1.docx";
    cwd = os.getcwd()+"\\"
    DocType=DocName.split(".")[1]

    jobDesc=readDesc(cwd+DocName,DocType)
    print(jobDesc)

    education=edReq(jobDesc)
    print(education)

def readDesc(name,type):
    if(type=="docx"):
        doc = docx.Document(name)
        i=0
        jobDescStr=""
        for p in doc.paragraphs:
            i+=1
        for x in range(0, i):
            jobDescStr=jobDescStr+doc.paragraphs[x].text+" "
        return jobDescStr
    else:
        #TODO: insert support for other file formats (.pdf, .txt, etc.)
        return

def edReq(desc):
    edInfo=edReqs.edR()
    degReq=""

    idx=edInfo.matchDegree(desc)
    if idx!=-1:
        majReq=desc[idx:idx+200]
    else:
        majReq="No Match :("
    return [majReq]


main()

# TknString=nltk.word_tokenize(string)
# #print(bigresult)
#
# #big= nltk.help.upenn_tagset() #-to see the parts of speech identifiers
# #print(big)
#
# #Puts in the stop word set
# stop_words = set(stopwords.words('english'))
# filtTknString = [w for w in TknString if not w in stop_words]
# print(filtTknString)
#
# #Tags the words with their parts of speech
# taggedResult=nltk.pos_tag(filtTknString)
# print(taggedResult)
#
# #Count highest appearing parts of speech
# def findtags(tag_prefix, tagged_text):
#     cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text
#                                   if tag.startswith(tag_prefix))
#     return dict((tag, cfd[tag].most_common(5)) for tag in cfd.conditions())
#
# tagdict = findtags('JJ', taggedResult)
# for tag in sorted(tagdict):
#     print(tag, tagdict[tag])
