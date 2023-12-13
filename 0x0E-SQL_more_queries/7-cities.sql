-- Creating database and table.
CREATE DATABASE IF NOT EXIST hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
	    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	    name VARCHAR(256) NOT NULL
	    );
