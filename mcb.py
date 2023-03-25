#! python3

#mcb.py - a multiclipboard program that saves and returns contents to the clipboard

import os, sys, pyperclip, shelve

# Changes the current working directory 
# to the directory that is storing the file being run (ie. mcb.py)
os.chdir(os.path.dirname(__file__))

if len(sys.argv) < 2:
    print('''Please run the program again and specify what you want to do in your command.
save 'keyword': saves current clipboard contents under the given keyword
'keyword': copies the contents saved under the given keyword to the clipboard
list: shows a list of the keywords already used for saving contents''')
    sys.exit()
    
else:
    command = sys.argv

shelfFile = shelve.open('mcbData')

if command[1] == 'save':
    if len(command) < 3:
        keyword = input('Please enter a keyword for saving your contents: ')
    else:
        keyword = str(command[2])

    contents = pyperclip.paste()

    if keyword in shelfFile.keys():
        print('Keyword already in use.')
        overwrite = input('Do you wish to overwrite (Y/N)?: ')
        while overwrite not in ['y', 'Y', 'n', 'N']:
            overwrite = input('Enter either Y or N: ')
        overwrite = overwrite.upper()
        if overwrite == 'Y':
            shelfFile[keyword] = contents
            print("Clipboard contents saved under '{}'.".format(keyword))
        else:
            print('You selected not to overwrite.')
    else:
        shelfFile[keyword] = contents
        print("Clipboard contents saved under '{}'.".format(keyword))

elif command[1] == 'list':
    print('You currently have clipboard contents saved under the following keywords:')
    for keyword in shelfFile.keys():
        print(keyword)

else:
    keyword = command[1]

    while (keyword not in shelfFile.keys()) and (keyword != 'list'):
        print("There are no contents saved under the keyword '{}'".format(keyword))
        keyword = input("Please try another keyword or enter 'list' to get "
                        "a list of saved keywords: ")
    if keyword == 'list':
        print('You currently have clipboard contents saved under the following keywords:')
        for keyword in shelfFile.keys():
            print(keyword)
    else:
        contents = shelfFile[keyword]
        pyperclip.copy(contents)
        print("Contents for '{}' have been copied to the clipboard.".format(keyword))