import os
import shutil

# ##<<------Dir we are goin to managing--------->>## #
dirs = "c:/users/bhuva/downloads"
os.chdir(dirs) # os.chdir() will change the current working dir.

# ##<<------Getting all the files in the current working dir--------->>## #
listdir = os.listdir() # os.listdir() // will return all the files and folders in current woking directory.

# Create a Empty list :- cause we are going extract all the files and folders in cwd, and split the extention from the file and then we store it in set datatype.
folder_name = set() # Unchagable, unorder, no-duplication allowed.

# ##<<<<<<---- This loop will find extention of available file and store it in the Folder_name set --------------->>>>>>>>######
for i in listdir:
    x = i.rsplit(".",1)
    if len(x) > 1:
        folder_name.add(x[-1]) ##----add() add item to the set.

# ####<<-----------This loop will create a folder if the folder is ot exist----->>###
for x in folder_name:
    if os.path.exists('./'+x):
        pass
    else:
        os.makedirs(x)

# ####<<<<------This loop will move the file to the destination------>>#####
for x in folder_name:
    src = dirs+"/"+str(x)
    for y in listdir:
        file = y.rsplit(".",1)
        if len(file) > 1:
            if str(x) == str(file[-1]):
                shutil.move(file[0]+"."+file[1],src)
               





############<<<<<-----------WHILE CODING THIS PROGRAM---------------->>>>############### 
# os.chdir("D:\CORONA\Python\Modules\BASIC")
# print(folder_path)
# listdir = os.listdir()
# print( os.listdir())
# for i in listdir:
#     print(i)
# print(len(x)," -> ",x[0]+"."+x[1])
# print(file[0]+"."+file[1],"->",str(dirs+"/"+str(x)))
# os.chdir(dirs,"/",x)
# print(str(file[-1]))
# folder_path = os.getcwd()
# for x in folder_name:
#     for y in listdir:
#         file = y.rsplit(".",1)
#         if len(file) > 1:
#             if str(x) == str(file[-1]):
#                 pass
                