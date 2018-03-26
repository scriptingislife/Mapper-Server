#
# Flask server for frontend.
# Author: N. Beckstead
# TODO: Implement API
# TODO: Display maps
# TODO: Get statistics
# TODO: Interactive search.
# TODO: Implement render_template instead of send_from_directory
#

from flask import Flask, send_from_directory
#from flask.ext.jsonpify import jsonify
import folium

import server_vars
import db_helper as database
import geo_helper as geo
import shodan_helper as sh

app = Flask(__name__)

db, curs = database.connect()
    
##################### API #####################
    
@app.route('/api/ip/<ip>')
def api_ip(ip):
    return "{}".format(ip)
    
@app.route('/api/country/<country>')
def api_country(country):
    return "{}".format(country)
    
@app.route('/api/service/<service>')
def api_service(service):
    return "{}".format(service)
    
@app.route('/api/port/<port>')
def api_port(port):
    return "{}".format(port)
    
@app.route('/api/recent/<num>')
def api_recent(num):
    recents = database.get_recent(db, curs, num)
    ret_str = ""
    for row in recents:
        ret_str += str(row)
        ret_str += '<br>'
    return ret_str
    
    
@app.route('/api/stats/totals')
def api_totals():
    total_attempts = database.get_total_attempts(db, curs)
    total_ips = database.get_total_ips(db, curs)
    return "Total Attempts: {}<br>Total IPs: {}".format(total_attempts, total_ips)


@app.route('/api/stats/total-attempts')
def api_totalattempts():
    return str(database.get_total_attempts(db, curs))

@app.route('/api/stats/total-ips')
def apt_totalips():
    return str(database.get_total_ips(db, curs))


##################### PAGES #####################

@app.route('/')
def index():
    return send_from_directory('res/html', 'index.html')
    
    
@app.route('/ip/<ip>')
def address(ip):
    # Get host info from Shodan
    page = sh.lookup_host(str(ip))
    
    # Add interactive map
    lat, lon = geo.get_coordinates(str(ip))
    ip_map = folium.Map(location=[lat, lon], zoom_start=10, tiles='CartoDB positron')
    folium.Marker(location=(lat, lon)).add_to(ip_map)
    #page += "<iframe style=\"height:20%; width:20%;\">"
    page += str(ip_map.get_root().render())
    #page += "</iframe>"
    return page

    
@app.route('/color/<ip>')
def starred(ip):
    marker_color = database.get_color(db, curs, ip)
    return '<html><body style="background:{};"></body></html>'.format(marker_color)
    
@app.route('/recent/')
def recent():
    return send_from_directory('res/html', 'recent.html')
    
##################### RESOURCES #####################

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('res/img', 'favicon.ico')

@app.route('/res/img/<image>')
def return_img(image):
    return send_from_directory('res/img', image)

@app.route('/res/html/maps/<getmap>')
def return_map(getmap):
    return send_from_directory(server_vars.MAP_DIRECTORY, getmap)

##################### ERRORS #####################
@app.errorhandler(404)
def page_not_found(e):
    return send_from_directory('res/html/errors', '404.html'), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3306)