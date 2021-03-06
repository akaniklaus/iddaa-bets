-- login as root to mysql and run
CREATE DATABASE sportbets_db;
CREATE USER 'sportbets'@'localhost' IDENTIFIED BY 'sportbets';
GRANT ALL PRIVILEGES ON sportbets_db.* TO 'sportbets'@'localhost';

-- Then login with the new user and run the following
-- mysql -u sportbets -psportbets sportbets_db

CREATE TABLE tbl_Ratios(
    `weekID` int(11) NOT NULL,
    `matchID` int(11) NOT NULL,
    `r1` double DEFAULT NULL,
    `r2` double DEFAULT NULL,
    `r3` double DEFAULT NULL,
    `r4` double DEFAULT NULL,
    `r5` double DEFAULT NULL,
    `r6` double DEFAULT NULL,
    `r7` double DEFAULT NULL,
    `r8` double DEFAULT NULL,
    `r9` double DEFAULT NULL,
    `r10` double DEFAULT NULL,
    `r11` double DEFAULT NULL,
    `r12` double DEFAULT NULL,
    `r13` double DEFAULT NULL,
    `r14` double DEFAULT NULL,
    `r15` double DEFAULT NULL,
    `r16` double DEFAULT NULL,
    `r17` double DEFAULT NULL,
    `r18` double DEFAULT NULL,
    `r19` double DEFAULT NULL,
    `r20` double DEFAULT NULL,
    `r21` double DEFAULT NULL,
    `r22` double DEFAULT NULL,
    `r23` double DEFAULT NULL,
    `r24` double DEFAULT NULL,
    `r25` double DEFAULT NULL,
    `r26` double DEFAULT NULL,
    `r27` double DEFAULT NULL,
    `r28` double DEFAULT NULL,
    `r29` double DEFAULT NULL,
    `r30` double DEFAULT NULL,
    `r31` double DEFAULT NULL,
    `r32` double DEFAULT NULL,
    `r33` double DEFAULT NULL,
    `r34` double DEFAULT NULL,
    `r35` double DEFAULT NULL,
    `r36` double DEFAULT NULL,
    `r37` double DEFAULT NULL,
    `r38` double DEFAULT NULL,
    `r39` double DEFAULT NULL,
    `r40` double DEFAULT NULL,
    `r41` double DEFAULT NULL,
    `r42` double DEFAULT NULL,
    `r43` double DEFAULT NULL,
    `r44` double DEFAULT NULL,
    `r45` double DEFAULT NULL,
    `r46` double DEFAULT NULL,
    `r47` double DEFAULT NULL,
    `r48` double DEFAULT NULL,
    `r49` double DEFAULT NULL,
    `r50` double DEFAULT NULL,
    `r51` double DEFAULT NULL,
    `r52` double DEFAULT NULL,
    `r53` double DEFAULT NULL,
    `r54` double DEFAULT NULL,
    `r55` double DEFAULT NULL,
    `r56` double DEFAULT NULL,
    `r57` double DEFAULT NULL,
    `r58` double DEFAULT NULL,
    `r59` double DEFAULT NULL,
    `r60` double DEFAULT NULL,
    `r61` double DEFAULT NULL,
    `r62` double DEFAULT NULL,
    `r63` double DEFAULT NULL,
    `r64` double DEFAULT NULL,
    `r65` double DEFAULT NULL,
    `r66` double DEFAULT NULL,
    `r67` double DEFAULT NULL,
    `r68` double DEFAULT NULL,
    `r69` double DEFAULT NULL,
    `r70` double DEFAULT NULL,
    `r71` double DEFAULT NULL,
	PRIMARY KEY (`weekID`,`matchID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE tbl_MatchInfo(
    `weekID` int(11) NOT NULL,
    `matchID` int(11) NOT NULL,
    `datetime` datetime NOT NULL,
    `league` varchar(5) NOT NULL,
    `team_1` varchar(40) CHARACTER SET utf8 NOT NULL,
    `team_2` varchar(40) CHARACTER SET utf8 NOT NULL,
    `mbs` tinyint DEFAULT NULL,
    `iy_goals_1` tinyint DEFAULT NULL,
    `iy_goals_2` tinyint DEFAULT NULL,
    `ms_goals_1` tinyint DEFAULT NULL,
    `ms_goals_2` tinyint DEFAULT NULL,
    `h1` tinyint NOT NULL,
    `h2` tinyint NOT NULL,
    `was_played` boolean NOT NULL DEFAULT 0,
  	PRIMARY KEY (`weekID`,`matchID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE tbl_Results(
    `weekID` int(11) NOT NULL,
    `matchID` int(11) NOT NULL,
	`r1` boolean NOT NULL DEFAULT 0,
	`r2` boolean NOT NULL DEFAULT 0,
	`r3` boolean NOT NULL DEFAULT 0,
	`r4` boolean NOT NULL DEFAULT 0,
	`r5` boolean NOT NULL DEFAULT 0,
	`r6` boolean NOT NULL DEFAULT 0,
	`r7` boolean NOT NULL DEFAULT 0,
	`r8` boolean NOT NULL DEFAULT 0,
	`r9` boolean NOT NULL DEFAULT 0,
	`r10` boolean NOT NULL DEFAULT 0,
	`r11` boolean NOT NULL DEFAULT 0,
	`r12` boolean NOT NULL DEFAULT 0,
	`r13` boolean NOT NULL DEFAULT 0,
	`r14` boolean NOT NULL DEFAULT 0,
	`r15` boolean NOT NULL DEFAULT 0,
	`r16` boolean NOT NULL DEFAULT 0,
	`r17` boolean NOT NULL DEFAULT 0,
	`r18` boolean NOT NULL DEFAULT 0,
	`r19` boolean NOT NULL DEFAULT 0,
	`r20` boolean NOT NULL DEFAULT 0,
	`r21` boolean NOT NULL DEFAULT 0,
	`r22` boolean NOT NULL DEFAULT 0,
	`r23` boolean NOT NULL DEFAULT 0,
	`r24` boolean NOT NULL DEFAULT 0,
	`r25` boolean NOT NULL DEFAULT 0,
	`r26` boolean NOT NULL DEFAULT 0,
	`r27` boolean NOT NULL DEFAULT 0,
	`r28` boolean NOT NULL DEFAULT 0,
	`r29` boolean NOT NULL DEFAULT 0,
	`r30` boolean NOT NULL DEFAULT 0,
	`r31` boolean NOT NULL DEFAULT 0,
	`r32` boolean NOT NULL DEFAULT 0,
	`r33` boolean NOT NULL DEFAULT 0,
	`r34` boolean NOT NULL DEFAULT 0,
	`r35` boolean NOT NULL DEFAULT 0,
	`r36` boolean NOT NULL DEFAULT 0,
	`r37` boolean NOT NULL DEFAULT 0,
	`r38` boolean NOT NULL DEFAULT 0,
	`r39` boolean NOT NULL DEFAULT 0,
	`r40` boolean NOT NULL DEFAULT 0,
	`r41` boolean NOT NULL DEFAULT 0,
	`r42` boolean NOT NULL DEFAULT 0,
	`r43` boolean NOT NULL DEFAULT 0,
	`r44` boolean NOT NULL DEFAULT 0,
	`r45` boolean NOT NULL DEFAULT 0,
	`r46` boolean NOT NULL DEFAULT 0,
	`r47` boolean NOT NULL DEFAULT 0,
	`r48` boolean NOT NULL DEFAULT 0,
	`r49` boolean NOT NULL DEFAULT 0,
	`r50` boolean NOT NULL DEFAULT 0,
	`r51` boolean NOT NULL DEFAULT 0,
	`r52` boolean NOT NULL DEFAULT 0,
	`r53` boolean NOT NULL DEFAULT 0,
	`r54` boolean NOT NULL DEFAULT 0,
	`r55` boolean NOT NULL DEFAULT 0,
	`r56` boolean NOT NULL DEFAULT 0,
	`r57` boolean NOT NULL DEFAULT 0,
	`r58` boolean NOT NULL DEFAULT 0,
	`r59` boolean NOT NULL DEFAULT 0,
	`r60` boolean NOT NULL DEFAULT 0,
	`r61` boolean NOT NULL DEFAULT 0,
	`r62` boolean NOT NULL DEFAULT 0,
	`r63` boolean NOT NULL DEFAULT 0,
	`r64` boolean NOT NULL DEFAULT 0,
	`r65` boolean NOT NULL DEFAULT 0,
	`r66` boolean NOT NULL DEFAULT 0,
	`r67` boolean NOT NULL DEFAULT 0,
	`r68` boolean NOT NULL DEFAULT 0,
	`r69` boolean NOT NULL DEFAULT 0,
	`r70` boolean NOT NULL DEFAULT 0,
	`r71` boolean NOT NULL DEFAULT 0,
	PRIMARY KEY (`weekID`,`matchID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS tbl_UserCoupon;
CREATE TABLE tbl_UserCoupon(
    `user_ID` int(11) NOT NULL,
    `couponID` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
    `start_date` datetime DEFAULT NULL,
    `end_date` datetime DEFAULT NULL,
	`won` boolean DEFAULT NULL,
	`ratio` double DEFAULT NULL,
  `couponPrice` double NOT NULL,
  `noCustomers` int(11) NOT NULL,
  `noPlayed` int(11) DEFAULT 0,
  `isCreated` boolean NOT NULL DEFAULT 0,
  `isReleased` boolean DEFAULT NULL,
  `couponCRating` double DEFAULT 0,
  `couponSRating` double DEFAULT 0,
  `couponRating` double DEFAULT 0,
	PRIMARY KEY (`couponID`, `user_ID`)
);

DROP TABLE IF EXISTS tbl_Users;
CREATE TABLE `tbl_Users` (
  `user_ID` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `facebookID` varchar(64) DEFAULT NULL,
  `userName` varchar(64) DEFAULT NULL,
  `winRatio` double DEFAULT NULL,
  `matchRatio` double DEFAULT NULL,
  `winMulti` double DEFAULT 1,
  `matchMulti` double DEFAULT 1,
  `moneyWonRatio` double DEFAULT NULL,
  `userCRating` double DEFAULT 1,
  `userSRating` double DEFAULT 1,
  PRIMARY KEY (`user_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS tbl_Coupons;
CREATE TABLE tbl_Coupons(
    `couponID` int(11) NOT NULL,
    `weekID` int(11) NOT NULL,
    `matchID` int(11) NOT NULL,
    `bet_index` int(11) NOT NULL,
	`won` boolean DEFAULT NULL,
  `ratio` double DEFAULT NULL,
	PRIMARY KEY (`couponID`, `weekID`,`matchID`)
);

DROP TRIGGER IF EXISTS updateUserCoupon;
delimiter //
CREATE TRIGGER updateUserCoupon BEFORE INSERT ON tbl_Coupons
    FOR EACH ROW
BEGIN
-- update start date and end date
    DECLARE sd datetime;
    DECLARE ed datetime;
	SELECT MIN(m.datetime), MAX(m.datetime)
	INTO sd, ed
	FROM tbl_MatchInfo m, tbl_Coupons c
	WHERE c.couponID=NEW.couponID AND m.weekID=c.weekID AND m.matchID=c.matchID;

	UPDATE tbl_UserCoupon
	SET start_date=sd, end_date=ed
	WHERE couponID=NEW.couponID;
END;//
delimiter ;

DROP TRIGGER IF EXISTS beforeStatistics;
delimiter //
CREATE TRIGGER beforeStatistics BEFORE UPDATE ON tbl_UserCoupon
    FOR EACH ROW
BEGIN

IF NEW.noPlayed >= NEW.noCustomers THEN
  SET NEW.isReleased = TRUE;
END IF;

END;//
delimiter ;

DROP TRIGGER IF EXISTS afterStatistics;
delimiter //
CREATE TRIGGER afterStatistics AFTER UPDATE ON tbl_UserCoupon
    FOR EACH ROW
BEGIN
-- update start date and end date
  DECLARE wr double;
  DECLARE wm double;
  DECLARE mr double;
  DECLARE mm double;
  DECLARE wrc double;
  DECLARE ucr double;
  DECLARE usr double;

  SELECT SUM(a.won)/COUNT(a.won), AVG(a.won*a.ratio), SUM(b.won)/COUNT(b.won), AVG(b.won*b.ratio),
  SUM(a.won*a.noPlayed*a.couponPrice)/SUM(a.noPlayed*a.couponPrice),
  AVG(a.won*a.noPlayed*a.couponPrice*a.ratio)/(SUM(a.noPlayed*a.couponPrice)+1),
  AVG(a.isReleased * a.couponPrice * a.noPlayed)+1
  INTO wr, wm, mr, mm, wrc, ucr, usr
  FROM tbl_UserCoupon a, tbl_Coupons b
  WHERE user_ID=NEW.user_ID AND a.CouponID=b.CouponID;

  UPDATE tbl_Users
  SET winRatio=wr, matchRatio=wm, winMulti=mr, matchMulti=mm,
  moneyWonRatio=wrc, userCRating=ucr, userSRating=usr
  WHERE user_ID=NEW.user_ID;

  #UPDATE tbl_UserCoupon
  #SET couponCRating=(ucr*NEW.ratio)/NEW.couponPrice,
  #couponSRating=usr*NEW.couponPrice*(NEW.noPlayed+1),
  #couponRating=ucr*usr*NEW.ratio*(NEW.noPlayed+1)
  #WHERE user_ID=NEW.user_ID AND couponID=NEW.couponID;


END;//
delimiter ;
