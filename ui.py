import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter.ttk import *
global user_input
b=0

root = tk.Tk()
root.attributes('-fullscreen', True)
bg = Image.open("C:\\Users\\DELL\\OneDrive\\Desktop\\PBL\\with_matrix\\flower-background-floral-border.png")
bg = bg.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.ANTIALIAS)
bg_image = ImageTk.PhotoImage(bg) # create compatible image
bg_label = Label(root, image=bg_image) #a lable to hold image
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
# Create a style object
style = Style(root)
root.title("Dijkstra's Algorithm Visualization")
for i in range(100):
    root.rowconfigure(i, weight=1)
    root.columnconfigure(i, weight=1)

heading= tk.Label(root, text="", font=("bold", 70, "underline"))
heading.grid(row=0,column=35,sticky="nw")

def nodes():
    global entry_a, entry_b, entry_c, k, e
    def submit():
        for i in range(b):
            entry_a = entry_a_list[i]
            entry_b = entry_b_list[i]
            entry_c = entry_c_list[i]
            
            a_ = int(entry_a.get())
            b_ = int(entry_b.get())
            c_ = int(entry_c.get())
            
            file = open('C:\\Users\\DELL\\OneDrive\\Desktop\\PBL\\with_matrix\\user_input.txt','a')
            file.write(str(a_)+'\n')
            file.write(str(b_)+'\n')
            file.write(str(c_)+'\n')
            file.close()
            print("stored node is: ",a_)
            print("stored node is: ",b_)
            print("stored node is: ",c_)
            print("data sorted in file")
        
    entry_a_list = []
    entry_b_list = []
    entry_c_list = []
    e=0
    def data():
        global x,y,z,k,e
        if k==True:
            x=7
            y=8
            z=9
            e=9
            k=False
        
        a= tk.Label(root, text="enter 1st node of an edge: ")
        a.grid(row=i+x,column=0,sticky="nw")
        entry_a = tk.Entry(root,bg="#BFFFC1")
        entry_a.grid(row=i+x,column=1,sticky="nw")
        entry_a_list.append(entry_a)
        
        a= tk.Label(root, text="enter 2nd node of an edge: ")
        a.grid(row=i+y,column=0,sticky="nw")
        entry_b = tk.Entry(root,bg="#BFFFC1")
        entry_b.grid(row=i+y,column=1,sticky="nw")
        entry_b_list.append(entry_b)
        
        a= tk.Label(root, text="enter weight between the 2 nodes: ")
        a.grid(row=i+z,column=0,sticky="nw")
        entry_c = tk.Entry(root,bg="#BFFFC1")
        entry_c.grid(row=i+z,column=1,sticky="nw")
        entry_c_list.append(entry_c)
        
        a= tk.Label(root, text="--------------------------------")
        a.grid(row=(i+z)+1,column=0,sticky="nw")
        x=x+4
        y=y+4
        z=z+4
        e=e+5
    k=True
    for i in range(b):
        data()
    button= tk.Button(root, text="Submit Data", bg='#ADD8E6', command=submit)
    button.grid(row=e,column=3)
    reset= tk.Button(root, text="Reset", bg='#ADD8E6', command=submit)
    reset.grid(row=e,column=3+1)

def submit0():
    user_input = int(entry0.get())
    print("User input:", user_input)
    file = open('C:\\Users\\DELL\\OneDrive\\Desktop\\PBL\\with_matrix\\user_input.txt','a')
    file.write(str(user_input)+'\n')
    file.close()
    print("total node sorted in file")
    total_edge()
n= tk.Label(root, text="enter the total number of nodes: ")
n.grid(row=1,column=0,sticky="nw")
entry0 = tk.Entry(root,bg="#BFFFC1")
entry0.grid(row=2,column=0,sticky="nw")
button= tk.Button(root, text="Submit Total Nodes", bg='#ADD8E6', command=submit0)
button.grid(row=3,column=0,sticky="nw")

def total_edge():
    def submit1():
        global b
        user_input = int(entry1.get())
        b=int(user_input)
        print("User input:", user_input)
        file = open('C:\\Users\\DELL\\OneDrive\\Desktop\\PBL\\with_matrix\\user_input.txt','a')
        file.write(str(user_input)+'\n')
        file.close()
        print("total edges sorted in file")
        nodes()
    e= tk.Label(root, text="enter the total number of edges: ")
    e.grid(row=4,column=0,sticky="nw")
    entry1 = tk.Entry(root,bg="#BFFFC1")
    entry1.grid(row=5,column=0,sticky="nw")
    button= tk.Button(root, text="Submit Total Edges", bg='#ADD8E6', command=submit1)
    button.grid(row=6,column=0,sticky="nw")

def submit():
    source_input = int(source.get())
    destination_input = int(destination.get())
    print("User input:", source_input)
    print("User input:", destination_input)
    file = open('C:\\Users\\DELL\\OneDrive\\Desktop\\PBL\\with_matrix\\user_input.txt','a')
    file.write(str(source_input)+'\n')
    file.write(str(destination_input)+'\n')
    file.close()
    print("source and destination are sorted in file")
    import dijkestra_algo
    file=open('C:\\Users\\DELL\\OneDrive\\Desktop\\PBL\\with_matrix\\user_input.txt','a')
    file.clear()
    file.close()
n= tk.Label(root, text="enter the destination node: ")
n.grid(row=1,column=3,sticky="nw")
source = tk.Entry(root,bg="#BFFFC1")
source.grid(row=2,column=3,sticky="nw")
d= tk.Label(root, text="enter the source node: ")
d.grid(row=3,column=3,sticky="nw")
destination = tk.Entry(root,bg="#BFFFC1")
destination.grid(row=4,column=3,sticky="nw")
button= tk.Button(root, text="Run Dijkestra!", bg='#ADD8E6', command=submit)
button.grid(row=5,column=3,sticky="nw")

root.mainloop()