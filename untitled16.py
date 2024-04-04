# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 11:51:06 2024

@author: MS Surface Laptop
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 15:49:32 2024

@author: MS Surface Laptop
"""

from tkinter import*
from tkinter import messagebox
root=Tk()
root.title("advise to visit doctor or not")
root.geometry("500x434")

q1_rb=StringVar(value="0")
q1=Label(root,text="do you experience shortness of breath during routine activities?")
q1.pack()
q1_r1=Radiobutton(root,text="yes",variable=q1_rb,value="yes")
q1_r1.pack()
q1_r2=Radiobutton(root,text="no",variable=q1_rb,value="no")
q1_r2.pack()

q2_rb=StringVar(value="0")
q2=Label(root,text="  do you have swelling in your feet/ankles/legs(shoes fell lighter)or abdomen?")
q2.pack()
q2_r1=Radiobutton(root,text="yes",variable=q2_rb,value="yes")
q2_r1.pack()
q2_r2=Radiobutton(root,text="no",variable=q2_rb,value="no")
q2_r2.pack()


q3_rb=StringVar(value="0")
q3=Label(root,text="do you feel any of these symptoms - confusion disorientation or loss of memory?")
q3.pack()
q3_r1=Radiobutton(root,text="yes",variable=q1_rb,value="yes")
q3_r1.pack()
q3_r2=Radiobutton(root,text="no",variable=q1_rb,value="no")
q3_r2.pack()

q4_rb=StringVar(value="0")
q4=Label(root,text="do you experience shortness of breath while laying down?")
q4.pack()
q4_r1=Radiobutton(root,text="yes",variable=q3_rb,value="yes")
q4_r1.pack()
q4_r2=Radiobutton(root,text="no",variable=q3_rb,value="no")
q4_r2.pack()


q5_rb=StringVar(value="0")
q5=Label(root,text="do you experience wheezing/coughing that produes white or pnk blood tingled mucus?")
q5.pack()
q5_r1=Radiobutton(root,text="yes",variable=q3_rb,value="yes")
q5_r1.pack()
q5_r2=Radiobutton(root,text="no",variable=q3_rb,value="no")
q5_r2.pack()








def fever_score():
    score=0
    if q1_rb.get()=="yes":
        score=score+10
        print(score)
        
def fever_score():
    score=0
    if q2_rb.get()=="yes":
        score=score+10
        print(score)
        
def fever_score():
    score=0
    if q3_rb.get()=="yes":
        score=score+10
        print(score)
        
def fever_score():
    score=0
    if q4_rb.get()=="yes":
        score=score+10
        print(score)
        
        
def fever_score():
    score=0
    if q5_rb.get()=="yes":
        score=score+10
        print(score)
        
        
    
        
    if  score <=10:
        messagebox.showinfo("report-"," you dont need to visit the doctor")
            
    
    
 
        
    elif score >10 and score<=30:
        messagebox.showinfo("report-"," you might perhaps have to  visit the doctor")
        
    else :
        messagebox.showinfo("report-","  I strongly advise you visit the doctor")
        
       
btn=Button(root, text="click me",command=fever_score)
btn.pack()
root.mainloop()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    
    














