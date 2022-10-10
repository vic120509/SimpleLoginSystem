import sqlite3
import sys
sys.setrecursionlimit(2000)



def open_db():
    # create  a connection to the database
    global conn
    conn = sqlite3.connect('Accounts.db')
    # create  a connection to the database
    global c

    c = conn.cursor()




def close_db():
    c.close()
    conn.close()


def create_table():
    open_db()

    c.execute('''

    CREATE TABLE IF NOT EXISTS Accounts(
        first_name  TEXT,
        last_name TEXT,
        username  TEXT,
        password TEXT,
        date_registered TEXT
    )

    ''')
    close_db()


def register(first, last, username, password, date):
    open_db()

    c.execute('''
    INSERT INTO Accounts VALUES (?,?,?,?,?)


    ''', (first, last, username, password, date))
    conn.commit()
    close_db()



def update_last_name(username, password, new_last):
    open_db()

    c.execute('''

    UPDATE Accounts
    SET last_name = (?)
    WHERE username = (?) AND password = (?)

    ''', (new_last, username, password))

    conn.commit()
    close_db()


def update_first_name(username, password, new_first):
    open_db()

    c.execute('''

    UPDATE Accounts
    SET first_name = (?)
    WHERE username = (?) AND password = (?)

    ''', (new_first, username, password))

    conn.commit()
    close_db()


def get_AccountData(username, password):
    open_db()

    c.execute('''

    SELECT * from Accounts
    WHERE  username = (?) AND password = (?)

    ''', (username, password))
    data = c.fetchone()
    return data


def ShowData(first,last,username, password,date):
    open_db()

    c.execute('''

    SELECT * from Accounts
    WHERE first_name = (?) AND last_name = (?) AND username = (?) AND password = (?) AND date_registered = (?)

    ''', (first_name,last_name,username, password,date_registered))
    data = c.fetchall()
    return data



def update_username(username, password, new_user):
    open_db()

    c.execute('''

    UPDATE Accounts
    SET username = (?)
    WHERE username = (?) AND password = (?)

    ''', (new_user, username, password))

    conn.commit()
    close_db()


def update_password(username, password, new_password):
    open_db()

    c.execute('''

    UPDATE Accounts
    SET password = (?)
    WHERE username = (?) AND password = (?)

    ''', (new_password, username, password))

    conn.commit()
    close_db()

update_password('yana1205','kurt120509','yana123')
def delete_AccountData(username,password):
    open_db()

    c.execute('''

    DELETE FROM Accounts
    WHERE username = (?) AND password = (?) 
    
   
   

    ''',(username,password))

    
    conn.commit
    
    close_db()

def login(username, password):
    open_db()

    c.execute('''

    SELECT * from Accounts
    WHERE username = (?) AND password = (?)

    ''', (username, password))
    data = c.fetchone()
    if data:
        close_db()
        return True
    else:
        close_db()
        return False

    conn.commit()
    close_db()

def search_account(first, last, username, password, date):

    open_db()


    c.execute('''


     SELECT  * FROM Accounts
     WHERE first_name = (?) AND last_name =(?) AND username = (?)AND password = (?) AND date_registered = (?)
   
    


    ''',(first, last, username, password, date))
  
    data= c.fetchall()

    return data


    close_db()

create_table()
# register('Aldai','Villaruel','ald120509','kurt120509','09-20-2022')

update_first_name('ald120509', 'kurt120501', 'Ayana')


