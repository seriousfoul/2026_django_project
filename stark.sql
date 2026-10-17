BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "internal_banner" (
	"bannerid"	integer NOT NULL,
	"name"	varchar(30) NOT NULL,
	"imgpath"	varchar(100) NOT NULL,
	"enable"	bool NOT NULL,
	"addtime"	bigint NOT NULL,
	PRIMARY KEY("bannerid" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "internal_category" (
	"categoryid"	integer NOT NULL,
	"name"	varchar(30) NOT NULL,
	"enable"	bool NOT NULL,
	PRIMARY KEY("categoryid" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "internal_company" (
	"name"	varchar(30) NOT NULL,
	"email"	varchar(100) NOT NULL,
	"address"	varchar(100) NOT NULL,
	"phone"	varchar(20) NOT NULL,
	"fax"	varchar(20) NOT NULL,
	"servicetime"	text NOT NULL,
	PRIMARY KEY("name")
);
CREATE TABLE IF NOT EXISTS "internal_downloads" (
	"downloadsid"	integer NOT NULL,
	"name"	varchar(30) NOT NULL,
	"filepath"	varchar(100) NOT NULL,
	"size"	varchar(30) NOT NULL,
	"version"	varchar(30) NOT NULL,
	"info"	text NOT NULL,
	"addtime"	bigint NOT NULL,
	"lastUpdate"	bigint NOT NULL,
	PRIMARY KEY("downloadsid" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "internal_faq" (
	"faqid"	integer NOT NULL,
	"question"	varchar(200) NOT NULL,
	"answer"	text NOT NULL,
	"addtime"	bigint NOT NULL,
	"lastUpdate"	bigint NOT NULL,
	PRIMARY KEY("faqid" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "internal_featureinfo" (
	"featureinfoid"	integer NOT NULL,
	"title"	text NOT NULL,
	"content"	text NOT NULL,
	"addtime"	bigint NOT NULL,
	"lastUpdate"	bigint NOT NULL,
	"topic_id"	integer NOT NULL,
	PRIMARY KEY("featureinfoid" AUTOINCREMENT),
	FOREIGN KEY("topic_id") REFERENCES "internal_featuretype"("featuretypeid") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "internal_featuretype" (
	"featuretypeid"	integer NOT NULL,
	"name"	varchar(30) NOT NULL,
	"chinese_name"	text NOT NULL,
	"enable"	bool NOT NULL,
	PRIMARY KEY("featuretypeid" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "internal_form" (
	"formid"	integer NOT NULL,
	"companyname"	varchar(30) NOT NULL,
	"contactname"	varchar(10) NOT NULL,
	"email"	varchar(100) NOT NULL,
	"address"	varchar(100) NOT NULL,
	"phone"	varchar(20) NOT NULL,
	"title"	varchar(30) NOT NULL,
	"content"	text NOT NULL,
	"addtime"	bigint NOT NULL,
	PRIMARY KEY("formid" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "internal_history" (
	"historyid"	integer NOT NULL,
	"title"	varchar(30) NOT NULL,
	"content"	text NOT NULL,
	"addtime"	bigint NOT NULL,
	"lastUpdate"	bigint NOT NULL,
	PRIMARY KEY("historyid" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "internal_info" (
	"infoid"	integer NOT NULL,
	"title"	varchar(30) NOT NULL,
	"imgpath"	varchar(100) NOT NULL,
	"enable"	bool NOT NULL,
	"addtime"	bigint NOT NULL,
	PRIMARY KEY("infoid" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "internal_item" (
	"itemid"	integer NOT NULL,
	"name"	varchar(30) NOT NULL,
	"imgpath"	varchar(100) NOT NULL,
	"dimension"	text NOT NULL,
	"material"	varchar(100) NOT NULL,
	"info"	text NOT NULL,
	"addtime"	bigint NOT NULL,
	"lastUpdate"	bigint NOT NULL,
	"categoryid_id"	integer NOT NULL,
	PRIMARY KEY("itemid" AUTOINCREMENT),
	FOREIGN KEY("categoryid_id") REFERENCES "internal_category"("categoryid") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "internal_message" (
	"messageid"	integer NOT NULL,
	"read"	bool NOT NULL,
	"processed"	bool NOT NULL,
	"lastUpdate"	bigint NOT NULL,
	"formid_id"	integer NOT NULL,
	PRIMARY KEY("messageid" AUTOINCREMENT),
	FOREIGN KEY("formid_id") REFERENCES "internal_form"("formid") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "internal_news" (
	"newsid"	integer NOT NULL,
	"title"	varchar(30) NOT NULL,
	"content"	text NOT NULL,
	"addtime"	bigint NOT NULL,
	"lastUpdate"	bigint NOT NULL,
	PRIMARY KEY("newsid" AUTOINCREMENT)
);
CREATE INDEX IF NOT EXISTS "internal_featureinfo_topic_id_94a17cc0" ON "internal_featureinfo" (
	"topic_id"
);
CREATE INDEX IF NOT EXISTS "internal_item_categoryid_id_2c5b4aa0" ON "internal_item" (
	"categoryid_id"
);
CREATE INDEX IF NOT EXISTS "internal_message_formid_id_de999121" ON "internal_message" (
	"formid_id"
);
COMMIT;
