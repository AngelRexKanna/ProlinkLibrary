from fileSystem import DirectoryLibrary

file_sys= DirectoryLibrary()

# create
folder_name="PBNet_Files"
print(f"TEST- CREATE FOLDER {folder_name}", end='\n')
response= file_sys.create_folder(folder_name)
print (response)

# copy_files function requires parameters in this order
# 1. Array- full path of the source file with filename and extension like this C:/Users/PROLINK Staff/Downloads/HUBSPOT/firstname-.txt
# 2. destination folder name (if not exists- a new folder is created)
# 3. Array-filename with extension
folder_name="Angel1"
filepath_list=["C:/Users/PROLINK Staff/Downloads/HUBSPOT/uploadFile.txt", "C:/Users/PROLINK Staff/Downloads/HUBSPOT/Untitled.png"]
filename_list=["uploadFile.txt", "Untitled.png"]
print(f"TEST- COPY FILES {filename_list} to {folder_name}", end='\n')
response= file_sys.copy_files(filepath_list, folder_name, filename_list)
print (response)

# move_files function requires parameters in this order
# 1. Array- full path of the source file with filename and extension like this C:/Users/PROLINK Staff/Downloads/HUBSPOT/firstname-.txt
# 2. destination folder name (if not exists- a new folder is created)
# 3. Array- filename with extension
folder_name= "Angel2"
filepath_list=["C:/Users/PROLINK Staff/Downloads/HUBSPOT/test1.txt", "C:/Users/PROLINK Staff/Downloads/HUBSPOT/test2.txt"]
filename_list=["test1.txt", "test2.txt"]
print(f"TEST- Move FILES {filename_list} to {folder_name}", end='\n')
response= file_sys.move_files(filepath_list, folder_name , filename_list)
print (response)

folder_name="Angel1"
print(f"TEST- IS {folder_name} A DIRECTORY", end='\n')

print(file_sys.is_directory(folder_name))

folder_name="Angel1"
print(f"TEST- LIST ALL FILES FROM {folder_name} DIRECTORY", end='\n')
print(file_sys.list_directory(folder_name))

# remove_files function requires parameters in this order
# 1. destination folder name 
# 2. Array- filename with extension
folder_name="Angel2"
filename_list=["test1.txt", "test2.txt"]
print(f"TEST- FILES {filename_list} removed from {folder_name} DIRECTORY", end='\n')
response= file_sys.remove_files(folder_name, filename_list)
print (response)