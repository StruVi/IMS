import sqlite3
def create_db():
    con=sqlite3.connect(database='ims.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT,Name text,Email text,Gender text,Contact text,dob text,doj text,Password text,utype text,Address text,Salary text)")
    con.commit()
              
create_db()