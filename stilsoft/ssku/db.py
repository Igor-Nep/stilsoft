from sqlalchemy import create_engine 

class DbSsku:
    '''
    удалить все архивные модули - del_archived_modules\n
    получить все подключенные и не удаленные модули - get_not_archived_modules\n
    получить количество модулей по типам: все / подключенные / архивные - get_modules_count\n
    записать ID всех заведенных модулей в файл (kill_modules_ssku) - write_not_archived_modules\n
    запись ID всех заведенных модулей с последующим их удалением - archive_and_del_all_modules\n
    запись ID всех заведенных модулей с передачей названия файла - archive_all_modules
    '''

    def __init__(self, ip):
        self.ip = ip
        db_connection_string = f"postgresql+psycopg2://postgres:postgrespassword@{self.ip}:5432/postgres"
        self.db = create_engine(db_connection_string)


    def get_not_archived_modules(self):
        rows = self.db.execute(f"select * from system.module where archived=false").fetchall()
        return rows
    

    def get_modules_count(self,type) -> str:
        '''принимает type ("all" / "archived" / "not_archived")'''
        if type == 'all':
            count_all = self.db.execute("select * from system.module").fetchall()
            return len(count_all)
        elif type == 'archived':
            count_archived = self.db.execute("select * from system.module where archived=true").fetchall()
            return len(count_archived)
        elif type == 'not_archived':
            count_not_archived = self.db.execute("select * from system.module where archived=false").fetchall()
            return len(count_not_archived)
        elif type != 'all' and type != 'archived' and type != 'not archived':
            return 'ERROR! Not supprted type'
    

    def del_archived_modules(self):
        count = self.db.execute("select * from system.module where archived=true").fetchall()
        self.db.execute("delete from system.module where archived=true")
        return len(count)


    def write_not_archived_modules(self, file):
        from datetime import datetime
        rows = self.get_not_archived_modules()
        with open(f'D:\work\WHPython\stilsoft\ssku\deleted_modules\{file}', 'w') as file:
            for i in range(len(rows)):
                file.write(str(rows[i]['id'])+'\n')
        with open(f'D:\work\WHPython\stilsoft\ssku\deleted_modules\list_data_files.txt', 'a') as file:
            file.write(f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")} - {file}\n')


    def print_not_archived_modules(self):
        rows = self.get_not_archived_modules()
        for i in range(len(rows)):
                print((str(rows[i]['id'])+'\n')                )


    def archive_and_del_all_modules(self, file='kill_modules_ssku'):
        self.write_not_archived_modules(file)
        self.db.execute(f"update system.module set archived=true WHERE archived=false")


    def get_module_name_by_id(self, id):
        rows = self.db.execute(f"select * from system.module where archived = false and id = '{id}'").fetchall() 
        return rows[0]['name']


    def archive_and_del_needed_modules(self, from_n, to_n, file_name):
        import sys
        from datetime import datetime
        sys.path.append('D:\work\WHPython\stilsoft')
        from ssku.api import ApiSsku
        for i in range(from_n, to_n):
            name = f'Камера {str(i)}'
            reserved = ApiSsku(self.ip).get_module_by_name(name)
            with open(f'D:/work/WHPython/stilsoft/ssku/reserved/{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_{file_name}', 'a') as file:
                file.write(str(reserved)+'\n')
            self.db.execute(f"update system.module set archived=true WHERE archived=false and name='{name}'")


    def change_arm_type(self, type):
        if type == 'new':
            self.db.execute(f"update security.arm set type='arm-o' WHERE type='arm-cpu'")
            self.db.execute(f"update security.users set role='operator-o' WHERE role='operator-cpu'")
            self.db.execute(f"update security.role set name='operator-o' WHERE name='operator-cpu'")
            self.db.execute(f"update security.role set type_arm='arm-o' WHERE type_arm='arm-cpu'")
        elif type =='old':
            self.db.execute(f"update security.arm set type='arm-cpu' WHERE type='arm-o'")
            self.db.execute(f"update security.users set role='operator-cpu' WHERE role='operator-o'")
            self.db.execute(f"update security.role set name='operator-cpu' WHERE name='operator-o'")
            self.db.execute(f"update security.role set type_arm='arm-cpu' WHERE type_arm='arm-o'")
        else:
            print("'wrong type: need 'old' or 'new'")    




    def reset_needed_modules(self,from_n, to_n):

        for i in range(from_n, to_n):
            name = f'Камера {str(i)}'
            try:
                self.db.execute(f"update system.module set archived=false WHERE archived=true and name='{name}'")            
            except Exception as err:
                print(f'{err} - {name}')
                pass



    def archive_all_modules(self, file='archived_modules'):
        '''возможно передать название файла как параметр'''
        self.write_not_archived_modules(file)
        return file
        

    def reset_archived_modules(self,file):
        import os
        with open(f'D:\work\WHPython\stilsoft\ssku\deleted_modules\{file}', 'r', encoding='utf-8') as file:
            massive = file.read().split('\n')
            for row in massive:
                if row.split() != []:
                    self.db.execute(f"update system.module set archived=false where id='{row}'")
        delete = input('Удалить список восстановления y/n: ')
        if delete == 'y':         
            if os.path.exists(f'D:\work\WHPython\stilsoft\ssku\deleted_modules\{file}'):
                os.remove(f'D:\work\WHPython\stilsoft\ssku\deleted_modules\{file}')


    def get_user_id_by_login(self, login):
        rows = self.db.execute(f"select * from security.users where login='{login}'").fetchall()
        return rows[0]['id']
    
    def get_user_hash_by_name(self, name):
        rows = self.db.execute(f"select * from security.arm where name='{name}'").fetchall()
        return rows[0]['hash']


    def get_user_login_by_id(self, id):
        rows = self.db.execute(f"select * from security.users where id='{id}'").fetchall()
        return rows[0]['login']


    def get_user_argon_password(self, id):
        rows = self.db.execute(f"select * from security.users where id='{id}'").fetchall()
        return rows[0]['password']
                           
    
    def change_password(self, login, new_password):
        from time import sleep
        import sys
        print(login+ ' login')
        print(new_password+' new_password')
        sys.path.append('D:\work\WHPython\stilsoft')
        from murom.api import ApiMurom
        apim = ApiMurom('https://gate.synerget.ru:8179')
        print('apiMurom >')
        apim.add_user(login, login, new_password)
        print('add user is ok')
        from murom.db import DbMurom
        dbm = DbMurom('192.168.202.30')
        print('dbMurom')
        changed_password = dbm.get_user_argon_password(dbm.get_user_id_by_login(login))
        sleep(1)
        self.db.execute(f"update security.users set password='{changed_password}' where login='{login}'")
        apim.del_user_by_id(dbm.get_user_id_by_login(login))


    def get_rows_in_massive(self,select):
        sorted_list=[]
        rows = self.db.execute(select).fetchall()
        row_list = [row[0] for row in rows]
        print(set(row_list))
