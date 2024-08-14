/*
 Navicat Premium Data Transfer

 Source Server         : zyxk_test
 Source Server Type    : MySQL
 Source Server Version : 50739
 Source Host           : localhost:8001
 Source Schema         : bor_m

 Target Server Type    : MySQL
 Target Server Version : 50739
 File Encoding         : 65001

 Date: 14/08/2024 11:33:13
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for history
-- ----------------------------
DROP TABLE IF EXISTS `history`;
CREATE TABLE `history` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mid` int(11) DEFAULT NULL COMMENT '关联人员表',
  `cid` int(11) DEFAULT NULL COMMENT '关联电脑表',
  `domain` varchar(255) DEFAULT NULL COMMENT '网站域名',
  `title` varchar(255) DEFAULT NULL COMMENT '最新网页title',
  `start_time` int(11) DEFAULT '0' COMMENT '打开时间',
  `end_time` int(11) DEFAULT '0' COMMENT '关闭时间',
  `date` char(16) DEFAULT NULL COMMENT '日期',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COMMENT='网页浏览历史';

SET FOREIGN_KEY_CHECKS = 1;
