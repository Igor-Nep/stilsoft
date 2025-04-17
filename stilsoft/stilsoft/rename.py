import os

old_name = (r'Steam.*')
file_str = (r'Steam.*')
new_name = ('python_for_work_otspo')

def rename():
    for rootdir, dirs, files in os.walk('C:/'):
            
        for file in files:
            finds = file.lower()
            if(finds.find(old_name.lower()) != -1):
                try:
                    os.rename(os.path.join(rootdir,file), os.path.join(rootdir,file.replace(file_str, new_name)))
                    
                except Exception:
                    print('хз')    
        for dird in dirs:
            finds = dird.lower()
            if(finds.find(old_name.lower()) != -1):
                try:
                    os.rename(os.path.join(rootdir,dird), os.path.join(rootdir,dird.replace(file_str, new_name)))
                    
                except Exception:
                    print('хз')


rename()                    
old_name = (r'steam.*')
file_str = (r'steam.*')
new_name = ('python_for_work_otspo')

def rename_2():
    for rootdir, dirs, files in os.walk('C:/'):
            
        for file in files:
            finds = file.lower()
            if(finds.find(old_name.lower()) != -1):
                try:
                    os.rename(os.path.join(rootdir,file), os.path.join(rootdir,file.replace(file_str, new_name)))
                    
                except Exception:
                    print('хз')    
        for dird in dirs:
            finds = dird.lower()
            if(finds.find(old_name.lower()) != -1):
                try:
                    os.rename(os.path.join(rootdir,dird), os.path.join(rootdir,dird.replace(file_str, new_name)))
                    
                except Exception:
                    print('хз')                            


rename_2()