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
DROP TABLE IF EXISTS `houseprice`;
CREATE TABLE `houseprice` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `HouseCity` varchar(255) COLLATE utf8_bin NOT NULL,
  `HouseArea` varchar(255) COLLATE utf8_bin NOT NULL,
  `HouseCommunity` varchar(255) COLLATE utf8_bin NOT NULL,
  `HousePrice` double(12,2) NOT NULL,
  `HouseSquare` double(4,2) NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `default` (`HouseCity`,`HouseArea`,`HouseCommunity`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of houseprice
-- ----------------------------
