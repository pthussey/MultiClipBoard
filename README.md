# MultiClipBoard
A simple clipboard program for saving commonly used text.

The idea for this program comes from the book [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) by Al Sweigart.

The only additional module needed for this program to work is pyperclip.

It can be set up to run as a script using a .bat file set up as below:  
#mcb.bat  
@python.exe C:\your\path\mcb.py %*  
@pause

Of course you will need to have the paths to python.exe and the script saved in your environment variable paths.

The database that holds the saved text clips will be created in the same folder that holds the file being run (ie. mcb.py).
