import mysql.connector as msc

mydb = msc.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'week53'
            )
        
mycursor = mydb.cursor()

def write_fun(name_e,place_e,age_e):
    
    sqlCommand = 'INSERT INTO results (name,placeOfBirth,age) VALUES (%s,%s,%s)'
    values = (name_e,place_e,age_e)
    mycursor.execute(sqlCommand,values)
    mydb.commit()