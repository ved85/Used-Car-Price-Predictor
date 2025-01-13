"""
Author: Vedant Varma

"""
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox
import joblib
from PIL import Image, ImageTk, ImageSequence
import pandas as pd

class App:
    def __init__(self,root):
        self.root = root
        self.root.configure()
        self.root.title("[V]_CAR_PRICE_PREDICTOR")
        self.center_window(root,828,500)
        self.root.resizable(0,0)
        vcmd = (self.root.register(self.validate_entry), '%P')
        llf = ("comic sans",14,"bold")
        ltitle = Label(self.root,fg="#ff5900", bg="blue",text="[V]_CAR_PRICE_PREDICTOR",font=("comic sans", 28, "bold"))
        ltitle.pack(fill=BOTH,pady=20)
        pplb = Label(root,text="Present Price:",font=llf)
        pplb.place(x=28,y=100)
        self.ppr = ttk.Entry(root,font=llf,validate="key", validatecommand=vcmd,width=14)
        self.ppr.place(x=220,y=100)
        kmlb = Label(root,text="Kilometers Driven:",font=llf)
        kmlb.place(x=28,y=150)
        self.kmd = ttk.Entry(root,font=llf,validate="key", validatecommand=vcmd,width=14)
        self.kmd.place(x=220,y=150)
        ftlb = Label(root,text="Fuel Type:",font=llf)
        ftlb.place(x=28,y=200)
        self.combo_list = ["Petrol", "Diesel"]
        self.ft = ttk.Combobox(root, font=llf, values=self.combo_list,width=8)
        self.ft.current(0)
        self.ft.place(x=220,y=200)
        stlb = Label(root,text="Seller Type:",font=llf)
        stlb.place(x=28,y=250)
        self.combo_listst = ["Dealer", "Individual"]
        self.st = ttk.Combobox(root, font=llf, values=self.combo_listst,width=9)
        self.st.current(0)
        self.st.place(x=220,y=250)
        ttlb = Label(root,text="Transmission Type:",font=llf)
        ttlb.place(x=28,y=300)
        self.combo_listtt = ["Manual", "Automatic"]
        self.tt = ttk.Combobox(root, font=llf, values=self.combo_listtt,width=9)
        self.tt.current(1)
        self.tt.place(x=220,y=300)
        nolb = Label(root,text="Number of Owners:",font=llf)
        nolb.place(x=28,y=350)
        self.no = ttk.Spinbox(root,from_=1,to=8888,font=llf,validate="key",validatecommand=vcmd,width=5)
        self.no.place(x=220,y=350)
        aclb = Label(root,text="Age of Car:",font=llf)
        aclb.place(x=28,y=400)
        self.ac = ttk.Spinbox(root,from_=1,to=8888,font=llf,validate="key", validatecommand=vcmd,width=5)
        self.ac.place(x=220,y=400)
        canvas = Canvas(root, width=400, height=238,bd=5,relief="sunken")
        canvas.place(x=400,y=80)
        gif = Image.open(".//vr//agh.gif")
        frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(gif)]
        current_frame = 0
        gif_image = canvas.create_image(400//2, 238//2, image=frames[current_frame])
        def play_gif():
            nonlocal current_frame
            current_frame = (current_frame + 1) % len(frames)
            canvas.itemconfig(gif_image, image=frames[current_frame])
            root.after(100, play_gif)
        play_gif()
        opl = Label(root,text="Selling_Price = ",font=("comic sans",20,"bold"))
        opl.place(x=400,y=338)
        self.opll = Label(root,text="£8888888",font=("LCDMONO2",28,"bold"),fg="#22FF0E",bg="black",borderwidth=8, relief="sunken")
        self.opll.place(x=618,y=338)
        cbtn = Button(root,font=("LCDMONO2",20,"bold"),bg="blue",fg="white",text="CALCULATE",bd=4,command=self.calculate)
        cbtn.place(x=618,y=400)
        self.cvar = IntVar()
        style = ttk.Style()
        style.configure('Custom.TCheckbutton',font=("LCDMONO2",20,"bold"), foreground='blue')
        sonic = ttk.Checkbutton(root,variable=self.cvar,text="SONIC MODE",style='Custom.TCheckbutton',command=self.sonic)
        sonic.place(x=418,y=408)
        cltn = Button(root,font=("LCDMONO2",20,"bold"),bg="blue",fg="white",text="CLEAR",bd=4,command=self.clean)
        cltn.place(x=28,y=448)
        cntn = Button(root,font=("LCDMONO2",20,"bold"),bg="blue",fg="white",text="CONVERT",bd=4,command=self.convert)
        cntn.place(x=180,y=448)
        vf = Label(root,text="[V] VARMA INDUSTRIES")
        vf.pack(side=(BOTTOM))

    def validate_entry(self,text):
        if text == "" or text.replace('.', '', 1).isdigit():
            return True
        else:
            return False

    def center_window(self,window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        window.geometry(f'{width}x{height}+{x}+{y}')

    def sonic(self):
        if self.cvar.get() == 1:
            self.no.set("1")
            self.no.config(state=DISABLED)
            self.ac.set("8")
            self.ac.config(state=DISABLED)
            self.kmd.insert(0,"80000")
            self.kmd.config(state=DISABLED)
        else:
            self.no.config(state=NORMAL)
            self.no.delete(0,END)
            self.ac.config(state=NORMAL)
            self.ac.delete(0,END)
            self.kmd.config(state=NORMAL)
            self.kmd.delete(0,END)

    def convert(self):
        tcon = Toplevel()
        vcmd = (tcon.register(self.validate_entry), '%P')
        tcon.title("Mi to Km Converter")
        tcon.resizable(0,0)
        self.center_window(tcon,348,180)
        mll = Label(tcon,text="Miles:",font=("Comic Sans",14,"bold"))
        mll.grid(row=0, column=0, padx=10, pady=10)
        em = ttk.Entry(tcon,font=("Comic Sans",14,"bold"),validate="key", validatecommand=vcmd,width=14)
        em.grid(row=0, column=1, padx=10, pady=10)

        def cmtk():
            miles = float(em.get())
            km = miles * 1.60934
            lr.config(text=f"{km:.2f}")

        def cpc():
            km_text = lr.cget("text")
            root.clipboard_clear()
            root.clipboard_append(km_text)

        cb = ttk.Button(tcon, text="Convert", command=cmtk)
        cb.grid(row=0, column=2, padx=10, pady=10)
        lr = Label(tcon, text="0.00 km",font=("Comic Sans",14,"bold"))
        lr.grid(row=1, column=0, columnspan=3, pady=10)
        ccb = ttk.Button(tcon, text="Copy km value", command=cpc)
        ccb.grid(row=2, column=0, columnspan=3, pady=10)

    def calculate(self):
        
        prp = self.ppr.get()
        kkd = self.kmd.get()
        fuel = self.ft.get()
        sellt = self.st.get()
        transmission = self.tt.get()
        noo = self.no.get()
        acc = self.ac.get()

        if prp  == "" or kkd == "" or fuel == "" or sellt == "" or transmission == "" or noo == "" or acc == "":
                tkinter.messagebox.showwarning("Unable to Process","Please enter all details")
        else:
            def ci(value):
                if value.lower() == 'dealer' or value.lower() == 'petrol' or value.lower() == 'manual':
                    return '0'
                elif value.lower() == 'individual' or value.lower() == 'diesel' or value.lower() == 'automatic':
                    return '1'
                else:
                    return None
            prp = float(prp)
            prp = prp/1000
            kkd = float(kkd)
            fuel = ci(self.ft.get())
            sellt = ci(self.st.get())
            transmission = ci(self.tt.get())
            noo = int(noo)
            acc = int(acc)

            vmodel = joblib.load('vr//vcar_predictor')
            vdf = pd.DataFrame({
            'Present_Price': prp,
            'Kms_Driven': kkd,
            'Fuel_Type': fuel,
            'Seller_Type': sellt,
            'Transmission': transmission,
            'Owner': noo,
            'age': acc
        }, index=[0])
            
        vr = vmodel.predict(vdf)
        vr = (' '.join(map(str, vr*1000)))
        vr = float(vr)

        self.opll.config(text=(f"£{vr:.2f}"))
            



    def clean(self):
        self.ppr.delete(0,END)
        self.kmd.delete(0,END)
        self.ft.delete(0,END)
        self.st.delete(0,END)
        self.tt.delete(0,END)
        self.no.delete(0,END)
        self.ac.delete(0,END)
        tkinter.messagebox.showinfo("Notification:", "All Entrys Cleared")


if __name__ == "__main__":
    root=Tk()
    obj = App(root)
    root.mainloop()