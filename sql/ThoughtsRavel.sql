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

 Date: 15/03/2026 15:12:17
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for inside_nodes
-- ----------------------------
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
CREATE TABLE `nodes` (
  `id` bigint NOT NULL,
  `name` varchar(150) NOT NULL,
  `desc` varchar(255) DEFAULT NULL,
  `positionX` float NOT NULL,
  `positionY` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of nodes
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for nodes_relations
-- ----------------------------
CREATE TABLE `nodes_relations` (
  `parentId` bigint NOT NULL,
  `nodeId` bigint NOT NULL,
  `spaceId` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of nodes_relations
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for spaces
-- ----------------------------
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
COMMIT;

-- ----------------------------
-- Table structure for users
-- ----------------------------
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
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
