import sqlite3
def create_db():
    con=sqlite3.connect(database=r'ims.db')
    cur=con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS employee(
        Emp-ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Email TEXT NOT NULL,
        Gender TEXT NOT NULL,
        Contact TEXT NOT NULL,
        DOB TEXT NOT NULL,
        DOJ TEXT NOT NULL,
        Password TEXT NOT NULL,
        UserType TEXT NOT NULL,
        Address TEXT NOT NULL,
        Salary TEXT NOT NULL
    )''')
    con.commit()
              
create_db()