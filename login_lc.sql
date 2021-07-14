-- MySQL dump 10.13  Distrib 8.0.25, for Win64 (x86_64)
--
-- Host: localhost    Database: login_lc
-- ------------------------------------------------------
-- Server version	8.0.25

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(25) NOT NULL,
  `date_login` date DEFAULT NULL,
  `login` time DEFAULT NULL,
  `logout` time DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `username` (`username`),
  CONSTRAINT `login_ibfk_1` FOREIGN KEY (`username`) REFERENCES `users` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login`
--

LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` VALUES (1,'uthmaanb','2021-07-11','23:41:17','23:59:20'),(2,'uthmaanb','2021-07-11','23:41:46','23:59:20'),(3,'abdul','2021-07-12','00:24:07','00:24:21'),(4,'uthmaanb','2021-07-12','20:28:27','20:32:05'),(5,'uthmaanb','2021-07-12','20:30:41','20:32:05'),(6,'uthmaanb','2021-07-12','20:31:27','20:32:05'),(7,'uthmaanb','2021-07-12','20:31:53','20:32:05'),(8,'bob','2021-07-12','20:35:37','20:36:59'),(9,'baadles','2021-07-12','20:45:21','20:45:33');
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `next_of_kin`
--

DROP TABLE IF EXISTS `next_of_kin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `next_of_kin` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `user_id` varchar(13) NOT NULL,
  `name` varchar(25) NOT NULL,
  `surname` varchar(25) NOT NULL,
  `cell` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `next_of_kin_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id_num`),
  CONSTRAINT `next_of_kin_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id_num`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `next_of_kin`
--

LOCK TABLES `next_of_kin` WRITE;
/*!40000 ALTER TABLE `next_of_kin` DISABLE KEYS */;
INSERT INTO `next_of_kin` VALUES (1,'9609095470083','malik','mo','123popo'),(2,'1231231231231','mommy','mo','1231231231'),(3,'3123123121111','poppy','lee','1234567890'),(4,'1242623542654','pops','dirt','3213121232'),(5,'0987654321234','moms','theman','1231231231'),(6,'0891230981231','lady','boss','0981230981'),(7,'1237650986543','moms','bread','8768768767');
/*!40000 ALTER TABLE `next_of_kin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `id_num` varchar(13) NOT NULL,
  `username` varchar(25) NOT NULL,
  `password` varchar(25) NOT NULL,
  `name` varchar(25) NOT NULL,
  `surname` varchar(25) NOT NULL,
  `email` varchar(40) NOT NULL,
  `cell` varchar(10) NOT NULL,
  `role` varchar(8) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_num` (`id_num`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'9609095470083','uthmaanb','123','uthmaan','breda','uthmaan@breda.com','0794637741','lecturer'),(2,'1231231231231','abdul','123','malik','mo','abdul@malik.com','1231231231','Student'),(3,'3123123121111','bob','123','boblin','lee','boblin@lee.com','3212312312','Student'),(5,'1242623542654','john','123','johnstone','dirt','johnstone@dirt.com','1231231231','Student'),(6,'0987654321234','jan','123','jan','theman','jan@theman.com','1231231231','visitor'),(9,'0891230981231','bossman','123','boss','man','boss@man.com','0981230981','admin'),(10,'1237650986543','baadles','123','ubaid','bread','ubaid@breda.com','0989870989','Student'),(11,'1231245234512','gon','123','killua','james','killua@james.com','3211233211','student'),(12,'9348962936238','drax','123','gg','mates','gg@mates.com','1231231231','lecturer'),(13,'','','','','','','',''),(14,'1236543243543','bones','123','bobo','jones','bobojones@gmail.com','7657657655','lecturer');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-14 19:43:41
