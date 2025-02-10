---
title: Fipi v2 Bug Report and Fixes
---
2025-01-27 22:05
Tags: [[Fipi]]  [[Python]]

# Bugs to Fix

Compiled as a .EXE crashes during startup because images cant be found

# Features to Add

Improved Color Pallette to increase legibility and appearance
	In program as a list of hex values manually inputted and are assigned to fix graph size without having jumps in the color spectrum but they arent generated they are hard coded

View Report Button on Import Page
	Generate a text file with a Comprehensive Breakdown of Inter-Category Spend over month and year, with highlighted areas of highest and lowest spend and possible areas of improvement
# Fixes

## Images not found problem:

This is a very easy problem to fix just by changing the path called in script from:
```
fileexplorericon = ctk.CTkImage(Image.open("C:\Users\username\fipi\fileexplorericon.png"))
```
to:
```
currentpath = getcwd()
fileexplorericon = ctk.CTkImage(Image.open(currentpath+"/fileexplorericon.png"))
```
using the getcwd function from the os module for inter-os compatibility

Now as long as the image is stored in the same directory with fipi.exe the icoon will show up

But just in case I will also add a try/except block to allow the program to run without the image if needed

```
try:
	Self.fileexplorerbuttonimage = ctk.CTkImage(Image.open(currentpath+"/fileexplorericon.png"), size=(30, 30))
	
Except FileNotFoundError:
	Self.fileexplorerbuttonimage = None
	
```
A little fidgeting with the size of the button back to 30, 30 pixels after image loss and it works perfectly


## Adding the Report Feature

the format of this function output should be in a text format as follows:
		    ######## Your Spending for Year Year1 ########
		
	Account 1:
	
		### Category 1: Amount 1 ### 
		### Category 2: Amount 2 ###
		### Category 3: Amount 2 ###
		### Category 4: Amount 2 ###
		.
		.
		.
		
	## Highest Spend Category: HighestCategoryAccount1: HighestAmountAccount1 ##
		
	Account 2:
	
		### Category 1: Amount 1 ### 
		### Category 2: Amount 2 ###
		### Category 3: Amount 2 ###
		### Category 4: Amount 2 ###
		.
		.
		.
		
	## Highest Spend Category: HighestCategoryAccount2: HighestAmountAccount2 ##
	
	.
	.
	.
	# Total Spending for Year1      TotalSpendingYear1 #
	# Highest Spend Category        HighestSpendYear1  #
	# Lowest Spend Category         LowestSpendYear1   #
	
Input Is a Dataframe with columns  ["Amount", "Category", "Description", "Month","Year"]

This function will be added as a button next to the export and graph options
Program will ask for a file prompt where user will type desired name and save as a txt where it will then be filled with the data above

```
filepath = ctk.filedialog.asksaveasfile(

                initialdir="Downloads",  

                title="Select a File",  

                filetypes=(("TXT files", "*.txt"), ("All files", "*.*"))

                )

                if filepath:

                    with open(filepath.name, "w") as f:

                        for year in ntotalyears:

                            for a in ntotalaccounts:

                                newtotal = total.loc[total["Account"] == a]

                                newtotal = newtotal.loc[total["Year"] == int(year)]

                                ntotalcategories = list(newtotal.loc[newtotal["Category"] != '']["Category"].unique())

                                alist = []

                                f.write(f"<< Spending Summary on Account {a} for {year} >>\n\n")

                                for i in ntotalcategories:

                                    alist.append(newtotal.loc[newtotal["Category"] == i]["Amount"].sum())

                                    f.writelines(f'    ### {i} >> ${int(newtotal.loc[newtotal["Category"] == i]["Amount"].sum())}\n')

  

                                f.write(f"\n## You spent the least amount on {ntotalcategories[alist.index(min(alist))]} at ${int(min(alist))} ##\n")

                                f.write(f"## You spent the highest amount on {ntotalcategories[alist.index(max(alist))]} at ${int(max(alist))} ##")

  

                                f.write(f"\n## Total spend for {year} on Account {a} is >> ${int(newtotal['Amount'].sum())} ##\n\n---------------------------------------------------------------------------------------------------------- \n")

  

                        f.write(f"Your Highest spending category is {totalcategories[sums.index(max(sums))]} at ${int(max(sums))}\n")

                        f.write(f"Your Lowest spending category is {totalcategories[sums.index(min(sums))]} at ${int(min(sums))}\n")

                        f.write(f"Total Spending Across all Accounts for {ntotalyears} is ${int(total['Amount'].sum())}\n")      

  

                    self.reportsuccesslabel = ctk.CTkLabel(HomeScreen.frames["importpage"], text="Report Generated Successfully", font=("Terminal", 15), text_color="#fcae74")

                    self.reportsuccesslabel.grid(row=8, column=0, columnspan=2)

  

            except (FileNotFoundError, NameError, ValueError, KeyError):

                handle_fileError()

```
``
![[generatereportscreenshot1.png]]

![[generatereportscreenshot2.png]]
# Report

The Generate Report feature is working as intended and has a button added nicely to the home screen 

I also added a popup message embedded into the homescreen so the user knows when the report has generated succesfully

See [[Fipi v3 Bug Report and Fixes]] for next iteration