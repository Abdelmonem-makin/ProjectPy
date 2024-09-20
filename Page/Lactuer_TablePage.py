import customtkinter as ctk
import tkinter as ttk
from Fun.teacherFun import teacherFun
from Fun.LactuerFun import lacTableFun
from Fun.SubjectFun import SubjecFun
import calendar
from Page.Home_Page import HomePage

ctk.set_appearance_mode("System")


class lactuerTablePage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.homePage = None
        self.lacTableFun = lacTableFun(self)
        self.TeacherDB = teacherFun(self)
        self.DB = SubjecFun(self)

        # configure grid layout (4x4)

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.navframe = ctk.CTkFrame(self)
        self.navframe.configure(width=850, height=50, corner_radius=3, fg_color="white")
        self.navframe.pack_propagate(False)
        self.navframe.pack(side="top", fill="both", expand="true")

        self.logo_label = ctk.CTkLabel(self.navframe, text="lactuer Table Screen Page", text_color="dark blue",
                                       font=ctk.CTkFont(size=15, weight="bold"))
        self.logo_label.pack(side="left", fill="x", ipady=10, padx=13, )

        self._ok_button = ctk.CTkButton(master=self.navframe, width=50, height=10, fg_color="transparent",
                                        text_color="dark blue", border_color='dark blue', border_width=2,
                                        text='Search', )
        self._ok_button.pack(side="right", fill="x", ipady=6, padx=13, )
        self._entry = ctk.CTkEntry(master=self.navframe, width=200, height=10,
                                   placeholder_text='Enter Subject Name .....', fg_color="transparent",
                                   border_color='dark blue', border_width=2, )
        self._entry.pack(side="right", fill="x", ipady=6, padx=13, )
        # create Lac table
        self.lacTable = ctk.CTkFrame(self)
        self.lacTable.configure(height=750, fg_color="transparent")
        self.lacTable.pack_propagate(False)
        self.lacTable.pack(side="top", fill="both", expand="true")
        # create textbox
        self.scrollable_frame2 = ctk.CTkScrollableFrame(self.lacTable, label_fg_color="white",
                                                        label_text_color="dark blue", label_text="Lactuer List")
        self.scrollable_frame2.configure(width=250, height=100, fg_color="transparent")
        self.scrollable_frame2.pack_propagate(False)
        self.scrollable_frame2.pack(side="left", padx=8, pady=8, fill="both", expand="true")
        self.Dataview()
        self.regestForm1 = ctk.CTkFrame(self.lacTable)
        self.regestForm1.configure(width=420, height=50, fg_color="white")
        self.regestForm1.pack_propagate(False)
        self.regestForm1.pack(side="top", ipady=20, pady=(10, 0), fill="x", expand="true")

        self._label = ctk.CTkLabel(master=self.regestForm1, width=300, text='Add Lactuer Table', text_color="dark blue",
                                   font=ctk.CTkFont(size=15, weight="bold"), wraplength=300, fg_color="transparent", )
        self._label.pack(side="top", padx=40, fill="both", expand="true")

        self.regestForm = ctk.CTkFrame(self.lacTable)
        self.regestForm.configure(width=420, height=750, fg_color="white")
        self.regestForm.pack_propagate(False)
        self.regestForm.pack(side="top", pady=(0, 10), fill="both", expand="true")

        self._label = ctk.CTkLabel(master=self.regestForm, text='Subj Name', width=50, wraplength=300,
                                   fg_color="transparent", text_color="dark blue",
                                   font=ctk.CTkFont(size=15, weight="bold"))
        self._label.place(x=30, y=50)
        self.Subj_Name = ctk.CTkComboBox(self.regestForm, width=200, fg_color="white", button_color='dark blue',
                                         border_width=2,
                                         values=self.subjectName())
        self.Subj_Name.place(x=130, y=50)

        self._label = ctk.CTkLabel(master=self.regestForm, text='Date', width=50, wraplength=300,
                                   fg_color="transparent", text_color="dark blue",
                                   font=ctk.CTkFont(size=15, weight="bold"))
        self._label.place(x=30, y=100)
        self.Date = ctk.CTkComboBox(self.regestForm, width=200, fg_color="white", button_color='dark blue',
                                    border_width=2, values=['Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu'])
        self.Date.place(x=130, y=100)

        self._label = ctk.CTkLabel(master=self.regestForm, text='Teacher', width=50, wraplength=300,
                                   fg_color="transparent", text_color="dark blue",
                                   font=ctk.CTkFont(size=15, weight="bold"))
        self._label.place(x=30, y=150)
        self.Teacher = ctk.CTkComboBox(self.regestForm, width=200, fg_color="white", button_color='dark blue',
                                       border_width=2,
                                       values=self.Teachername())
        self.Teacher.place(x=130, y=150)

        self._ok_button = ctk.CTkButton(master=self.regestForm, width=100, border_width=0, text='Add',
                                        fg_color="dark blue", command=self.save_Lac_table)
        self._ok_button.place(x=50, y=200)

        self._ok_button = ctk.CTkButton(master=self.regestForm, width=100, border_width=0, text='Edite',
                                        fg_color="dark blue")
        self._ok_button.place(x=160, y=200)

        self._ok_button = ctk.CTkButton(master=self.regestForm, width=100, border_width=0, text='Delete',
                                        fg_color="dark blue")
        self._ok_button.place(x=270, y=200)

    def Dataview(self):
        headers = ['Day', "Time", "Subj Name", "Teacher"]
        for col, header in enumerate(headers):
            self.label = ctk.CTkLabel(self.scrollable_frame2, fg_color='dark blue', text_color='white', width=130,
                                      corner_radius=3, text=header, font=("Arial", 12, "bold"))
            self.label.grid(row=0, column=col, padx=1, pady=1)

        data = self.lacTableFun.listLacTable()
        widths = [175, 175, 175, 175]
        for row, row_data in enumerate(data, start=1):
            for col, value in enumerate(row_data):
                entry = ctk.CTkLabel(self.scrollable_frame2, text=value, text_color='dark blue', fg_color='white',
                                     width=130)
                entry.grid(row=row, column=col, padx=1, pady=1)

    def Teachername(self):
        name = []
        data = self.TeacherDB.lisTeacherName()
        for row, row_data in enumerate(data):
            for col, value in enumerate(row_data):
                name.append(value)
        return name

    def subjectName(self):
        name = []
        data = self.DB.listSubject()
        for row, row_data in enumerate(data):
            for col, value in enumerate(row_data):
                name.append(value)
        return name

    def save_Lac_table(self):
        self.lacTableFun.addLacTable(self.Subj_Name.get(), self.Date.get(), '8:00', self.Teacher.get())
        self.homePage = HomePage(self)
        self.homePage.dataview()
        self.Dataview()
        self.Date.delete(0, 'end')
