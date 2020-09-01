/*
Navicat MySQL Data Transfer

Source Server         : DevM
Source Server Version : 80019
Source Host           : 10.192.5.16:3306
Source Database       : house-price-analyzer

Target Server Type    : MYSQL
Target Server Version : 80019
File Encoding         : 65001

Date: 2020-09-01 16:16:27
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for houseprice
-- ----------------------------
DROP TABLE IF EXISTS `py_house_price`;
CREATE TABLE `py_house_price` (
  `id` int NOT NULL AUTO_INCREMENT,
  `house_city` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `house_area` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `house_community` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `house_price` double(12,2) NOT NULL,
  `house_square` double(4,2) NOT NULL,
  `update_date` datetime NOT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `default` (`house_city`,`house_area`,`house_community`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of houseprice
-- ----------------------------
