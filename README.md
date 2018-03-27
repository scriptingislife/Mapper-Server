# Mapper-Server
Log Mapper server which pulls from a MySQL database.

### Requires MySQLdb connector
[Install with yum on Amazon Linux](https://lazyprogrammer.me/installing-the-python-mysql-mysqldb-connector/)

**Ubuntu** systems can install it with apt using `sudo apt-get install python-mysqldb`


### Setup

#### Configuration
All variables are in `server_vars.py`.

Enter database credentials.

Add [Shodan](https://shodan.io) API key.


#### Daemon
Edit variables in `mapper-server` service file.

`sudo mv mapper-server /etc/init.d/`

`sudo service mapper-server start`