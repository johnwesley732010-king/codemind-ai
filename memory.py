import sqlite3
def save_memory(user,msg):
    c=sqlite3.connect("memory.db")
    c.execute("CREATE TABLE IF NOT EXISTS memory(user TEXT,msg TEXT)")
    c.execute("INSERT INTO memory VALUES(?,?)",(user,msg))
    c.commit()
    c.close()
