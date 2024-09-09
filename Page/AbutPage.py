import customtkinter as ctk
import tkinter as tk
ctk.set_appearance_mode("System") 
class AbutPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.logo_label = ctk.CTkLabel(self, text="Admin Abut Page", font=ctk.CTkFont(size=15, weight="bold"))
        self.logo_label.pack(side="top",fill="x",ipady=10, padx  = 10, )
        
