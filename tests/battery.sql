-- phpMyAdmin SQL Dump
-- version 3.5.1
-- http://www.phpmyadmin.net
--
-- 主机: localhost
-- 生成日期: 2013 年 01 月 12 日 17:22
-- 服务器版本: 5.5.23
-- PHP 版本: 5.4.3

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- 数据库: `battery_null`
--

-- --------------------------------------------------------

--
-- 表的结构 `authassignment`
--

CREATE TABLE IF NOT EXISTS `authassignment` (
  `itemname` varchar(64) NOT NULL,
  `userid` varchar(64) NOT NULL,
  `bizrule` text,
  `data` text,
  PRIMARY KEY (`itemname`,`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 转存表中的数据 `authassignment`
--

INSERT INTO `authassignment` (`itemname`, `userid`, `bizrule`, `data`) VALUES
('admin', '1', NULL, 'N;'),
('admin', '15', NULL, 'N;'),
('admin', '20', NULL, 'N;'),
('admin', '22', NULL, 'N;'),
('DictBattery.*', '16', NULL, 'N;'),
('DictManufacturer.*', '9', NULL, 'N;'),
('jz', '48', NULL, 'N;'),
('jz', '52', NULL, 'N;'),
('jz', '53', NULL, 'N;'),
('jz', '60', NULL, 'N;'),
('master', '10', NULL, 'N;'),
('master', '11', NULL, 'N;'),
('master', '12', NULL, 'N;'),
('master', '13', NULL, 'N;'),
('master', '19', NULL, 'N;'),
('master', '4', NULL, 'N;'),
('MtsysBase.*', '9', NULL, 'N;'),
('ssq', '49', NULL, 'N;'),
('ssq', '50', NULL, 'N;'),
('ssq', '51', NULL, 'N;'),
('ssq', '54', NULL, 'N;'),
('ssq', '55', NULL, 'N;'),
('ssq', '56', NULL, 'N;'),
('ssq', '57', NULL, 'N;'),
('ssq', '58', NULL, 'N;'),
('ssq', '59', NULL, 'N;');

-- --------------------------------------------------------

--
-- 表的结构 `authitem`
--

CREATE TABLE IF NOT EXISTS `authitem` (
  `name` varchar(64) NOT NULL,
  `type` int(11) NOT NULL,
  `description` text CHARACTER SET utf8,
  `bizrule` text,
  `data` text,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 转存表中的数据 `authitem`
--

INSERT INTO `authitem` (`name`, `type`, `description`, `bizrule`, `data`) VALUES
('admin', 1, '超级管理员', NULL, 'N;'),
('BtBattery.*', 0, '电池组模块管理', NULL, 'N;'),
('BtBatterys.*', 0, '运行报表模块管理', NULL, 'N;'),
('DictBattery.*', 0, '电池规格模块管理', NULL, 'N;'),
('DictBatterySort.*', 0, '电池类型模块管理', NULL, 'N;'),
('DictManufacturer.*', 0, '电池制造商模块管理', NULL, 'N;'),
('Helper.*', 0, '系统帮助模块管理', NULL, 'N;'),
('Helper.Admin', 0, '系统帮助模块.管理操作', NULL, 'N;'),
('jz', 2, '基站', NULL, 'N;'),
('master', 0, '基本权限包', NULL, 'N;'),
('MtsysBase.*', 0, '基站信息模块管理', NULL, 'N;'),
('MtsysBasetype.*', 0, '基站类型模块管理', NULL, 'N;'),
('MtsysProvince.*', 0, '省级单位管理模块管理', NULL, 'N;'),
('Sensors.*', 0, '设备管理模块管理', NULL, 'N;'),
('Setting.*', 0, '参数设置模块管理', NULL, 'N;'),
('ssq', 2, '省市区', NULL, 'N;'),
('Suggestion.*', 0, '系统意见簿模块管理', NULL, 'N;'),
('Suggestion.Delete', 0, '系统帮助模块.删除操作', NULL, 'N;'),
('Suggestion.Update', 0, '系统帮助模块.修改操作', NULL, 'N;'),
('Unit.*', 0, '单位管理模块管理', NULL, 'N;'),
('UploadFiles.*', 0, '导入检测数据模块管理', NULL, 'N;'),
('User.Activation.*', 0, '激活用户', NULL, 'N;'),
('User.Admin.*', 0, '管理用户', NULL, 'N;'),
('User.Default.*', 0, '用户模块', NULL, 'N;'),
('User.Profile.*', 0, '用户信息管理', NULL, 'N;'),
('User.ProfileField.*', 0, '用户信息扩展管理', NULL, 'N;');

-- --------------------------------------------------------

--
-- 表的结构 `authitemchild`
--

CREATE TABLE IF NOT EXISTS `authitemchild` (
  `parent` varchar(64) NOT NULL,
  `child` varchar(64) NOT NULL,
  PRIMARY KEY (`parent`,`child`),
  KEY `child` (`child`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 转存表中的数据 `authitemchild`
--

INSERT INTO `authitemchild` (`parent`, `child`) VALUES
('jz', 'BtBattery.*'),
('master', 'BtBattery.*'),
('jz', 'BtBatterys.*'),
('master', 'BtBatterys.*'),
('ssq', 'BtBatterys.*'),
('jz', 'DictBattery.*'),
('master', 'DictBattery.*'),
('jz', 'DictBatterySort.*'),
('master', 'DictBatterySort.*'),
('jz', 'DictManufacturer.*'),
('master', 'DictManufacturer.*'),
('jz', 'Helper.*'),
('master', 'Helper.*'),
('ssq', 'Helper.*'),
('jz', 'MtsysBase.*'),
('master', 'MtsysBase.*'),
('ssq', 'MtsysBase.*'),
('jz', 'MtsysBasetype.*'),
('master', 'MtsysBasetype.*'),
('jz', 'Sensors.*'),
('master', 'Sensors.*'),
('jz', 'Setting.*'),
('master', 'Setting.*'),
('jz', 'Suggestion.*'),
('ssq', 'Suggestion.*'),
('jz', 'Unit.*'),
('master', 'Unit.*'),
('ssq', 'Unit.*'),
('jz', 'UploadFiles.*'),
('master', 'UploadFiles.*'),
('jz', 'User.Admin.*'),
('ssq', 'User.Admin.*'),
('jz', 'User.Default.*'),
('ssq', 'User.Default.*'),
('master', 'User.Profile.*'),
('ssq', 'User.Profile.*'),
('ssq', 'User.ProfileField.*');

-- --------------------------------------------------------

--
-- 表的结构 `bt_battery`
--

CREATE TABLE IF NOT EXISTS `bt_battery` (
  `RECORD_ID` int(11) NOT NULL AUTO_INCREMENT,
  `BASE_N` int(11) DEFAULT NULL COMMENT '基站编码,来自mtsys_base中的base_id',
  `GROUP_V` varchar(255) COLLATE utf8_unicode_ci NOT NULL COMMENT '电池组编码,来自bt_batterys中的record_id',
  `BATTERYTYPE_V` int(11) DEFAULT NULL COMMENT '电池型号来自dict_battery中的record_id，用于确定这个电池组采用的电池类型',
  `SERIAL_N` decimal(5,0) DEFAULT NULL COMMENT '电池序号与电池组的相对应',
  `SETUP_D` date DEFAULT NULL COMMENT '安装日期',
  `CURDATE_D` datetime DEFAULT NULL COMMENT '采集时间',
  `CREATE_USERID` int(11) DEFAULT NULL COMMENT '创建人来自mtsys_user中的USER_ID',
  `STATUS_N` decimal(2,0) DEFAULT NULL COMMENT '单体电池状态：0绿色，1黄色警告，2红色警告',
  `CURVAL_N` float(10,4) DEFAULT NULL COMMENT '当前的电压',
  `CURINNER_N` float(10,4) DEFAULT NULL COMMENT '当前内阻',
  `CUR_ELECTRIC_N` float(10,4) DEFAULT NULL COMMENT '电流',
  `CUR_HL_INNER_N` float(10,4) DEFAULT NULL COMMENT '混流排内阻',
  `CUR_TEMPERATURE_N` decimal(10,4) DEFAULT NULL COMMENT '电池温度',
  `FORCASTVOLUME_N` float(10,4) DEFAULT NULL COMMENT '预估容量',
  `TESTVOLUME_N` float(10,4) DEFAULT NULL COMMENT '电池放电测试容量',
  `POWERSUPPLY_N` float(10,4) DEFAULT NULL COMMENT '供电情况',
  `BACKLOAD_N` float(10,4) DEFAULT NULL COMMENT '后备负载，这个以后可能不需要了',
  `REMARK_V` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`RECORD_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='电池信息' AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `bt_batterys`
--

CREATE TABLE IF NOT EXISTS `bt_batterys` (
  `RECORD_ID` varchar(255) COLLATE utf8_unicode_ci NOT NULL COMMENT '电池组编码,手工输入,不得重复,这个在信息采集中用到电池组的信息',
  `BASE_TYPE` int(11) DEFAULT NULL,
  `BASE_N` int(11) NOT NULL COMMENT '基站名称编码，来源于mtsys_base',
  `GROUPNAME_V` varchar(255) COLLATE utf8_unicode_ci NOT NULL COMMENT '电池组名称,相当于一个别名可以重复',
  `BATTERYTYPE_V` int(11) NOT NULL COMMENT '电池型号来自dict_battery中的record_id，用于确定这个电池组采用的电池类型',
  `BATTERYNUM_N` int(11) NOT NULL COMMENT '电池个数',
  `SETUP_D` date DEFAULT NULL COMMENT '电池组年代，生产日期',
  `INSTALL_TIME` date DEFAULT NULL COMMENT '电池安装日期',
  `CREATE_USERID` int(11) DEFAULT NULL COMMENT '创建人来自mtsys_user中的USER_ID',
  `CUR_DATE` datetime DEFAULT NULL COMMENT '采集数据的日期',
  `DEVICE_V` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '测量地址',
  `IP_V` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '设备IP地址',
  `PORT_N` int(11) DEFAULT NULL COMMENT '设备端口地址',
  `ADDR_N` int(11) DEFAULT NULL COMMENT '传感器设备地址',
  `EVENT_NUM` decimal(5,0) DEFAULT NULL COMMENT '事件数量,这个目前没用上',
  `SETUPADDR_V` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '电池组安装地址',
  `BACKLOAD_V` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '后备负载,这个可能不再需要了',
  `POWERSUPPLY_V` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '供电情况',
  `ALARMRED_N` decimal(5,2) DEFAULT NULL COMMENT '黄色电池组最大红色单体',
  `NORMALRED_N` decimal(5,2) DEFAULT NULL COMMENT '绿色电池组最大红色单体',
  `NORMALYELLOW_N` decimal(5,2) DEFAULT NULL COMMENT '绿色电池组最大黄色单体',
  `ALARMYELLOW_N` decimal(5,2) DEFAULT NULL COMMENT '黄色电池组最大黄色单体',
  `STATUS_N` decimal(2,0) DEFAULT NULL COMMENT '电池组状态：0正常，1黄色警告，2红色警告',
  `GREEN` decimal(3,0) DEFAULT NULL COMMENT '绿色电池数',
  `YELLOW` decimal(3,0) DEFAULT NULL COMMENT '黄色电池数',
  `RED` decimal(3,0) DEFAULT NULL COMMENT '红色电池数',
  `REMARK_V` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '备注',
  `MANCODE_V` int(11) DEFAULT NULL,
  PRIMARY KEY (`RECORD_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='电池组信息';

-- --------------------------------------------------------

--
-- 表的结构 `bt_rundata`
--

CREATE TABLE IF NOT EXISTS `bt_rundata` (
  `RECORD_ID` int(11) NOT NULL AUTO_INCREMENT,
  `BTKEY_V` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '电池组编码',
  `BASE_N` int(11) DEFAULT NULL COMMENT '基站编码',
  `BTTYPEKEY_V` int(11) DEFAULT NULL COMMENT '电池类型编码',
  `BTSERIALNO_V` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '电池序列号',
  `HVOL_N` decimal(10,0) DEFAULT NULL COMMENT '电压高字节',
  `LVOL_N` decimal(10,0) DEFAULT NULL COMMENT '电压低字节',
  `VOL_N` decimal(10,4) DEFAULT NULL COMMENT '电压值',
  `VOLUNIT_V` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '电压单位',
  `HINTER_N` decimal(10,0) DEFAULT NULL COMMENT '内阻高字节',
  `LINTER_N` decimal(10,0) DEFAULT NULL COMMENT '内阻低字节',
  `INTER_N` decimal(10,4) DEFAULT NULL COMMENT '内阻值',
  `INTERUNIT_V` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '内阻单位',
  `HCONDUCTION_N` decimal(10,0) DEFAULT NULL COMMENT '电导高字节',
  `LCONDUCTION_N` decimal(10,0) DEFAULT NULL COMMENT '电导低字节',
  `CONDUCTION_N` decimal(10,4) DEFAULT NULL COMMENT '电导值',
  `CONDUCTIONUNIT_V` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '电导单位',
  `RUNTIME_D` datetime DEFAULT NULL COMMENT '数据采集时间',
  `STATUS_N` decimal(2,0) DEFAULT NULL COMMENT '电池状态：0:绿色正常，1：黄色警告，2红色警告',
  `BTRRCORD_V` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '电池编号',
  `CUR_HL_INNER_N` decimal(10,4) DEFAULT NULL COMMENT '混流排内阻',
  `CUR_ELECTRIC_N` decimal(10,4) DEFAULT NULL COMMENT '电流',
  `CUR_TEMPERATURE_N` decimal(10,4) DEFAULT NULL COMMENT '电池温度',
  `FORCASTVOLUME_N` decimal(10,4) DEFAULT NULL COMMENT '预估容量',
  PRIMARY KEY (`RECORD_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='电池的历史状态信息表' AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `bt_statics`
--

CREATE TABLE IF NOT EXISTS `bt_statics` (
  `RECORD_ID` int(11) NOT NULL AUTO_INCREMENT,
  `BTKEY_V` varchar(255) COLLATE utf8_unicode_ci NOT NULL COMMENT '电池组编码,这个是人工输入的,数据采集时用到的',
  `TIMESTAMP_V` date DEFAULT NULL COMMENT '插入时间,用于确定用户在将数据临时插入时确定插入的数据时间,用于向正式表中插入使用',
  `BASE_N` int(11) DEFAULT NULL COMMENT '基站编码',
  `BTTYPEKEY_V` int(11) DEFAULT NULL COMMENT '电池类型编码来自dict_battery中的record_id',
  `BTSERIALNO_V` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '电池序列号',
  `HVOL_N` decimal(10,0) DEFAULT NULL COMMENT '电压高字节',
  `LVOL_N` decimal(10,0) DEFAULT NULL COMMENT '电压低字节',
  `VOL_N` decimal(10,4) DEFAULT NULL COMMENT '电压值',
  `VOLUNIT_V` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '电压单位',
  `HINTER_N` decimal(10,0) DEFAULT NULL COMMENT '内阻高字节',
  `LINTER_N` decimal(10,0) DEFAULT NULL COMMENT '内阻低字节',
  `INTER_N` decimal(10,4) DEFAULT NULL COMMENT '内阻值',
  `INTERUNIT_V` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '内阻单位',
  `HCONDUCTION_N` decimal(10,0) DEFAULT NULL COMMENT '电导高字节',
  `LCONDUCTION_N` decimal(10,0) DEFAULT NULL COMMENT '电导低字节',
  `CONDUCTION_N` decimal(10,4) DEFAULT NULL COMMENT '电导值',
  `CONDUCTIONUNIT_V` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '电导单位',
  `RUNTIME_D` datetime DEFAULT NULL COMMENT '数据采集时间',
  `STATUS_N` decimal(2,0) DEFAULT NULL COMMENT '电池状态：0:绿色正常，1：黄色警告，2红色警告',
  `BACKLOAD_N` decimal(10,4) DEFAULT NULL COMMENT '后备负载',
  `BTRRCORD_V` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '电池编号',
  `CUR_HL_INNER_N` decimal(10,4) DEFAULT NULL COMMENT '混流排内阻',
  `CUR_ELECTRIC_N` decimal(10,4) DEFAULT NULL COMMENT '电流',
  `CUR_TEMPERATURE_N` decimal(10,4) DEFAULT NULL COMMENT '电池温度',
  `FORCASTVOLUME_N` decimal(10,2) DEFAULT NULL COMMENT '预估容量',
  PRIMARY KEY (`RECORD_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='用来形成预估容量公式的统计数据' AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `dict_battery`
--

CREATE TABLE IF NOT EXISTS `dict_battery` (
  `RECORD_ID` int(11) NOT NULL AUTO_INCREMENT,
  `BATTERYSORT_V` int(11) DEFAULT NULL COMMENT '电池类型来自dict_battery_sort中的recordid',
  `MANCODE_V` int(11) DEFAULT NULL COMMENT '制造商名称代码，来自dict_manufacturer的recordid',
  `BATTERYTYPE_V` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '电池型号类似某一类电池名字比如 T2003',
  `VOLTAGE_V` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '标称电压',
  `STDINNER_V` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '标称内阻',
  `STDVOLUME_V` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '标称容量',
  `CREATE_DATE` date DEFAULT NULL,
  `CHARGEVOL_V` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '浮充电压',
  `ISINNER` decimal(1,0) DEFAULT NULL,
  `B0` varchar(128) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '预估容量第一参数:y=b0+b1*x',
  `B1` varchar(128) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '预估容量第二参数:y=b0+b1*x',
  `YELLOWVALUE_N` decimal(10,4) DEFAULT NULL COMMENT '内阻黄色经验值',
  `REDVALUE_N` decimal(10,4) DEFAULT NULL COMMENT '内阻红色色经验值',
  `REMARK_V` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`RECORD_ID`),
  UNIQUE KEY `index_battery_unique` (`MANCODE_V`,`BATTERYTYPE_V`) USING HASH
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='电池型号,型号的名字 等记录电池的基本类型如制造商 电池规格' AUTO_INCREMENT=4 ;

-- --------------------------------------------------------

--
-- 表的结构 `dict_battery_sort`
--

CREATE TABLE IF NOT EXISTS `dict_battery_sort` (
  `RECORD_ID` int(11) NOT NULL AUTO_INCREMENT,
  `SORTNAME_V` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '电池类型，比如铅酸类 锂电池类',
  `REMARK_V` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '备注',
  `CREATE_DATE` datetime DEFAULT NULL,
  PRIMARY KEY (`RECORD_ID`),
  UNIQUE KEY `index_battery_sort_name_unique` (`SORTNAME_V`) USING HASH
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='电池类型表,比如铅酸电池 锂电池等' AUTO_INCREMENT=3 ;

-- --------------------------------------------------------

--
-- 表的结构 `dict_check_condition`
--

CREATE TABLE IF NOT EXISTS `dict_check_condition` (
  `RECORD_ID` int(11) NOT NULL AUTO_INCREMENT,
  `ITEM_NAME` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `TYPE_VALUE` int(11) NOT NULL,
  PRIMARY KEY (`RECORD_ID`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=5 ;

--
-- 转存表中的数据 `dict_check_condition`
--

INSERT INTO `dict_check_condition` (`RECORD_ID`, `ITEM_NAME`, `TYPE_VALUE`) VALUES
(1, '电池组黄色警告(红色单体最大数)', 3),
(2, '电池组绿色正常(红色单体最大数)', 1),
(3, '电池组绿色正常(黄色单体最大数)', 3),
(4, '电池组黄色警告(黄色单体最大数)', 5);

-- --------------------------------------------------------

--
-- 表的结构 `dict_manufacturer`
--

CREATE TABLE IF NOT EXISTS `dict_manufacturer` (
  `RECORD_ID` int(11) NOT NULL AUTO_INCREMENT,
  `MANNAME_V` varchar(50) COLLATE utf8_unicode_ci NOT NULL COMMENT '制造商名称',
  `REMARK_V` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '备注',
  `CREATE_DATE` datetime DEFAULT NULL,
  PRIMARY KEY (`RECORD_ID`),
  UNIQUE KEY `index_manname_unique` (`MANNAME_V`) USING HASH
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='制造商表' AUTO_INCREMENT=3 ;

-- --------------------------------------------------------

--
-- 表的结构 `mtsys_base`
--

CREATE TABLE IF NOT EXISTS `mtsys_base` (
  `BASE_ID` int(11) NOT NULL AUTO_INCREMENT,
  `PROVINCE_ID` int(11) NOT NULL COMMENT '对应的省级单位的编号',
  `CITY_ID` int(11) NOT NULL COMMENT '对应的市级单位的编号',
  `COUNTY_ID` int(11) NOT NULL COMMENT '对应的县区级单位的编号',
  `LEVEL_N` int(11) NOT NULL DEFAULT '4' COMMENT '基站单位的级别编号为4',
  `BASE_NAME` varchar(50) COLLATE utf8_unicode_ci NOT NULL COMMENT '基站的名字',
  `BASE_TYPE` int(11) NOT NULL COMMENT '基站类型,来自mtsys_base中的recordid。用于记录基站类型比如vip',
  PRIMARY KEY (`BASE_ID`),
  UNIQUE KEY `index_county_name_unique` (`PROVINCE_ID`,`CITY_ID`,`COUNTY_ID`,`BASE_NAME`) USING HASH
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='基站表' AUTO_INCREMENT=2 ;

-- --------------------------------------------------------

--
-- 表的结构 `mtsys_basetype`
--

CREATE TABLE IF NOT EXISTS `mtsys_basetype` (
  `RECORD_ID` int(11) NOT NULL AUTO_INCREMENT COMMENT '基站',
  `BASE_TYPE` varchar(255) COLLATE utf8_unicode_ci NOT NULL COMMENT '基站类型，vip viip等',
  `YELTHRMAXRED_N` int(11) NOT NULL COMMENT '电池组黄色警告值红色单体最大数',
  `YELTHRMAXYEL_N` int(11) NOT NULL COMMENT '电池组黄色警告值黄色单体最大数',
  `GRETHRMAXYEL_N` int(11) NOT NULL COMMENT '电池组绿色警告值黄色单体最大数',
  `GRETHRMAXRED_N` int(11) NOT NULL COMMENT '电池组绿色警告值红色色单体最大数',
  `REMARK` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '备注',
  `CREATE_DATE` datetime DEFAULT NULL,
  PRIMARY KEY (`RECORD_ID`),
  UNIQUE KEY `index_base_type_unique` (`BASE_TYPE`) USING HASH
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=3 ;

-- --------------------------------------------------------

--
-- 表的结构 `mtsys_city`
--

CREATE TABLE IF NOT EXISTS `mtsys_city` (
  `CITY_ID` int(11) NOT NULL AUTO_INCREMENT,
  `PROVINCE_ID` int(11) NOT NULL COMMENT '对应的上级省级单位',
  `CITY_NAME` varchar(50) COLLATE utf8_unicode_ci NOT NULL COMMENT '市级单位的名字',
  `LEVEL_N` int(11) NOT NULL DEFAULT '2' COMMENT '市级单位的级别默认为2',
  PRIMARY KEY (`CITY_ID`),
  UNIQUE KEY `index_cityname_unique` (`CITY_NAME`,`PROVINCE_ID`) USING BTREE
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='市级单位表' AUTO_INCREMENT=2 ;

-- --------------------------------------------------------

--
-- 表的结构 `mtsys_county`
--

CREATE TABLE IF NOT EXISTS `mtsys_county` (
  `COUNTY_ID` int(11) NOT NULL AUTO_INCREMENT,
  `CITY_ID` int(11) NOT NULL COMMENT '对应的市级单位的编号',
  `LEVEL_N` int(11) NOT NULL DEFAULT '3' COMMENT '县区级单位的级别默认为3',
  `COUNTY_NAME` varchar(50) COLLATE utf8_unicode_ci NOT NULL COMMENT '县区单位的名字',
  PRIMARY KEY (`COUNTY_ID`),
  UNIQUE KEY `index_county_unique` (`CITY_ID`,`COUNTY_NAME`) USING HASH
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='县区级单位表' AUTO_INCREMENT=2 ;

-- --------------------------------------------------------

--
-- 表的结构 `mtsys_province`
--

CREATE TABLE IF NOT EXISTS `mtsys_province` (
  `PROVINCE_ID` int(11) NOT NULL AUTO_INCREMENT,
  `LEVEL_N` int(11) NOT NULL DEFAULT '1' COMMENT '单位级别省级单位为1',
  `PROVINCE_NAME` varchar(50) COLLATE utf8_unicode_ci NOT NULL COMMENT '省级单位名字',
  PRIMARY KEY (`PROVINCE_ID`),
  UNIQUE KEY `province_unique` (`PROVINCE_NAME`) USING HASH
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='省级单位表' AUTO_INCREMENT=2 ;

-- --------------------------------------------------------

--
-- 表的结构 `mtsys_role`
--

CREATE TABLE IF NOT EXISTS `mtsys_role` (
  `ROLE_ID` int(11) NOT NULL AUTO_INCREMENT COMMENT '角色ID',
  `ROLE_NAME` varchar(20) COLLATE utf8_unicode_ci NOT NULL COMMENT '角色名称',
  `CREATE_DATE` datetime DEFAULT NULL COMMENT '创建时间',
  `MARK_V` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '角色说明',
  PRIMARY KEY (`ROLE_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='角色表' AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `mtsys_role_func`
--

CREATE TABLE IF NOT EXISTS `mtsys_role_func` (
  `ROLE_ID` int(11) NOT NULL COMMENT '角色ID,来自mtsys_role中的role id',
  `FUNC_ID` int(11) NOT NULL COMMENT '功能ID,具体可操作的权限控制，可结合框架作对应的调整'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='角色功能对应表';

-- --------------------------------------------------------

--
-- 表的结构 `mtsys_user`
--

CREATE TABLE IF NOT EXISTS `mtsys_user` (
  `USER_ID` int(11) NOT NULL AUTO_INCREMENT COMMENT '用户ID',
  `ROLE_ID` int(10) NOT NULL COMMENT '用户功能角色ID来自mtsys_role中的role id',
  `USER_NAME` varchar(30) COLLATE utf8_unicode_ci NOT NULL COMMENT '用户名',
  `USER_PASSWORD` varchar(30) COLLATE utf8_unicode_ci NOT NULL COMMENT '密码',
  `REAL_NAME` varchar(50) COLLATE utf8_unicode_ci NOT NULL COMMENT '真实姓名',
  `ENABLE_FLAG` decimal(1,0) DEFAULT NULL COMMENT '是否可用',
  `CREATE_DATE` datetime DEFAULT NULL COMMENT '创建时间',
  `ORG_ID` int(11) NOT NULL COMMENT '用户所在单位,与省市县基站的标号对应',
  `LEVEL_N` int(11) NOT NULL COMMENT '1表示省 2表示市 3表示县 4表示base单位',
  `USER_EMAIL` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '用户电子邮件',
  PRIMARY KEY (`USER_ID`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='用户表' AUTO_INCREMENT=3 ;

--
-- 转存表中的数据 `mtsys_user`
--

INSERT INTO `mtsys_user` (`USER_ID`, `ROLE_ID`, `USER_NAME`, `USER_PASSWORD`, `REAL_NAME`, `ENABLE_FLAG`, `CREATE_DATE`, `ORG_ID`, `LEVEL_N`, `USER_EMAIL`) VALUES
(1, 1, 'wzy', '1', '1', '1', '2011-12-24 16:42:00', 1, 1, NULL);

-- --------------------------------------------------------

--
-- 表的结构 `mysys_btstype`
--

CREATE TABLE IF NOT EXISTS `mysys_btstype` (
  `ID` int(11) NOT NULL AUTO_INCREMENT COMMENT '电池组类型id',
  `NAME` varchar(128) DEFAULT NULL COMMENT '电池组类型名称',
  `YELTHRMAXRED_N` int(11) DEFAULT NULL COMMENT '电池组黄色警告值红色单体最大数',
  `YELTHRMAXYEL_N` int(11) DEFAULT NULL COMMENT '电池组黄色警告值黄色单体最大数',
  `GRETHRMAXYEL_N` int(11) DEFAULT NULL COMMENT '电池组绿色警告值黄色',
  `GRETHRMAXRED_N` int(11) DEFAULT NULL COMMENT '电池组绿色警告值红色色单体最大数',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `rights`
--

CREATE TABLE IF NOT EXISTS `rights` (
  `itemname` varchar(64) NOT NULL,
  `type` int(11) NOT NULL,
  `weight` int(11) DEFAULT NULL,
  PRIMARY KEY (`itemname`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- 转存表中的数据 `rights`
--

INSERT INTO `rights` (`itemname`, `type`, `weight`) VALUES
('admin', 2, 1),
('master', 2, 5);

-- --------------------------------------------------------

--
-- 表的结构 `tbl_btstype`
--

CREATE TABLE IF NOT EXISTS `tbl_btstype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `remarks` varchar(256) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

-- --------------------------------------------------------

--
-- 表的结构 `tbl_compute`
--

CREATE TABLE IF NOT EXISTS `tbl_compute` (
  `RECORD_ID` int(11) NOT NULL AUTO_INCREMENT,
  `BTKEY_V` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '电池组编码',
  `BASE_N` int(11) DEFAULT NULL COMMENT '基站编码',
  `BTTYPEKEY_V` int(11) DEFAULT NULL COMMENT '电池类型编码',
  `VOL_N` decimal(10,4) DEFAULT NULL COMMENT '电压值',
  `INTER_N` decimal(10,4) DEFAULT NULL COMMENT '内阻值',
  `FORCASTVOLUME_N` decimal(10,2) DEFAULT NULL COMMENT '预估容量',
  PRIMARY KEY (`RECORD_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='计算预估容量信息表' AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `tbl_event`
--

CREATE TABLE IF NOT EXISTS `tbl_event` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bts_id` varchar(128) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `event_str` varchar(256) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `event_des` varchar(256) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `create_time` date DEFAULT NULL,
  `extra` varchar(256) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `tbl_helper`
--

CREATE TABLE IF NOT EXISTS `tbl_helper` (
  `RECORD_ID` int(11) NOT NULL AUTO_INCREMENT,
  `MODULE_V` varchar(128) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `SUBSYSTEM_V` varchar(128) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `HELPER_V` text CHARACTER SET utf8 COLLATE utf8_unicode_ci,
  `CREATE_TIME` date DEFAULT NULL,
  PRIMARY KEY (`RECORD_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `tbl_pickdata`
--

CREATE TABLE IF NOT EXISTS `tbl_pickdata` (
  `RECORD_ID` int(11) NOT NULL AUTO_INCREMENT,
  `USER_ID` int(11) DEFAULT NULL COMMENT '用户ID，标识用户',
  `BTKEY_V` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '电池组编码',
  `BASENAME_V` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '基站名称',
  `SENSORNAME_V` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '传感器设备名称',
  `SENSOR_SETUP_NAME_V` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '传感器设备安装地址',
  `SENSOR_N` int(11) DEFAULT NULL COMMENT '电池组传感器标识',
  `BATTERY_N` int(11) DEFAULT NULL COMMENT '电池单体标识，标识第几节电池',
  `PICKEDTIME_D` datetime DEFAULT NULL,
  `VOL_N` decimal(10,4) DEFAULT NULL COMMENT '单体电压值',
  `ELEC_N` decimal(10,4) DEFAULT NULL COMMENT '单体电流值',
  `INTER_N` decimal(10,4) DEFAULT NULL COMMENT '单体内阻值',
  `HINTER_N` decimal(10,4) DEFAULT NULL COMMENT '汇流条内阻值',
  `TEMPER_N` decimal(10,4) DEFAULT NULL COMMENT '温度值',
  `STATUS_V` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `REMARK_V` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`RECORD_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='采集数据表' AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `tbl_profiles`
--

CREATE TABLE IF NOT EXISTS `tbl_profiles` (
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `tbl_profiles`
--

INSERT INTO `tbl_profiles` (`user_id`) VALUES
(1);

-- --------------------------------------------------------

--
-- 表的结构 `tbl_profiles_fields`
--

CREATE TABLE IF NOT EXISTS `tbl_profiles_fields` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `varname` varchar(50) NOT NULL,
  `title` varchar(255) NOT NULL,
  `field_type` varchar(50) NOT NULL,
  `field_size` int(3) NOT NULL DEFAULT '0',
  `field_size_min` int(3) NOT NULL DEFAULT '0',
  `required` int(1) NOT NULL DEFAULT '0',
  `match` varchar(255) NOT NULL DEFAULT '',
  `range` varchar(255) NOT NULL DEFAULT '',
  `error_message` varchar(255) NOT NULL DEFAULT '',
  `other_validator` varchar(5000) NOT NULL DEFAULT '',
  `default` varchar(255) NOT NULL DEFAULT '',
  `widget` varchar(255) NOT NULL DEFAULT '',
  `widgetparams` varchar(5000) NOT NULL DEFAULT '',
  `position` int(3) NOT NULL DEFAULT '0',
  `visible` int(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `varname` (`varname`,`widget`,`visible`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `tbl_sensors`
--

CREATE TABLE IF NOT EXISTS `tbl_sensors` (
  `RECORD_ID` int(11) NOT NULL AUTO_INCREMENT,
  `SENSORNAME_V` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `GROUPNAME_V` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '电池组名称',
  `BASENAME_V` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '基站名称',
  `PROVINCENAME_V` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '省级名称',
  `CITYNAME_V` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '市级名称',
  `COUNTRYNAME_V` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '县级名称',
  `SENSOR_SETUP_NAME_V` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '传感器设备安装地址',
  `SENSOR_N` int(11) DEFAULT NULL COMMENT '电池组传感器标识',
  `BATTERYNUM_N` int(11) DEFAULT NULL,
  `SENSOR_ADDR_N` int(11) DEFAULT NULL COMMENT '传感器命令地址，通过该地址采集数据',
  `COM_N` int(11) DEFAULT NULL COMMENT '串口号',
  `IP_V` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT 'IP地址',
  `SETUP_D` datetime DEFAULT NULL COMMENT '创建日期，通过创建日期计算使用年限',
  `REMARK_V` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`RECORD_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='传感器设备管理表' AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `tbl_setting`
--

CREATE TABLE IF NOT EXISTS `tbl_setting` (
  `RECORD_ID` int(11) NOT NULL AUTO_INCREMENT,
  `CYCLE_N` int(11) DEFAULT NULL,
  `TYPE_N` int(11) DEFAULT NULL,
  `BAUD_V` int(128) DEFAULT NULL,
  `PARITY_V` int(128) DEFAULT NULL,
  `DATABITS_N` int(11) DEFAULT NULL,
  `STOPBITS_N` int(11) DEFAULT NULL,
  PRIMARY KEY (`RECORD_ID`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- 转存表中的数据 `tbl_setting`
--

INSERT INTO `tbl_setting` (`RECORD_ID`, `CYCLE_N`, `TYPE_N`, `BAUD_V`, `PARITY_V`, `DATABITS_N`, `STOPBITS_N`) VALUES
(1, 1, 0, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- 表的结构 `tbl_suggestion`
--

CREATE TABLE IF NOT EXISTS `tbl_suggestion` (
  `RECORD_ID` int(11) NOT NULL AUTO_INCREMENT,
  `CONTEXT_V` text CHARACTER SET utf8 COLLATE utf8_unicode_ci,
  `USER_ID` int(11) DEFAULT NULL,
  `CREATE_TIME` date DEFAULT NULL,
  PRIMARY KEY (`RECORD_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `tbl_users`
--

CREATE TABLE IF NOT EXISTS `tbl_users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `email` varchar(128) NOT NULL,
  `activkey` varchar(128) NOT NULL DEFAULT '',
  `createtime` int(10) NOT NULL DEFAULT '0',
  `lastvisit` int(10) NOT NULL DEFAULT '0',
  `superuser` int(1) NOT NULL DEFAULT '0',
  `status` int(1) NOT NULL DEFAULT '0',
  `unit_id` varchar(128) DEFAULT NULL COMMENT '单位ID',
  `unit_level` int(4) NOT NULL COMMENT '单位级别',
  `telephone` varchar(255) DEFAULT NULL,
  `surname` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`),
  KEY `status` (`status`),
  KEY `superuser` (`superuser`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=61 ;

--
-- 转存表中的数据 `tbl_users`
--

INSERT INTO `tbl_users` (`id`, `username`, `password`, `email`, `activkey`, `createtime`, `lastvisit`, `superuser`, `status`, `unit_id`, `unit_level`, `telephone`, `surname`) VALUES
(1, 'admin', '21232f297a57a5a743894a0e4a801fc3', 'webmaster@example.com', '9a24eff8c15a6a141ece27eb6947da0f', 1261146094, 1346081640, 1, 1, '0', 0, '13588997766', '超管');

-- --------------------------------------------------------

--
-- 表的结构 `user`
--

CREATE TABLE IF NOT EXISTS `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

--
-- 限制导出的表
--

--
-- 限制表 `authassignment`
--
ALTER TABLE `authassignment`
  ADD CONSTRAINT `authassignment_ibfk_1` FOREIGN KEY (`itemname`) REFERENCES `authitem` (`name`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- 限制表 `authitemchild`
--
ALTER TABLE `authitemchild`
  ADD CONSTRAINT `authitemchild_ibfk_1` FOREIGN KEY (`parent`) REFERENCES `authitem` (`name`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `authitemchild_ibfk_2` FOREIGN KEY (`child`) REFERENCES `authitem` (`name`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- 限制表 `rights`
--
ALTER TABLE `rights`
  ADD CONSTRAINT `rights_ibfk_1` FOREIGN KEY (`itemname`) REFERENCES `authitem` (`name`) ON DELETE CASCADE ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
