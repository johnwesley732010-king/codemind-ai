import sqlite3
def create_user(u,p):
    c=sqlite3.connect("users.db")
    c.execute("CREATE TABLE IF NOT EXISTS users(username TEXT,password TEXT)")
    c.execute("INSERT INTO users VALUES(?,?)",(u,p))
    c.commit()
    c.close()

def login_user(u,p):
    c=sqlite3.connect("users.db")
    r=c.execute("SELECT * FROM users WHERE username=? AND password=?",(u,p)).fetchone()
    c.close()
    return r
