from __future__ import print_function

'''
Week Two Assignment 2 - File Hashing
'''
# Name = Austin Kruse
# Date = 1/29/2020
# Assignment Number = Week2 - 3

'''
Complete the script below to do the following:
1) Add your name, date, assignment number to the top of this script
2) Using the os library and the os.walk() method 
   a) Create a list of all files
   b) Create an empty dictionary named fileHashes 
   c) Iterate through the list of files and
      - calculate the md5 hash of each file
      - create a dictionary entry where:
        key   = md5 hash
        value = filepath
    d) Tterate through the dictionary
       - print out each key, value pair
    
3) Submit
   NamingConvention: lastNameFirstInitial_Assignment_.ext
   for example:  hosmerC_WK1_script.py
                 hosmerC_WK1_screenshot.jpg
   A) Screenshot of the results in WingIDE
   B) Your Script
'''
import os
import hashlib

directory = "."

fileList   = []
fileHashes = {}

for root, dirs, files in os.walk(directory):
    # Walk the path from top to bottom.
    # For each file obtain the filename 

    for fileName in files:
        path = os.path.join(root, fileName)
        fullPath = os.path.abspath(path)
        # a) 
        fileList.append(fullPath)
        # c) key = md5 hash
        key = hashlib.md5(fileName.encode())
        # c) value = filepath
        value = fullPath
        entry = {
            key : value
        }
        fileHashes.update(entry)


for eaHash, eaPath in fileHashes.items():
    print(f"Hash: {eaHash.hexdigest()}")
    print(f"FilePath: {eaPath}")
        
