import tkinter as tk

root = tk.Tk()

root.title("Addition Calculator")
root.geometry("400x300")

tk.Label(root,text="marvellous infosystem",
         font=("Arial", 18,"bold")).pack(padx=10)

tk.Label(root, text="Enter first number").pack()
entry1=tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number").pack()
entry2=tk.Entry(root)
entry2.pack()

def Addition():
    no1 = int(entry1.get())
    no2 = int(entry2.get())
    
    result = no1 + no2
    
    labelResult.config(text="Addition is :"+str(result))
    
tk.Button(root,text="Ans",command=Addition).pack(pady=15)

labelResult = tk.Label(root,text="",font=("Arial",14))

labelResult.pack()

root.mainloop()                                                                 