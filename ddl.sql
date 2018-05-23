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
