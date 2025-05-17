import mysql.connector
from tkinter import messagebox
def connect_database():
    global mycursor,conn
    try:
        conn=mysql.connector.connect(host='localhost',user='root',password='9435751688')
        mycursor=conn.cursor()
    except:
        messagebox.showerror('Error','Something went wrong,Please open mysql app before running again')
        return

    mycursor.execute('CREATE DATABASE IF NOT EXISTS employee_data')
    mycursor.execute('USE employee_data')
    mycursor.execute('CREATE TABLE IF NOT EXISTS data (Employee_Id VARCHAR(20),Name VARCHAR(50),Phone VARCHAR(15), Role VARCHAR(50), Gender VARCHAR(20), Salary DECIMAL(10,2))')




def insert(employee_id,name,phone,role,gender,salary):
    mycursor.execute('INSERT INTO data VALUES (%s,%s,%s,%s,%s,%s)',(employee_id,name,phone,role,gender,salary))
    conn.commit()

def id_exists(employee_id):
    mycursor.execute('SELECT COUNT(*) FROM data WHERE employee_id=%s', (employee_id,))
    result=mycursor.fetchone()
    return result[0]>0

def fetch_employees():
    mycursor.execute('SELECT * from data')
    result=mycursor.fetchall()
    return result

def update(employee_id,new_name,new_phone,new_role,new_gender,new_salary):
    mycursor.execute('UPDATE data SET name=%s,phone=%s,role=%s,gender=%s,salary=%s WHERE Employee_id=%s',(new_name,new_phone,new_role,new_gender,new_salary,id))
    conn.commit()

# In database.py

def delete(employee_id):
    mycursor.execute('DELETE FROM data WHERE employee_id=%s', (employee_id,))  # Wrap id in a tuple
    conn.commit()


def search(option,value):
    mycursor.execute(f'SELECT * FROM data WHERE {option}=%s',value)
    result=mycursor.fetchall()
    return result

def deleteall_records():
    mycursor.execute('TRUNCATE TABLE data')
    conn.commit()



connect_database()