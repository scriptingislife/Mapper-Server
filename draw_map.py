#
# Draw maps using Folium and write to an html file.
# Author: N. Beckstead
#
# TODO: Debug when a marker field is None.
# TODO: Draw heatmap using log_mapper.attempts table.
# TODO: Optimize by looking up geo data first. Then call make_marker()
#

import folium
from folium import plugins
import db_helper as database
import geo_helper as geo
import server_vars

MARKER_RADIUS = 4
db, curs = database.connect()


#
# Main map function. Draw all maps.
#
def draw():
    
    markers_map = folium.Map(location=[24.635246, 2.616971], zoom_start=3, tiles='CartoDB dark_matter')
    heatmap = folium.Map(location=[24.635246, 2.616971], zoom_start=3, tiles='CartoDB positron')
    

    markers_map = make_markersmap(markers_map)
    markers_map.save(server_vars.MAP_LOCATION)
    
    heatmap = make_heatmap(heatmap)
    heatmap.save(server_vars.HEATMAP_LOCATION)
    
    
#
# Produce a heatmap from all attempts
#
def make_heatmap(map_obj):
    curs.execute("SELECT ip FROM markers ORDER BY INET_ATON(ip);")
    addresses = [ip[0] for ip in curs.fetchall()]
    points = list()
    max_attempts = "0.0.0.0", 0
    for ip in addresses:
        curs.execute("SELECT COUNT(stamp) FROM attempts WHERE ip='{}'".format(ip))
        attempts = int(curs.fetchone()[0])
        marker = geo.lookup(ip)
        if marker is None or marker.location is None:
            print("Error with {}:{}".format(ip, attempts))
            continue
       # print("Adding {}:{} to map.".format(ip, attempts))
        if attempts > max_attempts[1]:
            max_attempts = (ip, attempts)
        #folium.CircleMarker(location=marker.location, radius=1, color=server_vars.COL_DEFAULT, fill=True).add_to(map_obj)
        points.append([marker.location[0], marker.location[1], attempts])
    folium.plugins.HeatMap(points, radius=12).add_to(map_obj)
    print("Max attempts: {}:{}".format(max_attempts[0], max_attempts[1]))
    return map_obj
    
    
#
# Function to make a map with circle markers.
#
def make_markersmap(map_obj):
    curs.execute("SELECT ip from log_mapper.markers ORDER BY INET_ATON(ip);")# ip ASC;")
    list_ips = curs.fetchall()
    for ip_tup in list_ips:
        if ip_tup[0] is None:
            continue
        try:
            make_marker(map_obj, str(ip_tup[0]))
        except:
            print("[*] Error with IP: {}".format(ip_tup[0]))
    return map_obj
    
    
#
# Add a marker to a Folium map object
#
def make_marker(map_obj, ip):
    #print("Making marker for: {}".format(ip))
    
    marker = geo.lookup(ip)
    if marker is None:
        return None
        
    host = database.get_sensor(db, curs, ip)
        
    success = database.get_success(db, curs, ip)
    if success is None:
        success = "Unknown"
    elif success == 0:
        success = "Failed"
    elif success == 1:
        success = "Successful"
    else:
        success = "Unknown"
    
   # popup_text = """<a href=\"https://www.shodan.io/host/{}\" target=\"_blank\">{}</a><br>
    popup_text = """<a href=\"{}\" target=\"_blank\">{}</a><br>
                Sensor: {}<br>
                Success: {}<br>
                Country: {}<br>
                Continent: {}<br>
                Latitude: {}<br>
                Longitude: {}<br>
                <a href=\"https://shodan.io/host/{}\" target=\"_blank\">Shodan</a><br>
                <a href=\"https://www.censys.io/ipv4/{}\" target=\"_blank\">Censys</a><br>
                """
    
    # TODO: Print debug message if a field in marker is None
    popup_text = popup_text.format(server_vars.POPUP_URL.format(ip), ip, host, success, marker.country, marker.continent, marker.location[0], marker.location[1], ip, ip)
    
    marker_color = database.get_color(db, curs, ip)
    
    folium.CircleMarker(location=marker.location, radius=MARKER_RADIUS, color=marker_color, fill=False, popup=popup_text).add_to(map_obj)

if __name__ == '__main__':
    draw()