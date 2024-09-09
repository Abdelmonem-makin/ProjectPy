import customtkinter as ctk
import tkinter as tk
from Page.Home_Page import HomePage
from Page.StudantPage import StudantPage 
from Page.TetcherPage import TetcherPage 
from Page.AbutPage import  AbutPage 
from Page.subjectPage import  subjectPage
from Page.Admin import  admin
from Page.Lactuer_TablePage import lactuerTablePage 
from Page.AttendancePage import  AttendancePage 
ctk.set_appearance_mode("System") 
# Supported themes : green, dark-blue, blue
# ctk.set_default_color_theme("white")    

class sidebar(ctk.CTkFrame):
    def __init__(self, master ):
        super().__init__(master)
        self.sidebarFrame = ctk.CTkFrame(self)
        self.sidebarFrame.configure(width=80,height=400 ,fg_color="dark blue")
        self.sidebarFrame.pack_propagate(False)
        self.sidebarFrame.pack(side="left" ,pady = 8, padx=8 ,fill="both", expand="true")
        
        self.mainFrame = ctk.CTkFrame(self)
        self.mainFrame.configure(width=850,height=400 ,fg_color="transparent")
        self.mainFrame.pack_propagate(False)
        self.mainFrame.pack(side="left" ,fill="both", expand="true")
        
        self.homePage = HomePage(self.mainFrame)
        self.homePage.configure(width=850,height=600 ,fg_color="transparent")
        self.homePage.pack_propagate(False)
        self.homePage.pack(side="left",pady = 8, padx=8 ,fill="both", expand="true")
        
        self.StudantPage = StudantPage(self.mainFrame)
        self.TetcherPage = TetcherPage(self.mainFrame)
        self.AbutPage = AbutPage(self.mainFrame)
        self.subjectPage = subjectPage(self.mainFrame)
        self.AdminPage = admin(self.mainFrame)
        
        self.Lactuer_Table_Page = lactuerTablePage(self.mainFrame)
        self.AttendancePage = AttendancePage(self.mainFrame)
        
        self.logo_label = ctk.CTkLabel(self.sidebarFrame, text="Dashbord   ",text_color="white", font=ctk.CTkFont(size=15, weight="bold"))
        self.logo_label.pack(side="top",fill="x",ipady=13, padx  = 13, )
        
        
        self.home = ctk.CTkButton(self.sidebarFrame,corner_radius=8,hover="False",text_color="black",fg_color="white", text="Home",font=ctk.CTkFont(weight="bold"), command=lambda: self.haver(self.home , self.homePage))
        self.home.pack(side="top",fill="x",ipady=8,padx=8 , )
        
        self.Studant = ctk.CTkButton(self.sidebarFrame,text_color="white",hover="False",corner_radius=8,fg_color="transparent", text="Student",font=ctk.CTkFont(weight="bold"), command=lambda: self.haver(self.Studant,self.StudantPage))
        self.Studant.pack(side="top",fill="x",ipady = 8,padx=8, )
        
        
        self.Lactuer_Table = ctk.CTkButton(self.sidebarFrame,text_color="white",hover="False",corner_radius=8,fg_color="transparent", text="Lactuer Table",font=ctk.CTkFont(weight="bold"), command=lambda: self.haver(self.Lactuer_Table,self.Lactuer_Table_Page))
        self.Lactuer_Table.pack(side="top",fill="x",ipady = 8,padx=8, )
        
        self.Attendance = ctk.CTkButton(self.sidebarFrame,text_color="white",hover="False",corner_radius=8,fg_color="transparent", text="Attendance",font=ctk.CTkFont(weight="bold"), command=lambda: self.haver(self.Attendance,self.AttendancePage))
        self.Attendance.pack(side="top",fill="x",ipady = 8,padx=8, )
        
        
        self.Tetcher = ctk.CTkButton(self.sidebarFrame, text="Tetcher",corner_radius=8,hover="False",text_color="white",fg_color="transparent",font=ctk.CTkFont(weight="bold"), command=lambda: self.haver(self.Tetcher, self.TetcherPage))
        self.Tetcher.pack(side="top",fill="x",ipady = 8, padx=8)
        
        self.subject = ctk.CTkButton(self.sidebarFrame, text="subject",corner_radius=8,hover="False",text_color="white",fg_color="transparent",font=ctk.CTkFont(weight="bold"), command=lambda: self.haver(self.subject, self.subjectPage))
        self.subject.pack(side="top",fill="x",ipady = 8, padx=8)
        

        
        self.Admin = ctk.CTkButton(self.sidebarFrame,text_color="white",hover="False",corner_radius=8,fg_color="transparent", text="Admin",font=ctk.CTkFont(weight="bold"), command=lambda: self.haver(self.Admin,self.AdminPage))
        self.Admin.pack(side="top",fill="x",ipady = 8,padx=8, )

        
        self.Abut = ctk.CTkButton(self.sidebarFrame, text="Abut",corner_radius=8,hover="False",text_color="white",fg_color="transparent",font=ctk.CTkFont(weight="bold"), command=lambda: self.haver(self.Abut, self.AbutPage))
        self.Abut.pack(side="top",fill="x",ipady = 8, padx=8)
        
    def hide_haver(self):
        self.home.configure(text_color="white",fg_color="transparent")
        self.Studant.configure(text_color="white",fg_color="transparent")
        self.Tetcher.configure(text_color="white",fg_color="transparent")
        self.subject.configure(text_color="white",fg_color="transparent")
        
        self.Lactuer_Table.configure(text_color="white",fg_color="transparent")
        self.Admin.configure(text_color="white",fg_color="transparent")
        self.Attendance.configure(text_color="white",fg_color="transparent")
        
        
        self.Abut.configure(text_color="white",fg_color="transparent")
    def hide_fram(self):
        for fram in self.mainFrame.winfo_children():
            fram.forget()
    def haver(self , btn, page):
        self.hide_fram()
        self.hide_haver()
        page.configure(width=850,height=600 ,fg_color="transparent")
        page.pack_propagate(False)
        page.pack(side="left",pady = 8, padx=8 ,fill="both", expand="true")
        btn.configure(text_color="black",fg_color="white",font=ctk.CTkFont(weight="bold"))
