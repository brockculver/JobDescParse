import tkinter as tk
from tkinter import *
from pyresparser import ResumeParser
from tkinter import filedialog, Tk, Label, Button
from JobDescriptionParse import JDparser
import time

class PromptGUI:
    def __init__(self, master):
        self.master = master
        master.title("Resume Remake")

        self.userInfo = Label(master, text="Select the resume to be altered with the \"Select Resume\" button\n Select the job description to be used with the \"Select Job Description\" button\n\nThere must be a selection of both resume and job description for a new resume to be created\n")
        self.userInfo.pack()

        self.resSelectionMade = Label(master, text="resume selected: No")
        self.resSelectionMade.pack()

        self.JDselectionMade = Label(master, text="job description selected: No\n")
        self.JDselectionMade.pack()

        self.resume_button = Button(master, text="Select Resume", command=self.ResSelect)
        self.resume_button.pack()

        self.jd_button = Button(master, text="Select Job Description", command=self.JDSelect)
        self.jd_button.pack()

        self.mkNew_button = Button(master, text="Make Resume", command=self.mkResume)

        self.resUploaded=0
        self.jdUploaded=0

        self.promptTech=Label(master, text ="technical skills:")
        self.promptTech.pack()
        self.promptTechPhrase=Label(master, text ='[]')
        self.promptTechPhrase.pack()

        self.promptSoft=Label(master, text ="soft skills:")
        self.promptSoft.pack()
        self.promptSoftPhrase=Label(master, text ='[]')
        self.promptSoftPhrase.pack()

        self.commonPrompt=Label(master, text ="most common words:")
        self.commonPrompt.pack()
        self.commonPromptWords=Label(master, text ='[]')
        self.commonPromptWords.pack()

        self.promptSkill=Label(master, text ="words identified as skill:")
        self.promptSkill.pack()
        self.promptSkillWords=Label(master, text ='[]')
        self.promptSkillWords.pack()

    def ResSelect(self):
        resFile= filedialog.askopenfilename(initialdir = "C:\\",title = "Select file",filetypes = (("pdf files","*.pdf"),("all files","*.*")))
        try:
            print(ResumeParser(resFile).get_extracted_data())
            self.resUploaded=1
            self.resSelectionMade['text'] = 'resume selected: Yes'
            if(self.resUploaded==1 and self.jdUploaded==1):
                self.mkNew_button.pack()
        except:
            self.errormessage1 = Label(master, text="Resume Selection Error")
            self.errormessage1.pack()

    def JDSelect(self):
        self.jdFile = filedialog.askopenfilename(initialdir = "C:\\Users\\brock\\OneDrive\\Desktop\\BokoMaru\\ReadfromJobApplication\\Job Descriptions",title = "Select file",filetypes = (("docx files","*.docx"),("all files","*.*")))
        try:
            tst=JDparser(self.jdFile)
            self.SkillRawMaterials=tst.get_attributes()

            majorPhrase = tst.mkAllPhrases(self.SkillRawMaterials)

            self.jdUploaded=1
            self.JDselectionMade['text'] = 'job description selected: Yes'

            self.promptSkills(majorPhrase)
            if(self.resUploaded==1 and self.jdUploaded==1):
                self.mkNew_button.pack()
        except:
            self.errormessage0 = Label(master, text="Job Description Selection Error")
            self.errormessage0.pack()

    def promptSkills(self, text):
        self.promptTechPhrase['text'] = text[0]
        self.promptSoftPhrase['text'] = text[1]
        self.commonPromptWords['text']=text[2]
        self.promptSkillWords['text']=text[3]

    def mkResume(self):
        jdFile = filedialog.askopenfilename(initialdir = "C:\\Users\\brock\\OneDrive\\Desktop\\BokoMaru\\ReadfromJobApplication\\Job Descriptions",title = "Select file",filetypes = (("docx files","*.docx"),("all files","*.*")))
        self.JDselectionMade.pack()
        tst=JDparser(jdFile)


root = Tk()
root.geometry('1000x600')
my_gui = PromptGUI(root)
root.mainloop()

#dfromfile=ResumeParser(resFile).get_extracted_data()
