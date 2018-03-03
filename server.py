from flask import Flask
app = Flask(__name__)

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
    return "{}".format(ip)

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3306)