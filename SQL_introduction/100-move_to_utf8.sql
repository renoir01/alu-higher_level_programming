-- Alter the db to utf8
-- ALTER TABLE `first_table` (ALTER COLUMN `name` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci);
USE `hbtn_0c_0`;
ALTER DATABASE `hbtn_0c_0` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE `first_table` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
