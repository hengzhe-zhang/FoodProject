/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50717
Source Host           : localhost:3306
Source Database       : canteen

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2017-11-02 16:37:54
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for food
-- ----------------------------
DROP TABLE IF EXISTS `food`;
CREATE TABLE `food` (
  `id` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `num` int(11) DEFAULT NULL,
  `food_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of food
-- ----------------------------
INSERT INTO `food` VALUES ('b\'\\x97UqlP\\x01\\x04\\xe0A\'', '炒空心菜', '100', '1');
INSERT INTO `food` VALUES ('b\'$zqlP\\x01\\x04\\xe0A\'', '煎蛋', '100', '2');
INSERT INTO `food` VALUES ('b\'\">qlP\\x01\\x04\\xe0A\'', '二两米饭', '100', '3');

-- ----------------------------
-- Table structure for order
-- ----------------------------
DROP TABLE IF EXISTS `order`;
CREATE TABLE `order` (
  `id` int(11) NOT NULL,
  `user_id` varchar(255) NOT NULL,
  `date` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of order
-- ----------------------------
INSERT INTO `order` VALUES ('1', '8B95E1C4', '2017-07-03 19:48:33.977505');
INSERT INTO `order` VALUES ('2', '8B95E1C4', '2017-07-03 19:49:47.731049');
INSERT INTO `order` VALUES ('3', '8B95E1C4', '2017-07-03 19:52:43.537342');
INSERT INTO `order` VALUES ('4', '8B95E1C4', '2017-07-03 19:55:41.277982');
INSERT INTO `order` VALUES ('5', '8B95E1C4', '2017-07-03 19:57:06.017976');
INSERT INTO `order` VALUES ('6', '8B95E1C4', '2017-07-03 21:44:32.279731');
INSERT INTO `order` VALUES ('7', '8B95E1C4', '2017-07-03 22:21:52.150863');
INSERT INTO `order` VALUES ('8', '8B95E1C4', '2017-07-03 22:25:38.604032');
INSERT INTO `order` VALUES ('9', '8B95E1C4', '2017-07-03 22:25:40.941781');
INSERT INTO `order` VALUES ('10', '8B95E1C4', '2017-07-03 22:27:29.414603');
INSERT INTO `order` VALUES ('11', '8B95E1C4', '2017-07-03 22:27:33.158280');
INSERT INTO `order` VALUES ('12', '8B95E1C4', '2017-07-03 22:27:36.409271');
INSERT INTO `order` VALUES ('13', '8B95E1C4', '2017-07-03 22:27:38.122303');
INSERT INTO `order` VALUES ('14', '8B95E1C4', '2017-07-03 23:39:35.016226');

-- ----------------------------
-- Table structure for order_food
-- ----------------------------
DROP TABLE IF EXISTS `order_food`;
CREATE TABLE `order_food` (
  `id` int(11) NOT NULL,
  `food_id` varchar(255) NOT NULL,
  `food_num` int(11) NOT NULL,
  PRIMARY KEY (`id`,`food_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of order_food
-- ----------------------------
INSERT INTO `order_food` VALUES ('1', 'b\'\">qlP\\x01\\x04\\xe0A\'', '1');
INSERT INTO `order_food` VALUES ('1', 'b\'$zqlP\\x01\\x04\\xe0A\'', '1');
INSERT INTO `order_food` VALUES ('1', 'b\'\\x97UqlP\\x01\\x04\\xe0A\'', '1');
INSERT INTO `order_food` VALUES ('2', 'b\'\">qlP\\x01\\x04\\xe0A\'', '1');
INSERT INTO `order_food` VALUES ('2', 'b\'\\x97UqlP\\x01\\x04\\xe0A\'', '1');
INSERT INTO `order_food` VALUES ('3', 'b\'\">qlP\\x01\\x04\\xe0A\'', '1');
INSERT INTO `order_food` VALUES ('3', 'b\'\\x97UqlP\\x01\\x04\\xe0A\'', '1');
INSERT INTO `order_food` VALUES ('4', 'b\'\">qlP\\x01\\x04\\xe0A\'', '1');
INSERT INTO `order_food` VALUES ('4', 'b\'\\x97UqlP\\x01\\x04\\xe0A\'', '1');
INSERT INTO `order_food` VALUES ('5', 'b\'\">qlP\\x01\\x04\\xe0A\'', '2');
INSERT INTO `order_food` VALUES ('5', 'b\'\\x97UqlP\\x01\\x04\\xe0A\'', '3');
INSERT INTO `order_food` VALUES ('6', 'b\'\">qlP\\x01\\x04\\xe0A\'', '1');
INSERT INTO `order_food` VALUES ('6', 'b\'\\x97UqlP\\x01\\x04\\xe0A\'', '1');
INSERT INTO `order_food` VALUES ('7', 'b\'\">qlP\\x01\\x04\\xe0A\'', '3');
INSERT INTO `order_food` VALUES ('14', 'b\'\">qlP\\x01\\x04\\xe0A\'', '3');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `user_id` varchar(255) NOT NULL,
  `password` varchar(255) DEFAULT NULL,
  `nickname` varchar(255) NOT NULL,
  `photo` varchar(255) DEFAULT NULL,
  `sex` varchar(255) DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL,
  `height` float DEFAULT NULL,
  `weight` float DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('0BD960C3', '123456', '小乔', null, null, null, null, null);
INSERT INTO `user` VALUES ('8B95E1C4', '123456', '子乔', null, null, null, null, null);
SET FOREIGN_KEY_CHECKS=1;
