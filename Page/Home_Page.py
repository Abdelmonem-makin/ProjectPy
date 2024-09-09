import customtkinter as ctk
import tkinter as tk
import datetime
from Fun.LactuerFun  import lacTableFun
import Attendance
from Fun.SubjectFun  import SubjecFun

ctk.set_appearance_mode("System") 
class HomePage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.lacTableFunDB = lacTableFun(self)
        self.DB = SubjecFun(self)

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        
        self.navframe = ctk.CTkFrame(self)
        self.navframe.configure(width=850,height=50 ,corner_radius=3,fg_color="white")
        self.navframe.pack_propagate(False)
        self.navframe.pack(side="top" ,fill="both", expand="true",pady=(0,10)) 
        
        self.logo_label = ctk.CTkLabel(self.navframe, text="Home Screen   ",text_color="dark blue", font=ctk.CTkFont(size=15, weight="bold"))
        self.logo_label.pack(side="left",fill="x",ipady=10, padx=8)

        
          
        self.mainFrame = ctk.CTkFrame(self)
        self.mainFrame.configure(width=850,height=100 ,fg_color="transparent")
        self.mainFrame.pack_propagate(False)
        self.mainFrame.pack(side="top" ,fill="both", expand="true")
        
        self.logo_label1 = ctk.CTkLabel(self.mainFrame,text="",fg_color="dark blue",width=5,height=100,corner_radius=3)
        self.logo_label1.pack(side="left",  )
        self.Techer_label = ctk.CTkLabel(self.mainFrame, text="Total Techer \n\n  0",width=110,height=80,fg_color='white',text_color="dark blue", font=ctk.CTkFont(size=15, weight="bold"))
        self.Techer_label.pack(side="left",fill="both",ipady=2, padx  = (0,11),expand="true"  )
        
        self.logo_label1 = ctk.CTkLabel(self.mainFrame,text="",fg_color="dark blue",width=5,height=100,corner_radius=3)
        self.logo_label1.pack(side="left", padx  = (10,0)  )
        self.Student_label = ctk.CTkLabel(self.mainFrame, text="Total Student \n\n  0",width=110,height=80,fg_color='white',text_color="dark blue",font=ctk.CTkFont(size=15, weight="bold"))
        self.Student_label.pack(side="left",fill="both",ipady=2, padx  = (0,10), expand="true" )
        
        self.logo_label1 = ctk.CTkLabel(self.mainFrame,text="",fg_color="dark blue",width=5,height=100,corner_radius=3)
        self.logo_label1.pack(side="left", padx  = (10,0)  )
        self.Subject_label = ctk.CTkLabel(self.mainFrame, text="Total Subject \n\n  0",width=110,height=50,fg_color='white',text_color="dark blue", font=ctk.CTkFont(size=15, weight="bold"))
        self.Subject_label.pack(side="left",fill="both",ipady=2, expand="true")
        
      
        
        # create Lac table
        self.lacTable = ctk.CTkFrame(self)
        self.lacTable.configure(height=750 ,fg_color="transparent")
        self.lacTable.pack_propagate(False)
        self.lacTable.pack(side="top" ,fill="both", expand="true")
         # create textbox
        self.scrollable_frame2 = ctk.CTkScrollableFrame(self.lacTable,label_fg_color="white", label_text_color="dark blue", label_text="Lac today")
        self.scrollable_frame2.configure(width=675,height=100 ,fg_color="transparent")
        self.scrollable_frame2.pack_propagate(False)
        self.scrollable_frame2.pack(side="left" ,pady=8, fill="both", expand="true")
        self.dataview()
    
        self.regestForm = ctk.CTkFrame(self.lacTable)
        self.regestForm.configure(width=470,height=800 ,fg_color="white")
        self.regestForm.pack_propagate(False)
        self.regestForm.pack(side="top" ,  pady=(5,0) ,fill="both", expand="true")
        
        self.attendancframe = ctk.CTkFrame(self.regestForm) 
        self.attendancframe.configure(width=470,height=100 ,fg_color="white")
        self.attendancframe.pack_propagate(False)
        self.attendancframe.pack(side="top" ,fill="x" )

        self.Subj_Name = ctk.CTkComboBox(master=self.attendancframe,width=100,fg_color="white", button_color= 'dark blue',border_width=2,
                                         values=self.subjectName() )
        self.Subj_Name.pack(side="top", fill="x", pady="5", expand="true", padx=8)

        self._ok_button = ctk.CTkButton(master=self.attendancframe,width=100 ,height=100,fg_color="dark blue",border_width=0,text='Star Attendanc', command=self.startAttendance)
        self._ok_button.pack(side="left",fill="x",pady="5", expand="true",padx=8)
        
        
        self._ok_button = ctk.CTkButton(master=self.attendancframe,width=100,height=100,fg_color="dark blue",border_width=0,text='End Attendanc',command=self.end_Attendance)
        self._ok_button.pack(side="left" ,fill="x",pady="5", expand="true",padx=8)

        self.Printreport = ctk.CTkFrame(self.regestForm)
        self.Printreport.configure(width=470,height=100 ,fg_color="white")
        self.Printreport.pack_propagate(False)
        self.Printreport.pack(side="top" ,fill="x" )
        self._ok_button = ctk.CTkButton(master=self.Printreport, width=100, height=100, fg_color="dark blue",
                                        border_width=0, text='Print report', command=self.end_Attendance)
        self._ok_button.pack(side="top", fill="x", pady="5", expand="true", padx=8)

        self.reportFrame = ctk.CTkFrame(self.regestForm) 
        self.reportFrame.configure(width=470,height=400 ,fg_color="white")
        self.reportFrame.pack_propagate(False)
        self.reportFrame.pack(side="top",fill="x", ) 

    def dataview(self):
        headers = ['Day',"Time", "Subject",'teacher']    
        for col, header in enumerate(headers):
            self.label = ctk.CTkLabel(self.scrollable_frame2,fg_color= 'dark blue',text_color='white',width=150,corner_radius=3, text=header,font=("Arial", 12, "bold"))
            self.label.grid(row=0, column=col, padx=1, pady=1)

        data = self.lacTableFunDB.toDayLac()
        for row, row_data in enumerate(data, start=1):
            for col, value in enumerate(row_data):
                entry = ctk.CTkLabel(self.scrollable_frame2,text=value,text_color='dark blue', fg_color='white', width=150)
                entry.grid(row=row, column=col,padx=1, pady=1)
        

      

        
    def subjectName(self):
        name =[]
        data = self.lacTableFunDB.list_Atten_Subject()
        for row, row_data in enumerate(data):
            for col, value in enumerate(row_data):
               name.append(value)
        return name
    def startAttendance(self):
        Attendance.start_attendence(self.suSubj_Name.g)
    
    def end_Attendance(self):
        Attendance.close_video()
        
     
  

        
