#
# Flask server for frontend.
# Author: N. Beckstead
# TODO: Implement API
# TODO: Display maps
# TODO: Get statistics
# TODO: Interactive search.
#

from flask import Flask
#from flask.ext.jsonpify import jsonify

import db_helper as database
import shodan_helper as sh

app = Flask(__name__)

db, curs = database.connect()

@app.route('/')
def hello():
    return "Hello, world!"
    
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
    
@app.route('/ip/<ip>')
def address(ip):
    return sh.lookup_host(str(ip))

    
@app.route('/color/<ip>')
def starred(ip):
    marker_color = database.get_color(db, curs, ip)
    return '<html><body style="background:{};"></body></html>'.format(marker_color)
    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3306)