from Sidebar import *

ctk.set_appearance_mode("System")


# Supported themes : green, dark-blue, blue
# ctk.set_default_color_theme("white")
class App(ctk.CTk):
    def __init__(self):
        super().__init__() 
        self.title("Attendance Using Face Recognition")
        self.geometry("1300x670")
        self.checkbox_frame = sidebar(self)
        self.checkbox_frame.configure(width=1120, height=600)
        self.checkbox_frame.pack_propagate(False)
        self.checkbox_frame.pack(side="left", fill="both", expand="true")


app = App()
app.mainloop()
