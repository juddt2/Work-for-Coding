#!/usr/bin/env python
# coding: utf-8

# I first start by creating the database and connect to sqlite3. I then use the cursor funtion to execute SQL commands and assign it to 'connection'. I then check to see if the table exists so I use the cursor.execute funtion to see if the Entries table already exists. I then create a if function if the table doesnt exist to create the table. I start by using the cursor.execute funtion to create the Entries table. I then need to define the columns of the table so I use a type of INTEGER and use it as the primary key for the table. The PRIMARY KEY will make sure each row has a unique value for its column. I then store name and phone number and make sure it doesnt contain null values. 
# 
# I then need make the add_entries funtion to add a name and number. I use the cursor.execute function insert name and phone number into the table. 
# 
# 
# I then create the lookup_name funtion to look up name. I use SQL SELECT statement to get the phone number and FROM to tell program to look for it in the Entries table. 
# 
# I create the update_entry funtion to update a phone number from name. I use SQL SET statement to assign new_phone_number from phone_number. And use SQL WHERE statement to tell program to assign new_phone_number correlated with the name. I also use name=? as a placeholder. 
# 
# Lastly, I create the delete_entry funtion to delete an entry from the table. I use the SQL DELETE statement to delete an entire entry from the table. 
# 

# In[8]:


import sqlite3

def create_database():
    #connect to sqlite3 database
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
        
# create add entry funtion
def add_entry(name,phone_number):
    connection=sqlite3.connect('phonebook.db')
    cursor=connection.cursor()
    
    # insert a new entry into entries table
    cursor.execute('''
        INSERT INTO Entries (name,phone_number)
        VALUES (?,?)
    ''', (name,phone_number))
    
    # commit changes
    connection.commit()
    

    connection.close()
    print(f"Entry added: Name: {name} Phone Number: {phone_number}")
    
# create funtion to lookup name
def lookup_name(name):
    connection=sqlite3.connect('phonebook.db')
    cursor=connection.cursor()
    
    # look up persons phone number by name
    cursor.execute('''
        SELECT phone_number FROM Entries WHERE name=?
    ''',(name,))
    
    # get the result 
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
        UPDATE Entries SET phone_number=? WHERE name=?
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
        DELETE FROM Entries WHERE name=?
        ''',(name,))
    
    # commit changes and close
    connection.commit()
    connection.close()

    


# In[ ]:




