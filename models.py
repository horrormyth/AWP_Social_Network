__author__ = 'devndraghimire'

import datetime
from flask.ext.bcrypt import generate_password_hash
from flask.ext.login import UserMixin
from peewee import *


DATABASE = SqliteDatabase('awp_social.db') #Database

class User (UserMixin, Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField(max_length=100)
    joined_at = DateTimeField(default=datetime.datetime.now)
    is_admin = BooleanField(default=False)

    class Meta:
        database = DATABASE
        order_by =('-joined_at',) #DESCENDING DISPLAY OF THE USERS

    @classmethod  #it will create the user model instance when it runs the method
    def create_users(cls, username, email, password,admin=False):
        try:
            cls.create(
                username=username,
                password=generate_password_hash(password),
                is_admin =admin
            )
        except IntegrityError:
            raise ValueError('User Already Exists')

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User],safe=True)
    DATABASE.close()