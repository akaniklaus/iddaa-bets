import MySQLdb
from sqlalchemy import *

DB_CONN = MySQLdb.connect(host="localhost",
                        user="sportbets",
                        passwd="sportbets",
                        db="sportbets_db",
                        use_unicode=True, charset="utf8")

SQL_ALCHEMY_ENGINE = create_engine("mysql+mysqldb://sportbets:sportbets@localhost/sportbets_db?charset=utf8&use_unicode=1")
