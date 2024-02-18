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
-- Table structure for table `story_category`
--

DROP TABLE IF EXISTS `story_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `story_category` (
  `category_id` tinyint unsigned NOT NULL AUTO_INCREMENT,
  `category_name` varchar(50) NOT NULL,
  `parent_category_id` tinyint unsigned DEFAULT NULL,
  `creation_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `modification_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `disable_time` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`category_id`),
  KEY `fk_story_category_parent_id` (`parent_category_id`),
  CONSTRAINT `fk_story_category_parent_id` FOREIGN KEY (`parent_category_id`) REFERENCES `story_category` (`category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `story_category`
--

LOCK TABLES `story_category` WRITE;
/*!40000 ALTER TABLE `story_category` DISABLE KEYS */;
INSERT INTO `story_category` VALUES (1,'文學故事',NULL,'2024-02-09 06:11:12','2024-02-09 06:11:12',NULL),(2,'迪士尼故事',1,'2024-02-09 06:11:12','2024-02-09 06:11:12',NULL),(3,'格林童話',1,'2024-02-09 06:11:12','2024-02-09 06:11:12',NULL),(4,'安徒生童話',1,'2024-02-09 06:11:12','2024-02-09 06:11:12',NULL),(5,'經典兒童文學',1,'2024-02-09 06:11:12','2024-02-09 06:11:12',NULL),(6,'民間故事',NULL,'2024-02-09 06:11:12','2024-02-09 06:11:12',NULL),(7,'中國民間故事',6,'2024-02-09 06:11:12','2024-02-09 06:11:12',NULL),(8,'日本民間故事',6,'2024-02-09 06:11:12','2024-02-09 06:11:12',NULL),(9,'英國民間故事',6,'2024-02-09 06:11:12','2024-02-09 06:11:12',NULL),(10,'阿拉伯民間故事',6,'2024-02-09 06:11:12','2024-02-09 06:11:12',NULL),(11,'一千零一夜',10,'2024-02-09 06:11:12','2024-02-09 06:11:12',NULL),(12,'神話故事',NULL,'2024-02-09 06:11:12','2024-02-09 06:11:12',NULL),(13,'中國神話故事',12,'2024-02-09 06:11:12','2024-02-09 06:11:12',NULL),(14,'寓言故事',NULL,'2024-02-09 06:11:12','2024-02-09 06:11:12',NULL),(15,'伊索寓言',14,'2024-02-09 06:11:12','2024-02-09 06:11:12',NULL);
/*!40000 ALTER TABLE `story_category` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-02-18 20:53:54
