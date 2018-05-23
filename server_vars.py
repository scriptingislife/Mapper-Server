# MySQL database credentials
DB_URL = "mapperdb"
DB_USER = "mapperserver"
DB_PASSWD = "mapperserver"
DB_DATABASE = "log_mapper"

# Marker colors based on attempt result
COL_SUCCESS = "#33CC00"
COL_FAILURE = "#FF0033"
COL_STARRED = "#FFCC33"
COL_DEFAULT = "#0066FF"

# Where map files should be written
HTML_DIRECTORY = "res/html/"
MAP_DIRECTORY = HTML_DIRECTORY + "maps/"
MAP_LOCATION = MAP_DIRECTORY + "markers.html"
HEATMAP_LOCATION = MAP_DIRECTORY + "heatmap.html"

# URL that should be linked on a marker's popup window
# Put {} in place of IP address.
POPUP_URL = "/ip/{}"

# Shodan API Key
SHODAN_KEY = "[secure]"
