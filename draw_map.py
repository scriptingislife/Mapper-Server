import folium
import db_helper as database
import geo_helper as geo
import server_vars

MARKER_RADIUS = 7
db, curs = database.connect()

#
# Main map function. Draw all maps.
#
def draw():
    
    markers_map = folium.Map(location=[24.635246, 2.616971], zoom_start=3, tiles='CartoDB dark_matter')
    #folium_heatmap = folium.Map(location=[24.635246, 2.616971], zoom_start=3, tiles='CartoDB positron')
    
    curs.execute("SELECT ip from log_mapper.markers;")
    list_ips = curs.fetchall()
    for ip_tup in list_ips:
        if ip_tup[0] is None:
            continue
        try:
            make_marker(markers_map, str(ip_tup[0]))
        except:
            print("[*] Error with IP: {}".format(ip_tup[0]))

    markers_map.save(server_vars.MAP_LOCATION)
    
    
#
# Add a marker to a Folium map object
#
def make_marker(map_obj, ip):
    print("Making marker for: {}".format(ip))
    
    marker = geo.lookup(ip)
    if marker is None:
        return None
        
    success = database.get_success(db, curs, ip)
    if success is None:
        success = "Unknown"
    elif success == 0:
        success = "Failed"
    elif success == 1:
        success = "Successful"
    else:
        success = "Unknown"
    
    popup_text = """<a href=\"https://www.shodan.io/host/{}\" target=\"_blank\">{}</a><br>
                Success: {}<br>
                Country: {}<br>
                Continent: {}<br>
                Latitude: {}<br>
                Longitude: {}<br>"""
    
    # TODO: Print debug message if a field in marker is None            
    
    popup_text = popup_text.format(ip, ip, success, marker.country, marker.continent, marker.location[0], marker.location[1])
    
    marker_color = database.get_color(db, curs, ip)
    
    folium.CircleMarker(location=marker.location, radius=MARKER_RADIUS, color=marker_color, fill=False, popup=popup_text).add_to(map_obj)

if __name__ == '__main__':
    draw()