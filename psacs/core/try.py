import tkinter as tk
from tkinter import messagebox
import gettext
_ = gettext.gettext
class Application(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)  
        self.grid()
        self.createWidgets()
        self.parent = parent
    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit', command=self.close)
        self.quitButton.grid()
    def close(self):
        if messagebox.askyesno(title=('Quit'), message=('Are you sure?')):
            self.quit()

app = Application()
app.master.title('Sample application')
app.mainloop()
