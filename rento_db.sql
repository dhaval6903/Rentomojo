-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Nov 28, 2024 at 08:46 AM
-- Server version: 5.7.26
-- PHP Version: 7.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rento_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `bill_tb`
--

DROP TABLE IF EXISTS `bill_tb`;
CREATE TABLE IF NOT EXISTS `bill_tb` (
  `bill_id` int(11) NOT NULL AUTO_INCREMENT,
  `b_id` int(11) NOT NULL,
  `bill_startdate` date NOT NULL,
  `bill_enddate` date NOT NULL,
  `bill_month` varchar(20) NOT NULL,
  `bill_rent` double NOT NULL,
  `bill_status` enum('Pending','Complete') NOT NULL,
  `bill_cdate` datetime NOT NULL,
  `bill_udate` datetime NOT NULL,
  PRIMARY KEY (`bill_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bill_tb`
--

INSERT INTO `bill_tb` (`bill_id`, `b_id`, `bill_startdate`, `bill_enddate`, `bill_month`, `bill_rent`, `bill_status`, `bill_cdate`, `bill_udate`) VALUES
(1, 2, '2024-12-27', '2025-01-26', '12-2024', 18600, 'Pending', '2024-11-27 11:18:48', '2024-11-27 11:18:48'),
(2, 1, '2024-11-27', '2024-12-27', '11-2024', 10560, 'Complete', '2024-11-27 11:20:41', '2024-11-27 13:35:28'),
(3, 2, '2024-11-27', '2024-12-27', '11-2024', 18600, 'Pending', '2024-11-27 11:20:41', '2024-11-27 11:20:41');

-- --------------------------------------------------------

--
-- Table structure for table `booking_tb`
--

DROP TABLE IF EXISTS `booking_tb`;
CREATE TABLE IF NOT EXISTS `booking_tb` (
  `b_id` int(11) NOT NULL AUTO_INCREMENT,
  `u_id` int(11) NOT NULL,
  `p_id` int(11) NOT NULL,
  `b_shippingadd` text,
  `b_pincode` int(11) DEFAULT NULL,
  `b_quantity` int(11) NOT NULL,
  `b_price` int(11) NOT NULL,
  `b_total` int(11) NOT NULL,
  `b_startdate` date NOT NULL,
  `b_enddate` date NOT NULL,
  `b_duration` varchar(20) NOT NULL,
  `b_duestatus` enum('Active','Deactive') NOT NULL,
  `b_status` enum('Cart','Pending','Complete','Cancel') NOT NULL,
  `b_cdate` datetime NOT NULL,
  `b_udate` datetime NOT NULL,
  `b_deposite` int(11) NOT NULL,
  PRIMARY KEY (`b_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `booking_tb`
--

INSERT INTO `booking_tb` (`b_id`, `u_id`, `p_id`, `b_shippingadd`, `b_pincode`, `b_quantity`, `b_price`, `b_total`, `b_startdate`, `b_enddate`, `b_duration`, `b_duestatus`, `b_status`, `b_cdate`, `b_udate`, `b_deposite`) VALUES
(1, 6, 20, 'Vavol', 382016, 1, 10560, 10560, '2024-11-27', '2024-12-27', '1', 'Active', 'Complete', '2024-11-27 10:54:14', '2024-11-27 10:54:51', 5280),
(2, 6, 15, 'Vavol', 382016, 1, 6200, 18600, '2024-11-27', '2025-02-25', '3', 'Active', 'Complete', '2024-11-27 10:54:25', '2024-11-27 10:54:51', 3100),
(3, 6, 5, 'cccxxc', 382014, 5, 851, 12765, '2024-11-28', '2025-02-26', '3', 'Active', 'Pending', '2024-11-28 10:00:33', '2024-11-28 11:34:22', 425),
(4, 6, 14, 'cccxxc', 382014, 5, 958, 14370, '2024-11-28', '2025-02-26', '3', 'Active', 'Pending', '2024-11-28 10:35:37', '2024-11-28 11:34:22', 479),
(5, 6, 20, NULL, NULL, 5, 10560, 52800, '2024-11-28', '2024-12-28', '1', 'Active', 'Cart', '2024-11-28 11:38:42', '2024-11-28 11:42:35', 5280),
(6, 6, 2, NULL, NULL, 3, 538, 58104, '2024-11-28', '2027-11-13', '36', 'Active', 'Cart', '2024-11-28 12:45:04', '2024-11-28 13:30:31', 269);

-- --------------------------------------------------------

--
-- Table structure for table `category_tb`
--

DROP TABLE IF EXISTS `category_tb`;
CREATE TABLE IF NOT EXISTS `category_tb` (
  `cat_id` int(11) NOT NULL AUTO_INCREMENT,
  `cat_name` varchar(50) NOT NULL,
  `cat_img` varchar(100) NOT NULL,
  `cat_status` enum('Active','Deactive') NOT NULL,
  `cat_cdate` datetime NOT NULL,
  `cat_udate` datetime NOT NULL,
  PRIMARY KEY (`cat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `category_tb`
--

INSERT INTO `category_tb` (`cat_id`, `cat_name`, `cat_img`, `cat_status`, `cat_cdate`, `cat_udate`) VALUES
(1, ' Packages', 'packages.jpg', 'Deactive', '2024-09-25 11:25:33', '2024-11-07 11:42:31'),
(2, 'Furniture', 'Furniture.jpg', 'Active', '2024-09-25 11:27:12', '2024-09-25 11:27:12'),
(3, 'Appliances', 'h.png', 'Active', '2024-09-25 11:27:58', '2024-09-25 11:27:58'),
(4, 'Electronics', 'Electronics.jpg', 'Active', '2024-09-25 11:29:24', '2024-09-25 11:29:24'),
(5, 'Bikes', 'Bikes.jpg', 'Active', '2024-09-25 11:30:40', '2024-11-12 15:11:14'),
(6, 'Baby & Kids', 'Baby & Kids.jpg', 'Deactive', '2024-09-25 11:32:15', '2024-11-07 11:43:18'),
(7, 'Fitness', 'Fitness.jpg', 'Active', '2024-09-25 11:33:23', '2024-09-25 11:33:23');

-- --------------------------------------------------------

--
-- Table structure for table `city_tb`
--

DROP TABLE IF EXISTS `city_tb`;
CREATE TABLE IF NOT EXISTS `city_tb` (
  `c_id` int(11) NOT NULL AUTO_INCREMENT,
  `c_name` varchar(50) NOT NULL,
  `c_status` enum('Active','Deactive') NOT NULL,
  `c_cdate` datetime NOT NULL,
  `c_udate` datetime NOT NULL,
  PRIMARY KEY (`c_id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `city_tb`
--

INSERT INTO `city_tb` (`c_id`, `c_name`, `c_status`, `c_cdate`, `c_udate`) VALUES
(2, 'Gandhinagar', 'Active', '2024-09-03 17:53:12', '2024-09-23 10:47:45'),
(3, 'Ahemedabad', 'Active', '2024-09-23 10:47:55', '2024-09-23 10:47:55'),
(5, 'Bangalore', 'Active', '2024-09-23 16:38:29', '2024-09-23 16:38:29'),
(6, 'Mumbai', 'Active', '2024-09-23 16:38:46', '2024-09-23 16:38:46'),
(7, 'Pune', 'Active', '2024-09-23 16:38:51', '2024-09-23 16:38:51'),
(8, 'Delhi', 'Active', '2024-09-23 16:39:01', '2024-09-23 16:39:01'),
(9, 'Noida', 'Active', '2024-09-23 16:39:11', '2024-09-23 16:39:11'),
(10, 'Gurgaon', 'Active', '2024-09-23 16:39:33', '2024-09-23 16:39:33'),
(11, 'Hydrabad', 'Active', '2024-09-23 16:40:24', '2024-09-23 16:40:24'),
(12, 'Chennai', 'Active', '2024-09-23 16:40:33', '2024-09-23 16:40:33'),
(13, 'Jaipur', 'Active', '2024-09-23 16:41:27', '2024-09-23 16:41:27'),
(14, 'Faridabad', 'Active', '2024-09-23 16:41:50', '2024-09-23 16:41:50'),
(15, 'Mysore', 'Active', '2024-09-23 16:42:13', '2024-09-23 16:42:13'),
(16, 'Ghaziyabad', 'Active', '2024-09-23 16:42:32', '2024-09-23 16:42:32'),
(17, 'Chandigarh', 'Active', '2024-09-23 16:42:57', '2024-09-23 16:42:57');

-- --------------------------------------------------------

--
-- Table structure for table `feedback_tb`
--

DROP TABLE IF EXISTS `feedback_tb`;
CREATE TABLE IF NOT EXISTS `feedback_tb` (
  `f_id` int(11) NOT NULL AUTO_INCREMENT,
  `f_name` varchar(50) NOT NULL,
  `f_contact` bigint(22) NOT NULL,
  `f_msg` text NOT NULL,
  `f_status` enum('Active','Deactive') NOT NULL,
  `f_cdate` datetime NOT NULL,
  `f_udate` datetime NOT NULL,
  PRIMARY KEY (`f_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `feedback_tb`
--

INSERT INTO `feedback_tb` (`f_id`, `f_name`, `f_contact`, `f_msg`, `f_status`, `f_cdate`, `f_udate`) VALUES
(1, 'Khushbu', 9313247890, 'I love the clothes from this website!! I am so glad I found them.....everything has been spot on, fits wonderfully, styles are trendy and lots to choose from!! Thanks for being here for us!!!', 'Active', '2024-09-09 11:49:13', '2024-09-20 11:49:13'),
(2, 'Rajshree', 9722233347, 'This is my very first order through site, and I am totally and completely satisfied! The fit is great and so are the prices. I will definitely return again and again...', 'Active', '2024-02-08 15:44:41', '2024-02-08 15:44:41'),
(3, 'Jinal', 9322887799, 'Thank you for offering these beautifully unique tops. They are flattering and gorgeous.\r\n', 'Active', '2024-02-08 15:45:37', '2024-02-08 15:45:37'),
(6, 'Himanshu Makwana', 8320115701, 'i like this website and their services', 'Active', '2024-09-20 16:02:43', '2024-09-20 16:02:43');

-- --------------------------------------------------------

--
-- Table structure for table `login_tb`
--

DROP TABLE IF EXISTS `login_tb`;
CREATE TABLE IF NOT EXISTS `login_tb` (
  `l_id` int(11) NOT NULL AUTO_INCREMENT,
  `l_username` varchar(50) NOT NULL,
  `l_password` varchar(20) NOT NULL,
  `l_img` varchar(100) NOT NULL,
  `l_lastseen` datetime NOT NULL,
  PRIMARY KEY (`l_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login_tb`
--

INSERT INTO `login_tb` (`l_id`, `l_username`, `l_password`, `l_img`, `l_lastseen`) VALUES
(1, 'admin', '12345', 'PROFILEIMG.jpeg', '2024-11-27 13:37:06');

-- --------------------------------------------------------

--
-- Table structure for table `payment_tb`
--

DROP TABLE IF EXISTS `payment_tb`;
CREATE TABLE IF NOT EXISTS `payment_tb` (
  `pay_id` int(11) NOT NULL AUTO_INCREMENT,
  `b_id` int(11) NOT NULL,
  `b_type` enum('Rent','Deposite') NOT NULL,
  `p_amount` int(11) NOT NULL,
  `p_status` enum('Success','Failed') NOT NULL,
  `p_cdate` datetime NOT NULL,
  PRIMARY KEY (`pay_id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `payment_tb`
--

INSERT INTO `payment_tb` (`pay_id`, `b_id`, `b_type`, `p_amount`, `p_status`, `p_cdate`) VALUES
(1, 2, 'Deposite', 3100, 'Success', '2024-11-27 10:55:33'),
(2, 1, 'Deposite', 5280, 'Success', '2024-11-27 10:55:33'),
(11, 3, 'Deposite', 425, 'Success', '2024-11-28 11:34:33'),
(10, 4, 'Deposite', 479, 'Success', '2024-11-28 11:34:33'),
(9, 1, 'Rent', 10560, 'Success', '2024-11-27 13:35:28');

-- --------------------------------------------------------

--
-- Table structure for table `product_tb`
--

DROP TABLE IF EXISTS `product_tb`;
CREATE TABLE IF NOT EXISTS `product_tb` (
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `cat_id` int(11) NOT NULL,
  `sub_id` int(11) NOT NULL,
  `c_id` int(11) NOT NULL,
  `p_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `p_details` text CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `p_img1` varchar(100) NOT NULL,
  `p_img2` varchar(100) NOT NULL,
  `p_img3` varchar(100) NOT NULL,
  `p_size` varchar(20) NOT NULL,
  `p_color` varchar(20) NOT NULL,
  `p_material` varchar(100) NOT NULL,
  `p_mrp` int(11) NOT NULL,
  `p_price` int(11) NOT NULL,
  `p_status` enum('Active','Deactive') NOT NULL,
  `p_cdate` datetime NOT NULL,
  `p_udate` datetime NOT NULL,
  `p_deposite` int(11) NOT NULL,
  PRIMARY KEY (`p_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `product_tb`
--

INSERT INTO `product_tb` (`p_id`, `cat_id`, `sub_id`, `c_id`, `p_name`, `p_details`, `p_img1`, `p_img2`, `p_img3`, `p_size`, `p_color`, `p_material`, `p_mrp`, `p_price`, `p_status`, `p_cdate`, `p_udate`, `p_deposite`) VALUES
(1, 2, 10, 2, 'Napster Metal Queen Bed', 'High-quality metal (Black)  \r\nIdeal mattress size (L x B): 72\" x 60\"\r\nPlywood mattress surface \r\nFootboard height: 17.2\"\r\nLightweight and rust-free ', 'bad1.jpg', 'bad13.jpg', 'bad13.jpg', 'Queen', 'Mate Black', 'Metal', 762, 352, 'Active', '2024-09-25 12:26:53', '2024-09-25 17:38:24', 176),
(2, 2, 10, 2, 'Miller Engineered Wood Non Storage Queen Bed', 'Space Saving \n\r\nDurable Build \n\r\nMeasurements may vary +/- 3 inches \n\r\nMattress size to fit- 72\"L x 60\"B \n', 'bad21.jpg', 'bad22.jpg', 'bad23.jpg', 'Double King', 'Wooden Brown', 'Engineered Wood', 847, 538, 'Active', '2024-09-25 13:27:30', '2024-09-25 13:27:30', 269),
(3, 2, 10, 2, 'Hutch Metal Queen Hydraulic Storage Bed', 'Honey brown finish \n\r\nIdeal mattress size (L x B): 72\" x 60\" \n\r\nSturdy metal frame \n\r\nLeathered headboard \n\r\nAnti-rust, durable coating', 'bad31.jpg', 'bad32.jpg', 'bad33.jpg', 'Single XL', 'Shining Brown', 'Solid Wood', 758, 363, 'Active', '2024-09-25 13:32:54', '2024-09-25 13:32:54', 182),
(4, 2, 11, 2, 'Titan Pro Gaming Chair', 'Metal body \n\r\nWooden furniture finish \n\r\nHigh back gaming chair \n\r\nHeadrest pillow and lumbar cushion \n\r\nTilt control & easy reclining', 'chair1.jpg', 'chair2.jpg', 'chair3.jpg', 'Midium', 'Red & Black', 'Foam & Metal', 1054, 528, 'Active', '2024-09-25 13:39:17', '2024-09-25 13:39:17', 264),
(5, 2, 11, 2, 'Roma Fabric Recliner', 'Reclines upto 160 degrees \n\r\nSingle step reclining \n\r\nSeat Height: 20\"', 'sofa1.jpg', 'sofa2.jpg', 'sofa3.jpg', 'Single', 'Iridium Grey', ' Roma Fabric', 1543, 851, 'Active', '2024-09-25 13:44:56', '2024-09-25 13:44:56', 425),
(6, 2, 11, 2, 'Caramel 4-Seater Wooden Coffee Table', 'Material/Finish: Antique cherry \n\r\nTable (LxBxH):36\"x36\"x14\" \n \r\nChair (LxBxH):17\"x17\"x12\" \n\r\nUpholstered matching stools \n\r\nIncludes 1 table+4 chair', 't1.jpg', 't2.jpg', 't3.jpg', '14 inch x 36 inch', 'Wenge', 'Solid Wood', 1092, 479, 'Active', '2024-09-25 13:50:38', '2024-09-25 13:50:38', 240),
(7, 2, 12, 2, 'Downey Wooden Bar Unit', 'Wood/Finish: Antique cherry \n\r\nStorage: 8 + 4 bottle grid \n\r\nHinged door mechanism \n\r\nTermite resistant', 't21.jpg', 't22.jpg', 't23.jpg', '29 inch x 22 inch', 'Brown', 'Solid Wood', 683, 342, 'Active', '2024-09-25 13:54:53', '2024-09-25 13:54:53', 171),
(8, 2, 12, 2, 'Poise 2-Seater Dining Table & Chairs', 'Material: Metal and solid wood \n\r\nTable (L x B x H): 33\" x 33\" x 30\" \n\r\nChair (L x B x H): 16\" x 16\" x 36\" \n\r\nMetal bodied chairs \n\r\nIncludes 1 table+2 chairs', 'd1.jpg', 'd2.jpg', 'd3.jpg', '30 inch x 33 inch', 'Brown & Black', 'Metal & Solid Wood', 870, 450, 'Active', '2024-09-25 13:59:23', '2024-09-25 13:59:23', 225),
(9, 2, 12, 2, 'Moonshine Bar Unit', 'Wood/Finish: Acacia wood \n\r\nSturdy metal frame \n\r\nStorage: 1 Drawer, 1 Cabinet \n\r\nMetal Hooks : Upto 9 glasses \n\r\nWine Grid: Up to 8 bottles', 'b1.jpg', 'b2.jpg', 'b3.jpg', '64 inch x 13 inch', 'Grey & Light-Brown', 'Wood & Metal', 931, 430, 'Active', '2024-09-25 14:04:42', '2024-09-25 14:04:42', 215),
(10, 4, 4, 2, 'Apple iPhone XS', 'Super Retina HD display\r\n\r\n5.8‑inch (diagonal) all‑screen OLED Multi‑Touch display\r\n\r\nHDR display\r\n\r\n2436‑by-1125‑pixel resolution at 458 ppi\r\n\r\n1,000,000:1 contrast ratio (typical)\r\n\r\nTrue Tone display\r\n\r\nWide color display (P3)\r\n\r\n3D Touch\r\n\r\n625 cd/m2 max brightness (typical)\r\n\r\nFingerprint-resistant oleophobic coating\r\n\r\nSupport for display of multiple languages and characters simultaneously', 'cbxs.jpg', 'iphone3.jpg', 'iphone3.jpg', '5.8\"', 'Gold', 'high-quality glass, Metal', 12130, 2860, 'Active', '2024-09-25 14:15:20', '2024-11-08 12:15:08', 1430),
(11, 4, 6, 2, 'Apple iPad Pro 11', 'Capacity/Size : 64GB/11\" \r\n\r\nWiFi + cellular data \r\n\r\n12MP rear camera \r\n\r\nFace ID \r\n\r\nComes with charger and USB cable', 'tab1.jpg', 'tab3.jpg', 'tab3.jpg', '11\"', 'Space Grey', 'Metal', 9230, 2419, 'Active', '2024-09-25 14:21:25', '2024-11-11 11:33:04', 1209),
(12, 4, 5, 2, 'Asus Tuf F15 Gaming Laptop', 'Capacity/Size : 15.6\" \n\r\nGeneration: Ryzen 7 \n\r\nProcessor: Ryzen 7 Hexa Core, RAM: 16 GB \n\r\nStorage:512GB SSD \n\r\nGraphics Card: 4 GB Graphics Card \n\r\nAsus/Acer (As per the availability)', 'l1_xK6vgty.jpg', 'l2_G9LsY1o.jpg', 'l3_56KagL7.jpg', '15.6\"', 'Fortress Gray', 'high-quality plastic', 18000, 5625, 'Active', '2024-09-25 14:29:04', '2024-09-25 14:29:04', 2812),
(13, 7, 1, 2, 'Motorized Treadmill AF 517', 'Max. user weight: 100kg \r\n\r\nSpeed: 0.8 -14 Kmph \r\n\r\nElevation: 3 levels, manual \r\n\r\nMonitor distance, time, calories, heart-rate \r\n\r\nBuilt-in 14 programs, 12 preset modes', 't1_Lk8WLq8.jpg', 't3_mMFoa9K.jpg', 't3_mMFoa9K.jpg', '65\" x 29\"', 'Black', 'Metal', 4268, 2810, 'Active', '2024-09-25 14:35:51', '2024-11-11 11:32:43', 1405),
(14, 7, 2, 2, 'HRX Willie Exercise Bike', 'Magnetic resistance 8 level \r\n\r\nMax user weight 120 Kg \r\n\r\nLCD Display & Tablet Holder \r\n\r\nLocking Pedal \r\n\r\nEasy to Move around & Store', 'bike1.jpg', 'bike3.jpg', 'bike3.jpg', '43\" x 20\"', 'Black', 'Metal', 1440, 958, 'Active', '2024-09-25 14:40:02', '2024-11-11 11:32:25', 479),
(15, 7, 3, 2, '5D Luxury Massage Chair with Ai Voice Command', 'Double layer airbag belt \n\r\nMassage Intensities 6 gears \n\r\nWaist hip swing massage \n\r\nShoulder height detection', 'm1.jpg', 'm2.jpg', 'm3.jpg', '57\" x 57\"', 'Matte Blue, Black', 'Matte & Metal', 12554, 6200, 'Active', '2024-09-25 14:43:51', '2024-09-25 14:43:51', 3100),
(16, 7, 3, 3, 'Massage Chair with Ai Voice Command', 'Double layer airbag belt \r\n\r\nMassage Intensities 6 gears \r\n\r\nWaist hip swing massage \r\n\r\nShoulder height detection', '4d-massage-chairfull-jrv9-1-768x768.jpg', '4d-massage-chairfull-jrv9-9-768x768.jpg', 'm3.jpg', '57\" x 57\"', 'Matte Blue, Black', 'Matte & Metal', 12554, 6200, 'Active', '2024-09-25 14:43:51', '2024-09-26 17:49:36', 3100),
(17, 7, 2, 3, 'Exercise Bike', 'Magnetic resistance 8 level \r\n\r\nMax user weight 120 Kg \r\n\r\nLCD Display & Tablet Holder \r\n\r\nLocking Pedal \r\n\r\nEasy to Move around & Store', '81iEmlGMqRL._SX679_.jpg', 'bike3.jpg', 'bike3.jpg', '43\" x 20\"', 'Black', 'Metal', 1440, 958, 'Active', '2024-09-25 14:40:02', '2024-11-11 11:32:02', 479),
(18, 2, 10, 3, 'Engineered Wood Queen Bed', 'Space Saving \r\n\r\nDurable Build \r\n\r\nMeasurements may vary +/- 3 inches \r\n\r\nMattress size to fit- 72\"L x 60\"B \r\n', 'bad21.jpg', 'bad22.jpg', 'bad23.jpg', 'Double King', 'Wooden Brown', 'Engineered Wood', 847, 538, 'Active', '2024-09-25 13:27:30', '2024-09-25 13:27:30', 269),
(19, 4, 5, 3, 'Asus Tuf A15 Gaming Laptop', 'Capacity/Size : 15.6\" \r\n\r\nGeneration: Ryzen 7 \r\n\r\nProcessor: Ryzen 7 Hexa Core, RAM: 16 GB \r\n\r\nStorage:512GB SSD \r\n\r\nGraphics Card: 4 GB Graphics Card \r\n\r\nAsus/Acer (As per the availability)', 'a15.jpg', 'l3_56KagL7.jpg', 'l3_56KagL7.jpg', '15.6\"', 'Fortress Gray', 'high-quality plastic', 18000, 5625, 'Active', '2024-09-25 14:29:04', '2024-09-26 17:46:42', 2812),
(20, 5, 13, 2, 'Royal reborn classic - Powered by RB', 'Braking System: Dual-channel ABS for improved safety\r\nInstrument Cluster: Combination of analogue speedometer and LCD display\r\nComfort: Ergonomically designed seat for long rides\r\nTyre Size: Front 90/90-19, Rear 120/80-18\r\nColors Available: 11 different color options including Halcyon Black, Madras Red, and Emerald', '1.jpg', '2.jpg', '3.jpg', 'Regular', 'Matte Blue, Black', 'high-quality Metal', 16720, 10560, 'Active', '2024-11-12 15:20:29', '2024-11-12 15:20:29', 5280);

-- --------------------------------------------------------

--
-- Table structure for table `subcategory_tb`
--

DROP TABLE IF EXISTS `subcategory_tb`;
CREATE TABLE IF NOT EXISTS `subcategory_tb` (
  `sub_id` int(11) NOT NULL AUTO_INCREMENT,
  `cat_id` int(11) NOT NULL,
  `sub_name` varchar(20) NOT NULL,
  `sub_img` varchar(100) NOT NULL,
  `sub_status` enum('Active','Deactive') NOT NULL,
  `sub_cdate` datetime NOT NULL,
  `sub_udate` datetime NOT NULL,
  PRIMARY KEY (`sub_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `subcategory_tb`
--

INSERT INTO `subcategory_tb` (`sub_id`, `cat_id`, `sub_name`, `sub_img`, `sub_status`, `sub_cdate`, `sub_udate`) VALUES
(1, 7, 'Treadmills', 'Treadmills.jpg', 'Active', '2024-09-25 11:35:19', '2024-09-25 11:35:19'),
(2, 7, ' Exercise bikes', 'Exercise bikes.jpg', 'Active', '2024-09-25 11:38:21', '2024-09-25 11:38:21'),
(3, 7, 'Massagers', 'Massagers.jpg', 'Active', '2024-09-25 11:40:04', '2024-09-25 11:40:04'),
(4, 4, 'Smartphones', 'Smartphones.jpg', 'Active', '2024-09-25 11:41:55', '2024-09-25 11:41:55'),
(5, 4, 'Laptops', 'Laptops.jpg', 'Active', '2024-09-25 11:43:23', '2024-09-25 11:43:23'),
(6, 4, 'Tablets', 'Tablets.jpg', 'Active', '2024-09-25 11:46:16', '2024-09-25 11:46:16'),
(7, 3, 'Washing machines', 'Washing machines_bn9rHFE.jpg', 'Active', '2024-09-25 11:55:39', '2024-11-07 15:06:00'),
(8, 3, ' Air coolers', 'cooler-removebg-preview.png', 'Active', '2024-09-25 12:00:25', '2024-11-07 15:07:09'),
(9, 3, 'Television', 'tv_f5IKjvM.jpg', 'Active', '2024-09-25 12:05:05', '2024-09-25 12:05:05'),
(10, 2, 'Bedroom', 'Bedroom.jpg', 'Active', '2024-09-25 12:08:23', '2024-09-25 12:08:23'),
(11, 2, 'Living Room', 'Living room.jpg', 'Active', '2024-09-25 12:11:28', '2024-09-25 12:11:28'),
(12, 2, 'Kitchen & Dining', 'dining.jpg', 'Active', '2024-09-25 12:14:35', '2024-11-07 12:30:17'),
(13, 5, 'Motorbikes', '195e0ddc-b9ab-4138-80f5-457cc05c5f6f.jpg', 'Active', '2024-11-12 15:15:29', '2024-11-12 15:15:29');

-- --------------------------------------------------------

--
-- Table structure for table `user_tb`
--

DROP TABLE IF EXISTS `user_tb`;
CREATE TABLE IF NOT EXISTS `user_tb` (
  `u_id` int(11) NOT NULL AUTO_INCREMENT,
  `u_name` varchar(50) NOT NULL,
  `u_contact` bigint(22) NOT NULL,
  `u_address` text NOT NULL,
  `u_img` varchar(100) NOT NULL,
  `u_password` varchar(20) NOT NULL,
  `u_status` enum('Active','Deactive') NOT NULL,
  `u_cdate` datetime NOT NULL,
  `u_udate` datetime NOT NULL,
  PRIMARY KEY (`u_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_tb`
--

INSERT INTO `user_tb` (`u_id`, `u_name`, `u_contact`, `u_address`, `u_img`, `u_password`, `u_status`, `u_cdate`, `u_udate`) VALUES
(5, 'khushbu', 9537433214, 'ewd', '21.png', '3444', 'Active', '2024-09-18 18:13:31', '2024-09-18 18:13:31'),
(1, 'Ria Verani', 9725510295, 'C-504 Sahyog Greens Gandhinagar', 'whiteshirt_FDK0fjL.jpeg', '12345', 'Active', '2024-09-09 15:19:55', '2024-09-21 12:31:34'),
(3, 'Urvi Jam', 9313932817, '9 Pragati Residency Vadtal Anand', '9253960_5wed7J7.jpg', '123456', 'Active', '2024-02-08 15:21:33', '2024-11-09 17:41:02'),
(6, 'DHAVALKUMAR G CHAUHAN', 9558174609, 'J-204,SHUBHAM RESIDENCY,VAVOL,NR KOLAVADA,GANDHINAGAR', '307ce493-b254-4b2d-8ba4-d12c080d6651.jpg', '123456789', 'Active', '2024-09-20 14:46:10', '2024-11-28 14:16:09');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
