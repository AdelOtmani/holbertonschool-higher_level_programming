-- script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(id INT PRIMARY KEY NOT NULL UNIQUE AUTO_INCREMENT, states_id INT FOREIGN KEY(states_id) REFERENCES states(id), name VARCHAR(256) NOT NULL);
