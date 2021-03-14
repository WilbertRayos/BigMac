from tkinter import Tk, Frame, Label, Entry, StringVar
from socket import gethostname, gethostbyname
from getmac import get_mac_address as gma

class MainWindow(Frame):
    FONT_SIZE = 24
    FONT_FAMILY = "Courier"

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Big MAC")
        self.widgets()
        self.modify_text_design()
        self.grid()

    def widgets(self):
        ''' Host Name '''
        self.lblHostName = Label(self.master, text="Host Name")
        self.strEntHostName = StringVar()
        self.strEntHostName.set(MainWindow.get_host_name())
        self.entHostname = Entry(self.master, textvariable=self.strEntHostName,)
        
        ''' IP Address '''
        self.lblIPAddress = Label(self.master, text="IP Address")
        self.strEntIPAddress = StringVar()
        self.strEntIPAddress.set(MainWindow.get_ip_address())
        self.entIPAddress = Entry(self.master, textvariable=self.strEntIPAddress)

        ''' MAC Address '''
        self.lblMACAddress = Label(self.master, text="MAC Address")
        self.strEntMACAddress = StringVar()
        self.strEntMACAddress.set(MainWindow.get_mac_address())
        self.entMACAddress = Entry(self.master, textvariable=self.strEntMACAddress)

        ''' Programmer '''
        self.lblProgrammer = Label(self.master, text="Programmed by Wilbert Raymund R. Rayos")

        '''  =Layout=  '''
        
        ''' HostName '''
        self.lblHostName.grid(row=0,column=0,sticky="nsew")
        self.entHostname.grid(row=0,column=1,sticky="nsew")

        ''' IP Address '''
        self.lblIPAddress.grid(row=1,column=0, sticky="nsew")
        self.entIPAddress.grid(row=1,column=1, sticky="nsew")

        ''' MAC Address '''
        self.lblMACAddress.grid(row=2,column=0, sticky="nsew")
        self.entMACAddress.grid(row=2,column=1, sticky="nsew")

        ''' Programmer '''
        self.lblProgrammer.grid(row=3,column=0, sticky="nsew", columnspan=2)
    
    def modify_text_design(self):
        for item in self.master.winfo_children():
            if item.winfo_class() == "Frame":
                continue
            else:
                item.configure(font=(self.FONT_FAMILY, self.FONT_SIZE))

            if item.winfo_class() == "Label":
                item.config(bg="pink")
            elif item.winfo_class() == "Entry":
                item.configure(state="readonly")
    
    @staticmethod
    def get_host_name():
        try:
            return gethostname()
        except Exception as e:
            return "Error"

    @staticmethod
    def get_ip_address():
        try:
            return gethostbyname(MainWindow.get_host_name())
        except Exception as e:
            return "Error"

    @staticmethod
    def get_mac_address():
        try:
            return gma()
        except Exception as e:
            return "Error"

if __name__ == "__main__":
    root = Tk()
    app = MainWindow(master=root)
    app.mainloop()


