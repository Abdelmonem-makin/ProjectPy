
import customtkinter as ctk
from Fun.SubjectFun import SubjecFun
import tkinter as tk

ctk.set_appearance_mode("System") 
class subjectPage(ctk.CTkFrame):
    def __init__(self, master):
        
        self.DB = SubjecFun(self)
        
        super().__init__(master)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        
        self.navframe = ctk.CTkFrame(self)
        self.navframe.configure(width=850,height=50 ,fg_color="white",corner_radius=3)
        self.navframe.pack_propagate(False)
        self.navframe.pack(side="top" ,fill="both", expand="true") 
        
        self.logo_label = ctk.CTkLabel(self.navframe, text="subject   Screen Page ",text_color="dark blue", font=ctk.CTkFont(size=15, weight="bold"))
        self.logo_label.pack(side="left",fill="x",ipady=10, padx  = 13, )
       
        self._ok_button = ctk.CTkButton(master=self.navframe,width=50,height=10,fg_color="transparent",text_color="dark blue" , border_color= 'dark blue',border_width=2,text='Search',)
        self._ok_button.pack(side="right",fill="x",ipady=6, padx  = 13, )
        self._entry = ctk.CTkEntry(master=self.navframe,width=200,height=10,placeholder_text='Enter Subject Name .....',fg_color="transparent", border_color= 'dark blue',border_width=2,)
        self._entry.pack(side="right",fill="x",ipady=6, padx  = 13, )
        
        # create Lac table
        self.lacTable = ctk.CTkFrame(self)
        self.lacTable.configure(height=750 ,fg_color="transparent")
        self.lacTable.pack_propagate(False)
        self.lacTable.pack(side="top" ,fill="both", expand="true")
         # create textbox
        self.scrollable_frame2 = ctk.CTkScrollableFrame(self.lacTable,label_fg_color="white", label_text_color="dark blue", label_text="Subject List")
        self.scrollable_frame2.configure(width=250,height=100 ,fg_color="transparent")
        self.scrollable_frame2.pack_propagate(False)
        self.scrollable_frame2.pack(side="left" , padx=8,pady=8, fill="both", expand="true")
        self.Dataview()
        self.regestForm1 = ctk.CTkFrame(self.lacTable)
        self.regestForm1.configure(width=420,height=50 ,fg_color="white")
        self.regestForm1.pack_propagate(False)
        self.regestForm1.pack(side="top" , ipady=20, pady=(10,0) ,fill="x", expand="true")
        
        self._label = ctk.CTkLabel(master=self.regestForm1,width=300,text= 'Add subject' ,text_color="dark blue", font=ctk.CTkFont(size=15, weight="bold"),wraplength=300,fg_color="transparent",)
        self._label.pack(side="top" ,padx=40,  fill="both", expand="true")

        self.regestForm = ctk.CTkFrame(self.lacTable)
        self.regestForm.configure(width=420,height=750 ,fg_color="white")
        self.regestForm.pack_propagate(False)
        self.regestForm.pack(side="top" ,  pady=(0,10) ,fill="both", expand="true")
            
        
   
           
        self._label = ctk.CTkLabel(master=self.regestForm,text= 'Subject_name' ,width=50,wraplength=300,fg_color="transparent",text_color="dark blue", font=ctk.CTkFont(size=15, weight="bold"))
        self._label.place(x=50, y=50)
        self.Subj_name = ctk.CTkEntry(master=self.regestForm,width=200,fg_color="transparent", border_color= 'dark blue',border_width=2,)
        self.Subj_name.place(x=160, y=50)
           
        self.saveStud = ctk.CTkButton(master=self.regestForm,width=100,fg_color="dark blue",border_width=0,text='Save',command=self.saveFun)
        self.saveStud.place(x=50, y=100)
                
        self.editStd = ctk.CTkButton(master=self.regestForm,width=100,fg_color="dark blue",border_width=0,text='Edite',)
        self.editStd.place(x=160, y=100)
        
        self.deleteStd = ctk.CTkButton(master=self.regestForm,width=100,fg_color="dark blue",border_width=0,text='Delete',)
        self.deleteStd.place(x=270, y=100)

    def Dataview(self):
        headers = ["Name"]    
        for col, header in enumerate(headers):
            self.label = ctk.CTkLabel(self.scrollable_frame2,fg_color='dark blue',text_color='white',width=100,corner_radius=3, text=header,font=("Arial", 12, "bold"))
            self.label.grid(row=0, column=col, padx=1, pady=1)
        data = self.DB.listSubject()
        
        for row, row_data in enumerate(data, start=1):
            for col, value in enumerate(row_data):
                entry = ctk.CTkLabel(self.scrollable_frame2,text=value,text_color='dark blue', fg_color='white', width=100)
                entry.grid(row=row, column=col,padx=1, pady=1)
           
##############دالة حفظ البيانات في قاعدة البانات##################################################        
    def saveFun(self):
      
        self.DB.addSubject(self.Subj_name.get())
        self.Dataview()
        self.Subj_name.delete(0,'end')
        