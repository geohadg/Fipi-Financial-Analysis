import pandas as pd
import customtkinter as ctk
import tkinter
from PIL import Image
from os import getcwd, remove
import matplotlib.pyplot as plt  
import matplotlib.dates as mdates
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

graph_pallettes = {
    #'flare': ['#fcc98d', '#fcbd74', '#e98d6b', '#e3685c', '#d63c56', '#c93673', '#9e3460', '#8f3371', '#6c2b6d', '#511852'],
    # 'flare':  ['#160b39', '#420a68', '#6a176e', '#932667', '#bc3754', '#dd513a', '#f37819', '#fca50a', '#f6d746', '#fcffa4'],
    'flare':  ['#420a68', '#601394', '#6a176e', '#932667', '#bc3754', '#dd513a', '#f37819', '#fca50a', '#f6d746', '#fae375', '#fcffa4'],
    'forest':  ['#302652', '#372b61', '#46327e', '#365c8d','#277f8e', '#008f8f', '#1fa187', '#4ac16d', '#a0da39', '#bbf556', '#e3fa70']
                   }



def handleaccountError():
    popup = ctk.CTkToplevel()
    popup.title("Error Report")
    popup.geometry("500x100 + 500 + 500")
    popup.attributes("-topmost", False)

    label = ctk.CTkLabel(popup, text="Account Type Does not Match CSV")
    label.pack(pady=10)

    button = ctk.CTkButton(popup, text="OK", command=popup.destroy, width=50, height=20)
    button.pack(pady=10)

def AlreadyConsolidated(file):
    AlreadyConsolidated_df = pd.read_csv(file)
    a = pd.DataFrame()

    try:
        print(AlreadyConsolidated_df["Transaction Date"])
        return a    

    except KeyError:
        return AlreadyConsolidated_df

unwanted_categories = ["New Share Deposit", "Online Banking Transfer", "ACH Deposit", "ACH Withdrawal", "Interest", "Online Banking Deposit", "ACH Share Withdrawal", "ACH Share Deposit", "ACH Credit", "Dividend"]
Groceries = ["DOLLAR GENERAL", "WAL-MART", "WALMART","WM SUPERCENTER", "DOLLAR GE", "PUBLIX", "DOLLAR TREE", "FAMILY DOLLAR", "CVS", "DOLLAR"]
Restaurant = ["NOODLES", "MCDONALD'S", "WENDYS", "CHICK-FIL-A", "POPEYES", "TACO BELL", "AZTECA", "OLIVE GARDEN", "MCDONALDS", "WAFFLE HOUSE", "CULVERS", "BURGER KING", "SONIC", "PIZZA HUT", "DOMINOS", "SUBWAY", "JIMMY JOHNS", "CHIPOTLE", "PANDA EXPRESS", "KFC", "CHILIS", "RED LOBSTER", "IHOP", "STARBUCKS", "DUNKIN", "KRISPY KREME"]
Gas = ["CUMBERLANDFARMS", "CEFCO", "CUMBERLAND FARMS", "TOM THUMB", "DODGE", "EXXON", "SHELL", "RACETRACK", "RACEWAY", "MOBILE", "BP", "CITGO", "CHEVRON", "7-ELEVEN", "7 ELEVEN", "7ELEVEN", "7-11"]
ACHWhitdrawal = ["CreditOne", "WEBULL", "VENMO", "CASHAPP", "Stride Bank", "CASH APP", "CREDITONE"]
fun = ["VENDING","ULTA", "TARGET", "MICHAELS", "2ND AND CHARLES", "BOOKS A MILLION", "HOT TOPIC", "SPENCER", "TOMMY GUNNS", "BEALLS", "MERCARI", "EBAY", "RADBAR", "CORDOVA MALL", "DESTIN COMMONS", "PLANET FI", "HIBBETT"]
keys = ["Amazon", "Groceries", "Fast Food", "Gas", "Fun", "ACH Withdrawal", "Other"]
Health = ["VISION HUB", "BEHEALTHY", "ASPEN"]

def Eglin(file):
    eglin_df = pd.read_csv(file)
    a = pd.DataFrame()
    try:
        eglin_df["Month"] = pd.to_datetime(eglin_df["Date"]).dt.month_name()
        eglin_df["Year"] = pd.to_datetime(eglin_df.Date, format="mixed").dt.year
        
        for category in unwanted_categories:
            eglin_df = eglin_df.drop(eglin_df[eglin_df['Ext'] == category].index)

        for grocery in Groceries:
            eglin_df.loc[eglin_df["Description"].str.contains(grocery), "Category"] = "Groceries"

        for place in Restaurant:
            eglin_df.loc[eglin_df["Description"].str.contains(place), "Category"] = "Dining"
            
        for station in Gas:
            eglin_df.loc[eglin_df["Description"].str.contains(station), "Category"] = "Gas"

        for f in fun:
            eglin_df.loc[eglin_df["Description"].str.contains(f), "Category"] = "Fun"

        eglin_df.loc[eglin_df["Description"].str.contains("AMAZON"), "Category"] = "Amazon"

        for ach in ACHWhitdrawal:
            eglin_df.loc[eglin_df["Description"].str.contains(ach), "Category"] = "ACH"

        eglin_df.loc[eglin_df["Category"].isnull(), "Category"] = "Other"
        eglin_df.loc[eglin_df["Description"].str.contains("TMOBILE"), "Category"] = "Phone"
        eglin_df.drop(["Ext", "Draft", "Balance"], axis=1, inplace=True)
        eglin_df["Amount"] *= -1
        eglin_df["Account"] = "Eglin FCU"
        return eglin_df
    
    except KeyError:
        return a

def CapitalOneChecking(file):
    CapitalOneChecking_df = pd.read_csv(file)
    a = pd.DataFrame()

    try:
        CapitalOneChecking_df["Month"] = pd.to_datetime(CapitalOneChecking_df["Transaction Date"], format="%m/%d/%y").dt.month_name()
        CapitalOneChecking_df["Year"] = pd.to_datetime(CapitalOneChecking_df["Transaction Date"], format="mixed").dt.year
        CapitalOneChecking_df["Date"] = CapitalOneChecking_df["Transaction Date"]
        CapitalOneChecking_df["Amount"] = CapitalOneChecking_df["Transaction Amount"]
        CapitalOneChecking_df["Description"] = CapitalOneChecking_df["Transaction Description"]

        for grocery in Groceries:
            CapitalOneChecking_df.loc[CapitalOneChecking_df["Transaction Description"].str.contains(grocery), "Category"] = "Groceries"

        for place in Restaurant:
            CapitalOneChecking_df.loc[CapitalOneChecking_df["Transaction Description"].str.contains(place), "Category"] = "Dining"
            
        for station in Gas:
            CapitalOneChecking_df.loc[CapitalOneChecking_df["Transaction Description"].str.contains(station), "Category"] = "Gas"

        for f in fun:
            CapitalOneChecking_df.loc[CapitalOneChecking_df["Transaction Description"].str.contains(f), "Category"] = "Fun"

        CapitalOneChecking_df.loc[CapitalOneChecking_df["Transaction Description"].str.contains("AMAZON"), "Category"] = "Amazon"

        for ach in ACHWhitdrawal:
            CapitalOneChecking_df.loc[CapitalOneChecking_df["Transaction Description"].str.contains(ach), "Category"] = "ACH"

        CapitalOneChecking_df.loc[CapitalOneChecking_df["Category"].isnull(), "Category"] = "Other"
        CapitalOneChecking_df.loc[CapitalOneChecking_df["Transaction Description"].str.contains("Deposit"), "Category"] = "Deposit"
        CapitalOneChecking_df.loc[CapitalOneChecking_df["Transaction Description"].str.contains("TMOBILE"), "Category"] = "Phone"
        CapitalOneChecking_df.loc[CapitalOneChecking_df["Transaction Type"] == "Credit", "Category"] = None
        CapitalOneChecking_df["Account"] = "CapitalOne Checking"
        CapitalOneChecking_df.dropna(inplace=True)
        CapitalOneChecking_df.drop(["Transaction Description", "Account Number", "Transaction Type", "Transaction Date", "Transaction Amount", "Balance"], axis=1, inplace=True)

        return CapitalOneChecking_df
    
    except KeyError:
        return a

def Quicksilver(file):
    Quicksilver_df = pd.read_csv(file)
    a = pd.DataFrame()
    """Adds a column to the dataframe containing the month name"""
    try:
        Quicksilver_df["Month"] = pd.to_datetime(Quicksilver_df["Transaction Date"]).dt.month_name()
        Quicksilver_df["Year"] = pd.to_datetime(Quicksilver_df["Transaction Date"], format="mixed").dt.year
        Quicksilver_df["Date"] = pd.to_datetime(Quicksilver_df["Transaction Date"]).dt.strftime("%m/%d/%Y")
        Quicksilver_df.loc[Quicksilver_df["Category"] == "Gas/Automotive", "Category"] = "Gas"
        Quicksilver_df.loc[Quicksilver_df["Category"] == "Other Services", "Category"] = "Other"
        Quicksilver_df.loc[Quicksilver_df["Category"] == "Professional Services", "Category"] = "Other"
        Quicksilver_df.loc[Quicksilver_df["Category"] == "Internet", "Category"] = "Internet"
        Quicksilver_df.loc[Quicksilver_df["Category"] == "Payment/Credit", "Category"] = "ACH"
        Quicksilver_df.loc[Quicksilver_df["Category"] == "Merchandise", "Category"] = "Merchandise"
        Quicksilver_df.loc[Quicksilver_df["Category"] == "Fee/Interest Charge", "Category"] = "Interest"
        Quicksilver_df.loc[Quicksilver_df["Description"].str.contains("AMAZON"), "Category"] = "Amazon"

        for a in ACHWhitdrawal:
            Quicksilver_df.loc[Quicksilver_df["Description"].str.contains(a), "Category"] = "ACH"

        for f in fun:
            Quicksilver_df.loc[Quicksilver_df["Description"].str.contains(f), "Category"] = "Fun"

        for place in Groceries:
            Quicksilver_df.loc[Quicksilver_df["Description"].str.contains(place), "Category"] = "Groceries"

        Quicksilver_df["Amount"] = Quicksilver_df["Debit"]
        Quicksilver_df.drop(["Transaction Date", "Posted Date", "Card No.", "Debit", "Credit"], axis=1, inplace=True)
        Quicksilver_df.dropna(inplace=True)
        Quicksilver_df["Account"] = "Quicksilver"
        print(Quicksilver_df)
        return Quicksilver_df
    
    except KeyError:
        return a

