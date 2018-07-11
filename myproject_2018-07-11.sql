# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.7.22)
# Database: myproject
# Generation Time: 2018-07-11 17:26:36 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table tblPostCategory
# ------------------------------------------------------------

CREATE TABLE `tblPostCategory` (
  `catId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `Category` varchar(20) NOT NULL DEFAULT '',
  PRIMARY KEY (`catId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `tblPostCategory` WRITE;
/*!40000 ALTER TABLE `tblPostCategory` DISABLE KEYS */;

INSERT INTO `tblPostCategory` (`catId`, `Category`)
VALUES
	(1,'Children'),
	(2,'Adults'),
	(3,'Others');

/*!40000 ALTER TABLE `tblPostCategory` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table tblpostdetails
# ------------------------------------------------------------

CREATE TABLE `tblpostdetails` (
  `PostId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `PostTitle` varchar(100) NOT NULL DEFAULT '',
  `Description` text NOT NULL,
  `UserId` int(11) NOT NULL,
  `Img` varchar(200) DEFAULT '',
  `catId` int(11) NOT NULL,
  PRIMARY KEY (`PostId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `tblpostdetails` WRITE;
/*!40000 ALTER TABLE `tblpostdetails` DISABLE KEYS */;

INSERT INTO `tblpostdetails` (`PostId`, `PostTitle`, `Description`, `UserId`, `Img`, `catId`)
VALUES
	(1,'hello malika','world for u',2,'http://res.cloudinary.com/myprojectx/image/upload/v1528796991/bztgag757s2lpes5h4wt.jpg',1),
	(2,'sunt aut facere repellat provident occaecati excepturi optio reprehenderit','quia et suscipit\\nsuscipit recusandae consequuntur expedita et cum\\nreprehenderit molestiae ut ut quas totam\\nnostrum rerum est autem sunt rem eveniet architecto',1,'https://res.cloudinary.com/myprojectx/image/upload/v1528186918/essjvaznikosini5s1se.png',2),
	(4,'qui est esse','est rerum tempore vitae\\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\\nqui aperiam non debitis possimus qui neque nisi nulla',1,'https://res.cloudinary.com/myprojectx/image/upload/v1528195946/eimwc3hdermwfm3h54rm.png',3),
	(6,'eum et est occaecati','ullam et saepe reiciendis voluptatem adipisci\\nsit amet autem assumenda provident rerum culpa\\nquis hic commodi nesciunt rem tenetur doloremque ipsam iure\\nquis sunt voluptatem rerum illo velit',42,'https://res.cloudinary.com/myprojectx/image/upload/v1528195892/ohwurq7mmcxacaswamir.png',1),
	(7,'Python','Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace. It provides constructs that enable clear programming on both small and large scales.[26]\n\nPython features a dynamic type system and automatic memory management. It supports multiple programming paradigms, including object-oriented, imperative, functional and procedural, and has a large and comprehensive standard library.[27]\n\nPython interpreters are available for many operating systems. CPython, the reference implementation of Python, is open source software[28] and has a community-based development model, as do nearly all of its variant implementations. CPython is managed by the non-profit Python Software Foundation.\nPython was conceived in the late 1980s,[29] and its implementation began in December 1989[30] by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to the ABC language (itself inspired by SETL)[31] capable of exception handling and interfacing with the Amoeba operating system.[7] Van Rossum remains Python\'s principal author. His continuing central role in Python\'s development is reflected in the title given to him by the Python community: Benevolent Dictator For Life (BDFL).\n\nOn the origins of Python, Van Rossum wrote in 1996:[32]\n\n...In December 1989, I was looking for a \"hobby\" programming project that would keep me occupied during the week around Christmas. My office ... would be closed, but I had a home computer, and not much else on my hands. I decided to write an interpreter for the new scripting language I had been thinking about lately: a descendant of ABC that would appeal to Unix/C hackers. I chose Python as a working title for the project, being in a slightly irreverent mood (and a big fan of Monty Python\'s Flying Circus).\n\n— Guido van Rossum\nPython 2.0 was released on 16 October 2000 and had many major new features, including a cycle-detecting garbage collector and support for Unicode. With this release, the development process became more transparent and community-backed.[33]\n\nPython 3.0 (initially called Python 3000 or py3k) was released on 3 December 2008 after a long testing period. It is a major revision of the language that is not completely backward-compatible with previous versions.[34] However, many of its major features have been backported to the Python 2.6.x[35] and 2.7.x version series, and releases of Python 3 include the 2to3 utility, which automates the translation of Python 2 code to Python 3.[36]\n\nPython 2.7\'s end-of-life date was initially set at 2015, then postponed to 2020 out of concern that a large body of existing code could not easily be forward-ported to Python 3.[37][38] In January 2017, Google announced work on a Python 2.7 to Go transcompiler to improve performance under concurrent workloads.',1,'http://res.cloudinary.com/myprojectx/image/upload/v1528887946/hg3a6cr0zg37ypb3tife.jpg',2),
	(8,'nesciunt quas odio','repudiandae veniam quaerat sunt sed\\nalias aut fugiat sit autem sed est\\nvoluptatem omnis possimus esse voluptatibus quis\\nest aut tenetur dolor neque',2,'https://res.cloudinary.com/myprojectx/image/upload/v1528195998/eqrsh55abggzptzyg58l.png',3),
	(9,'magnam facilis autem','dolore placeat quibusdam ea quo vitae\\nmagni quis enim qui quis quo nemo aut saepe\\nquidem repellat excepturi ut quia\\nsunt ut sequi eos ea sed quas',42,'https://res.cloudinary.com/myprojectx/image/upload/v1528186876/ieiu5ko1wpfwee4lgj0t.png',1),
	(10,'optio molestias id quia mala','quo et expedita modi cum officia vel magnindoloribus qui repudiandae nvero nisi sitnquos veniam quod sed accusamus veritatis ella',2,'http://res.cloudinary.com/myprojectx/image/upload/v1529339805/vw2xwyeytjvtu6vjjpzx.png',2),
	(11,'dolorum ut in voluptas mollitia et saepe quo animi','aut dicta possimus sint mollitia voluptas commodi quo doloremque\\niste corrupti reiciendis voluptatem eius rerum\\nsit cumque quod eligendi laborum minima\\nperferendis recusandae assumenda consectetur porro architecto ipsum ipsam',42,'http://res.cloudinary.com/myprojectx/image/upload/v1529425818/br9zjzg2cbevsephflih.png',3);

/*!40000 ALTER TABLE `tblpostdetails` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table tbluser
# ------------------------------------------------------------

CREATE TABLE `tbluser` (
  `UserId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `FirstName` varchar(45) NOT NULL DEFAULT '',
  `LastName` varchar(45) NOT NULL DEFAULT '',
  `Email` varchar(45) NOT NULL DEFAULT '',
  `Password` varchar(100) NOT NULL DEFAULT '',
  PRIMARY KEY (`UserId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `tbluser` WRITE;
/*!40000 ALTER TABLE `tbluser` DISABLE KEYS */;

INSERT INTO `tbluser` (`UserId`, `FirstName`, `LastName`, `Email`, `Password`)
VALUES
	(1,'Malika','Nallaperuma','malika@gmail.com','sha256$yWuS9YIy$b06c9b34730c721ff523c640efb2884b7fbcb73eb7e8ca4d7ad717efc27c1c02'),
	(2,'Tharaka','Abeyratne','tharaka@gmail.com','sha256$EOH9vAht$aebcb520bdb05f9908f9e709513a8e2d98da8b0f0c6af6beef21fcc4f5bf5206'),
	(42,'Leo','Messi','leo@gmail.com','sha256$BnlrkduG$764e8748224b85edfda57f4a0aa727070f40dce448da34f83dbeee208010db20');

/*!40000 ALTER TABLE `tbluser` ENABLE KEYS */;
UNLOCK TABLES;



--
-- Dumping routines (PROCEDURE) for database 'myproject'
--
DELIMITER ;;

# Dump of PROCEDURE spAddPost
# ------------------------------------------------------------

/*!50003 SET SESSION SQL_MODE="ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION"*/;;
/*!50003 CREATE*/ /*!50020 DEFINER=`root`@`localhost`*/ /*!50003 PROCEDURE `spAddPost`(IN `p_uid` INT(11), IN `p_postTitle` VARCHAR(100), IN `P_postDesc` TEXT, IN `p_img` VARCHAR(200))
BEGIN
insert into tblpostdetails(
    
    UserId,
    PostTitle,
    Description,
    Img
    
 )VALUES(
     
	p_uid,
    p_postTitle,
    p_postDesc,
    p_img
     
);
END */;;

/*!50003 SET SESSION SQL_MODE=@OLD_SQL_MODE */;;
# Dump of PROCEDURE spAuthenticateUser
# ------------------------------------------------------------

/*!50003 SET SESSION SQL_MODE="ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION"*/;;
/*!50003 CREATE*/ /*!50020 DEFINER=`root`@`localhost`*/ /*!50003 PROCEDURE `spAuthenticateUser`(IN `p_Email` VARCHAR(45))
BEGIN

	SELECT * FROM tblUser WHERE Email = p_Email;

END */;;

/*!50003 SET SESSION SQL_MODE=@OLD_SQL_MODE */;;
# Dump of PROCEDURE spCreateUser
# ------------------------------------------------------------

/*!50003 SET SESSION SQL_MODE="ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION"*/;;
/*!50003 CREATE*/ /*!50020 DEFINER=`root`@`localhost`*/ /*!50003 PROCEDURE `spCreateUser`(
IN p_FirstName varchar(45),
IN p_LastName varchar(45),
IN p_Email varchar(50),
IN p_Password varchar(80)
)
BEGIN

if ( select exists (select 1 from `tbluser` where `Email` = p_Email) ) THEN

    select 'Username Exists !!';

ELSE

insert into `tbluser`
(
    FirstName,
    LastName,
    Email,
    Password
)
values
(
    p_FirstName,
    p_LastName,
    p_Email,
    p_Password
);
END IF;

select LAST_INSERT_ID() from tbluser;
END */;;

/*!50003 SET SESSION SQL_MODE=@OLD_SQL_MODE */;;
# Dump of PROCEDURE spEditPost
# ------------------------------------------------------------

/*!50003 SET SESSION SQL_MODE="ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION"*/;;
/*!50003 CREATE*/ /*!50020 DEFINER=`root`@`localhost`*/ /*!50003 PROCEDURE `spEditPost`(
IN p_postId int(45),
IN p_postTitle varchar(45),
IN p_desc TEXT,
IN p_img varchar(200)
)
BEGIN

UPDATE `tblpostdetails` set postTitle = p_postTitle, `Description`= p_desc, Img= p_img where `PostId` = p_postId;

END */;;

/*!50003 SET SESSION SQL_MODE=@OLD_SQL_MODE */;;
# Dump of PROCEDURE spGetAllPostFromLoginUser
# ------------------------------------------------------------

/*!50003 SET SESSION SQL_MODE="ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION"*/;;
/*!50003 CREATE*/ /*!50020 DEFINER=`root`@`localhost`*/ /*!50003 PROCEDURE `spGetAllPostFromLoginUser`(IN `p_userid` INT(11))
    READS SQL DATA
BEGIN

select `PostId`,`PostTitle`,`Description`,`Img` from tblpostdetails where UserId = p_userid;

END */;;

/*!50003 SET SESSION SQL_MODE=@OLD_SQL_MODE */;;
# Dump of PROCEDURE spGetPosts
# ------------------------------------------------------------

/*!50003 SET SESSION SQL_MODE="ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION"*/;;
/*!50003 CREATE*/ /*!50020 DEFINER=`root`@`localhost`*/ /*!50003 PROCEDURE `spGetPosts`()
    READS SQL DATA
BEGIN

select * from tblpostdetails order by PostId;

END */;;

/*!50003 SET SESSION SQL_MODE=@OLD_SQL_MODE */;;
# Dump of PROCEDURE spGetSinglePost
# ------------------------------------------------------------

/*!50003 SET SESSION SQL_MODE="ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION"*/;;
/*!50003 CREATE*/ /*!50020 DEFINER=`root`@`localhost`*/ /*!50003 PROCEDURE `spGetSinglePost`(IN `p_id` INT(45))
    READS SQL DATA
BEGIN

select * from tblpostdetails where PostId = p_id;

END */;;

/*!50003 SET SESSION SQL_MODE=@OLD_SQL_MODE */;;
DELIMITER ;

/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
