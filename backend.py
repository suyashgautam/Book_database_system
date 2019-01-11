
# coding: utf-8

# In[165]:


import sqlite3


# In[166]:


def viewall():
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("SELECT * from book")
    row=cur.fetchall()
    conn.close()
    return row


# In[167]:


def search_entry(title="",author="",year="",isbn=""):
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    row=cur.execute("SELECT * from book where title=? or author=? or year=? or isbn=?",(title,author,year,isbn))
    row=cur.fetchall()
    conn.close()
    return row


# In[168]:


def add_entry(title,author,year,isbn):
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()


# In[169]:


def updateselected(id,title,author,year,isbn):
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?,author=?,year=?,isbn=? where id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()


# In[170]:


def deleteselected(id):
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()


# In[171]:


def connect():
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY,title TEXT,author TEXT,year INTEGER,isbn INTEGER)")
    conn.commit()
    conn.close()
