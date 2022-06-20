import tkinter
import tkinter.messagebox
import AddProducts
import Billing
import update_products
import view_products


class myprogram:
    def open_AddProducts(self):
        obj=AddProducts.sup()
    def open_view_products(self):
        obj=view_products.sup()
    def open_update_products(self):
        obj=update_products.sup()
    def open_raisebill(self):
        obj=Billing.billing()
    def __init__(self):

        self.root=tkinter.Tk()
        self.root.geometry("1000x1000")

        self.mymenu=tkinter.Menu(self.root)
        self.root.title("Welcome to My Super Market")

        self.root.config(menu=self.mymenu)
        self.submenu1=tkinter.Menu(self.mymenu, tearoff=False)
        self.mymenu.add_cascade(label="Product Management", menu=self.submenu1)
        self.submenu1.add_command(label="Add product",command=self.open_AddProducts)
        self.submenu1.add_command(label="View product",command=self.open_view_products)
        self.submenu1.add_command(label="Remove product",command=self.open_update_products)

        self.submenu2=tkinter.Menu(self.mymenu, tearoff=False)
        self.mymenu.add_cascade(label="Billing Management", menu=self.submenu2)
        self.submenu2.add_command(label="Raise Bill", command=self.open_raisebill)


        self.root.mainloop()
#------------------------------------------
obj=myprogram()