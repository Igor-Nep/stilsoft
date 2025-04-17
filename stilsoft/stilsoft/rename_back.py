import os

old_name = ('python_for_work_otspo')
FindFileStr = ('python_for_work_otspo')
new_name = ('Steam')

def rename_back():
    for rootdir, dirs, files in os.walk('C:/'):
            
        for file in files:
            finds = file.lower()
            if(finds.find(old_name.lower()) != -1):
                try:
                    os.rename(os.path.join(rootdir,file), os.path.join(rootdir,file.replace(FindFileStr, new_name)))
                    
                except Exception:
                    print('хз')    
        for dird in dirs:
            finds = dird.lower()
            if(finds.find(old_name.lower()) != -1):
                try:
                    os.rename(os.path.join(rootdir,dird), os.path.join(rootdir,dird.replace(FindFileStr, new_name)))
                    
                except Exception:
                    print('хз')    
                    


rename_back() 