import pymysql

connection = pymysql.connect(
    host        = 'localhost',      
    user        = 'root',
    password    = '',
    db          = 'recordDB',
)




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

    
AddEmployee()