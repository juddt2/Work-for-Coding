#!/usr/bin/env python
# coding: utf-8

# In[4]:


import sqlite3
def create_database():
    # connect to sqlite database
    connection=sqlite3.connect('phonebook.db')
    cursor=connection.cursor()
    
   # check if table exists
    cursor.execute('SELECT name FROM sqlite_master WHERE type="table" AND name="Entries"')
    table_exists=cursor.fetchone()





    # if table doesnt exist, create it
    if not table_exists:
        cursor.execute('''
            CREATE TABLE Entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT NOT NULL, 
            phone_number TEXT NOT NULL
            )
        ''')
    
    # commit changes
    connection.commit()
    connection.close()
    
# create add entry function
def add_entry(name,phone_number):
    connection=sqlite3.connect('phonebook.db')
    cursor=connection.cursor()
    
    # insert a new entry into entries table
    cursor.execute('''
        INSERT INTO ENTRIES (name,phone_number)
        VALUES (?,?)
    ''', (name,phone_number))
    
     # commit changes
    connection.commit()
    connection.close()
    
# create funtion to lookup name
def lookup_name(name):
    connection=sqlite3.connect('phonebook.db')
    cursor=connection.cursor()
    
    # look up persons phone number by name
    cursor.execute('''
        SELECT phone_number FROM ENTRIES WHERE name=?
    ''',(name,))
    result=cursor.fetchone()
    
    # close
    connection.close()
    
    # let user know if entry is not found
    if result:
        return result[0]
    else:
        return 'Entry not found'
    
# create funtion to update entry
def update_entry(name,new_phone_number):
    connection=sqlite3.connect('phonebook.db')
    cursor=connection.cursor()
    
    # update a persons phone number by name
    cursor.execute('''
        UPDATE ENTRIES SET phone_number=? WHERE name=?
        ''',(new_phone_number,name))
    
    # commit changes and close
    connection.commit()
    connection.close()
    
# create funtion to delete entry
def delete_entry(name):
    connection=sqlite3.connect('phonebook.db')
    cursor=connection.cursor()
    
    # delete a certain row by name
    cursor.execute('''
        DELETE FROM ENTRIES WHERE name=?
        ''',(name,))
    
     # commit changes and close
    connection.commit()
    connection.close()


# In[5]:


import sys
print(sys.path)


# In[ ]:




