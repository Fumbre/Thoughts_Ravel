/*
 Navicat Premium Dump SQL

 Source Server         : soloProject
 Source Server Type    : MySQL
 Source Server Version : 90600 (9.6.0)
 Source Host           : 127.0.0.1:3306
 Source Schema         : ThoughtsRavel

 Target Server Type    : MySQL
 Target Server Version : 90600 (9.6.0)
 File Encoding         : 65001

 Date: 15/03/2026 21:16:42
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for inside_nodes
-- ----------------------------
DROP TABLE IF EXISTS `inside_nodes`;
CREATE TABLE `inside_nodes` (
  `id` bigint NOT NULL,
  `nodeId` bigint NOT NULL,
  `content` longtext,
  `type` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of inside_nodes
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for nodes
-- ----------------------------
DROP TABLE IF EXISTS `nodes`;
CREATE TABLE `nodes` (
  `id` bigint NOT NULL,
  `name` varchar(150) NOT NULL,
  `desc` varchar(255) DEFAULT NULL,
  `positionX` float NOT NULL,
  `positionY` float NOT NULL,
  `color` varchar(10) NOT NULL,
  `shape` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of nodes
-- ----------------------------
BEGIN;
INSERT INTO `nodes` (`id`, `name`, `desc`, `positionX`, `positionY`, `color`, `shape`) VALUES (1234, 'root', 'main app test', 0, 0, '#ff00ff', 'circle');
INSERT INTO `nodes` (`id`, `name`, `desc`, `positionX`, `positionY`, `color`, `shape`) VALUES (12345, 'test', 'root test', 10, 10, '#ffff00', 'circle');
COMMIT;

-- ----------------------------
-- Table structure for nodes_relations
-- ----------------------------
DROP TABLE IF EXISTS `nodes_relations`;
CREATE TABLE `nodes_relations` (
  `parentId` bigint NOT NULL,
  `nodeId` bigint NOT NULL,
  `spaceId` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of nodes_relations
-- ----------------------------
BEGIN;
INSERT INTO `nodes_relations` (`parentId`, `nodeId`, `spaceId`) VALUES (0, 1234, 11234);
INSERT INTO `nodes_relations` (`parentId`, `nodeId`, `spaceId`) VALUES (1234, 12345, 11234);
COMMIT;

-- ----------------------------
-- Table structure for spaces
-- ----------------------------
DROP TABLE IF EXISTS `spaces`;
CREATE TABLE `spaces` (
  `id` bigint NOT NULL,
  `userId` bigint DEFAULT NULL,
  `title` varchar(25) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of spaces
-- ----------------------------
BEGIN;
INSERT INTO `spaces` (`id`, `userId`, `title`) VALUES (11234, 1, 'main');
COMMIT;

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` bigint NOT NULL,
  `username` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `password` char(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `status` char(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of users
-- ----------------------------
BEGIN;
INSERT INTO `users` (`id`, `username`, `password`, `status`) VALUES (1, 'admin', 'admin', '0');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
