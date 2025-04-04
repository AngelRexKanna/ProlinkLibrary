import os
import shutil
from dotenv import dotenv_values

class DirectoryLibrary:
    def __init__(self):   
        secrets= dotenv_values (".env")     
        os.chdir(secrets["PATH"])

    # Create folders (directories)
    # Create directories if they don't exist
    def create_folder(self, folder_name):    
       try:
           os.makedirs(folder_name, exist_ok=False)
           return f"Folder- {folder_name} created here {os.getcwd()}"
       except FileExistsError:
           return f"Folder- {folder_name} already exists here {os.getcwd()}"
       
    def copy_files(self, source, destination_folder, filename):
        word= "already exists"
        response= self.create_folder(destination_folder)
        #check if folder exists, if yes set the path and copy the file
        index=0
        result=[]
        for file in filename:
            if word in response:
                main_path= os.getcwd()
                destination=os.path.join(main_path, destination_folder, file)
                if os.path.exists(destination):
                    index+=1
                    result.append (f"The file {file} already exists. Can't overwrite")
                else:
                    shutil.copyfile(source[index], destination)
                    index+=1
                    result.append(f"The file {file} copied to {destination}") 
                    
        #if folder not found, a new folder is created and the file is copied
            else:
                main_path= os.getcwd()
                destination=os.path.join(main_path, destination_folder, file)
                if os.path.exists(destination):
                    index+=1
                    result.append (f"The file {file} already exists. Can't overwrite")
                else:
                    shutil.copyfile(source[index], destination)
                    index+=1
                    result.append (f"The file {file} copied to {destination}")
        return result
            
    
    def move_files(self, source, destination_folder, filename):
        word= "already exists"
        response= self.create_folder(destination_folder)
        index=0
        result=[]
        #check if folder exists, if yes set the path and move the file
        for file in filename:
            if word in response:
                main_path= os.getcwd()
                destination=os.path.join(main_path, destination_folder, file)
                if os.path.exists(destination):
                    index+=1
                    result.append (f"The file {file} already exists {destination} \nCan't overwrite")
                else:
                    shutil.move(source[index], destination)
                    index+=1
                    result.append (f"The file {file} moved to {destination}")
        #if folder not found, a new folder is created and the file is moved
            else:
                main_path= os.getcwd()
                destination=os.path.join(main_path, destination_folder, file)
                if os.path.exists(destination):
                    index+=1
                    result.append (f"The file {file} already exists here {destination} \nCan't overwrite")
                else:
                    shutil.move(source[index], destination)
                    index+=1
                    result.append (f"The file {file} moved to {destination}")
        return result
    
    def is_directory(self, folder_name):
        main_path= os.getcwd()
        destination=os.path.join(main_path, folder_name)        
        result= os.path.isdir(destination)
        if result== True:
            return (f"{folder_name} is a directory found here {destination}")
        else:
            return (f"{folder_name} is not a directory")

    def list_directory(self, folder_name):
        main_path= os.getcwd()
        destination=os.path.join(main_path, folder_name)
        os.chdir(destination)
        result= os.listdir()
        os.chdir(main_path)
        return result
    
    def remove_files(self, folder_name, file_list ):
        result=[]
        for file in file_list:
            main_path= os.getcwd()
            destination=os.path.join(main_path, folder_name, file)
            try: 
                os.remove(destination)
                os.chdir(main_path)
                result.append (f"File {destination} deleted successfully")
            except FileNotFoundError:
                os.chdir(main_path)
                result.append (f"File {destination} not found")
        return result


    
    
