import sqlite3


class Phonebook:
    query = """CREATE TABLE PHONEBOOK(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        FIRSTNAME CHAR(20) NOT NULL, 
        LASTNAME CHAR(20) NOT NULL, 
        ADDRESS CHAR(50), 
        CONTACTNUMBER CHAR(20) )"""
    
    insert = ('INSERT INTO PHONEBOOK (FIRSTNAME,LASTNAME,ADDRESS,CONTACTNUMBER) '
         'VALUES (:FIRSTNAME, :LASTNAME, :ADDRESS, :CONTACTNUMBER);')
        
    def __init__(self):
        self.conn = sqlite3.connect('phonebook.db')
        self.cursor = self.conn.cursor()
        
        self.cursor.execute("DROP TABLE IF EXISTS PHONEBOOK")        
        self.cursor.execute(self.query)       
               
        
    def create(self, fisrtname,lastname,address,contactnumber):
        params = {
        'FIRSTNAME': fisrtname,
        'LASTNAME': lastname,
        'ADDRESS': address,
        'CONTACTNUMBER': contactnumber
        }
        
        print(params)
        self.conn.execute(self.insert, params)    
        self.conn.commit()

    def read(self):        
        cursor = self.conn.execute("SELECT * from PHONEBOOK")
        return cursor.fetchall()

    def update(self, id):
        if id == 0000:
            return True
        
        cursor = self.conn.execute("SELECT * from PHONEBOOK where ID = %s;" % str(id))
        if len(cursor.fetchall()) > 0: 
            
            firstname = input("Type First name : ")
            lastname = input("Type Last name : ")
            address = input("Type Address : ")
            contactnumber = input("Type Contact number : ")
            
            to_set = ""
            if len(firstname) >0:
                to_set = to_set + "'FIRSTNAME' = '%s'" % firstname
                
            if len(lastname) >0:
                to_set = to_set +self.comma(to_set)+ "'LASTNAME' = '%s'" % lastname
                
            if len(address) >0:
                to_set = to_set +self.comma(to_set)+ "'ADDRESS' = '%s'" % address
                
            if len(contactnumber) >0:
                to_set = to_set +self.comma(to_set)+ "'CONTACTNUMBER' = '%s'" % contactnumber
                
            print(to_set)
                
            self.conn.execute("UPDATE PHONEBOOK set %s where ID = %x" % (to_set,id))
            self.conn.commit()  
        else:
            print("Contact Not Found")                  
        return True

    def delete(self, id):
        if id == 0000:
            return True
        
        cursor = self.conn.execute("SELECT * from PHONEBOOK where ID = %s;" % str(id))
        if len(cursor.fetchall()) > 0:
            self.conn.execute("DELETE from PHONEBOOK where ID = %s;" % str(id))
            self.conn.commit()
            print("Contact Deleted")          
        else:
            print("Contact Not Found")        
        return True
    
    def comma(self,text):
        if len(text)>5:
            return " , "
        else:
            return ""

if __name__ == '__main__':
    phonebook = Phonebook()

    while True:
        choice = input("1: Add | 2: Update | 3: Delete | 4: View \n> ")

        if choice == "1":
            firstname = input("Type First name : ")
            lastname = input("Type Last name : ")
            address = input("Type Address : ")
            contactnumber = input("Type Contact number : ")
            phonebook.create(firstname,lastname,address,contactnumber)
            
        elif choice == "2":
            while True:
                try:
                    id = int(input("type Id to update | 0000: to Exit \n>"))
                        
                    result = phonebook.update(id)
                    if result == True:
                        break                
                except:
                    print("Please Type Contact Id \n")
                    False                    
                    
        elif choice == "3":
            while True:
                try:
                    id = int(input("type Id to delete | 0000: to Exit \n>"))
                                            
                    result = phonebook.delete(id)
                    if result == True:
                        break
                except:
                    print("Please Type Contact Id \n")
                    False
                    
        elif choice == "4":
                for data in phonebook.read():
                    print(data)
    
    