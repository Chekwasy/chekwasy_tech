-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS chekwasy_test_db;
CREATE USER IF NOT EXISTS 'chekwasy_test'@'localhost' IDENTIFIED BY 'CHEKWASY_test_pwd_001';
GRANT ALL PRIVILEGES ON `chekwasy_test_db`.* TO 'chekwasy_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'chekwasy_test'@'localhost';
FLUSH PRIVILEGES;
