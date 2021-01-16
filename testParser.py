import tkinter as tk
from pyresparser import ResumeParser
from tkinter import filedialog, Tk, Label, Button
from JobDescriptionParse import JDparser

class PromptGUI:
    def __init__(self, master):
        self.master = master
        master.title("Resume Remake")

        self.userInfo = Label(master, text="Select the resume to be altered with the \"Select Resume\" button\n\n Select the job description to be used with the \"Select Job Description\" button\n")
        self.userInfo.pack()

        self.resume_button = Button(master, text="Select Resume", command=self.ResSelect)
        self.resume_button.pack()

        self.selectionMade = Label(master, text="resume selected\n")

        self.JDselectionMade = Label(master, text="job description selected\n")

        self.jd_button = Button(master, text="Select Job Description", command=self.JDSelect)
        self.jd_button.pack()

    def ResSelect(self):
        resFile= filedialog.askopenfilename(initialdir = "C:\\",title = "Select file",filetypes = (("pdf files","*.pdf"),("all files","*.*")))
        self.selectionMade.pack()
        print(ResumeParser(resFile).get_extracted_data())

    def JDSelect(self):
        jdFile = filedialog.askopenfilename(initialdir = "C:\\Users\\brock\\OneDrive\\Desktop\\BokoMaru\\ReadfromJobApplication\\Job Descriptions",title = "Select file",filetypes = (("docx files","*.docx"),("all files","*.*")))
        self.JDselectionMade.pack()
        tst=JDparser(jdFile)
        print(tst.get_attributes())
        # print(tst.DocName)
        # print(tst.DocType)
        # print(tst.jobDesc)
        # print(tst.education)
        # print(tst.major)


root = Tk()
my_gui = PromptGUI(root)
root.mainloop()
#dfromfile=ResumeParser(resFile).get_extracted_data()
