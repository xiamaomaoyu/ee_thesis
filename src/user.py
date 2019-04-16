from flask_login import UserMixin
from src.dbHandler import execute_db


class User(UserMixin):

    def __init__(self, form):
        self.id = form["username"]
        self.password = form["password"]
        self.city = form["city"]
        self.state = form["state"]

    def addUser(self):
        sql = """
              INSERT INTO user(username,password,
              city,state) VALUES (?,?,?,?)
              """
        args = (self.id,self.password,self.city,self.state)
        execute_db(sql, args)