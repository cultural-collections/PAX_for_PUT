# Create PAX packages for PUT Tool

The code is looking for a structure where each folder in the given parent folder refers to the lowest level CALM record, and each of those folders contain mixed access and preservation copies to be sorted

The code also creates the structure using hardlinked copies of the files, as to not create complexity in the origigal directories - and also as a failsafe

Example: Defining SB1 as the top directory

![Input Structure](https://i.ibb.co/fSH2q0m/1111.png)

 Becomes
 
![Output Structure](https://i.ibb.co/f2RCjqc/222222.png)
 
# Editing the config file

In the config file, put the path to the top level directory in the top_dir field - it would be \Path\to\SB1 in the above example

And change the .fmt in each of the formats to access and preservation formats, so the above example would be .tif and .jpg

You have the option here to not create use a hardlinked version of the folder structure - but it's reccomended

# Running the code

