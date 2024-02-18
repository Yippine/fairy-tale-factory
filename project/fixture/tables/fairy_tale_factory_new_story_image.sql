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
-- Table structure for table `new_story_image`
--

DROP TABLE IF EXISTS `new_story_image`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `new_story_image` (
  `new_story_id` mediumint unsigned NOT NULL,
  `line_id` tinyint unsigned NOT NULL,
  `tw_line_content` varchar(255) NOT NULL,
  `en_line_content` varchar(720) NOT NULL,
  `item_id` tinyint unsigned DEFAULT NULL,
  `cover_design_id` tinyint unsigned DEFAULT NULL,
  `tw_storyboard_desc` varchar(1500) DEFAULT NULL,
  `en_storyboard_desc` varchar(4250) DEFAULT NULL,
  `line_image_link` varchar(255) DEFAULT NULL,
  `creation_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`new_story_id`,`line_id`),
  KEY `fk_new_story_image_cover_design_id` (`item_id`,`cover_design_id`),
  CONSTRAINT `fk_new_story_image_cover_design_id` FOREIGN KEY (`item_id`, `cover_design_id`) REFERENCES `cover_design` (`item_id`, `cover_design_id`),
  CONSTRAINT `fk_new_story_image_item_id` FOREIGN KEY (`item_id`) REFERENCES `item` (`item_id`),
  CONSTRAINT `fk_new_story_image_story_id` FOREIGN KEY (`new_story_id`) REFERENCES `new_story` (`new_story_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `new_story_image`
--

LOCK TABLES `new_story_image` WRITE;
/*!40000 ALTER TABLE `new_story_image` DISABLE KEYS */;
/*!40000 ALTER TABLE `new_story_image` ENABLE KEYS */;
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