def Savor(file):
    Savor_df = pd.read_csv(file)
    a = pd.DataFrame()

    try:
        """Adds a column to the dataframe containing the month name"""
        Savor_df["Month"] = pd.to_datetime(Savor_df["Transaction Date"]).dt.month_name()
        Savor_df["Year"] = pd.to_datetime(Savor_df["Transaction Date"], format="mixed").dt.year
        Savor_df["Date"] = Savor_df["Transaction Date"]

        Savor_df.loc[Savor_df["Category"] == "Gas/Automotive", "Category"] = "Gas"
        Savor_df.loc[Savor_df["Category"] == "Other Services", "Category"] = "Other"
        Savor_df.loc[Savor_df["Category"] == "Professional Services", "Category"] = "Other"
        Savor_df.loc[Savor_df["Category"] == "Internet", "Category"] = "Internet"
        Savor_df.loc[Savor_df["Category"] == "Merchandise", "Category"] = "Merchandise"
        Savor_df.loc[Savor_df["Category"] == "Payment/Credit", "Category"] = "ACH "
        Savor_df.loc[Savor_df["Description"].str.contains("AMAZON"), "Category"] = "Amazon"
        Savor_df.loc[Savor_df["Category"] == "Fee/Interest Charge", "Category"] = "Interest"

        for f in fun:
            Savor_df.loc[Savor_df["Description"].str.contains(f), "Category"] = "Fun"

        for place in Groceries:
            Savor_df.loc[Savor_df["Description"].str.contains(place), "Category"] = "Groceries"

        Savor_df["Amount"] = Savor_df["Debit"]
        Savor_df.drop(["Transaction Date", "Posted Date", "Card No.", "Debit", "Credit"], axis=1, inplace=True)
        Savor_df.dropna(inplace=True)
        Savor_df["Account"] = "Savor"

        return Savor_df
    
    except KeyError:
        return a

def Amex(file):
    Amex_df = pd.read_csv(file)
    a = pd.DataFrame()
    """Adds a column to the dataframe containing the month name"""
    try:
        Amex_df["Month"] = pd.to_datetime(Amex_df["Date"]).dt.month_name()
        Amex_df["Year"] = pd.to_datetime(Amex_df.Date, format="mixed").dt.year

        for place in Restaurant:
            Amex_df.loc[Amex_df["Description"].str.contains(place), "Category"] = "Dining"
            
        for station in Gas:
            Amex_df.loc[Amex_df["Description"].str.contains(station), "Category"] = "Gas"

        for f in fun:
            Amex_df.loc[Amex_df["Description"].str.contains(f), "Category"] = "Fun"

        Amex_df.loc[Amex_df["Description"].str.contains("AMAZON"), "Category"] = "Amazon"

        for ach in ACHWhitdrawal:
            Amex_df.loc[Amex_df["Description"].str.contains(ach), "Category"] = "ACH"

        for h in Health:
            Amex_df.loc[Amex_df["Description"].str.contains(h), "Category"] = "Health"

        Amex_df.loc[Amex_df["Category"].isnull(), "Category"] = "Other"
        Amex_df.loc[Amex_df["Description"].str.contains("DAVID SCOTT LEE"), "Category"] = "Car"
        Amex_df.loc[Amex_df["Description"].str.contains("MOBILE PAYMENT"), "Category"] = "Payment"
        Amex_df.loc[Amex_df["Description"].str.contains("TMOBILE"), "Category"] = "Phone"
        Amex_df.loc[Amex_df["Description"].str.contains("Interest"), "Category"] = "Interest"
        Amex_df.loc[Amex_df["Description"].str.contains("MOBILE PAYMENT - THANK YOU"), "Category"] = None
        Amex_df["Account"] = "AMEX"
        for place in Groceries:
            Amex_df.loc[Amex_df["Description"].str.contains(place), "Category"] = "Groceries"

        Amex_df.dropna(inplace=True)
        #Amex_df.drop("Description", axis=1, inplace=True)

        return Amex_df
    
    except KeyError:
        return a

def BILT(file):
    Bilt_df = pd.read_csv(file)
    a = pd.DataFrame()
    """Adds a column to the dataframe containing the month name"""
    try:
        Bilt_df["Month"] = pd.to_datetime(Bilt_df["Date"]).dt.month_name()
        Bilt_df["Year"] = pd.to_datetime(Bilt_df.Date, format="mixed").dt.year
        Bilt_df["Category"] = None

        for place in Restaurant:
            Bilt_df.loc[Bilt_df["Description"].str.contains(place), "Category"] = "Dining"
            
        for station in Gas:
            Bilt_df.loc[Bilt_df["Description"].str.contains(station), "Category"] = "Gas"

        for f in fun:
            Bilt_df.loc[Bilt_df["Description"].str.contains(f), "Category"] = "Fun"

        Bilt_df.loc[Bilt_df["Description"].str.contains("AMAZON"), "Category"] = "Amazon"

        for ach in ACHWhitdrawal:
            Bilt_df.loc[Bilt_df["Description"].str.contains(ach), "Category"] = "ACH"

        Bilt_df.loc[Bilt_df["Category"].isnull(), "Category"] = "Other"
        Bilt_df.loc[Bilt_df["Description"].str.contains("Bill Pay Payment"), "Category"] = "Payment"
        Bilt_df.loc[Bilt_df["Description"].str.contains("TMOBILE"), "Category"] = "Phone"
        Bilt_df.loc[Bilt_df["Category"] == "Payment", "Category"] = None

        for place in Groceries:
            Bilt_df.loc[Bilt_df["Description"].str.contains(place), "Category"] = "Groceries"

        Bilt_df.drop(["Type"], axis=1, inplace=True)
        Bilt_df.dropna(inplace=True)
        Bilt_df["Account"] = "BILT"
        Bilt_df["Amount"] *= -1

        return Bilt_df

    except KeyError:
        return a
    
def alreadyconsolidated(file):
    alcons = pd.read_csv(file)
    a = pd.DataFrame()

    return alcons


""" GUI """

