from django.db import models

#Creates an instance for each student
class Student:
    def __init__(self,number_of_classes,registration,name,school_absence,p1, p2, p3):
        self.registration = int(registration)
        self.name = name
        self.school_absence= school_absence
        self.number_of_classes = number_of_classes
        self.media = int((int(p1) + int(p2) + int(p3))/3)

#With student data, it returns the necessary information in tuple form
    def get_situation(self):
        #failed due to absence
        if int(self.school_absence) > int(self.number_of_classes)/4:
            return (self.name,self.registration+3,'Reprovado Por Falta',self.media,0)
        #insufficient average
        elif self.media < 50:
            return (self.name,self.registration+3,'Reprovado por Média',self.media,0)
        #approved
        elif self.media >= 70:
            return (self.name,self.registration+3,'Aprovado',self.media,0)
        #final exam
        else:
            return(self.name,self.registration+3,'Exame Final',self.media,100-self.media)




