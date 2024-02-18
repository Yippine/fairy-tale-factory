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
-- Table structure for table `new_story`
--

DROP TABLE IF EXISTS `new_story`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `new_story` (
  `new_story_id` mediumint unsigned NOT NULL AUTO_INCREMENT,
  `new_story_name` varchar(50) NOT NULL,
  `main_character_id` tinyint unsigned DEFAULT NULL,
  `supporting_character_id` tinyint unsigned DEFAULT NULL,
  `item_id` tinyint unsigned DEFAULT NULL,
  `tw_new_story_content` varchar(1500) NOT NULL,
  `en_new_story_content` varchar(4250) DEFAULT NULL,
  `user_id` mediumint unsigned DEFAULT NULL,
  `creation_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `favorites` tinyint DEFAULT '0',
  `valid_days` smallint unsigned DEFAULT '1',
  `expiration_time` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`new_story_id`),
  KEY `fk_new_story_user_id` (`user_id`),
  KEY `fk_new_story_item_id` (`item_id`),
  KEY `fk_new_story_supporting_character_id` (`supporting_character_id`),
  KEY `fk_new_story_main_character_id` (`main_character_id`),
  CONSTRAINT `fk_new_story_item_id` FOREIGN KEY (`item_id`) REFERENCES `item` (`item_id`),
  CONSTRAINT `fk_new_story_main_character_id` FOREIGN KEY (`main_character_id`) REFERENCES `item` (`item_id`),
  CONSTRAINT `fk_new_story_supporting_character_id` FOREIGN KEY (`supporting_character_id`) REFERENCES `item` (`item_id`),
  CONSTRAINT `fk_new_story_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`),
  CONSTRAINT `new_story_chk_1` CHECK ((`favorites` in (0,1)))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `new_story`
--

LOCK TABLES `new_story` WRITE;
/*!40000 ALTER TABLE `new_story` DISABLE KEYS */;
/*!40000 ALTER TABLE `new_story` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-02-18 20:53:52
