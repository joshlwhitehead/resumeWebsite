from tkinter import *
from testt import test2
def xxx():
    print(test2.x)
root = Tk()                                                                                             #initialize user interface window
root.geometry("400x400")                                                                                #set size of window

root.title("Heat Spreader Characterization Analysis Tool")                                                             #name ui window

run = Button(root,height=2,width=20,text='Analyze PCR',command=lambda:xxx())                            #create button that runs the above code when pushed
# run2 = Button(root,height=2,width=20,text='Analyze TC',command=lambda:analyzeTC())                            #create button that runs the above code when pushed
run.pack()
# run2.pack()
mainloop()
