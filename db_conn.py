import MySQLdb

DB_CONN_LOCAL = MySQLdb.connect(host="localhost",
                        user="sportbets",
                        passwd="sportbets",
                        db="sportbets_db",
                        use_unicode=True, charset="utf8")

DB_CONN_SERVER = MySQLdb.connect(host="localhost",
                        user="admin_sportbets",
                        passwd="OCdLAyyFzK",
                        db="admin_sportbets_db",
                        use_unicode=True, charset="utf8")

DB_CONN = DB_CONN_LOCAL

