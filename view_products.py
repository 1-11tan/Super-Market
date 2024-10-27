import csv
import tkinter
import tkinter.ttk

class sup:
    def __init__(self):
        self.root=tkinter.Tk()
        self.t1=tkinter.ttk.Treeview(self.root,columns=("pid","pname","price","catg","discount","offer","cno"))
        self.t1.heading("pid", text="Product ID")
        self.t1.heading("pname", text="Product Name")
        self.t1.heading("catg", text="Category")
        self.t1.heading("price", text="Price")
        self.t1.heading("discount", text="Discount")
        self.t1.heading("offer", text="Offer")
        self.t1.heading("cno", text="Customer No")
        self.t1.pack()
        self.t1["show"]="headings"

        rd=open("products.csv","r")
        reader=csv.reader(rd)
        i=0
        for row in reader:
            self.t1.insert("",index=i,values=row)
            i=i+1


        self.root.mainloop()
#--------------------------------------------------------------
#obj=sup()