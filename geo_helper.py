#
# Lookup data using the maxmind geolocation database
# Author: N. Beckstead
# TODO: Add more specialty functions.
#

from geoip import geolite2

def lookup(ip):
    return geolite2.lookup(ip)


def get_coordinates(ip):
    match = lookup(ip)
    if match is None or match.location is None:
        return None
    return (match.location[0], match.location[1])
    