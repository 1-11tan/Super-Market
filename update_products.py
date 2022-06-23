import tkinter
import tkinter.ttk
import csv
import os
import tkinter.messagebox

class sup:

    def remove_record(self):
        rd=open("products.csv","r")
        wr=open("temp.csv","w", newline="")
        reader=csv.reader(rd)
        writer=csv.writer(wr)
        for row in reader:
            if row[0]==self.txt1.get():
                tkinter.messagebox.showinfo("Super Market","Record Removed")
            else:
                writer.writerow(row)
        rd.close()
        wr.close()
        os.remove("product.csv")
        os.rename("temp.csv","product.csv")

    def search(self):
        rd=open("product.csv","r")
        for row in reader:
            if row[0]==self.txt1.get():
                self.txt2.insert(0,row[1])
                self.cb1.set(row[3])
                self.txt3.insert(0,row[2])
                self.txt4.insert(0,row[4])
                self.txt5.insert(0,row[5])
                self.txt6.insert(0,row[6])
                break
        rd.close()


    def __init__(self):
        self.root=tkinter.Tk()
        self.root.geometry("500x500")

        self.lb1=tkinter.Label(self.root, text="Enter Product ID")
        self.txt1=tkinter.Entry(self.root)

        self.lb2 = tkinter.Label(self.root, text="Enter Product Name")
        self.txt2 = tkinter.Entry(self.root)

        self.lb3 = tkinter.Label(self.root, text="Category")
        self.cb1 = tkinter.ttk.Combobox(self.root, values=("FMCG", "Cosmetics", "Cleaning Solution", "Groceries", "Dairy Products"))

        self.lb4 = tkinter.Label(self.root, text="Price")
        self.txt3 = tkinter.Entry(self.root)

        self.lb5 = tkinter.Label(self.root, text="Offer")
        self.txt4 = tkinter.Entry(self.root)

        self.lb6 = tkinter.Label(self.root, text="Discount")
        self.txt5 = tkinter.Entry(self.root)

        self.lb7 = tkinter.Label(self.root, text="Customer Phone Number")
        self.txt6 = tkinter.Entry(self.root)

        self.bt1 = tkinter.Button(self.root,text="Add Product",command=self.remove_record)

        self.lb1.grid(row=0, column=0)
        self.txt1.grid(row=0, column=1)

        self.lb2.grid(row=1, column=0)
        self.txt2.grid(row=1, column=1)

        self.lb3.grid(row=2, column=0)
        self.cb1.grid(row=2, column=1)

        self.lb4.grid(row=3, column=0)
        self.txt3.grid(row=3, column=1)

        self.lb5.grid(row=4, column=0)
        self.txt4.grid(row=4, column=1)

        self.lb6.grid(row=5, column=0)
        self.txt5.grid(row=5, column=1)

        self.lb7.grid(row=6, column=0)
        self.txt6.grid(row=6, column=1)

        self.bt1.grid(row=7,column=1)

        self.root.mainloop()

# -------------------------------------------------------------
#obj=sup()