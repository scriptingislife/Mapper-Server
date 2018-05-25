CREATE DATABASE log_mapper;

CREATE TABLE log_mapper.attempts (
    id INT NOT NULL AUTO_INCREMENT,
    host VARCHAR(20) DEFAULT 'Anonymous',
    ip CHAR(15) NOT NULL,
    stamp DATETIME NOT NULL UNIQUE,
    success tinyint(4),
    PRIMARY KEY (id, stamp)
);

CREATE TABLE log_mapper.markers (
    ip CHAR(15) NOT NULL,
    starred tinyint(4),
    PRIMARY KEY (ip)
);

CREATE USER 'mapperserver'@'%' IDENTIFIED BY 'serverpasswd';
GRANT SELECT, UPDATE, DELETE ON log_mapper.* TO 'mapperserver'@'%';

CREATE USER 'sensor001'@'%' IDENTIFIED BY 'sensorpasswd';
GRANT INSERT ON log_mapper.* TO 'sensor001'@'%';
