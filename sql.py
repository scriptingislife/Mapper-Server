#import MySQLdb
import server_vars


def connect():
    pass
 #   return MySQLdb.connect(DB_URL, DB_USER, DB_PASSWD, DB_DATABASE)
    
    
def star_unstar(cursor, ip):
    cursor.execute("SELECT starred FROM markers WHERE ip='{}';".format(ip))
    starred = int(cursor.fetchone()[0])
    print(starred)
    
if __name__ == '__main__':
    db = connect()
    cur = db.cursor()
    star_unstar(cur, '90.188.182.183')