import mysql.connector
from datetime import datetime
from connection import connection

class Student:
    connection = connection
    mycursor = connection.cursor()

    def __init__(self, studentNumber,name,surname,birthdate,gender):
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender


    def saveStudent(self):
        sql = "INSERT INTO student (StudentNumber, Name, Surname, Birthdate, Gender) VALUES (%s, %s, %s, %s, %s)"
        value = (self.studentNumber, self.name, self.surname, self.birthdate, self.gender)

        try:
            Student.mycursor.execute(sql, value)
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayıt eklendi.')
        except mysql.connector.Error as err:
            print('Hata:', err)
        finally:
            Student.mycursor.close()


ahmet = Student("106","Ali","Cenk",datetime(2003, 8, 25),"E")
ahmet.saveStudent()


# sql = "INSERT INTO student(StudentNumber, Name, Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)"
# ogrenciler = [
# ("101","Ahmet","Yilmaz",datetime(2005, 5, 17),"E"),
# ("102","Ali","Can",datetime(2005, 6, 17),"E"),
# ("103","Canan","Tan",datetime(2005, 7, 17),"K"),
# ("104","Ayşe","Taner",datetime(2005, 9, 23),"K"),
# ("105","Bahadir","Toksoz",datetime(2004, 7, 27),"E"),
# ("106","Ali","Cenk",datetime(2003, 8, 25),"E")
# ]

# mycursor.executemany(sql, ogrenciler)

# try:
#     connection.commit()
#     print(f'{mycursor.rowcount} tane kayit eklendi.')
# except mysql.connector.Error as err:
#     print('hata:', err)
# finally:
#     connection.close()
