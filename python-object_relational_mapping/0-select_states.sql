CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"),
("Nevada");
-- This script creates a database named hbtn_0e_0_usa, a table named states,
-- and inserts some initial data into the states table.