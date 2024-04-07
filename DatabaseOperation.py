import mysql.connector
from odd import window_english
from profile_english import save_profile

class DBOperation():
    def __init__(self):
        try:
            self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="vaishnavi@123",
                database="user_info"
            )
            if self.mydb.is_connected():
                print("Connection successful")
        except mysql.connector.Error as e:
            print("Error connecting to MySQL:", e)

    def CreateTables(self):
        cursor = self.mydb.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS info (id INT AUTO_INCREMENT PRIMARY KEY, name_var VARCHAR(30), age_var INT(100), phone_var INT(10))")
        cursor.close()

    def InsertOneTimeData(self, name, age, phone):
        cursor = self.mydb.cursor()
        sql = "INSERT INTO info (name_var, age_var, phone_var) VALUES (%s, %s, %s)"
        values = (name, age, phone)
        cursor.execute(sql, values)
        self.mydb.commit()
        cursor.close()

# Assuming you have tkinter StringVar variables defined
name_var = name.get()
age_var = age.get()
phone_var = phone.get()

db_operation = DBOperation()
db_operation.CreateTables()
db_operation.InsertOneTimeData(name_var, age_var, phone_var)
