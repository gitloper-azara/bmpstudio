-- Script to setup a MySQL server for BMP Studio

-- Create the database
CREATE DATABASE IF NOT EXISTS bmpstudio_db;

-- Create user
CREATE USER IF NOT EXISTS 'bmp_dev'@'localhost' IDENTIFIED BY 'bmp_dev_pwd';

-- Grant necessary priviledges
GRANT USAGE ON *.* TO 'bmp_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'bmp_dev'@'localhost';
GRANT ALL PRIVILEGES ON bmpstudio_db.* TO 'bmp_dev'@'localhost';

-- flush privildges
FLUSH PRIVILEGES;
