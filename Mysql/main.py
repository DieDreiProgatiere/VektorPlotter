from Mysql import connect

conn = Mysql.connect(host="127.0.0.1", user="root", password="rbaron_2", db="vector" )

if conn is None:
    print("Terror")
