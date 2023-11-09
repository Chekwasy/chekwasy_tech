-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS chekwasy_dev_db;
CREATE USER IF NOT EXISTS 'chekwasy_dev'@'localhost' IDENTIFIED BY 'CHEKWASY_dev_pwd_001';
GRANT ALL PRIVILEGES ON `chekwasy_dev_db`.* TO 'chekwasy_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'chekwasy_dev'@'localhost';
FLUSH PRIVILEGES;
