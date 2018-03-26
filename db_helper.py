#
# Author: N. Beckstead
# TODO: Clean up checking for NULL values
#
import server_vars
import MySQLdb



#
# Connect to a remote MySQL database given credentials in server_vars.py
#
def connect():
    db = MySQLdb.connect(server_vars.DB_URL, server_vars.DB_USER, server_vars.DB_PASSWD, server_vars.DB_DATABASE)
    cur = db.cursor()
    return (db, cur)

def get_value(db, cursor, table, column, variable, where):
    cursor.execute("SELECT {} FROM {}.{} WHERE {} = '{}';".format(column, server_vars.DB_DATABASE, table, variable, where))
    value = cursor.fetchone()
    if value is None:
        return None
    else:
        value = value[0]
        return int(value)


#
# Get a specified number of recent attempts
# Returns all data about recent attempts
#
def get_recent(db, cursor, num):
    cursor.execute("SELECT * FROM attempts ORDER BY id DESC LIMIT {};".format(num))
    return cursor.fetchall()

#
# Get a sensor name given an IP address.
# Returns 'host' where an IP matches.
#
def get_sensor(db, cursor, ip):
    cursor.execute("SELECT host FROM attempts WHERE ip = '{}';".format(ip))
    host = cursor.fetchone()
    if host is None:
        return None
    else:
        host = host[0]
        if host is None:
            return None
        else:
            return host

#
# Get the success of an IP address
# TODO: Success is in multiple attempts. Compare success:failure ratio maybe.
#
def get_success(db, cursor, ip):
    cursor.execute("SELECT success FROM attempts WHERE ip = '{}';".format(ip))
    success = cursor.fetchone()
    if success is None:
        return None
    else:
        success = success[0]
        if success is None:
            return None
        else:
            return int(success)


#
# Get if an IP is starred or not
# Returns: 1 if starred, 0 if not starred
#
def get_starred(db, cursor, ip):
    cursor.execute("SELECT starred FROM markers WHERE ip='{}';".format(ip))
    starred = cursor.fetchone()
    if starred is None:
        return None
    else:
        starred = starred[0]
    if starred is None:
        return 0
    else:
        return int(starred)


#
# If an IP is starred, unstar it. If an IP is unstarred, star it.
#
def star_unstar(db, cursor, ip):
    starred = get_starred(db, cursor, ip)
    if starred == 1:
        print("{} is starred.".format(ip))
        val = 0
    elif starred == 0:
        print("{} is not starred.".format(ip))
        val = 1
    qry = "UPDATE markers SET starred = '{}' WHERE ip = '{}';".format(val, ip)
    cursor.execute(qry)
    db.commit()
    return cursor


#
# Return the color of the marker depending on success and starred-ness.
# Colors configured in server_vars.py
#
def get_color(db, cursor, ip):
    starred = get_starred(db, cursor, ip)
    if starred:
        return server_vars.COL_STARRED
    else:
        success = get_success(db, cursor, ip)
        if success == 1:
            return server_vars.COL_SUCCESS
        elif success == 0:
            return server_vars.COL_FAILURE
        else:
            return server_vars.COL_DEFAULT


################### STATS ###################

#
# Get total attempts
#
def get_total_attempts(db, cursor):
    cursor.execute("SELECT COUNT(*) FROM attempts;")
    return int(cursor.fetchone()[0])

#
# Get total IP addresses
#
def get_total_ips(db, cursor):
    cursor.execute("SELECT COUNT(ip) FROM markers;")
    return int(cursor.fetchone()[0])

#
# Get IP with most attempts
#

#
# Get country with most attempts
#

#
# 
#

if __name__ == '__main__':
    db, cur = connect()
    print(get_color(db, cur, '90.188.182.183'))
