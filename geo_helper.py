from geoip import geolite2

def lookup(ip):
    return geolite2.lookup(ip)
