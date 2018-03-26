#
# Look up shodan.io data for an IP address
# Author: N. Beckstead
# TODO: Handle None returns
#
import shodan
from server_vars import SHODAN_KEY

api = shodan.Shodan(SHODAN_KEY)

def lookup_host(ip):
    try:
        host = api.host(ip)
    except shodan.APIError:
        return "API Error"
        
    rt_string =  """
        <strong>IP: {}</strong>
        Organization: {}
        Operating System: {}
    """.format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a'))
    
    for item in host['data']:
            rt_string += """
                    <strong>Port: {}</strong>
                    <strong>Banner:</strong> {}\n\n
    
            """.format(item['port'], item['data'])
    rt_string = rt_string.replace('\n', '<br>')

    return rt_string
    
def get_coordinates(ip):
    lat = None
    lon = None
    try:
        host = api.host(ip)
    except shodan.APIError:
        return None
    for item in host['data']:
        lat = item['latitude']
        lon = item['longitude']
    return (lat, lon)