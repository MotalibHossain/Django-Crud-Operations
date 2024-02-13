from DBConnect import connection
import pandas as pd
from tabulate import tabulate


""" Inserting Record in Database"""
def AddEmployee():
    with connection.cursor() as cursor:
        sql = "INSERT INTO `employee` (`emp_id`, `name`, `gender`, `address`, `birthdate`, `birthplace`, `status`) VALUES (Null, %s, %s, %s, %s, %s, %s);"
        print(cursor, sql)
        try:
            cursor.execute(sql, ('Motalib', "male", "dhaka", "08.08.1900", "rangpur", "unmarried"))
            print("New Record Successfully Added!")
        except Exception as e:
            print("Fail to add data.", e)

    connection.commit()

def ShowEmployeeData():
    sql = "SELECT * FROM `employee`"

    with connection.cursor() as cursore:
        try:
            cursore.execute(sql);
            result=cursore.fetchall();
            df = pd.DataFrame(result)
            table = tabulate(df, headers='keys', tablefmt='grid', showindex=False)
            print(table)
            # print("Successfully show all data", result)
        except Exception as e:
            print("Fail to show data.", e)



    connection.commit()
        

    
AddEmployee()
ShowEmployeeData()