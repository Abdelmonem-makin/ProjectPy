
import customtkinter as ctk
from Fun.AttendanceFun import AttendanceFun
import tkinter as tk
ctk.set_appearance_mode("System") 
class AttendancePage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        # configure grid layout (4x4)
        self.AttendanceF = AttendanceFun(self)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        
        self.navframe = ctk.CTkFrame(self)
        self.navframe.configure(width=850,height=50 ,fg_color="white",corner_radius=3)
        self.navframe.pack_propagate(False)
        self.navframe.pack(side="top" ,fill="both", expand="true") 
        
        self.logo_label = ctk.CTkLabel(self.navframe, text="Attendance Screen Page ",text_color="dark blue", font=ctk.CTkFont(size=15, weight="bold"))
        self.logo_label.pack(side="left",fill="x",ipady=10, padx  = 13, )
    

        # create Lac table
        self.lacTable = ctk.CTkFrame(self)
        self.lacTable.configure(height=750 ,fg_color="transparent")
        self.lacTable.pack_propagate(False)
        self.lacTable.pack(side="top" ,fill="both", expand="true")
         # create textbox
        self.scrollable_frame2 = ctk.CTkScrollableFrame(self.lacTable,label_fg_color="white", label_text_color="dark blue", label_text="Attendanc List")
        self.scrollable_frame2.configure(width=675,height=100 ,fg_color="transparent")
        self.scrollable_frame2.pack_propagate(False)
        self.scrollable_frame2.pack(side="left" , padx=8,pady=8, fill="both", expand="true")
        headers = ['rollNum','Std Name',"Subject","count_attendance", 'Superviser', 'Time']
        for col, header in enumerate(headers):
            self.label = ctk.CTkLabel(self.scrollable_frame2,fg_color= 'dark blue',text_color='white',width=110,corner_radius=3, text=header,font=("Arial", 12, "bold"))
            self.label.grid(row=0, column=col, padx=1, pady=1)
        attendanc = self.AttendanceF.listAttendance()

        data = attendanc
        for row, row_data in enumerate(data, start=1):
            print(row_data)

            for col, value in enumerate(row_data):
                # print(value)
                entry = ctk.CTkLabel(self.scrollable_frame2,text=value,text_color='dark blue', fg_color='white', width=115)
                entry.grid(row=row, column=col,padx=1, pady=1)
