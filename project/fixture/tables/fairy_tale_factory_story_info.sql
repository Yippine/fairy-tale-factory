-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: fairy_tale_factory
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `story_info`
--

DROP TABLE IF EXISTS `story_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `story_info` (
  `story_id` mediumint unsigned NOT NULL AUTO_INCREMENT,
  `beginning_statistics_id` mediumint unsigned DEFAULT NULL,
  `middle_statistics_id` mediumint unsigned DEFAULT NULL,
  `turning_statistics_id` mediumint unsigned DEFAULT NULL,
  `ending_statistics_id` mediumint unsigned DEFAULT NULL,
  `full_text_statistics_id` mediumint unsigned DEFAULT NULL,
  `creation_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `modification_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`story_id`),
  KEY `fk_story_info_beginning_statistics_id` (`beginning_statistics_id`),
  KEY `fk_story_info_middle_statistics_id` (`middle_statistics_id`),
  KEY `fk_story_info_turning_statistics_id` (`turning_statistics_id`),
  KEY `fk_story_info_ending_statistics_id` (`ending_statistics_id`),
  KEY `fk_story_info_full_text_statistics_id` (`full_text_statistics_id`),
  CONSTRAINT `fk_story_info_beginning_statistics_id` FOREIGN KEY (`beginning_statistics_id`) REFERENCES `story_statistics` (`statistics_id`),
  CONSTRAINT `fk_story_info_ending_statistics_id` FOREIGN KEY (`ending_statistics_id`) REFERENCES `story_statistics` (`statistics_id`),
  CONSTRAINT `fk_story_info_full_text_statistics_id` FOREIGN KEY (`full_text_statistics_id`) REFERENCES `story_statistics` (`statistics_id`),
  CONSTRAINT `fk_story_info_middle_statistics_id` FOREIGN KEY (`middle_statistics_id`) REFERENCES `story_statistics` (`statistics_id`),
  CONSTRAINT `fk_story_info_new_story_id` FOREIGN KEY (`story_id`) REFERENCES `new_story` (`new_story_id`),
  CONSTRAINT `fk_story_info_original_story_id` FOREIGN KEY (`story_id`) REFERENCES `original_story` (`original_story_id`),
  CONSTRAINT `fk_story_info_turning_statistics_id` FOREIGN KEY (`turning_statistics_id`) REFERENCES `story_statistics` (`statistics_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `story_info`
--

LOCK TABLES `story_info` WRITE;
/*!40000 ALTER TABLE `story_info` DISABLE KEYS */;
/*!40000 ALTER TABLE `story_info` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-02-18 20:53:53
