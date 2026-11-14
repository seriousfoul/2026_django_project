BEGIN TRANSACTION;
DROP TABLE IF EXISTS "internal_banner";
CREATE TABLE "internal_banner" (
	"bannerid"	integer NOT NULL,
	"name"	varchar(30),
	"imgpath"	varchar(100) NOT NULL,
	"enable"	bool NOT NULL,
	"addtime"	bigint NOT NULL,
	PRIMARY KEY("bannerid" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "internal_category";
CREATE TABLE "internal_category" (
	"categoryid"	integer NOT NULL,
	"name"	varchar(30) NOT NULL,
	"enable"	bool NOT NULL,
	PRIMARY KEY("categoryid" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "internal_company";
CREATE TABLE "internal_company" (
	"name"	varchar(30) NOT NULL,
	"email"	varchar(100) NOT NULL,
	"address"	varchar(100) NOT NULL,
	"phone"	varchar(20) NOT NULL,
	"fax"	varchar(20),
	"servicetime"	text,
	PRIMARY KEY("name")
);
DROP TABLE IF EXISTS "internal_companylevel";
CREATE TABLE "internal_companylevel" (
	"companylevelid"	INTEGER NOT NULL,
	"level"	VARCHAR(6) NOT NULL,
	"name"	VARCHAR(30) NOT NULL,
	"grade"	VARCHAR(30) NOT NULL,
	"enable"	BOOLEAN NOT NULL DEFAULT 1,
	PRIMARY KEY("companylevelid" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "internal_downloads";
CREATE TABLE "internal_downloads" (
	"downloadsid"	integer NOT NULL,
	"name"	varchar(30) NOT NULL,
	"filepath"	varchar(100) NOT NULL,
	"size"	varchar(30) NOT NULL,
	"version"	varchar(30) NOT NULL,
	"info"	text,
	"addtime"	bigint NOT NULL,
	"lastUpdate"	bigint NOT NULL,
	PRIMARY KEY("downloadsid" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "internal_faq";
CREATE TABLE "internal_faq" (
	"faqid"	integer NOT NULL,
	"answer"	text NOT NULL,
	"addtime"	bigint NOT NULL,
	"lastUpdate"	bigint NOT NULL,
	"question"	text NOT NULL,
	PRIMARY KEY("faqid" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "internal_featureinfo";
CREATE TABLE "internal_featureinfo" (
	"featureinfoid"	integer NOT NULL,
	"title"	text NOT NULL,
	"content"	text NOT NULL,
	"addtime"	bigint NOT NULL,
	"lastUpdate"	bigint NOT NULL,
	"topic_id"	integer NOT NULL,
	PRIMARY KEY("featureinfoid" AUTOINCREMENT),
	FOREIGN KEY("topic_id") REFERENCES "internal_featuretype"("featuretypeid") DEFERRABLE INITIALLY DEFERRED
);
DROP TABLE IF EXISTS "internal_featuretype";
CREATE TABLE "internal_featuretype" (
	"featuretypeid"	integer NOT NULL,
	"name"	varchar(30) NOT NULL,
	"enable"	bool NOT NULL,
	"chinese_name"	varchar(30) NOT NULL,
	PRIMARY KEY("featuretypeid" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "internal_form";
CREATE TABLE "internal_form" (
	"formid"	integer NOT NULL,
	"companyname"	varchar(30),
	"contactname"	varchar(10) NOT NULL,
	"email"	varchar(100) NOT NULL,
	"address"	varchar(100) NOT NULL,
	"phone"	varchar(20) NOT NULL,
	"title"	varchar(30) NOT NULL,
	"content"	text,
	"addtime"	bigint NOT NULL,
	PRIMARY KEY("formid" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "internal_history";
CREATE TABLE "internal_history" (
	"historyid"	integer NOT NULL,
	"title"	varchar(30) NOT NULL,
	"content"	text NOT NULL,
	"addtime"	bigint NOT NULL,
	"lastUpdate"	bigint NOT NULL,
	PRIMARY KEY("historyid" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "internal_info";
CREATE TABLE "internal_info" (
	"infoid"	integer NOT NULL,
	"title"	varchar(30) NOT NULL,
	"imgpath"	varchar(100) NOT NULL,
	"enable"	bool NOT NULL,
	"addtime"	bigint NOT NULL,
	PRIMARY KEY("infoid" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "internal_item";
CREATE TABLE "internal_item" (
	"itemid"	integer NOT NULL,
	"name"	varchar(30) NOT NULL,
	"imgpath"	varchar(100) NOT NULL,
	"dimension"	text NOT NULL,
	"material"	varchar(100) NOT NULL,
	"info"	text,
	"addtime"	bigint NOT NULL,
	"lastUpdate"	bigint NOT NULL,
	"categoryid_id"	integer NOT NULL,
	PRIMARY KEY("itemid" AUTOINCREMENT),
	FOREIGN KEY("categoryid_id") REFERENCES "internal_category"("categoryid") DEFERRABLE INITIALLY DEFERRED
);
DROP TABLE IF EXISTS "internal_login";
CREATE TABLE "internal_login" (
	"loginid"	integer NOT NULL,
	"token"	varchar(100) NOT NULL,
	"tokenTime"	bigint NOT NULL,
	"loginTime"	bigint NOT NULL,
	"logoutTime"	bigint NOT NULL,
	"employeeid_id"	integer NOT NULL,
	PRIMARY KEY("loginid" AUTOINCREMENT),
	FOREIGN KEY("employeeid_id") REFERENCES "internal_employee"("employeeid") DEFERRABLE INITIALLY DEFERRED
);
DROP TABLE IF EXISTS "internal_message";
CREATE TABLE "internal_message" (
	"messageid"	integer NOT NULL,
	"read"	bool NOT NULL,
	"processed"	bool NOT NULL,
	"lastUpdate"	bigint NOT NULL,
	"formid_id"	integer NOT NULL,
	PRIMARY KEY("messageid" AUTOINCREMENT),
	FOREIGN KEY("formid_id") REFERENCES "internal_form"("formid") DEFERRABLE INITIALLY DEFERRED
);
DROP TABLE IF EXISTS "internal_news";
CREATE TABLE "internal_news" (
	"newsid"	integer NOT NULL,
	"title"	varchar(30) NOT NULL,
	"content"	text NOT NULL,
	"addtime"	bigint NOT NULL,
	"lastUpdate"	bigint NOT NULL,
	PRIMARY KEY("newsid" AUTOINCREMENT)
);
INSERT INTO "internal_banner" ("bannerid","name","imgpath","enable","addtime") VALUES (5,'compary_banner-1','/media/cdf35aff69.webp',1,1791680493),
 (6,'compary_banner-2','/media/2cce15e035.webp',1,1791680502),
 (7,'compary_banner-3','/media/0d086beacd.webp',1,1791680511),
 (8,'compary_banner-4','/media/ed3f6dbf67.webp',1,1791680520),
 (9,'compary_banner-5','/media/e716ad51e1.webp',1,1791680528),
 (10,'compary_banner-6','/media/6735611c73.webp',0,1791680537);
INSERT INTO "internal_category" ("categoryid","name","enable") VALUES (1,'航太科技',1),
 (2,'精密工業螺絲',1),
 (3,'智慧能源',1),
 (4,'工業整合',1);
INSERT INTO "internal_company" ("name","email","address","phone","fax","servicetime") VALUES ('史打客工業有限公司','Starkey01@StarkeyIndustrial.com','100臺北市中正區建國里重慶南路一段122號B5F','02-2311-3731','02-2720-0691','星期一: 13:00–22:00
星期二: 13:00–22:00
星期三: 13:00–22:00
星期四: 13:00–22:00
星期五: 13:00–22:00
星期六日: 休假');
INSERT INTO "internal_companylevel" ("companylevelid","level","name","grade","enable") VALUES (1,'C-0','董事長','頂層管理',1),
 (2,'C-1','執行長','頂層管理',1),
 (3,'C-1','總裁','頂層管理',1),
 (4,'C-1','財務長','頂層管理',1),
 (5,'C-1','營運長','頂層管理',1),
 (6,'C-1','技術長','頂層管理',1),
 (7,'C-1','行銷長','頂層管理',1),
 (8,'M-1','總經理','頂層管理',1),
 (9,'M-2','副總經理','頂層管理',1),
 (10,'M-3','協理','部門管理',1),
 (11,'M-4','總監','部門管理',1),
 (12,'M-5','經理','部門管理',1),
 (13,'M-6','副理','部門管理',1),
 (14,'M-7','襄理','部門管理',1),
 (15,'S-1','課長','基層人員',1),
 (16,'S-1','科長','基層人員',1),
 (17,'S-2','組長','基層人員',1),
 (18,'P-1','資深專員','基層人員',1),
 (19,'P-2','專員','基層人員',1),
 (20,'P-2','工程師','基層人員',1),
 (21,'P-3','管理師','基層人員',1),
 (22,'P-3','辦事員','基層人員',1),
 (23,'P-4','實習生','基層人員',1);
INSERT INTO "internal_downloads" ("downloadsid","name","filepath","size","version","info","addtime","lastUpdate") VALUES (1,'航太精密元件','/media/72a54efd55.pdf','4.20 MB','v1.0.0','ISO 9211 標準：定義了一般特性、測試和測量方法；
ISO 9022 標準：定義了與環境測試相關的術語；
MIL-F-48616：定義了表面品質的檢驗方法；
ECSS-Q-ST-70-17C 標準驗證塗層在惡劣條件下的耐久性。',1791893034,1791893034),
 (2,'逆變流器','/media/bfb9224463.pdf','2.43 MB','v1.0.0','1 安全事項 - 4
1.1 人員安全 - 4
1.2 設備保護  - 4
1.3 安裝安全 - 4
1.4 電氣連接 - 4
1.5 運行調適  - 5
1.6 保養維護 - 5
1.7 其他 - 5
2 產品介紹 - 6
2.1 功能型號 - 6
2.2 系統應用 - 6
2.3 尺寸及外觀 - 7
2.4 工作狀態 - 8
3 保存 - 9
4 安裝 - 10
4.1 選擇安裝位置 - 12
4.2 變流器安裝步驟 - 16
5 產品電氣連接 - 17
5.1 二次保護地線連接 - 18
5.2 交流線纜連接 - 19
5.3 太陽能模組連接 - 21
5.4 通訊線纜連接 - 25
6 安裝後檢查 - 30
7 運行與停止 - 31
8 介面訊息 - 32
9 保養維護 - 33
10 保固條件 - 37
11 回收處理 - 37
12 規格參數 - 38',1791893058,1791893058),
 (3,'綠氫儲存裝置','/media/7205c6f50e.pdf','515.31 KB','v1.0.0','Overview
Applications 03
System Purpose 04
Market Information & Trend 05
System Implementation
Hydrogen Electrolysis Types 07
System Architectures 08
System Description
AC-DC Rectifier 09
DC-DC Converter 10
Solution Overview
Block Diagram - Hydrogen Electrolyzer 11
High Power Integrated Modules (PIMs) 12
Full SiC Power Modules 13
SiC Discrete MOSFETs and SiC Cascode JFETs 14
1200V FS7 Discrete IGBTs 15
Gate Drivers 16
Current Sensing 17
Treo Platform 18
Recommended Products 19',1791893079,1791893079);
INSERT INTO "internal_faq" ("faqid","answer","addtime","lastUpdate","question") VALUES (1,'史打客工業有限公司創立於精密螺絲製造，憑藉多年累積的加工技術與品質管理經驗，
逐步發展為橫跨精密製造、低軌衛星應用及新能源技術的科技企業。

我們相信，製造不只是生產零件，
更是支撐產業創新的基礎。
因此，史打客工業持續投入智慧製造、自動化設備及新興技術，
希望成為企業值得信賴的長期合作夥伴。',1791728590,1791728590,'史打客工業是一間什麼樣的公司？'),
 (2,'目前史打客工業的事業版圖涵蓋三大領域：
1. 精密螺絲、扣件與金屬零組件製造
2. 低軌衛星相關零組件與系統整合應用
3. 新能源設備、能源管理及智慧解決方案

除了產品供應之外，
我們也提供客製化設計、產品共同開發及專案合作服務，
協助客戶從設計階段到量產導入，建立完整的合作流程。',1791728600,1791728601,'史打客工業主要提供哪些產品與服務？'),
 (3,'史打客工業認為，精密製造是許多科技產業的重要基礎。
隨著全球產業朝向太空科技、智慧能源及永續發展邁進，
公司也持續思考如何將既有製造能力延伸至更高附加價值的市場。

從精密加工到智慧製造，再到新興科技應用，
我們希望透過技術整合與持續創新，
陪伴客戶迎接下一個世代的產業發展。',1791728611,1791728611,'為什麼史打客工業會跨足低軌衛星與新能源產業？'),
 (4,'史打客工業重視與客戶建立長期合作關係，
提供客製化產品評估、共同開發及技術整合服務。
我們的團隊將依據不同產業需求，
協助規劃最適合的製造方案與產品方向，並透過專案管理機制，
提升開發效率與產品品質。

無論是少量試產、技術驗證，或是未來量產合作，
我們都期待與客戶共同完成每一項創新挑戰。',1791728623,1791728623,'如果企業有特殊需求，可以與史打客工業合作開發嗎？'),
 (5,'未來，
史打客工業將持續以「精密製造 × 太空科技 × 新能源」作為核心發展策略。

除了持續提升智慧製造能力之外，
公司也將深化低軌衛星供應鏈布局、拓展新能源應用，
並積極投入跨領域合作與人才培育。
我們希望從一家製造企業，成長為具備國際競爭力的科技公司，
持續為客戶創造更高的價值，並與合作夥伴共同迎向下一個產業世代。',1791728635,1791728635,'史打客工業未來的發展方向是什麼？');
INSERT INTO "internal_featureinfo" ("featureinfoid","title","content","addtime","lastUpdate","topic_id") VALUES (1,'🔨精密製造能力','累積多年精密加工經驗，具備高品質製造能力與嚴格品質管理流程。',1791719355,1791719355,1),
 (2,'🔬自主研發能力','持續投入產品設計、材料研究、系統整合及創新技術開發。',1791719467,1791719467,1),
 (3,'🤝跨領域整合','結合機械、電子、航太及能源技術，提供跨產業整合方案。',1791719478,1791719478,1),
 (4,'📄品質管理','建立完善品質管理制度，從設計、製造到檢驗，確保產品穩定可靠。',1791719488,1791719488,1),
 (5,'🌱永續發展','推動節能減碳、綠色製造及新能源應用，以科技支持永續發展目標。',1791719496,1791719496,1),
 (6,'🔩精密工業螺絲（Precision Fastening Systems）','特殊螺絲
客製化螺絲
高強度緊固件
CNC精密加工
特殊合金加工',1791719511,1791719511,2),
 (7,'🛰航太科技（Aerospace Technology）','航太零組件
低軌衛星系統
衛星結構設計
通訊模組
精密加工零件',1791719535,1791719535,2),
 (8,'🔋智慧能源（Smart Energy）','儲能系統
新型能源設備
能源管理系統
高效率能源轉換
綠能整合方案',1791719545,1791719545,2),
 (9,'⚙️工業整合（Engineering Solutions）','客製化設計
OEM / ODM
系統整合
技術顧問
工程服務',1791719553,1791719553,2),
 (10,'企業形象','From Precision to Possibility.
從精密開始，創造無限可能。',1791719567,1791719567,3),
 (11,'國際科技形象','Precision Beyond Earth.
精密，不止於地球。',1791719575,1791719575,3),
 (12,'航太定位','Engineering the Future of Space.
打造未來太空科技。',1791719584,1791719584,3),
 (13,'能源定位','Powering Tomorrow.
驅動未來能源。',1791719599,1791719599,3),
 (14,'全品牌定位','From One Screw to Infinite Possibilities.
從一顆螺絲，開啟無限可能。',1791719607,1791719607,3);
INSERT INTO "internal_featuretype" ("featuretypeid","name","enable","chinese_name") VALUES (1,'Specialty',1,'公司特色'),
 (2,'Topic',1,'生產品項'),
 (3,'BrandSlogan',1,'公司標語');
INSERT INTO "internal_form" ("formid","companyname","contactname","email","address","phone","title","content","addtime") VALUES (1,'WhiteHouse','王大明','wangdarming@gmail.com','1600 Pennsylvania Ave NW, Washington, DC 20500美國','12024567041','進100組低軌衛星','買買買買買
山姆大叔有錢
買買買買買
山姆大叔有錢
買買買買買
山姆大叔有錢
買買買買買
山姆大叔有錢
買買買買買
山姆大叔有錢
買買買買買
山姆大叔有錢',1785162013),
 (2,'qweqw','aaasaaasaaasaaas','aaas@aaas.com','aaasaaasaaasaaas','0912354678','qweqweqwe','qwdasda
qweqwe

zxczxczxc
asdasd
qweqweq',1791988058),
 (3,'qweqw','aaasaaasaaasaaas','aaas@aaas.com','aaasaaasaaasaaas','0912354678','qweqweqwe','qwdasda
qweqwe

zxczxczxc
asdasd
qweqweq',1791988115),
 (4,'qweqw','aaasaaasaaasaaas','aaas@aaas.com','aaasaaasaaasaaas','0912354678','qweqweqwe','qwdasda
qweqwe

zxczxczxc
asdasd
qweqweq',1791988206),
 (5,'EQWEQWE','EQW','qweqwe@qweqwe.com','100臺北市中正區建國里重慶南路一段122號B5F','0912354678','qweqweqwe','綠ASDASDAS',1792227394);
INSERT INTO "internal_history" ("historyid","title","content","addtime","lastUpdate") VALUES (1,'起點：一顆螺絲，奠定工業基礎','史打客工業有限公司創立之初，專注於高品質工業螺絲與精密緊固件的設計、生產與製造。

秉持著「每一顆螺絲，都承載著品質與責任」的理念，產品廣泛應用於機械設備、自動化生產、建築工程及精密製造領域，逐步建立穩固的技術實力與市場口碑。 ',1791687857,1791687857),
 (2,'跨越製造：邁向航太科技','累積多年精密加工與材料技術後，史打客開始投入航太零組件與衛星系統研發。

公司整合精密製造、電子控制、通訊工程及系統整合能力，投入低軌衛星相關技術開發，希望以自主技術打造更快速、更穩定、更具全球覆蓋能力的新世代通訊平台。

從地面上的每一顆螺絲，到環繞地球運行的衛星，史打客將精密製造的精神延伸至太空科技，展現台灣企業跨足航太領域的創新實力。',1791687871,1791687871),
 (3,'面向未來：開創新型能源','隨著全球邁向淨零排放與永續發展，史打客再次跨越產業疆界，投入新型能源技術研究。

公司聚焦於高效率能源轉換、儲能系統、綠色能源整合及次世代能源應用，希望透過創新科技降低能源消耗、提升使用效率，為產業及社會提供更潔淨、更安全、更永續的能源解決方案。',1791687879,1791687879),
 (4,'未來願景','史打客工業相信，每一次技術突破，都源自對未來的不斷探索。

從精密螺絲製造，到低軌衛星科技，再到新型能源研發，史打客始終秉持創新、品質、誠信與永續的核心價值，持續挑戰技術極限。

我們的目標，不只是製造產品，而是以科技串聯世界、以創新驅動未來，成為引領下一個世代的高科技企業。

從一顆螺絲開始，連結世界；從一顆衛星開始，連結宇宙；從一項能源開始，點亮未來。',1791687886,1791711972);
INSERT INTO "internal_info" ("infoid","title","imgpath","enable","addtime") VALUES (1,'工廠2','/media/ef19510387.webp',1,1791686633),
 (2,'工廠3','/media/386bfc8eac.webp',1,1791686649),
 (3,'工廠4','/media/a1c4bb787f.webp',1,1791686656),
 (4,'工廠5','/media/14688a2ca5.webp',1,1791686664),
 (5,'工廠6','/media/3c33e5aabf.webp',1,1791686671),
 (6,'工廠7','/media/808bcdd85c.webp',1,1791686679),
 (7,'工廠8','/media/e2ffb50b2f.webp',1,1791686685),
 (8,'工廠9','/media/cfe4c6b188.webp',1,1791686692),
 (9,'工廠10','/media/62b1369e08.webp',1,1791686698),
 (10,'工廠11','/media/90a742a11b.webp',1,1791686705),
 (11,'工廠12','/media/5bf7fc9d93.webp',1,1791686711),
 (12,'工廠13','/media/9c36344e2f.webp',1,1791686717);
INSERT INTO "internal_item" ("itemid","name","imgpath","dimension","material","info","addtime","lastUpdate","categoryid_id") VALUES (1,'光電光學零組件','/media/24594f42a7_mojbAJQ.webp','配件訂製:
	1. 專業加工製造治具
	2. 夾具
	3. LED模具
	4. 光電光學模具用澆口襯套
	5. 模仁
','不鏽鋼','內徑公差、外徑公差: 0.002mm

同心度、真圓度、圓筒度: 0.002mm

平行度、垂直度: 0.002mm',1791721739,1791721739,1),
 (2,'感測器通訊模組 ','/media/1fbee3dffd.webp','長:	41mm
	
寬:	36.7mm
	
高:	105.1mm','不鏽鋼、塑膠','說明:
	從導入到起動運轉， 
	均能夠「壓倒性」地改變作業現場的次世代感測器網路組件',1791721772,1791721772,1),
 (3,'美國細牙規格','/media/5370acb9e0.webp','名稱: 
	"美國細牙規格 MACHINE SCREW UNF 2A Q (60”)"
	
Size(號稱):
	"NO:0~NO:12；¼”~1”
	
T (牙數):
	12~80
	
美國標準螺紋: 
	公制螺紋: 
		1. 粗牙(NC)
		2. 細牙(NF)
		
    螺紋角:
		60度
		
備註:
	規格以每英吋有幾牙表示,	例如：NO:6-40NF 
	(NO:6：6#，螺紋外徑；40：每吋牙數；NF代表細牙規格)','不鏽鋼','NO:0
	T: 80,
    外徑MAX: 1.511
    外徑MIN: 1.430

NO:1
    T: 72,
    外徑MAX: 1.839
    外徑MIN: 1.750
	
NO:2
    T: 64,
    外徑MAX: 2.169
    外徑MIN: 2.073

NO:3
    T: 56,
    外徑MAX: 2.497
    外徑MIN: 2.393

NO:4
    T: 48,
    外徑MAX: 2.827
    外徑MIN: 2.713

NO:5
    T: 44,
    外徑MAX: 3.157
    外徑MIN: 3.035

NO:6
    T: 40,
    外徑MAX: 3.485
    外徑MIN: 3.355
	
NO:8
    T: 36,
    外徑MAX: 4.145
    外徑MIN: 4.006

NO:10
    T: 32,
    外徑MAX: 4.803
    外徑MIN: 4.651

NO:12
    T: 28,
    外徑MAX: 5.461
    外徑MIN: 5.296

1/4ln
	T: 28,
    外徑MAX: 6.325
    外徑MIN: 6.160

5/16ln,
    T: 24,
    外徑MAX: 7.910,
    外徑MIN: 7.727

3/8ln
    T: 24
    外徑MAX: 9.497
    外徑MIN: 9.314

7/16ln
    T: 20
    外徑MAX: 11.079
    外徑MIN: 10.874

1/2ln
    T: 20
    外徑MAX: 12.667
    外徑MIN: 12.461

9/16ln
    T: 18
    外徑MAX: 14.252
    外徑MIN: 14.031

5/8ln
    T: 18
    外徑MAX: 15.839
    外徑MIN: 15.618

3/4
	T: 16
	外徑MAX: 19.012
    外徑MIN: 18.773

7/8ln
    T: 14
    外徑MAX: 22.184
    外徑MIN: 21.963

1ln
	T: 12
    外徑MAX: 25.354
    外徑MIN: 25.065',1791721796,1791721796,2),
 (4,'高強度內六角螺絲緊固件','/media/d9eb1291b2.webp','規格:
	1. M3
	2. M4
	3. M5
	4. M6
	5. M8
	6. M10
	7. M12
	8. M14
	9. M16
	10. M20
	11. M24','不鏽鋼','標準:
	ISO 4762 / DIN 912
	
等級:8.8 / 10.9

長度範圍:
	6 毫米 – 200 毫米
	
表面處理:
	鋅（白色/黃色）/ 黑色氧化物 / 原色',1791721821,1791721821,2),
 (5,'綠氫存儲系統 ','/media/841b84695f.webp','容器:
	鎂基儲氫合金
	
儲存方式:
	固態的相態儲存
	
水電解:
	鹼性電解
	
溫度:
	300 ℃','不鏽鋼、塑膠','備註：
	二維活性碳材MXene (Mo2C) 作為基材的合成雙金屬有機骨架 (MOF) 全水分解電催化觸媒',1791721851,1791721851,3),
 (6,'電力儲存系統','/media/3cb07bfb73.webp','能源供應:
	太陽能板
	
逆變壓器:
	混和型逆變器

存儲裝置:
	智慧電池

電錶:
	智慧電錶','不鏽鋼、塑膠','備註：
	住宅型太陽光電儲能系統主要構成為太陽能板、混合型逆變器(Hybrid PV Inverter)及儲能電池等。儲能電池容量約為5kWh~15kWh，
	其中混合型逆變器功率約為10kW以內',1791721872,1791721872,3);
INSERT INTO "internal_message" ("messageid","read","processed","lastUpdate","formid_id") VALUES (1,1,0,1792229026,1),
 (2,1,0,1792229040,4),
 (3,1,1,1792229042,5);
INSERT INTO "internal_news" ("newsid","title","content","addtime","lastUpdate") VALUES (1,'2026 年 6 月 12 日 從螺絲工廠到低軌衛星供應鏈，史打客工業宣布完成首項衛星產品布局','全球低軌衛星市場持續升溫，
除了大型航太企業積極擴張外，也吸引許多具備精密製造能力的傳統產業投入。
以螺絲製造起家的史打客工業有限公司今日宣布，旗下首批衛星用結構固定模組已完成內部驗證，
並正式啟動低軌衛星事業布局，象徵公司正式跨入航太供應鏈。

史打客工業表示，
公司成立初期以工業螺絲與特殊扣件製造為核心，長年服務工具機、機械設備與汽車零組件市場。
近年則持續投入智慧製造、自動化設備與精密加工技術，希望將多年累積的製造能力延伸至更高附加價值的科技產業。

隨著全球衛星通訊需求快速增加，市場對高可靠度零組件的需求也同步提升。
史打客工業指出，公司近兩年開始成立專責團隊，投入衛星結構件、固定模組及相關產品開發，
希望藉由精密製造能力切入新興市場，逐步建立航太事業版圖。

「我們沒有改變製造的本質，而是讓製造的價值走向新的產業。」
史打客工業表示，公司過去累積的加工經驗、品質管理及供應鏈整合能力，
是跨足航太市場的重要基礎。

除了產品布局，公司近年也完成智慧工廠升級，
引進數位管理平台、自動化生產設備及AI品質檢測系統，希望縮短產品開發時程，
同時提升整體製造效率。
公司認為，未來航太產業除了技術能力外，
更重視供應鏈的穩定性與生產彈性。

市場觀察指出，低軌衛星已成為全球科技產業的重要發展方向，
從衛星本體、地面設備到零組件供應，都帶動新的商業機會。
對台灣製造業而言，具備精密加工能力的企業，
將有機會在全球供應鏈中扮演更重要角色。

史打客工業表示，今年將持續擴大相關產品開發，
同時尋求國際合作，希望從台灣出發，
逐步建立屬於自己的太空產業布局。',1791727170,1791727171),
 (2,'2026 年 8 月 29 日 布局新能源市場，史打客工業成立能源事業群，瞄準智慧儲能應用','能源轉型已成為全球產業共同課題，除了再生能源持續成長外，
如何提升能源使用效率，也成為企業投資的重要方向。
完成低軌衛星事業布局後，史打客工業有限公司今日宣布成立新能源事業群，
將以智慧儲能、能源管理及綠色製造為核心，展開企業第二波轉型。

史打客工業表示，公司並非能源產業的新創，
而是希望結合多年累積的製造能力與智慧控制技術，發展更符合未來市場需求的能源解決方案。
首波推出的模組化能源系統，可依不同場域彈性配置，
鎖定工廠、商業建築及資料中心等高耗能市場。

公司指出，近年AI應用快速發展，
也帶動資料中心與高科技產業的用電需求持續增加。
企業除了追求穩定供電，更開始重視能源管理效率，
因此史打客工業希望透過自主整合的系統平台，協助企業提升能源使用效益，
同時降低整體營運成本。

「未來能源不只是發電，更重要的是如何管理。」
史打客工業表示，能源管理將成為智慧工廠的重要一環，
因此公司除了投入設備開發，也同步建立軟體監控平台，
希望提供更完整的整合服務。

除了新事業布局，公司也宣布旗下工廠將全面推動綠色轉型，
包括導入再生能源設備、智慧用電監控及碳排放管理系統，希望在提升生產效率的同時，
也逐步實踐永續經營目標。

產業人士分析，近年不少傳統製造企業開始投入能源科技，
反映市場競爭已從產品本身延伸至整體解決方案。
對史打客工業而言，新能源事業不只是新的營收來源，
也代表企業正逐步建立製造、科技與永續並行的發展模式。

史打客工業表示，未來將持續擴大新能源產品布局，
並尋求更多跨領域合作，希望打造兼具智慧製造與能源創新的新世代企業。',1791727179,1791727179),
 (3,'2026 年 11 月 18 日 三大事業版圖成形，史打客工業啟用創新研發中心，加速布局下一個十年','從螺絲製造起家，到布局低軌衛星與新能源市場，
史打客工業有限公司今日宣布正式啟用全新創新研發中心，象徵公司歷經多年轉型後，正式邁入以科技創新為核心的新階段。
未來研發中心將整合智慧製造、航太應用及新能源技術，作為企業下一波成長的重要基地。

史打客工業表示，公司早期以精密螺絲與工業扣件聞名，
隨著全球製造業競爭加劇，逐步將資源投入智慧工廠、自動化設備及新興科技領域。
近年完成低軌衛星與新能源兩大事業布局後，公司希望透過研發中心整合不同領域資源，
加速產品開發速度。

「過去我們製造的是零件，未來希望創造的是產業價值。」
史打客工業表示，新的研發中心不只是產品開發基地，
更是跨領域合作平台，希望吸引更多來自不同背景的人才共同投入創新。

公司指出，未來研發重點將聚焦於智慧製造、自動化整合、航太零組件及能源管理等方向，同時持續深化數位化管理，
希望建立更具彈性的產品開發流程，以因應快速變化的市場需求。

除了技術發展，史打客工業也同步推動人才培育計畫，
將與學術單位及產業夥伴展開合作，建立長期人才交流機制。
公司認為，科技產業的競爭已不只是設備與資本，
更需要持續累積創新能量與跨領域合作能力。

市場觀察指出，近年台灣不少傳統製造企業積極投入科技轉型，
從智慧工廠、半導體設備到航太及能源領域，都可見企業尋找第二成長曲線。
史打客工業近年的布局，也反映傳統製造業正逐步從代工思維，
轉向以技術、品牌及創新為核心的經營模式。

史打客工業表示，公司未來將持續以精密製造為根基，
結合低軌衛星、新能源及智慧製造三大事業方向，打造具國際競爭力的台灣科技品牌，
並朝向全球市場穩健發展。',1791727187,1791727187);
DROP INDEX IF EXISTS "internal_featureinfo_topic_id_94a17cc0";
CREATE INDEX "internal_featureinfo_topic_id_94a17cc0" ON "internal_featureinfo" (
	"topic_id"
);
DROP INDEX IF EXISTS "internal_item_categoryid_id_2c5b4aa0";
CREATE INDEX "internal_item_categoryid_id_2c5b4aa0" ON "internal_item" (
	"categoryid_id"
);
DROP INDEX IF EXISTS "internal_login_employeeid_id_f35f3ed7";
CREATE INDEX "internal_login_employeeid_id_f35f3ed7" ON "internal_login" (
	"employeeid_id"
);
DROP INDEX IF EXISTS "internal_message_formid_id_de999121";
CREATE INDEX "internal_message_formid_id_de999121" ON "internal_message" (
	"formid_id"
);
COMMIT;
