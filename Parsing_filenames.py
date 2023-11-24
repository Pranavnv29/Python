#Importing OS Module
import os

#Changing the directory to where our file(to be parsed) present
os.chdir('/Users/Pranav/OneDrive/Desktop/Python_test/Python/Folder #2- File 1')
#To check the file
# print(os.getcwd)

for f in os.listdir():
    file_name = f
    #Creating f_rnmae(realname) and f_num to get the number and real file nmae
    f_rname, f_num = file_name.split('#')
    #creating f_rnum(real number format without .txt) and f_format(txt)
    f_rnum, f_format=f_num.split('.')
    #Using placeholders to rearragene the order with specific format
    new_name='{}-{}.{}'.format(f_rnum, f_rname, f_format)
    #Renaming the each files 
    os.rename(f,new_name)
