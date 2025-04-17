from sqlalchemy import create_engine 

class DbMurom:

    def __init__(self, ip):
        self.ip = ip
        db_connection_string = f"postgresql+psycopg2://postgres:postgrespassword@{self.ip}:5432/postgres"
        self.db = create_engine(db_connection_string)


    def get_module_id(self, type):
        rows = self.db.execute(f"select * from system.module where type = '{type}' and archived=false").fetchall()
        return rows[0]['id']
    

    def get_user_id_by_login(self, login):
        rows = self.db.execute(f"select * from security.users where login='{login}'").fetchall()
        return rows[0]['id']


    def get_user_argon_password(self, id):
        rows = self.db.execute(f"SELECT * FROM security.users WHERE id='{id}'").fetchall()
        return rows[0]['password']
           
    
        