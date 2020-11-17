#TODO Fill in all education Requirement data
class edR:
    edDegrees=[ "master", "associate", "bachelor", "b.s", "m.s", "phd","dr","doctor"]
    edMjrs=["Computer Science", "Engineering", "Data Science"]

    def matchDegree(self, desc):
        locDegree=-1
        desc=desc.lower()
        for x in edR.edDegrees:
            try:
                print(x)
                locDegree=desc.find(x)
                #print("locDegreeee: ")
                #print(locDegree)
            finally:
                #print("\n")
                if locDegree!=-1:
                    #print("\n found loc Degree")
                    return locDegree
        return locDegree
