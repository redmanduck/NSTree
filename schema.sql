-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               5.6.25 - MySQL Community Server (GPL)
-- Server OS:                    Win64
-- HeidiSQL Version:             9.3.0.4984
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- Dumping database structure for playground
CREATE DATABASE IF NOT EXISTS `playground` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;
USE `playground`;


-- Dumping structure for table playground.nstree
CREATE TABLE IF NOT EXISTS `nstree` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `nsleft` bigint(20) unsigned DEFAULT NULL,
  `nsright` bigint(20) unsigned DEFAULT NULL,
  `value` varchar(50) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  KEY `LR` (`nsleft`,`nsright`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- Dumping data for table playground.nstree: ~2 rows (approximately)
/*!40000 ALTER TABLE `nstree` DISABLE KEYS */;
/*!40000 ALTER TABLE `nstree` ENABLE KEYS */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
