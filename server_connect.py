import mysql.connector
from flask import make_response
import bleach

class User_model():
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="localhost", user="root", database="test")
            self.con.autocommit = True
            self.cur = self.con.cursor(dictionary=True)
            print("Connected Successfully")
        except:
            print("Error!")


    def server_upload(self, datas):
        name = bleach.clean(datas.name.data)
        email = bleach.clean(datas.e_mail.data)
        phone = datas.phone.data
        pasw = datas.pasw.data
        gender = datas.gender.data

        sql = """ INSERT INTO users (name, email, pasw, gender, phone) VALUES (%s, %s, %s, %s, %s) """

        self.cur.execute(sql,(name, email, pasw, gender, phone))
        self.con.commit()

        

    

