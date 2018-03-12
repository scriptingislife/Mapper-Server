#
# Look up shodan.io data for an IP address
# Author: N. Beckstead
# TODO: Everything. Search for all IPs with port, service, etc.
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
        IP: {}
        Organization: {}
        Operating System: {}
    """.format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a'))
    
    for item in host['data']:
            rt_string += """
                    Port: {}
                    Banner: {}
    
            """.format(item['port'], item['data'])

    return rt_string