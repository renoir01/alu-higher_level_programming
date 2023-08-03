-- a script that creates the database hbtn_0d_usa and the table cities
-- (in the database hbtn_0d_usa) on your MySQL server.
-- If the database hbtn_0d_usa already exists, your script should not fail
-- If the table cities already exists, your script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
	state_id INT,
	FOREIGN KEY(state_id) REFERENCES states(id),
	name VARCHAR(256) NOT NULL 
)ENGINE=InnoDB;
