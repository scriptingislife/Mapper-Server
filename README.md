# Mapper-Server
Log Mapper server which pulls from a MySQL database.

## Introduction

When I saw a huge amount of failed login attempts in my SSH logs, I wanted a way to get more information. I started out only mapping IPs using geolocation data and now the map is more interactive with links to Shodan and more statistics. This project is made up of a server and [sensor](https://github.com/becksteadn/Log-Sensor), both of which use the same SQL database. I also created a self-contained version [here](https://github.com/becksteadn/Log-Mapper) though it is not maintained.

The default log file is `auth.log` used for authentication, but any file with IP addresses can be used.

## Installation

### Prerequisites

Both the server and sensor require the MySQLdb connector. [Install it with yum on Amazon Linux](https://lazyprogrammer.me/installing-the-python-mysql-mysqldb-connector/) or Debian systems can  install it with apt using `sudo apt-get install python-mysqldb`.

### Database Configuration

![](https://lambda.sx/m4g.png)

Actual statements to come.

```
CREATE DATABASE log_mapper;
USE log_mapper;
CREATE TABLE attempts (

);
CREATE TABLE markers (

);
```

### Clone the Repository

Download or clone the repo anywhere. `https://github.com/becksteadn/Mapper-Server.git`


### Server Configuration
All variables are in `server_vars.py`.

Enter database credentials.

Add [Shodan](https://shodan.io) API key.

### Cron



### Daemon
Edit variables in `mapper-server` service file.

`sudo mv mapper-server /etc/init.d/`

`sudo service mapper-server start`