class HomeScreen(ctk.CTk):
    frames = {"importpage": None, "graphpage": None, "aboutpage": None}
    def __init__(self):
        super().__init__()

        '''                 Setting Background Image                    '''

        global image, background_image, handle_optionchange
        window_width, window_height = 1600, 700

        # icon = Image.open("C:\\Users\\geoha\\OneDrive\\Desktop\\my-official\\pythonpersf\\Fipi-Financial-Analysis\\fipiicon.ico")
        # photo = ImageTk.PhotoImage(icon)
        # self.iconphoto(True, photo) 

        '''                 Error Handling Functions                 '''
        
        def handle_fileError():
            if len(self.msgframe.winfo_children()) > 0:
                for widget in self.msgframe.winfo_children():
                    widget.destroy()

            self.fileerrorlabel = ctk.CTkLabel(self.msgframe, text="An error has occured with your selection(s)", font=("Terminal", 15))
            self.fileerrorlabel.grid(row=8, column=0, columnspan=2)
            
        def handle_report_success():
            if len(self.msgframe.winfo_children()) > 0:
                for widget in self.msgframe.winfo_children():
                    widget.destroy()

            self.reportsuccesslabel = ctk.CTkLabel(self.msgframe, text="Report Generated Successfully", font=("Terminal", 15))
            self.reportsuccesslabel.grid(row=8, column=0, columnspan=2)

        def handle_graph_success():
            if len(self.msgframe.winfo_children()) > 0:
                for widget in self.msgframe.winfo_children():
                    widget.destroy()
            
            self.graphsuccesslabel = ctk.CTkLabel(self.msgframe, text="Graph Generated Successfully!", font=("Terminal", 15))
            self.graphsuccesslabel.grid(row=8, column=0, columnspan=2)

        def handle_export_success():
            if len(self.msgframe.winfo_children()) > 0:
                for widget in self.msgframe.winfo_children():
                    widget.destroy()

            self.exportsuccesslabel = ctk.CTkLabel(self.msgframe, text="Exported to CSV Successful!", font=("Terminal", 15))
            self.exportsuccesslabel.grid(row=8, column=0, columnspan=2)

        def handle_empty_dataset():
            self.emptydatasetlabel = ctk.CTkLabel(self.grapherrorframe, font=("Terminal", 14), text="The dataset for your selections is empty")
            self.emptydatasetlabel.pack()

        '''                 File Explorer Dialogue Button                   '''
        def addfilebutton(textbox):
            
            
            filepath = ctk.filedialog.askopenfilename(
            initialdir="Downloads",  
            title="Select a File",  
            filetypes=(("CSV files", "*.csv"), ("All files", "*.*")) 
            )
            if filepath:
                global option_menu, selections
                textbox.delete("1.0", tkinter.END)
                textbox.insert('0.0', filepath)

        '''                 Export Selections to Csv without Empty Fields                   '''

        def export_csv(selections):
            selections[self.textbox1.get('0.0', 'end').replace("\n", "")] = self.option1.get()
            selections[self.textbox2.get('0.0', 'end').replace("\n", "")] = self.option2.get()
            selections[self.textbox3.get('0.0', 'end').replace("\n", "")] = self.option3.get()
            selections[self.textbox4.get('0.0', 'end').replace("\n", "")] = self.option4.get()
            selections[self.textbox5.get('0.0', 'end').replace("\n", "")] = self.option5.get()
            
            for key in list(selections):
                if selections[key] == "Select Account Type" or selections[key] == '':
                    del selections[key]
            
            fileslist = list(selections.keys())
            protocolslist = list(selections.values())
            outputlist = []
            try:
                for i in range(len(fileslist)):
                    if protocolslist[i] == "Eglin FCU":
                        eglin_df = Eglin(fileslist[i])
                        outputlist.append(eglin_df)

                    if protocolslist[i] == "BILT":
                        bilt_df = BILT(fileslist[i])
                        outputlist.append(bilt_df)

                    if protocolslist[i] == "Amex Skymiles":
                        amex_df = Amex(fileslist[i])
                        outputlist.append(amex_df)

                    if protocolslist[i] == "CapitalOne Quicksilver":
                        quicksilver_df = Quicksilver(fileslist[i])
                        outputlist.append(quicksilver_df)

                    if protocolslist[i] == "CapitalOne Savor":
                        savor_df = Savor(fileslist[i])
                        outputlist.append(savor_df)

                    if protocolslist[i] == "CapitalOne Checking":
                        CapitalOneChecking_df = CapitalOneChecking(fileslist[i])
                        outputlist.append(CapitalOneChecking_df)

                    if protocolslist[i] == "Already Consolidated":
                        alcons_df = alreadyconsolidated(fileslist[i])
                        outputlist.append(alcons_df)

                total = pd.concat(outputlist)


                def save_file():
                    f = ctk.filedialog.asksaveasfile(mode='w', defaultextension=".csv")
                    if f is None: 
                        return 

                    if f.name.__contains__(".csv"):
                        total.to_csv(f.name)

                    else:
                        total.to_csv(f.name+".csv")

                save_file()
                handle_export_success()

            except (FileNotFoundError, NameError, ValueError, KeyError) as e:
                self.loggingtextbox.insert("0.0", f"{str(e)}\n\n")
                handle_fileError()

        def gatherinputs(selections):
            global total
            selections[self.textbox1.get('0.0', 'end').replace("\n", "")] = self.option1.get()
            selections[self.textbox2.get('0.0', 'end').replace("\n", "")] = self.option2.get()
            selections[self.textbox3.get('0.0', 'end').replace("\n", "")] = self.option3.get()
            selections[self.textbox4.get('0.0', 'end').replace("\n", "")] = self.option4.get()
            selections[self.textbox5.get('0.0', 'end').replace("\n", "")] = self.option5.get()

            for key in list(selections):
                if selections[key] == "Select Account Type" or selections[key] == '':
                    del selections[key]
            
            print(selections)
            fileslist = list(selections.keys())
            protocolslist = list(selections.values())
            outputlist = []
            try:
                for i in range(len(fileslist)):
                    if protocolslist[i] == "Eglin FCU":
                        eglin_df = Eglin(fileslist[i])
                        outputlist.append(eglin_df)

                    if protocolslist[i] == "BILT Card":
                        bilt_df = BILT(fileslist[i])
                        outputlist.append(bilt_df)

                    if protocolslist[i] == "AMEX Skymiles":
                        amex_df = Amex(fileslist[i])
                        outputlist.append(amex_df)

                    if protocolslist[i] == "CapitalOne Quicksilver":
                        quicksilver_df = Quicksilver(fileslist[i])
                        outputlist.append(quicksilver_df)

                    if protocolslist[i] == "CapitalOne Savor":
                        savor_df = Savor(fileslist[i])
                        outputlist.append(savor_df)

                    if protocolslist[i] == "CapitalOne Checking":
                        CapitalOneChecking_df = CapitalOneChecking(fileslist[i])
                        outputlist.append(CapitalOneChecking_df)

                    if protocolslist[i] == "Already Consolidated":
                        alcons_df = alreadyconsolidated(fileslist[i])
                        outputlist.append(alcons_df)

                if len(outputlist) >1:
                    total = pd.concat(outputlist)

                elif len(outputlist) == 1:
                    total = outputlist[0]

                global totalaccounts, totalcategories, totalyears, totalmonths
                
                totalaccounts = list(total.loc[total["Account"] != '']["Account"].unique())
                totalcategories = list(total.loc[total["Category"] != '']["Category"].unique())
                totalcategories2 = list(total.loc[total["Category"] != '']["Category"].unique())
                totalyears = list(total.loc[total["Year"] != '']["Year"].unique())
                totalmonths = list(total.loc[total["Month"] != '']["Month"].unique())

                totalaccounts.insert(0, "All")
                totalcategories2.insert(0, "All")
                totalmonths.insert(0, "All")
                totalyears.insert(0, "All")

                for i in range(len(totalyears)):
                    totalyears[i] = str(totalyears[i])

                sums = []

                for key in totalcategories:
                    sums.append(total[total["Category"] == key]["Amount"].sum())# if key in keys else None

                handle_graph_success()
                graphpageselector()
                self.yearoptionmenu.configure(values=totalyears)
                self.monthoptionmenu.configure(values=totalmonths)
                self.categoryoptionmenu.configure(values=totalcategories2)
                self.accountoptionmenu.configure(values=totalaccounts)
                global current_pallette
                current_pallette = self.colorpalletteswitch.get()

                if self.colorpalletteswitch.get() == 0:
                    current_pallette = graph_pallettes["flare"]
                    graphpie(sums, totalcategories, current_pallette)     

                else:
                    current_pallette = graph_pallettes["forest"]
                    graphpie(sums, totalcategories, current_pallette)

                return total, totalaccounts, totalcategories, totalyears, totalmonths, sums
                            
            except (FileNotFoundError, NameError, ValueError, KeyError) as e:
                if self.textbox1.get('0.0', 'end').replace("\n", "") == "" or self.textbox2.get('0.0', 'end').replace("\n", "") == "" or self.textbox3.get('0.0', 'end').replace("\n", "") == "" or self.textbox4.get('0.0', 'end').replace("\n", "") == "" or self.textbox5.get('0.0', 'end').replace("\n", "") == "":
                    self.loggingtextbox.insert("0.0", "Please Select a File you left the box empty :)\n\n")
                    self.nofilelabel = ctk.CTkLabel(self.msgframe, text="Please Select a File you left the box empty :)", font=("Terminal", 15))
                    self.nofilelabel.grid(row=8, column=0, columnspan=2)
                    handle_fileError()

                if self.option1.get() == "Select Account Type" or self.option2.get() == "Select Account Type" or self.option3.get() == "Select Account Type" or self.option4.get() == "Select Account Type" or self.option5.get() == "Select Account Type":
                    self.loggingtextbox.insert("0.0", "Please Select an Account Type you left the box empty :)\n\n")
                    self.noaccountlabel = ctk.CTkLabel(self.msgframe, text="Please Select an Account Type you left the box empty :)", font=("Terminal", 15))
                    self.noaccountlabel.grid(row=8, column=0, columnspan=2)
                    handle_fileError()
                
                else:
                    self.loggingtextbox.insert("0.0", f"{str(e)}\n\n")
                    handle_fileError()

        def generate_report():
            global total
            selections[self.textbox1.get('0.0', 'end').replace("\n", "")] = self.option1.get()
            selections[self.textbox2.get('0.0', 'end').replace("\n", "")] = self.option2.get()
            selections[self.textbox3.get('0.0', 'end').replace("\n", "")] = self.option3.get()
            selections[self.textbox4.get('0.0', 'end').replace("\n", "")] = self.option4.get()
            selections[self.textbox5.get('0.0', 'end').replace("\n", "")] = self.option5.get()
            
            for key in list(selections):
                if selections[key] == "Select Account Type" or selections[key] == '':
                    del selections[key]
            
            print(selections)
            fileslist = list(selections.keys())
            protocolslist = list(selections.values())
            outputlist = []
            try:
                for i in range(len(fileslist)):
                    if protocolslist[i] == "Eglin FCU":
                        eglin_df = Eglin(fileslist[i])
                        outputlist.append(eglin_df)

                    if protocolslist[i] == "BILT Card":
                        bilt_df = BILT(fileslist[i])
                        outputlist.append(bilt_df)

                    if protocolslist[i] == "AMEX Skymiles":
                        amex_df = Amex(fileslist[i])
                        outputlist.append(amex_df)

                    if protocolslist[i] == "CapitalOne Quicksilver":
                        quicksilver_df = Quicksilver(fileslist[i])
                        outputlist.append(quicksilver_df)

                    if protocolslist[i] == "CapitalOne Savor":
                        savor_df = Savor(fileslist[i])
                        outputlist.append(savor_df)

                    if protocolslist[i] == "CapitalOne Checking":
                        CapitalOneChecking_df = CapitalOneChecking(fileslist[i])
                        outputlist.append(CapitalOneChecking_df)

                    if protocolslist[i] == "Already Consolidated":
                        alcons_df = alreadyconsolidated(fileslist[i])
                        outputlist.append(alcons_df)

                if len(outputlist) >1:
                    total = pd.concat(outputlist)

                elif len(outputlist) == 1:
                    total = outputlist[0]

                global totalaccounts, totalcategories, totalyears, totalmonths
                
                totalaccounts = list(total.loc[total["Account"] != '']["Account"].unique())
                totalcategories = list(total.loc[total["Category"] != '']["Category"].unique())
                totalcategories2 = list(total.loc[total["Category"] != '']["Category"].unique())
                totalyears = list(total.loc[total["Year"] != '']["Year"].unique())
                totalmonths = list(total.loc[total["Month"] != '']["Month"].unique())

                totalaccounts.insert(0, "All")
                totalcategories2.insert(0, "All")
                totalmonths.insert(0, "All")
                totalyears.insert(0, "All")

                for i in range(len(totalyears)):
                    totalyears[i] = str(totalyears[i])

                sums = []

                for key in totalcategories:
                    sums.append(total[total["Category"] == key]["Amount"].sum())# if key in keys else None

                ntotalyears = totalyears[1:]
                ntotalaccounts = totalaccounts[1:]
                           
                filepath = ctk.filedialog.asksaveasfile(
                initialdir="Downloads",  
                title="Select a File",  
                filetypes=(("TXT files", "*.txt"), ("All files", "*.*")) 
                )
                if filepath:
                    with open(filepath.name, "w") as f:
                        for year in ntotalyears:
                            newtotal = total.loc[total["Year"] == int(year)]
                            for a in ntotalaccounts:
                                newtotal = newtotal.query("Account == @a")
                                
                                ntotalcategories = list(newtotal.loc[newtotal["Category"] != '']["Category"].unique())
                                alist = []
                                f.write(f"<< Spending Summary on Account {a} for {year} >>\n\n")
                                for i in ntotalcategories:
                                    alist.append(newtotal.loc[newtotal["Category"] == i]["Amount"].sum())
                                    f.writelines(f'    ### {i} >> ${int(newtotal.loc[newtotal["Category"] == i]["Amount"].sum())}\n')

                                f.write(f"\n## You spent the least amount on {ntotalcategories[alist.index(min(alist))]} at ${int(min(alist))} ##\n")
                                f.write(f"## You spent the highest amount on {ntotalcategories[alist.index(max(alist))]} at ${int(max(alist))} ##")
                                f.write(f"\n## Total spend for {year} on Account {a} is >> ${int(newtotal['Amount'].sum())} ##\n\n----------------------------------------------------------------------------------------------------------\n\n")

                        f.write(f"\n ----- Statistics for Entire Report -----")
                        f.write(f"Your Highest spending category is {totalcategories[sums.index(max(sums))]} at ${int(max(sums))}\n")
                        f.write(f"Your Lowest spending category is {totalcategories[sums.index(min(sums))]} at ${int(min(sums))}\n")
                        f.write(f"Total Spending Across all Accounts for {ntotalyears} is ${int(total['Amount'].sum())}\n") 
                        f.write("\n------------------------------------------------------------------------- Complete Transaction Table -------------------------------------------------------------------------\n\n")      
                        f.writelines(total.to_string())

                    handle_report_success()

            except (FileNotFoundError, NameError, ValueError, KeyError) as e:
                self.loggingtextbox.insert("0.0", f"{str(e)}\n\n")
                handle_fileError()

        '''                 Setup Window                    '''

        global selections
        options = ["Already Consolidated", "Eglin FCU", "BILT Card", "CapitalOne Quicksilver", "CapitalOne Savor", "CapitalOne Checking", "AMEX Skymiles"]
        selections = {}
        
        def importpageselector():
            HomeScreen.frames["graphpage"].place_forget()
            HomeScreen.frames["aboutpage"].place_forget()
            HomeScreen.frames["importpage"].place(relx=0.2, rely=0, relwidth=0.8, relheight=1)

        def graphpageselector():
            HomeScreen.frames["importpage"].place_forget()
            HomeScreen.frames["aboutpage"].place_forget()
            HomeScreen.frames["graphpage"].place(relx=0.2, rely=0, relwidth=0.8, relheight=1)

        def aboutpageselector():
            HomeScreen.frames["importpage"].place_forget()
            HomeScreen.frames["graphpage"].place_forget()
            HomeScreen.frames["aboutpage"].place(relx=0.2, rely=0, relwidth=0.8, relheight=1)
        
        '''                 Setting Pages Frame                 '''
        self.pagesframe = ctk.CTkFrame(self, height=window_height, width=window_width*0.2, fg_color="#121110")
        self.pagesframe.place(relx=0, relwidth=0.2, relheight=1)
        

        currentpath = getcwd()
        try:
            self.fileexplorerbuttonimage = ctk.CTkImage(Image.open(currentpath+"/fileexplorericonorange.png"), size=(30, 30))

        except FileNotFoundError:
            self.fileexplorerbuttonimage = None

        self.geometry(f"{window_width}x{window_height}+100+300")
        self._set_appearance_mode("Dark")

        self.homeframe = ctk.CTkFrame(self, width=window_width*0.8, height=window_height)
        self.homeframe.place(relx=0, relwidth=0.8, relheight=1, anchor="sw")

        HomeScreen.frames["importpage"] = ctk.CTkFrame(self, width=window_width*0.8, height=window_height, fg_color="#000000")
        HomeScreen.frames["importpage"].place(relx=0.2, rely=0, relwidth=0.8, relheight=1)
        self.msgframe = ctk.CTkFrame(HomeScreen.frames["importpage"], fg_color="#000000", width=500, height=100)
        self.msgframe.grid(row=8, column=0, columnspan=2)
        
        HomeScreen.frames["graphpage"] = ctk.CTkFrame(self, width=window_width*0.8, height=window_height, fg_color='#000000')
        HomeScreen.frames["aboutpage"] = ctk.CTkFrame(self, width=window_width*0.8, height=window_height, fg_color='#000000')
        self.title("Fipi Analysis Tool")

        '''                 Populating Pages Frame                  '''
        self.pagesframetitle = ctk.CTkLabel(self.pagesframe, text="Spending Analysis", font=("Terminal", 24), text_color="#fcae74")
        self.pagesframetitle.place(relx=0.1, rely=0.02)

        self.importpagebutton = ctk.CTkButton(self.pagesframe, text="Import/Export", font=("Terminal", 15), text_color="#fcae74", height=35, width=180, command=importpageselector)
        self.importpagebutton.place(relx=0.05, rely=0.1, relwidth=0.9)
        self.importpagebutton.configure(border_color="#fa852e", border_width=2, fg_color="transparent", corner_radius=5, bg_color="#7d441a", text_color="#fcae74", hover_color="#7d441a")

        self.graphpagebutton = ctk.CTkButton(self.pagesframe, text="Graph", font=("Terminal", 15), text_color="#fcae74", height=35, command=graphpageselector)
        self.graphpagebutton.place(relx=0.05, rely=0.2, relwidth=0.9)
        self.graphpagebutton.configure(border_color="#fa852e", border_width=2, fg_color="transparent", corner_radius=5, bg_color="#7d441a", text_color="#fcae74", hover_color="#7d441a")

        self.aboutpagebutton = ctk.CTkButton(self.pagesframe, text="About/Help", font=("Terminal", 15), text_color="#fcae74", height=35, command=aboutpageselector)
        self.aboutpagebutton.place(relx=0.05, rely=0.3, relwidth=0.9)
        self.aboutpagebutton.configure(border_color="#fa852e", border_width=2, fg_color="transparent", corner_radius=5, bg_color="#7d441a", text_color="#fcae74", hover_color="#7d441a")

        self.grapherrorframe = ctk.CTkFrame(HomeScreen.frames["graphpage"], height=35, width=500, fg_color="transparent")
        self.grapherrorframe.pack()

        '''                 About Page                 ''' 
        tabview = ctk.CTkTabview(master=HomeScreen.frames["aboutpage"], width=window_width*0.6, height=window_height*0.8, fg_color="#1f1f1f")
        tabview.configure(text_color="#fcae74", segmented_button_fg_color="#fcae74", segmented_button_selected_color="#1f1f1f", segmented_button_unselected_color="#000000", border_color="#fcae74", border_width=2, segmented_button_selected_hover_color="#1f1f1f", segmented_button_unselected_hover_color="#1f1f1f")
        tabview.pack(padx=20, pady=20)

        tabview.add("About")  # add tab at the end
        tabview.add("Logging")  # add tab at the end
        tabview.set("About")  # set currently visible tab

        self.aboutparagraphframe = ctk.CTkFrame(HomeScreen.frames["aboutpage"], height=window_height, width=window_width)
        self.aboutparagraphframe.configure(fg_color="transparent", corner_radius=5, bg_color="#000000")
        self.aboutparagraphframe.pack(expand=True, fill="both")
        self.aboutparagraph = ctk.CTkLabel(tabview.tab("About"), text="Fipi was created by Donavin Geohagan\n\nIm just a Warehouse worker who codes on the side\n\nMy Github is https://github.com/geohadg")
        self.aboutparagraph2 = ctk.CTkLabel(tabview.tab("About"), text='Please give feedback this is the first real tool ive made!\nLeave a review at *wordpress site*!')
        self.aboutparagraph3 = ctk.CTkLabel(tabview.tab("About"), text='\nThis tool is designed to help you analyze your financial data\n\nIt is a work in progress and will be updated regularly\nto include more Bank types!')
        self.aboutparagraph.configure(text_color="#fcae74", font=("Terminal", 20), bg_color="#1f1f1f")
        self.aboutparagraph2.configure(text_color="#fcae74", font=("Terminal", 20), bg_color="#1f1f1f")
        self.aboutparagraph3.configure(text_color="#fcae74", font=("Terminal", 20), bg_color="#1f1f1f")
        self.aboutparagraph.pack(side=tkinter.TOP, pady=50)
        self.aboutparagraph2.pack(side=tkinter.TOP, pady=0)
        self.aboutparagraph3.pack(side=tkinter.TOP, pady=0)

        self.loggingtextbox = ctk.CTkTextbox(tabview.tab("Logging"), width=window_width*0.5, height=window_height*0.5, border_color="#fa852e", border_width=2, fg_color="#000000")
        self.loggingtextbox.pack(padx=20, pady=20)

        def save_log():
            try:
                content = self.loggingtextbox.get('0.0', 'end')
                filepath = ctk.filedialog.asksaveasfile(
                    initialdir="Downloads",  
                    title="Select a File",  
                    filetypes=(("TXT files", "*.txt"), ("All files", "*.*")) 
                    )
                if filepath:
                    if filepath.name.str.contains(".txt"): 
                        with open(filepath.name, "w") as f:
                            f.write(content)

                    else:
                        with open(filepath.name+".txt", "w") as f:
                            f.write(content)

            except Exception as e:
                self.loggingtextbox.insert("0.0", f"{e}\n\n")
                handle_fileError()

        self.savelogbutton = ctk.CTkButton(tabview.tab("Logging"), text="Save Log", command=lambda: save_log(), font=("Terminal", 14), border_color="#fa852e", border_width=2, fg_color="transparent", corner_radius=5, width=150, bg_color="#7d441a", text_color="#fcae74", hover_color="#7d441a")
        self.savelogbutton.pack(pady=20)

        '''                 Import Page                 '''
        '''                 Line 1                  '''
        self.colorpalletteswitch = ctk.CTkSwitch(HomeScreen.frames["importpage"], text="Theme", command=lambda: changepallettegreen() if self.colorpalletteswitch.get() == 1 else changepalletteorange(), font=("Terminal", 14), fg_color="#fcae74", bg_color="#7d441a", corner_radius=5, width=150, height=35, text_color="#fcae74", border_color="#fa852e", border_width=4)
        self.colorpalletteswitch.grid(row=6, column=1, sticky="e")
        self.textbox1 = ctk.CTkTextbox(HomeScreen.frames["importpage"], width=500, height=25, border_color="#fa852e", border_width=2)
        self.textbox1.grid(row=1, column=0, sticky="n", padx=45, pady=0)
        
        self.option1 = ctk.StringVar(value="Select Account Type")
        self.optionmenu1 = ctk.CTkComboBox(HomeScreen.frames["importpage"], variable=self.option1, values=options)
        self.optionmenu1.grid(row=1, column=1, sticky="n", padx=15, pady=0)
        self.optionmenu1.configure(border_color="#fa852e", button_color="#fa852e", dropdown_fg_color="#7d441a", width=200, fg_color="#7d441a", font=("Terminal", 14), text_color="#fcae74", dropdown_font=("Terminal", 14), dropdown_text_color="#fca05b", button_hover_color="#7d441a", dropdown_hover_color="#7d441a")


        self.filesearchbutton1 = ctk.CTkButton(HomeScreen.frames["importpage"], text="", command=lambda: addfilebutton(textbox=self.textbox1), image=self.fileexplorerbuttonimage, width=30, height=30, fg_color="transparent", hover_color="#7d441a", border_color="#fa852e", border_width=2)
        self.filesearchbutton1.grid(row=1, column=0, sticky="e", padx=0, pady=0)

        '''                 Line 2                    '''

        self.textbox2 = ctk.CTkTextbox(HomeScreen.frames["importpage"], width=500, height=25, border_color="#fa852e", border_width=2)
        self.textbox2.grid(row=2, column=0, sticky="n", padx=45, pady=20)
        
        self.option2 = ctk.StringVar(value="Select Account Type")
        self.optionmenu2 = ctk.CTkComboBox(HomeScreen.frames["importpage"], variable=self.option2, values=options, bg_color="transparent", button_color="#fa852e", fg_color="#212121", width=200)
        self.optionmenu2.grid(row=2, column=1, sticky="n", padx=15, pady=20)
        self.optionmenu2.configure(border_color="#fa852e", button_color="#fa852e", dropdown_fg_color="#7d441a", width=200, font=("Terminal", 14), fg_color="#7d441a", text_color="#fcae74", dropdown_font=("Terminal", 14), dropdown_text_color="#fca05b", button_hover_color="#7d441a", dropdown_hover_color="#7d441a")

        self.filesearchbutton2 = ctk.CTkButton(HomeScreen.frames["importpage"], text="", command=lambda: addfilebutton(textbox=self.textbox2), image=self.fileexplorerbuttonimage, width=30, height=30, fg_color="transparent", hover_color="#7d441a", border_color="#fa852e", border_width=2)
        self.filesearchbutton2.grid(row=2, column=0, sticky="e", padx=0, pady=0)

        '''                 Line 3                    '''

        self.textbox3 = ctk.CTkTextbox(HomeScreen.frames["importpage"], width=500, height=25, border_color="#fa852e", border_width=2)
        self.textbox3.grid(row=3, column=0, sticky="n", padx=45, pady=10)
        
        self.option3 = ctk.StringVar(value="Select Account Type")
        self.optionmenu3 = ctk.CTkComboBox(HomeScreen.frames["importpage"], variable=self.option3, values=options, bg_color="transparent", button_color="#d01efc", fg_color="#212121", width=200)
        self.optionmenu3.grid(row=3, column=1, sticky="n", padx=15, pady=10)
        self.optionmenu3.configure(border_color="#fa852e", button_color="#fa852e", dropdown_fg_color="#7d441a", font=("Terminal", 14), width=200, fg_color="#7d441a", text_color="#fcae74", dropdown_font=("Terminal", 14), dropdown_text_color="#fca05b", button_hover_color="#7d441a", dropdown_hover_color="#7d441a")

        self.filesearchbutton3 = ctk.CTkButton(HomeScreen.frames["importpage"], text="", command=lambda: addfilebutton(textbox=self.textbox3), image=self.fileexplorerbuttonimage, width=30, height=30, fg_color="transparent", hover_color="#7d441a", border_color="#fa852e", border_width=2)
        self.filesearchbutton3.grid(row=3, column=0, sticky="e", padx=0, pady=0)

        '''                 Line 4                     '''

        self.textbox4 = ctk.CTkTextbox(HomeScreen.frames["importpage"], width=500, height=25, border_color="#fa852e", border_width=2)
        self.textbox4.grid(row=4, column=0, sticky="n", padx=45, pady=20)
        
        self.option4 = ctk.StringVar(value="Select Account Type")
        self.optionmenu4 = ctk.CTkComboBox(HomeScreen.frames["importpage"], variable=self.option4, values=options, bg_color="transparent", button_color="#d01efc", fg_color="#212121", width=200)
        self.optionmenu4.grid(row=4, column=1, sticky="n", padx=15, pady=20)
        self.optionmenu4.configure(border_color="#fa852e", button_color="#fa852e", font=("Terminal", 14), dropdown_fg_color="#7d441a", width=200, fg_color="#7d441a", text_color="#fcae74", dropdown_font=("Terminal", 14), dropdown_text_color="#fca05b", button_hover_color="#7d441a", dropdown_hover_color="#7d441a")

        self.filesearchbutton4 = ctk.CTkButton(HomeScreen.frames["importpage"], text="", command=lambda: addfilebutton(textbox=self.textbox4), image=self.fileexplorerbuttonimage, width=30, height=30, fg_color="transparent", hover_color="#7d441a", border_color="#fa852e", border_width=2)
        self.filesearchbutton4.grid(row=4, column=0, sticky="e", padx=0, pady=0)

        '''                 Line 5                    '''

        self.textbox5 = ctk.CTkTextbox(HomeScreen.frames["importpage"], width=500, height=25, border_color="#fa852e", border_width=2)
        self.textbox5.grid(row=5, column=0, sticky="n", padx=45, pady=10)
        
        self.option5 = ctk.StringVar(value="Select Account Type")
        self.optionmenu5 = ctk.CTkComboBox(HomeScreen.frames["importpage"], variable=self.option5, values=options, bg_color="transparent", button_color="#d01efc", fg_color="#212121", width=200)
        self.optionmenu5.grid(row=5, column=1, sticky="n", padx=15, pady=10)
        self.optionmenu5.configure(border_color="#fa852e", button_color="#fa852e", font=("Terminal", 14), dropdown_fg_color="#7d441a", width=200, fg_color="#7d441a", text_color="#fcae74", dropdown_font=("Terminal", 14), dropdown_text_color="#fca05b", button_hover_color="#7d441a", dropdown_hover_color="#7d441a")

        self.filesearchbutton5 = ctk.CTkButton(HomeScreen.frames["importpage"], text="", command=lambda: addfilebutton(textbox=self.textbox5), image=self.fileexplorerbuttonimage, width=30, height=30, fg_color="transparent", hover_color="#7d441a", border_color="#fa852e", border_width=2)
        self.filesearchbutton5.grid(row=5, column=0, sticky="e", padx=0, pady=0)

        '''                 Export and Graph Buttons                  '''

        self.exportbutton = ctk.CTkButton(HomeScreen.frames["importpage"], text="Export...", command=lambda: export_csv(selections=selections), font=("Terminal", 14), border_color="#fa852e", border_width=2, fg_color="transparent", corner_radius=5, width=150, bg_color="#7d441a", text_color="#fcae74", hover_color="#7d441a")
        self.exportbutton.grid(row=6, column=0, sticky="w", padx=60, pady=20)

        self.graphbutton = ctk.CTkButton(HomeScreen.frames["importpage"], text="Graph",command=lambda: gatherinputs(selections=selections), font=("Terminal", 14), border_color="#fa852e", border_width=2, fg_color="transparent", corner_radius=5, bg_color="#7d441a", text_color="#fcae74", hover_color="#7d441a", width=150)
        self.graphbutton.grid(row=6, column=0, sticky="w", padx=220, pady=20)
        
        '''                 Generate Report Button                  '''

        self.generatereportbutton = ctk.CTkButton(HomeScreen.frames["importpage"], text="Generate Report", command=generate_report, font=("Terminal", 14), border_color="#fa852e", border_width=2, fg_color="transparent", corner_radius=5, bg_color="#7d441a", text_color="#fcae74", hover_color="#7d441a", width=150)
        self.generatereportbutton.grid(row=6, column=0, sticky="e", padx=90, pady=20)

        '''                 Warning Label for Type Already Consolidated                  '''

        self.warninglabel = ctk.CTkLabel(HomeScreen.frames["importpage"], text="** Already Consolidated Type is only for Files Previously exported in Fipi", font=("Terminal", 12), text_color="#fcae74")
        self.warninglabel.grid(row=7, column=0, sticky="s", padx=15, pady=45)

        self.warninglabel2 = ctk.CTkLabel(HomeScreen.frames["importpage"], text="** To update graph color you have to click the graph button again", font=("Terminal", 12), text_color="#fcae74")
        self.warninglabel2.grid(row=7, column=0, sticky="s", padx=15, pady=25)

        '''                 Title Label                 '''

        self.titlelabel = ctk.CTkLabel(HomeScreen.frames["importpage"], text="Import Files", font=ctk.CTkFont(family='Terminal', size=25), text_color="#fcae74")
        self.titlelabel.grid(row=0, column=0, padx=100, pady=20, sticky="n")

        '''                 Populating Graph Page                   '''

        '''                 Title Label                 '''

        self.graphdialogueframe = ctk.CTkFrame(HomeScreen.frames["graphpage"], height=40, width=window_width*0.7, fg_color="#000000")
        self.graphdialogueframe.pack(side=tkinter.TOP, anchor="center", pady=10)

        self.graphthemeswitch = ctk.CTkSwitch(HomeScreen.frames["graphpage"], text="Theme", command=lambda: changepallettegreen() if self.graphthemeswitch.get() == 1 else changepalletteorange(), font=("Terminal", 14), fg_color="#fcae74", bg_color="#7d441a", corner_radius=5, width=150, height=35, text_color="#fcae74", border_color="#fa852e", border_width=4)
        self.graphthemeswitch.pack(side=tkinter.TOP, anchor="e", padx=20)

        self.graphoptionframe = ctk.CTkFrame(HomeScreen.frames["graphpage"], height=70, fg_color='#000000', corner_radius=10)
        self.graphoptionframe.pack(anchor="center")

        self.graphframe = ctk.CTkFrame(HomeScreen.frames["graphpage"], height=window_height, width=window_width, fg_color="#000000")
        self.graphframe.pack(anchor="center")

        self.graphpagetitle = ctk.CTkLabel(self.graphdialogueframe, font=('Terminal', 25), text_color='#fcae74', text="Graph")
        self.graphpagetitle.grid(sticky='w', row=0, column=0, padx=20, pady=20)

        self.accountoptionmenuoption = ctk.StringVar(HomeScreen.frames["graphpage"], "All")
        self.accountoptionmenu = ctk.CTkComboBox(self.graphoptionframe, values=[' '], variable=self.accountoptionmenuoption)
        self.accountoptionmenu.grid(row=0, column=0, padx=0)
        self.accountoptionmenu.configure(border_color="#fa852e", button_color="#fa852e", dropdown_fg_color="#7d441a", width=160, fg_color="#7d441a", text_color="#fcae74", font=("Terminal", 14), dropdown_font=("Terminal", 14), dropdown_text_color="#fca05b", button_hover_color="#7d441a", dropdown_hover_color="#7d441a")

        self.categoryoptionmenuoption = ctk.StringVar(HomeScreen.frames["graphpage"], "All")
        self.categoryoptionmenu = ctk.CTkComboBox(self.graphoptionframe, values=[' '], variable=self.categoryoptionmenuoption)
        self.categoryoptionmenu.grid(row=0, column=1, padx=40)
        self.categoryoptionmenu.configure(border_color="#fa852e", button_color="#fa852e", dropdown_fg_color="#7d441a", width=160, fg_color="#7d441a", text_color="#fcae74", font=("Terminal", 14), dropdown_font=("Terminal", 14), dropdown_text_color="#fca05b", button_hover_color="#7d441a", dropdown_hover_color="#7d441a")

        self.monthoption = ctk.StringVar(HomeScreen.frames["graphpage"], "All")
        self.monthoptionmenu = ctk.CTkComboBox(self.graphoptionframe, values=[" "], variable=self.monthoption)
        self.monthoptionmenu.grid(row=0, column=2, padx=30)
        self.monthoptionmenu.configure(border_color="#fa852e", button_color="#fa852e", dropdown_fg_color="#7d441a", width=160, fg_color="#7d441a", text_color="#fcae74", font=("Terminal", 14), dropdown_font=("Terminal", 14), dropdown_text_color="#fca05b", button_hover_color="#7d441a", dropdown_hover_color="#7d441a")

        self.yearoption = ctk.StringVar(HomeScreen.frames["graphpage"], "All")
        self.yearoptionmenu = ctk.CTkComboBox(self.graphoptionframe, variable=self.yearoption, values=[" "])
        self.yearoptionmenu.grid(row=0, column=3, padx=10)
        self.yearoptionmenu.configure(border_color="#fa852e", button_color="#fa852e", dropdown_fg_color="#7d441a", width=160, fg_color="#7d441a", text_color="#fcae74", font=("Terminal", 14), dropdown_font=("Terminal", 14), dropdown_text_color="#fca05b", button_hover_color="#7d441a", dropdown_hover_color="#7d441a")
        
        

        def changepalletteorange():
            self.accountoptionmenu.configure(border_color="#fa852e", button_color="#fa852e", dropdown_fg_color="#7d441a", width=160, fg_color="#7d441a", text_color="#fcae74", font=("Terminal", 14), dropdown_font=("Terminal", 14), dropdown_text_color="#fca05b", button_hover_color="#7d441a", dropdown_hover_color="#7d441a")
            self.categoryoptionmenu.configure(border_color="#fa852e", button_color="#fa852e", dropdown_fg_color="#7d441a", width=160, fg_color="#7d441a", text_color="#fcae74", font=("Terminal", 14), dropdown_font=("Terminal", 14), dropdown_text_color="#fca05b", button_hover_color="#7d441a", dropdown_hover_color="#7d441a")
            self.monthoptionmenu.configure(border_color="#fa852e", button_color="#fa852e", dropdown_fg_color="#7d441a", width=160, fg_color="#7d441a", text_color="#fcae74", font=("Terminal", 14), dropdown_font=("Terminal", 14), dropdown_text_color="#fca05b", button_hover_color="#7d441a", dropdown_hover_color="#7d441a")
            self.yearoptionmenu.configure(border_color="#fa852e", button_color="#fa852e", dropdown_fg_color="#7d441a", width=160, fg_color="#7d441a", text_color="#fcae74", font=("Terminal", 14), dropdown_font=("Terminal", 14), dropdown_text_color="#fca05b", button_hover_color="#7d441a", dropdown_hover_color="#7d441a")
            self.titlelabel.configure(text_color="#fcae74")
            self.warninglabel.configure(text_color="#fcae74")
            self.warninglabel2.configure(text_color="#fcae74")
            self.exportbutton.configure(border_color="#fa852e", border_width=2, fg_color="transparent", corner_radius=5, bg_color="#7d441a", text_color="#fcae74", hover_color="#7d441a")
            self.graphbutton.configure(border_color="#fa852e", border_width=2, fg_color="transparent", corner_radius=5, bg_color="#7d441a", text_color="#fcae74", hover_color="#7d441a")
            self.generatereportbutton.configure(border_color="#fa852e", border_width=2, fg_color="transparent", corner_radius=5, bg_color="#7d441a", text_color="#fcae74", hover_color="#7d441a")
            self.savelogbutton.configure(border_color="#fa852e", border_width=2, fg_color="transparent", corner_radius=5, bg_color="#7d441a", text_color="#fcae74", hover_color="#7d441a")
            self.pagesframetitle.configure(text_color="#fcae74")
            self.importpagebutton.configure(border_color="#fa852e", border_width=2, fg_color="transparent", corner_radius=5, bg_color="#7d441a", text_color="#fcae74", hover_color="#7d441a")
            self.graphpagebutton.configure(border_color="#fa852e", border_width=2, fg_color="transparent", corner_radius=5, bg_color="#7d441a", text_color="#fcae74", hover_color="#7d441a")
            self.aboutpagebutton.configure(border_color="#fa852e", border_width=2, fg_color="transparent", corner_radius=5, bg_color="#7d441a", text_color="#fcae74", hover_color="#7d441a")
            self.optionmenu1.configure(border_color="#fa852e", button_color="#fa852e", dropdown_fg_color="#7d441a", width=200, fg_color="#7d441a", text_color="#fcae74", font=("Terminal", 14), dropdown_font=("Terminal", 14), dropdown_text_color="#fca05b", button_hover_color="#7d441a", dropdown_hover_color="#7d441a")
            self.optionmenu2.configure(border_color="#fa852e", button_color="#fa852e", dropdown_fg_color="#7d441a", width=200, fg_color="#7d441a", text_color="#fcae74", font=("Terminal", 14), dropdown_font=("Terminal", 14), dropdown_text_color="#fca05b", button_hover_color="#7d441a", dropdown_hover_color="#7d441a")
            self.optionmenu3.configure(border_color="#fa852e", button_color="#fa852e", dropdown_fg_color="#7d441a", width=200, fg_color="#7d441a", text_color="#fcae74", font=("Terminal", 14), dropdown_font=("Terminal", 14), dropdown_text_color="#fca05b", button_hover_color="#7d441a", dropdown_hover_color="#7d441a")
            self.optionmenu4.configure(border_color="#fa852e", button_color="#fa852e", dropdown_fg_color="#7d441a", width=200, fg_color="#7d441a", text_color="#fcae74", font=("Terminal", 14), dropdown_font=("Terminal", 14), dropdown_text_color="#fca05b", button_hover_color="#7d441a", dropdown_hover_color="#7d441a")
            self.optionmenu5.configure(border_color="#fa852e", button_color="#fa852e", dropdown_fg_color="#7d441a", width=200, fg_color="#7d441a", text_color="#fcae74", font=("Terminal", 14), dropdown_font=("Terminal", 14), dropdown_text_color="#fca05b", button_hover_color="#7d441a", dropdown_hover_color="#7d441a")
            self.textbox1.configure(border_color="#fa852e", border_width=2)
            self.textbox2.configure(border_color="#fa852e", border_width=2)
            self.textbox3.configure(border_color="#fa852e", border_width=2)
            self.textbox4.configure(border_color="#fa852e", border_width=2)
            self.textbox5.configure(border_color="#fa852e", border_width=2)
            self.graphpagetitle.configure(text_color="#fcae74")
            self.filesearchbutton1.configure(border_color="#fa852e", border_width=2, fg_color="transparent", corner_radius=5, text_color="#fcae74", hover_color="#7d441a")
            self.filesearchbutton2.configure(border_color="#fa852e", border_width=2, fg_color="transparent", corner_radius=5, text_color="#fcae74", hover_color="#7d441a")
            self.filesearchbutton3.configure(border_color="#fa852e", border_width=2, fg_color="transparent", corner_radius=5, text_color="#fcae74", hover_color="#7d441a")
            self.filesearchbutton4.configure(border_color="#fa852e", border_width=2, fg_color="transparent", corner_radius=5, text_color="#fcae74", hover_color="#7d441a")
            self.filesearchbutton5.configure(border_color="#fa852e", border_width=2, fg_color="transparent", corner_radius=5, text_color="#fcae74", hover_color="#7d441a")
            self.updatebutton.configure(border_color="#fa852e", border_width=2, fg_color="transparent", corner_radius=5, bg_color="#7d441a", text_color="#fcae74", hover_color="#7d441a")
            self.aboutparagraph.configure(text_color="#fcae74", font=("Terminal", 20), bg_color="#1f1f1f")
            self.aboutparagraph2.configure(text_color="#fcae74", font=("Terminal", 20), bg_color="#1f1f1f")
            self.aboutparagraph3.configure(text_color="#fcae74", font=("Terminal", 20), bg_color="#1f1f1f")
            tabview.configure(text_color="#fcae74", segmented_button_fg_color="#fcae74", segmented_button_selected_color="#1f1f1f", segmented_button_unselected_color="#000000", border_color="#fcae74", border_width=2, segmented_button_selected_hover_color="#1f1f1f", segmented_button_unselected_hover_color="#1f1f1f")
            self.loggingtextbox.configure(border_color="#fa852e")
            self.colorpalletteswitch.configure(border_color="#fa852e", fg_color="#fcae74", bg_color="#7d441a", corner_radius=5, width=150, height=35, text_color="#fcae74")
            self.savefigurebutton.configure(border_color="#fa852e", border_width=2, fg_color="transparent", corner_radius=5, bg_color="#7d441a", text_color="#fcae74", hover_color="#7d441a")
            global current_pallette
            current_pallette = graph_pallettes["flare"]
            self.graphthemeswitch.configure(border_color="#fa852e", fg_color="#fcae74", bg_color="#7d441a", corner_radius=5, width=150, height=35, text_color="#fcae74")
            
            try:
                self.fileexplorerbuttonimage = ctk.CTkImage(Image.open(currentpath+"/fileexplorericonorange.png"), size=(30, 30))

            except:
                self.loggingtextbox.insert("0.0", f"Error: Could not find 'fileexplorericonorange.png'\n")
                pass


            
            

        def changepallettegreen():
            self.accountoptionmenu.configure(border_color="#00ff38", button_color="#00ff38", dropdown_fg_color="#0d3818", width=160, fg_color="#0d3818", text_color="#00ff6b", font=("Terminal", 14), dropdown_font=("Terminal", 14), dropdown_text_color="#00ff6b", button_hover_color="#0d3818", dropdown_hover_color="#0d3818")
            self.categoryoptionmenu.configure(border_color="#00ff38", button_color="#00ff38", dropdown_fg_color="#0d3818", width=160, fg_color="#0d3818", text_color="#00ff6b", font=("Terminal", 14), dropdown_font=("Terminal", 14), dropdown_text_color="#00ff6b", button_hover_color="#0d3818", dropdown_hover_color="#0d3818")
            self.monthoptionmenu.configure(border_color="#00ff38", button_color="#00ff38", dropdown_fg_color="#0d3818", width=160, fg_color="#0d3818", text_color="#00ff6b", font=("Terminal", 14), dropdown_font=("Terminal", 14), dropdown_text_color="#00ff6b", button_hover_color="#0d3818", dropdown_hover_color="#0d3818")
            self.yearoptionmenu.configure(border_color="#00ff38", button_color="#00ff38", dropdown_fg_color="#0d3818", width=160, fg_color="#0d3818", text_color="#00ff6b", font=("Terminal", 14), dropdown_font=("Terminal", 14), dropdown_text_color="#00ff6b", button_hover_color="#0d3818", dropdown_hover_color="#0d3818")
            self.titlelabel.configure(text_color="#00ff6b")
            self.warninglabel.configure(text_color="#00ff6b")
            self.warninglabel2.configure(text_color="#00ff6b")
            self.exportbutton.configure(border_color="#00ff38", border_width=2, fg_color="transparent", corner_radius=5, bg_color="#0d3818", text_color="#00ff6b", hover_color="#0d3818")
            self.graphbutton.configure(border_color="#00ff38", border_width=2, fg_color="transparent", corner_radius=5, bg_color="#0d3818", text_color="#00ff6b", hover_color="#0d3818")
            self.generatereportbutton.configure(border_color="#00ff38", border_width=2, fg_color="transparent", corner_radius=5, bg_color="#0d3818", text_color="#00ff6b", hover_color="#0d3818")
            self.savelogbutton.configure(border_color="#00ff38", border_width=2, fg_color="transparent", corner_radius=5, bg_color="#0d3818", text_color="#00ff6b", hover_color="#0d3818")
            self.pagesframetitle.configure(text_color="#00ff6b")
            self.importpagebutton.configure(border_color="#00ff38", border_width=2, fg_color="transparent", corner_radius=5, bg_color="#0d3818", text_color="#00ff6b", hover_color="#0d3818")
            self.graphpagebutton.configure(border_color="#00ff38", border_width=2, fg_color="transparent", corner_radius=5, bg_color="#0d3818", text_color="#00ff6b", hover_color="#0d3818")
            self.aboutpagebutton.configure(border_color="#00ff38", border_width=2, fg_color="transparent", corner_radius=5, bg_color="#0d3818", text_color="#00ff6b", hover_color="#0d3818")
            self.optionmenu1.configure(border_color="#00ff38", button_color="#00ff38", dropdown_fg_color="#0d3818", width=200, fg_color="#0d3818", text_color="#00ff6b", font=("Terminal", 14), dropdown_font=("Terminal", 14), dropdown_text_color="#00ff6b", button_hover_color="#0d3818", dropdown_hover_color="#0d3818")
            self.optionmenu2.configure(border_color="#00ff38", button_color="#00ff38", dropdown_fg_color="#0d3818", width=200, fg_color="#0d3818", text_color="#00ff6b", font=("Terminal", 14), dropdown_font=("Terminal", 14), dropdown_text_color="#00ff6b", button_hover_color="#0d3818", dropdown_hover_color="#0d3818")
            self.optionmenu3.configure(border_color="#00ff38", button_color="#00ff38", dropdown_fg_color="#0d3818", width=200, fg_color="#0d3818", text_color="#00ff6b", font=("Terminal", 14), dropdown_font=("Terminal", 14), dropdown_text_color="#00ff6b", button_hover_color="#0d3818", dropdown_hover_color="#0d3818")
            self.optionmenu4.configure(border_color="#00ff38", button_color="#00ff38", dropdown_fg_color="#0d3818", width=200, fg_color="#0d3818", text_color="#00ff6b", font=("Terminal", 14), dropdown_font=("Terminal", 14), dropdown_text_color="#00ff6b", button_hover_color="#0d3818", dropdown_hover_color="#0d3818")
            self.optionmenu5.configure(border_color="#00ff38", button_color="#00ff38", dropdown_fg_color="#0d3818", width=200, fg_color="#0d3818", text_color="#00ff6b", font=("Terminal", 14), dropdown_font=("Terminal", 14), dropdown_text_color="#00ff6b", button_hover_color="#0d3818", dropdown_hover_color="#0d3818")
            self.textbox1.configure(border_color="#00ff38", border_width=2)
            self.textbox2.configure(border_color="#00ff38", border_width=2)
            self.textbox3.configure(border_color="#00ff38", border_width=2)
            self.textbox4.configure(border_color="#00ff38", border_width=2)
            self.textbox5.configure(border_color="#00ff38", border_width=2)
            self.graphpagetitle.configure(text_color="#00ff6b")
            self.filesearchbutton1.configure(border_color="#00ff38", border_width=2, hover_color="#0d3818", fg_color="transparent")
            self.filesearchbutton2.configure(border_color="#00ff38", border_width=2, hover_color="#0d3818", fg_color="transparent")
            self.filesearchbutton3.configure(border_color="#00ff38", border_width=2, hover_color="#0d3818", fg_color="transparent")
            self.filesearchbutton4.configure(border_color="#00ff38", border_width=2, hover_color="#0d3818", fg_color="transparent")
            self.filesearchbutton5.configure(border_color="#00ff38", border_width=2, hover_color="#0d3818", fg_color="transparent")
            self.updatebutton.configure(border_color="#00ff38", border_width=2, fg_color="transparent", corner_radius=5, bg_color="#0d3818", text_color="#00ff6b", hover_color="#0d3818")
            self.aboutparagraph.configure(text_color="#00ff6b", font=("Terminal", 20), bg_color="#1f1f1f")
            self.aboutparagraph2.configure(text_color="#00ff6b", font=("Terminal", 20), bg_color="#1f1f1f")
            self.aboutparagraph3.configure(text_color="#00ff6b", font=("Terminal", 20), bg_color="#1f1f1f")
            tabview.configure(text_color="#00ff6b", segmented_button_fg_color="#00ff6b", segmented_button_selected_color="#1f1f1f", segmented_button_unselected_color="#000000", border_color="#00ff6b", border_width=2, segmented_button_selected_hover_color="#1f1f1f", segmented_button_unselected_hover_color="#1f1f1f")
            self.loggingtextbox.configure(border_color="#00ff38")
            self.colorpalletteswitch.configure(border_color="#00ff38", fg_color="#00ff6b", bg_color="#0d3818", corner_radius=5, width=150, height=35, text_color="#00ff6b")
            self.savefigurebutton.configure(border_color="#00ff38", border_width=2, fg_color="transparent", corner_radius=5, bg_color="#0d3818", text_color="#00ff6b", hover_color="#0d3818")
            global current_pallette
            current_pallette = graph_pallettes["forest"]
            self.graphthemeswitch.configure(border_color="#00ff38", fg_color="#00ff6b", bg_color="#0d3818", corner_radius=5, width=150, height=35, text_color="#00ff6b")

            try:
                self.fileexplorerbuttonimage = ctk.CTkImage(Image.open(currentpath+"/fileexplorericongreen.png"), size=(30, 30))
            
            except:
                self.loggingtextbox.insert('0.0', "Error: Could not find fileexplorericongreen.png\n")
                pass
            

        def update_graph():
            for w in self.grapherrorframe.winfo_children():
                    w.destroy()
            month = self.monthoptionmenu.get()
            year = self.yearoptionmenu.get()
            account = self.accountoptionmenuoption.get()
            category = self.categoryoptionmenu.get()
            temp = total

            if category != "All":
                if month == "All":
                    pass

                if month != "All":
                    temp = temp.query("Month == @month")

                if year == "All":
                    pass

                if year != "All":
                    y = int(year)
                    temp = temp.query("Year == @y")

                if account == "All":
                    graphsums = []
                    graphkeys = []
                    graphcolors = []
                    graphlabels = []
                    accounts = list(temp.loc[temp["Account"] != '']["Account"].unique())
                    i = 2
                    temp = temp.query("Category == @category")
                    for account in accounts:
                        temp2 = temp.query("Account == @account")
                        
                        sums = temp2["Amount"].tolist()
                        keys = temp2["Date"].tolist()

                        if len(sums) == 0:
                            pass


                        else:
                            graphsums.append(sums)
                            graphkeys.append(keys)
                            graphcolors.append(current_pallette[i])
                            graphlabels.append(f"{account}: {category}")
                            
                            i += 1

                    print(temp)
                    if len(graphsums) == 0:
                        handle_empty_dataset()
                    
                    if len(graphsums) > 0:
                        if len(graphsums[0]) == 1:
                            graphline(graphsums[0], graphkeys[0], graphcolors[0], graphlabels[0])
                        
                        if len(graphsums[0]) > 1:
                            graphmultiplelines(graphsums, graphkeys, graphcolors, graphlabels)

                    
                        

                elif account != "All":
                    temp = temp.query("Category == @category")
                    temp = temp.query("Account == @account")
                    sums = temp["Amount"].tolist()
                    keys = temp["Date"].tolist()

                    graphline(sums, keys, current_pallette[2], f"{account}: {category}")

            else:
                if month != "All":
                    temp = temp.query("Month == @month")
                    

                elif month == "All":
                    pass

                if year != "All":
                    year = int(year)
                    temp = temp.query("Year == @year")

                elif year == "All":
                    pass

                if account != "All":
                    temp = temp.query("Account == @account")
                    

                totalcategories = list(temp.loc[temp["Category"] != ""]["Category"].unique())
                sums = []

                for key in totalcategories:
                    sums.append(total[total["Category"] == key]["Amount"].sum())

                graphpie(sums, totalcategories, current_pallette)
                

        def save_figure():
            try: 
                file = ctk.filedialog.asksaveasfile(mode='w', defaultextension=".png", filetypes=[("PNG file", "*.png")])
                if file:
                    self.fig.savefig(file.name)

            except Exception as e:
                self.loggingtextbox.insert(tkinter.END, f"Error: {e}\n")
                handle_fileError()
            

        self.updatebutton = ctk.CTkButton(self.graphdialogueframe, text="Update", command=update_graph, border_color="#fa852e", border_width=2, fg_color="transparent", corner_radius=5, bg_color="#7d441a", font=("Terminal", 14), text_color="#fcae74", hover_color="#7d441a", width=150)        
        self.updatebutton.grid(sticky='e', row=0, column=0, padx=0, pady=20)

        self.savefigurebutton = ctk.CTkButton(self.graphdialogueframe, text="Save Figure", command=save_figure, border_color="#fa852e", border_width=2, fg_color="transparent", corner_radius=5, bg_color="#7d441a", font=("Terminal", 14), text_color="#fcae74", hover_color="#7d441a", width=150)
        self.savefigurebutton.grid(sticky='e', row=0, column=0, padx=300, pady=20)
        
        self.fig=plt.Figure(figsize=(100,100), dpi=100, facecolor="Black")
        self.ax= self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, self.graphframe)
        self.canvas.draw()

        def graphpie(sums, keys, pallete):
            """Produces a pie chart from given list of sums and labels"""
            
            self.ax.clear()
            
            explodelist = []
            displaysums = []
            indexestodelete = []
            s = sum(sums)
            threshold = s*0.01
            
            for i in range(len(sums)):
                displaysums.append(f"{keys[i]}: {str(int(sums[i]))}$")
                sums[i] = sums[i].astype(int)
                if sums[i] < threshold:
                    indexestodelete.append(i)
            
            indexcount = 0
            indexestodelete.sort(reverse=True)
            for index in indexestodelete:
                del keys[index]
                del sums[index]
                index = index - indexcount
                indexcount += 1
            
            minsum = min(sums)
            maxsum = max(sums)
            for i in range(len(sums)):
                
                if sums[i] == minsum or sums[i] == maxsum:
                    explodelist.append(0.2)

                else:
                    explodelist.append(0)

            colors = ['#fcc98d', '#fcbd74', '#e98d6b', '#e3685c', '#d63c56', '#c93673', '#9e3460', '#8f3371', '#6c2b6d', '#511852']

            def custom_label(pct):
                return f'{pct:.0f}%' if pct > 2 else ''

            _, texts, _ = self.ax.pie(sums, labels=keys, explode=explodelist, autopct=custom_label, labeldistance=1.1, radius=1.2, colors=pallete, startangle=0, textprops={"fontsize": 14, "fontname": "power green"})#, wedgeprops={'edgecolor': 'black', 'linewidth': 1})
            #autopct=lambda p: '{:.1f}%'.format(round(p)) if p > 1 else '',
            if pallete == graph_pallettes["flare"]:
                for key in texts:
                    key.set_color("#fcae74")

            if pallete == graph_pallettes["forest"]:
                for key in texts:
                    key.set_color("#00ff6b")
            
            # self.ax.legend(loc='best', labels=displaysums)
            self.ax.legend(bbox_to_anchor=(-0.5, 0.1), loc='center left', labels=displaysums)
            # toolbar = NavigationToolbar2Tk(self.canvas, self.graphframe, pack_toolbar=False)
            # toolbar.update()
            # toolbar.pack(side=tkinter.BOTTOM, fill=tkinter.X)   
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(side=tkinter.RIGHT, anchor="e", fill="x")

        def graphmultiplelines(sums, keys, colors, label):
        
            self.ax.clear()
            """Produces a line chart from given list of sums and labels"""
            
            for i in range(len(sums)):
                if len(sums[i]) == 1:
                    dates = pd.to_datetime(keys[i])
                    self.ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y')) # Adjust the date format as needed
                    self.ax.xaxis.set_major_locator(mdates.AutoDateLocator())
                    self.ax.plot(dates, sums[i], marker="o", color=colors[i])
                    

                else:
                    dates = pd.to_datetime(keys[i])
                    self.ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y')) # Adjust the date format as needed
                    self.ax.xaxis.set_major_locator(mdates.AutoDateLocator())
                    
                    self.ax.set_xlabel("Date", color="white")
                    self.ax.set_ylabel("Amount", color="white")
                    self.ax.tick_params(axis="x", colors="white", rotation=45)
                    self.ax.tick_params(axis="y", colors="white")
                    
                    self.ax.plot(dates, sums[i], color=colors[i])
           
            self.ax.legend(loc="best", labels=label)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(side=tkinter.RIGHT, anchor="e", fill="x")

        def graphline(sums, keys, color, label):
            if len(sums) == 0:
                handle_empty_dataset()

            elif len(sums) == 1:
                for w in self.grapherrorframe.winfo_children():
                    w.destroy()

                self.ax.clear()
                dates = pd.to_datetime(keys)
                self.ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y')) # Adjust the date format as needed
                self.ax.xaxis.set_major_locator(mdates.AutoDateLocator())
                
                self.ax.set_xlabel("Date", color="white")
                self.ax.set_ylabel("Amount", color="white")
                self.ax.tick_params(axis="x", colors="white", rotation=45)
                self.ax.tick_params(axis="y", colors="white")
                
                self.ax.plot(dates, sums, marker="o", color=color, label=label)
            
                
                self.canvas.draw()
                self.canvas.get_tk_widget().pack(side=tkinter.RIGHT, anchor="e", fill="x")

            else:
                for w in self.grapherrorframe.winfo_children():
                    w.destroy()

                self.ax.clear()
                dates = pd.to_datetime(keys)
                self.ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y')) # Adjust the date format as needed
                self.ax.xaxis.set_major_locator(mdates.AutoDateLocator())
                
                self.ax.set_xlabel("Date", color="white")
                self.ax.set_ylabel("Amount", color="white")
                self.ax.tick_params(axis="x", colors="white", rotation=45)
                self.ax.tick_params(axis="y", colors="white")
                
                self.ax.plot(dates, sums, color=color, label=label)
            
                
                self.canvas.draw()
                self.canvas.get_tk_widget().pack(side=tkinter.RIGHT, anchor="e", fill="x")

            
'''                 Start Main App Loop                 '''

Home = HomeScreen()
Home.mainloop()