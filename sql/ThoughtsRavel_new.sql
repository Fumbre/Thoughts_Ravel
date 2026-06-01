/*
 Navicat Premium Dump SQL

 Source Server         : soloProject
 Source Server Type    : MySQL
 Source Server Version : 90600 (9.6.0)
 Source Host           : 127.0.0.1:3306
 Source Schema         : Thoughts_Ravel

 Target Server Type    : MySQL
 Target Server Version : 90600 (9.6.0)
 File Encoding         : 65001

 Date: 01/06/2026 20:50:53
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for node_contents
-- ----------------------------
DROP TABLE IF EXISTS `node_contents`;
CREATE TABLE `node_contents` (
  `id` bigint NOT NULL,
  `node_id` bigint NOT NULL,
  `content` text NOT NULL,
  `content_type` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of node_contents
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for node_correlations
-- ----------------------------
DROP TABLE IF EXISTS `node_correlations`;
CREATE TABLE `node_correlations` (
  `parent_node_id` bigint NOT NULL COMMENT 'this is an additional relationship between parent node and destination node',
  `destination_node_id` bigint NOT NULL COMMENT 'put the node id where do you want to store the paretn id logic; example: somewhere you have a parent_node_id with your self structure and you want to copy this to a different space (node). it will help you to build corelation',
  `name` varchar(255) DEFAULT NULL COMMENT 'the name of correlation between nodes'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of node_correlations
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for node_permissions
-- ----------------------------
DROP TABLE IF EXISTS `node_permissions`;
CREATE TABLE `node_permissions` (
  `id` bigint NOT NULL,
  `node_id` bigint NOT NULL,
  `permission_nam` varchar(255) NOT NULL,
  `unique_key` varchar(255) NOT NULL,
  `created_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of node_permissions
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for nodes
-- ----------------------------
DROP TABLE IF EXISTS `nodes`;
CREATE TABLE `nodes` (
  `id` bigint NOT NULL COMMENT 'id of the node',
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT 'name of node',
  `parent_id` bigint NOT NULL COMMENT '0 for root, parent_id is where nodes are stored',
  `ancestor` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT 'the full length of all ancestors like (0,1,2,3,4) for node id 5',
  `description` varchar(255) DEFAULT NULL COMMENT 'node description like h1 tag',
  `type` char(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '0 - node, 1 - space (node of nodes), 2 - show the content, 3 - make the node executable (if music is inside after click - play music)',
  `position_x` int NOT NULL COMMENT 'position X of node',
  `position_y` int NOT NULL COMMENT 'position Y of node',
  `creater_id` bigint NOT NULL COMMENT 'the user_id who created a node',
  `shape` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT 'shape of a node',
  `color` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT 'color of a node',
  `created_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'time when it was created',
  `updated_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Update time',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of nodes
-- ----------------------------
BEGIN;
INSERT INTO `nodes` (`id`, `name`, `parent_id`, `ancestor`, `description`, `type`, `position_x`, `position_y`, `creater_id`, `shape`, `color`, `created_time`, `updated_time`) VALUES (1, 'root', 0, '0', 'we are testing', '1', 0, 0, 1, 'circle', 'blue', '2026-06-01 13:11:55', '2026-06-01 13:11:55');
INSERT INTO `nodes` (`id`, `name`, `parent_id`, `ancestor`, `description`, `type`, `position_x`, `position_y`, `creater_id`, `shape`, `color`, `created_time`, `updated_time`) VALUES (2, 'paper', 1, '0,1', 'something', '0', 10, 10, 1, 'circle', 'blue', '2026-06-01 13:12:32', '2026-06-01 13:12:32');
INSERT INTO `nodes` (`id`, `name`, `parent_id`, `ancestor`, `description`, `type`, `position_x`, `position_y`, `creater_id`, `shape`, `color`, `created_time`, `updated_time`) VALUES (3, 'rock', 1, '0,1', 'nothing', '0', 15, 15, 1, 'circle', 'blue', '2026-06-01 13:15:01', '2026-06-01 13:15:01');
COMMIT;

-- ----------------------------
-- Table structure for role_permission_relationship
-- ----------------------------
DROP TABLE IF EXISTS `role_permission_relationship`;
CREATE TABLE `role_permission_relationship` (
  `permission_id` bigint NOT NULL,
  `role_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of role_permission_relationship
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for roles
-- ----------------------------
DROP TABLE IF EXISTS `roles`;
CREATE TABLE `roles` (
  `id` bigint NOT NULL,
  `role_name` varchar(255) NOT NULL,
  `created_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of roles
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` bigint NOT NULL,
  `email` varchar(255) NOT NULL,
  `username` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `status` char(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of users
-- ----------------------------
BEGIN;
INSERT INTO `users` (`id`, `email`, `username`, `password`, `status`) VALUES (7467258093718474752, 'Ihave@gmail.com', 'test', '$argon2id$v=19$m=65536,t=3,p=4$kJLSOud8D0FIyZnT2rt3jg$pfHyrs75yTfi1+OjrG61kCDQGpB3l3BQN6OYvYuo00g', '0');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
