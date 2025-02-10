---
	title: Fipi v3 Bug Report and Fixes
---
2025-02-08 13:28
Tags: [[Fipi]] [[Python]]

# Bugs to Fix:

Error Induced Popup Windows do not appear on top and are hard to see making the user experience worse

Overall Error Handling is not very good or appealing

# Features to Add:

Add a Logging section to the about page so people can view and copy any errors that may pop up

Maybe an FAQ or a warning label for known errors
# Fixes:
## Popup Window and Error Handling Problem

Change the handle_error() function to add messages to homescreen instead of a popup message and add more error messages to give clearer picture of the error that occured

The way it worked before was that if an error occured while doing the pre-programmed transformations to the dataframe then a small popup window would try to appear on top and tell you, with a button that when pressed closes the popup.

The problem with this is that the popup doesnt appearo n top and is in fact hidden thus not fulfilling its purpose

So instead I did awa ywith that concept and embedded a frame within the import page that is for displaying text messages to the user called  """  self.msgframe """  as a child of the HomeScreen.frames["importpage"] 

Now the labels for different alerts wont appear on top of eachother and can be cleared for each use

![[Error-messages-fipi-v3.PNG]]

each function checks if there are any labels currently set as children of the msgframe and if there is they are cleared so the new one can be redrawn in its place

Added several Custom Error Messages for if the Account type box is left at default or input textbox is still empty
## Adding the Logging Feature to About Page

I added a tabview instance to the About Page in order to keep it minimal and added a seperate tab for the logging

The logging tab is a textbox where error messages automatically get inserted and can be saved to  a text file with the save log button

![[loggingtab-fipi-v3.PNG]]
# Report:

The Error Message functions work exactly as intended and improve the user experiences

See [[Fipi v4 Bug Report and Fixes]] for next iteration
