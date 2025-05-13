import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    DEBUG = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:hejolena123@book-postgres:5432/booksdb"


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.sqlite')
    DEBUG = True