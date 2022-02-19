import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
data=pd.read_csv('Cryotherapy.csv')
X=data.drop(['Result_of_Treatment'],axis=1)
y=data['Result_of_Treatment']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.4,random_state=1)
log_reg=LogisticRegression()
model=log_reg.fit(X_train,y_train)
y_predict=log_reg.predict(X_test) 
print(y_predict)
import pickle    
Model = pickle.dumps(model)

import tkinter as tk
from tkinter.constants import LEFT, RAISED, RIGHT
window=tk.Tk()
window.title("Cryotherapy Classification")
frame1=tk.Frame(master=window,borderwidth=2,width=100,height=100,relief=tk.SUNKEN)
frame1.pack()

label1=tk.Label(master=frame1,text="Sex: ")
label1.grid(row=0,column=0,sticky='e')
sex=tk.Entry(master=frame1,relief=tk.SUNKEN,width=50)
sex.grid(row=0,column=1)

label2=tk.Label(master=frame1,text="Age: ")
label2.grid(row=1,column=0,sticky='e')
age=tk.Entry(master=frame1,relief=tk.SUNKEN,width=50)
age.grid(row=1,column=1)

label3=tk.Label(master=frame1,text="Time: ")
label3.grid(row=2,column=0,sticky='e')
Time=tk.Entry(master=frame1,relief=tk.SUNKEN,width=50)
Time.grid(row=2,column=1)

label4=tk.Label(master=frame1,text="Number_of_Warts: ")
label4.grid(row=3,column=0,sticky='e')
Number_of_Warts=tk.Entry(master=frame1,relief=tk.SUNKEN,width=50)
Number_of_Warts.grid(row=3,column=1)

label5=tk.Label(master=frame1,text="Type: ")
label5.grid(row=4,column=0,sticky='e')
Type=tk.Entry(master=frame1,relief=tk.SUNKEN,width=50)
Type.grid(row=4,column=1)

label6=tk.Label(master=frame1,text="Area: ")
label6.grid(row=5,column=0,sticky='e')
Area=tk.Entry(master=frame1,relief=tk.SUNKEN,width=50)
Area.grid(row=5,column=1)

frame2=tk.Frame(master=window,borderwidth=2)
frame2.pack(fill=tk.X,ipadx=5,ipady=5)
button2=tk.Button(master=frame2,text='Submit',width=10,relief=RAISED,command=lambda: Output())
button2.grid(row=0,column=0,padx=20,ipadx=10)
entry1=tk.Entry(master=frame2,relief=RAISED)
entry1.grid(row=0,column=1,padx=10,ipadx=10)
entry1.insert(0,'Result: ')
entry2=tk.Entry(master=frame2,relief=RAISED,width=40)
entry2.grid(row=1,column=1)
entry2.insert(0,'Accuracy: ')
entry2.insert(10,(roc_auc_score(y_test,y_predict)*100))

def Output():
    df=pd.DataFrame(columns=['sex','age','Time','Number_of_Warts','Type','Area'])
    df.loc[0,'sex']=sex.get()
    df.loc[0,'age']=age.get()
    df.loc[0,'Time']=Time.get()
    df.loc[0,'Number_of_Warts']=Number_of_Warts.get()
    df.loc[0,'Type']=Type.get()
    df.loc[0,'Area']=Area.get()

    if model.predict(df) == [0]:
        entry1.delete(8,tk.END)
        entry1.insert(8,'Not Affected')
    elif model.predict(df) == [1]:
        entry1.delete(8,tk.END)
        entry1.insert(8,'Affected')

    

window.mainloop()
