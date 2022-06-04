import mysql.connector
mycon = mysql.connector.connect(host='127.0.0.1', user='root',passwd='',database='BASE1')
mycursor = mycon.cursor()
# mycursor.execute('CREATE DATABASE BASE1')
# mycursor.execute('SHOW DATABASES')
# for x in mycursor:
#     print(x)

# mycursor.execute("CREATE TABLE ADMIN (ctn_id INT(4), Ful_name VARCHAR(30), Phone INT(20), Address VARCHAR(30), Password VARCHAR(15))")
# mycursor.execute("CREATE TABLE USER (ctn_id INT(4), Ful_name VARCHAR(30), Phone INT(20), Address VARCHAR(30), Password VARCHAR(15))") 
# mycursor.execute("ALTER TABLE ADMIN change ctn_id ctn_id INT(4) PRIMARY KEY AUTO_INCREMENT")
# mycursor.execute("ALTER TABLE ADMIN ADD UNIQUE(phone);")
# myquery = "INSERT INTO ADMIN (FUL_name,Phone,Address,Password) VALUES(%s,%s,%s,%s) "
# details = ('Busari Oluwapelumi Hafeez','07068750352','Oluyole extention','Pelumi2000')
# mycursor.execute(myquery,details)
# mycon.commit()


# mycursor.execute("CREATE TABLE USER (ctn_id INT(4), Ful_name VARCHAR(30), Phone VARCHAR(20), Address VARCHAR(30), Password VARCHAR(30))")