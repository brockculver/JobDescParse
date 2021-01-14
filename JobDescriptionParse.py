import nltk
from nltk import corpus
import docx
import time
import os

class JDparser:
    def readDesc(self,name,type):
        if(type=="docx"):
            doc = docx.Document(name+"."+type)
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

    def degReq(self,desc):
        edInfo=edR()
        degReq=""

        idx=edInfo.matchDegree(desc)
        if idx[0]!=-1:
            majReq=desc[idx[0]-20:idx[0]+40]
            # print(idx[1])
            return [idx[1],majReq]
        else:
            majReq="No Matching degree :("
        return [majReq]

    def majReq(self,desc):
        edInfo=edR()
        degReq=""

        idx=edInfo.matchMajor(desc)
        if idx[0]!=-1:
            return idx
            # majReq=desc[idx[0]-20:idx[0]+40]
            # # print(idx[1])
            # return [idx[1],majReq]
        else:
            majReq="No Matching major :("
        return [majReq]

    def get_attributes(self):
        education=self.degReq(self.jobDesc)
        major=self.majReq(self.jobDesc)
        return["Attributes Detected of the Job Description:", education, major]

    def __init__(self, DocName):
       self.DocName = DocName.split(".")[0]
       self.DocType=DocName.split(".")[1]
       self.jobDesc=self.readDesc(self.DocName,self.DocType)


class edR:
    edDegrees=[ "master", "associate", "bachelor", "b.s", "m.s", "phd","dr.","doctor", "degree"]
    edMjrs=["""geological and geophysical engineering""","""industrial and manufacturing engineering""","""materials engineering""","""materials science""","""mechanical engineering""","""metallurgical engineering""","""mining and mineral engineering""","""naval architecture and marine engineering""","""nuclear engineering""","""petroleum engineering""","""miscellaneous engineering""","""engineering technologies""","""engineering and industrial management""","""electrical engineering technology""","""industrial production technologies""","""mechanical engineering related technologies""","""miscellaneous engineering technologies""","""materials science""","""nutrition sciences""","""general medical and health services""","""communication disorders sciences and services""","""health and medical administrative services""","""medical assisting services""","""medical technologies technicians""","""health and medical preparatory programs""","""nursing""","""pharmacy pharmaceutical sciences and administration""","""treatment therapy professions""","""community and public health""","""miscellaneous health medical professions""","""area ethnic and civilization studies""","""linguistics and comparative language and literature""","""french german latin and other common foreign language studies""","""other foreign languages""","""english language and literature""","""composition and rhetoric""","""liberal arts""","""humanities""","""intercultural and international studies""","""philosophy""","""religious studies""","""theology""","""religious vocations""","""anthropology""","""archeology""","""art history and criticism""","""history""","""united states history""","""cosmetology services and culinary arts""","""family and consumer sciences""","""military technologies""","""physical fitness parks recreation and leisure""","""construction services""","""electrical, mechanical, and precision technologies and production""","""transportation sciences and technologies""","""multi/interdisciplinary studies""","""court reporting""","""pre-law""","""legal studies""","""criminal justice""","""fire protection""","""public administration""","""public policy""","""n/a (less than bachelor's degree)""","""physical sciences""","""astronomy and astrophysics""","""atmospheric sciences and meteorology""","""chemistry""","""geology and earth science""","""geosciences""","""oceanography""","""physics""","""multi-disciplinary or general science""","""nuclear, industrial radiology, and biological technologies""","""psychology""","""educational psychology""","""clinical psychology""","""counseling psychology""","""industrial and organizational psychology""","""social psychology""","""miscellaneous psychology""","""human services and community organization""","""social work""","""interdisciplinary social sciences""","""general social sciences""","""economics""","""criminology""","""geography""","""international relations""","""political science and government""","""sociology""","""miscellaneous social sciences""","""environmental engineering""","""general agriculture""","""agriculture production and management""","""agricultural economics""","""animal sciences""","""food science""","""plant science and agronomy""","""soil science""","""miscellaneous agriculture""","""forestry""","""natural resources management""","""fine arts""","""drama and theater arts""","""music""","""visual and performing arts""","""commercial art and graphic design""","""film video and photographic arts""","""studio arts""","""fine arts""","""environmental science""","""biology""","""biochemical sciences""","""botany""","""molecular biology""","""ecology""","""genetics""","""microbiology""","""pharmacology""","""physiology""","""zoology""","""neuroscience""","""miscellaneous biology""","""cognitive science and biopsychology""","""general business""","""accounting""","""actuarial science""","""business management and administration""","""operations logistics and e-commerce""","""business economics""","""marketing and marketing research""","""finance""","""human resources and personnel management""","""international business""","""hospitality management""","""management information systems and statistics""","""miscellaneous business & medical administration""","""degree in communications""","""communications degree""","""journalism""","""mass media""","""advertising and public relations""","""communication technologies""","""information systems""","""computer programming and data processing""","""computer science""","""information sciences""","""computer administration management and security""","""computer networking and telecommunications""","""mathematics""","""applied mathematics""","""statistics and decision science""","""mathematics and computer science""","""general education""","""educational administration and supervision""","""school student counseling""","""elementary education""","""mathematics teacher education""","""physical and health education teaching""","""early childhood education""","""science and computer teacher education""","""secondary teacher education""","""special needs education""","""social science or history teacher education""","""teacher education: multiple levels""","""language and drama education""","""art and music education""","""miscellaneous education""","""library science""","""architecture""","""engineering""","""aerospace engineering""","""biological engineering""","""architectural engineering""","""biomedical engineering""","""chemical engineering""","""civil engineering""","""computer engineering""","""electrical engineering""","""engineering mechanics physics and science"""]

    def matchDegree(self, desc):
        locDegree=-1
        desc=desc.lower()
        for x in edR.edDegrees:
            try:
                # print(x)
                locDegree=desc.find(x)
                #print("locDegreeee: ")
                #print(locDegree)
            finally:
                #print("\n")
                if locDegree!=-1:
                    #print("\n found loc Degree")
                    return [locDegree,x]
        return [locDegree]

    def matchMajor(self, desc):
        anyMatches=0
        hitMajors=[]
        locDegree=-1
        desc=desc.lower()

        for x in edR.edMjrs:
            locDegree=desc.find(x)
            if locDegree!=-1:
                anyMatches+=1
                hitMajors.append(x)
                hitMajors.append(locDegree)
        if anyMatches!=0:
            return hitMajors
        return [locDegree]
