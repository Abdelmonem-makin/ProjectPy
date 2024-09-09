
import customtkinter as ctk
import tkinter as tk
import tkinter as messagebox
from tkinter import filedialog
from Fun.studantFun import studantFun
from PIL import Image ,ImageTk
import os
import shutil

ctk.set_appearance_mode("System") 
class StudantPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        # configure grid layout (4x4)
        self.studantDB = studantFun(self)
        
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        
        
        self.navframe = ctk.CTkFrame(self)
        self.navframe.configure(width=850,height=50, corner_radius= 3  ,fg_color="white")
        self.navframe.pack_propagate(False)
        self.navframe.pack(side="top" ,fill="both", expand="true") 
        
        self.logo_label = ctk.CTkLabel(self.navframe, text="student Screen Page  ",text_color="dark blue", font=ctk.CTkFont(size=15, weight="bold"))
        self.logo_label.pack(side="left",fill="x",ipady=8, padx  = 13, ) 
        

        self._ok_button = ctk.CTkButton(master=self.navframe,width=50,height=10,fg_color="transparent",text_color="dark blue" , border_color= 'dark blue',border_width=2,text='Search',)
        self._ok_button.pack(side="right",fill="x",ipady=6, padx  = 13, )
        self.Stdsearch = ctk.CTkEntry(master=self.navframe,width=200,height=10,placeholder_text='Enter student Name .....',fg_color="transparent", border_color= 'dark blue',border_width=2,)
        self.Stdsearch.pack(side="right",fill="x",ipady=6, padx  = 13, )
            
        self.lacTable = ctk.CTkFrame(self)
        self.lacTable.configure(height=750 ,fg_color="transparent")
        self.lacTable.pack_propagate(False)
        self.lacTable.pack(side="top" ,fill="both", expand="true")
         # create textbox
        self.scrollable_frame2 = ctk.CTkScrollableFrame(self.lacTable,label_fg_color="white", label_text_color="dark blue", label_text="Studemt list")
        self.scrollable_frame2.configure(width=200,height=100 ,fg_color="transparent")
        self.scrollable_frame2.pack_propagate(False)
        self.scrollable_frame2.pack(side="left" , padx=8,pady=8, fill="both", expand="true")
        self.viewData()
                
######################## الفورم الخاص بتسجيل الطالب #################################
        self.regestForm1 = ctk.CTkFrame(self.lacTable)
        self.regestForm1.configure(width=420,height=20 ,fg_color="white")
        self.regestForm1.pack_propagate(False)
        self.regestForm1.pack(side="top" , ipady=20, pady=(10,0) ,fill="x", expand="true")
        
        self._label = ctk.CTkLabel(master=self.regestForm1,width=300,text= 'Add Student' ,text_color="dark blue", font=ctk.CTkFont(size=15, weight="bold"),wraplength=300,fg_color="transparent",)
        self._label.pack(side="top" ,padx=40,  fill="both", expand="true")

        self.regestForm = ctk.CTkFrame(self.lacTable)
        self.regestForm.configure(width=470,height=800 ,fg_color="white")
        self.regestForm.pack_propagate(False)
        self.regestForm.pack(side="top" ,  pady=(0,5) ,fill="both", expand="true")
            
        self.img_frame = ctk.CTkFrame(master=self.regestForm ,bg_color='transparent',corner_radius=8,border_width=3,border_color='darkblue', width=200,height=200)
        self.img_frame.place(x=130, y=0)
         
        self.img_label = ctk.CTkLabel(master=self.img_frame ,corner_radius=8, width=190,height=190,text="")
        self.img_label.place(x=3 ,y=3)
        
        self._ok_button = ctk.CTkButton(master=self.regestForm,width=200,fg_color="dark blue",border_width=0,text='Upload Image',command=self.upload_image)
        self._ok_button.place(x=130, y=203)

           
        self._label = ctk.CTkLabel(master=self.regestForm,text= 'Name' ,  width=50,wraplength=300,fg_color="transparent",text_color="dark blue", font=ctk.CTkFont(size=15, weight="bold"))
        self._label.place(x=30, y=240)
        self.StdName = ctk.CTkEntry(master=self.regestForm,width=200,fg_color="transparent", border_color= 'dark blue',border_width=2,)
        self.StdName.place(x=130, y=240)
        
        self._label = ctk.CTkLabel(master=self.regestForm,text= 'Roll Num' ,width=50,wraplength=300,fg_color="transparent",text_color="dark blue", font=ctk.CTkFont(size=15, weight="bold"))
        self._label.place(x=30, y=290)
        self.rollNum = ctk.CTkEntry(master=self.regestForm,width=200,fg_color="transparent", border_color= 'dark blue',border_width=2,)
        self.rollNum.place(x=130, y=290)
        
        self.saveStud = ctk.CTkButton(master=self.regestForm,width=100,fg_color="dark blue",border_width=0,text='Save',command=self.saveStdFun)
        self.saveStud.place(x=50, y=340)
                
        self.editStd = ctk.CTkButton(master=self.regestForm,width=100,fg_color="dark blue",border_width=0,text='Edite',command=self.updataFun)
        self.editStd.place(x=160, y=340)
        
        self.deleteStd = ctk.CTkButton(master=self.regestForm,width=100,fg_color="dark blue",border_width=0,text='Delete',)
        self.deleteStd.place(x=270, y=340)

    def viewData(self):
        headers = ["Roll Num","Name", "Img"]    
        for col, header in enumerate(headers):
            self.label = ctk.CTkLabel(self.scrollable_frame2,fg_color='dark blue',text_color='white',width=150,corner_radius=3, text=header,font=("Arial", 12, "bold"))
            self.label.grid(row=0, column=col, padx=1, pady=1)
####################تم انشاء كائن من الكلاس الخاص بقاعدة بيانات الطالب ###############################################
        studantData = self.studantDB.listStudant()
        self.data  = studantData
        # Add more rows as needed
       
        for row, row_data in enumerate(self.data, start=1):
            # print(row_data)
            for col, value in enumerate(row_data):
                entry = ctk.CTkLabel(self.scrollable_frame2,text=value,text_color='dark blue', fg_color='white', width=150)
                entry.grid(row=row, column=col,padx=1, pady=1)
        
##############دالة حفظ البيانات في قاعدة البانات##################################################
    def saveStdFun(self):
        self.studantDB.addStudant(self.StdName.get(),self.filename,self.rollNum.get())
        self.viewData()
        self.StdName.delete(0,'end')
        self.rollNum.delete(0,'end')
       

##############دالة حفظ البيانات في قاعدة البانات##################################################        
    def updataFun(self):
        self.studantDB.updataStudant(self.StdName.get(),self.filename,self.rollNum.get(),self.Stdsearch.get())
        self.viewData()
        self.StdName.delete(0,'end')
        self.rollNum.delete(0,'end')
       
# Define the function to upload and save the image
    def upload_image(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            self.image = Image.open(self.file_path)
            self.image.thumbnail((190, 190)) # Resize image if necessary
            self.photo = ImageTk.PhotoImage(self.image,size=(190, 190))
            self.img_label.configure(image=self.photo)
            self.img_label.image = self.photo # Keep a reference to avoid garbage collection
            self.save_image(self.file_path)
    def save_image(self , file_path):
        self.save_dir = "Std_images"
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)
        self.filename = os.path.basename(file_path)
        shutil.copy(file_path, os.path.join(self.save_dir, self.filename))
        print("Image saved to:", os.path.join(self.save_dir, self.filename))

