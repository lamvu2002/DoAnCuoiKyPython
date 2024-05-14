create database QuanLyBanHang
use QuanLyBanHang
CREATE TABLE KHACHHANG(
	MAKH CHAR(4) CONSTRAINT KH_MAKH_PK PRIMARY KEY,
	HOTEN VARCHAR(40) NOT NULL,
	DCHI VARCHAR(50),
	SODT VARCHAR(20) NOT NULL,
	NGSINH SMALLDATETIME,
	DOANHSO MONEY,
	NGDK SMALLDATETIME
)
CREATE TABLE NHANVIEN(
	MANV CHAR(4) CONSTRAINT NV_MANV_PK PRIMARY KEY,
	HOTEN VARCHAR(40) NOT NULL,
	SODT VARCHAR(20) NOT NULL,
	NGVL SMALLDATETIME
)
CREATE TABLE HOADON (
	SOHD INT CONSTRAINT HD_SOHD_PK PRIMARY KEY,
	NGHD SMALLDATETIME,
	MAKH CHAR(4) CONSTRAINT HD_MAKH_FK FOREIGN KEY (MAKH)
		REFERENCES KHACHHANG(MAKH),
	MANV CHAR(4) CONSTRAINT HD_MANV_FK FOREIGN KEY (MANV)
		REFERENCES NHANVIEN(MANV),
	TRIGIA MONEY
)
CREATE TABLE SANPHAM (
	MASP CHAR(4) NOT NULL CONSTRAINT SP_MASP_PK PRIMARY KEY(MASP),
	TENSP VARCHAR(40),
	DVT	VARCHAR(20),
	NUOCSX VARCHAR(40),
	GIA	MONEY
)
CREATE TABLE CTHD (
	SOHD INT,
	MASP CHAR(4),
	SL INT,
	CONSTRAINT CTHD_SOHD_MASP_PK PRIMARY KEY (SOHD, MASP),
	CONSTRAINT CTHD_SOHD_FK FOREIGN KEY (SOHD)
		REFERENCES HOADON(SOHD),
	CONSTRAINT CTHD_MASP_FK FOREIGN KEY (MASP)
		REFERENCES SANPHAM(MASP)
)
--1.2
ALTER TABLE SANPHAM ADD GHICHU VARCHAR(20)
--1.3
ALTER TABLE KHACHHANG ADD LOAIKH TINYINT
--1.4
ALTER TABLE SANPHAM ALTER COLUMN GHICHU VARCHAR(100)
--1.5
ALTER TABLE SANPHAM DROP COLUMN GHICHU
--1.6
ALTER TABLE KHACHHANG ALTER COLUMN LOAIKH VARCHAR(20)
--1.7
ALTER TABLE SANPHAM ADD CONSTRAINT SANPHAM_DVT CHECK (DVT = 'cay' OR DVT = 'hop' OR DVT = 'cai' OR DVT = 'quyen' OR DVT = 'chuc')
--1.8
ALTER TABLE SANPHAM ADD CONSTRAINT SANPHAM_GIA CHECK(GIA > 500)
--1.9
ALTER TABLE CTHD ADD CONSTRAINT CTHD_SL CHECK (SL>0)
--1.11
CREATE TRIGGER INS_UPD_NGHD_HOADON ON HOADON
FOR INSERT, UPDATE
AS
BEGIN
	DECLARE @MAKH CHAR(4), @NGDK smalldatetime, @NGHD smalldatetime

	SELECT @NGHD = NGHD, @MAKH = MAKH
	FROM inserted

	SELECT @NGDK = NGDK, @MAKH = MAKH
	FROM KHACHHANG
	WHERE @MAKH = MAKH

	IF (@NGDK>@NGHD)
	BEGIN
		PRINT 'LOI: NGAY HOA DON KHONG HOP LE!'
		ROLLBACK TRANSACTION
	END
	ELSE
	BEGIN
		PRINT 'THEM HOA DON THANH CONG!'
	END
END

INSERT INTO HOADON(SOHD,NGHD,MAKH,MANV,TRIGIA) VALUES (2001,'20/07/2006','KH01','NV01',320000)
--2.1
SET DATEFORMAT DMY 

INSERT INTO NHANVIEN(MANV,HOTEN,SODT,NGVL) VALUES ('NV01','NGUYEN NHU NHUT','0927345678','13/04/2006')
INSERT INTO NHANVIEN(MANV,HOTEN,SODT,NGVL) VALUES ('NV02','LE THI PHI YEN','0987567390','21/04/2006')
INSERT INTO NHANVIEN(MANV,HOTEN,SODT,NGVL) VALUES ('NV03','NGUYEN VAN B','0997047382','27/04/2006')
INSERT INTO NHANVIEN(MANV,HOTEN,SODT,NGVL) VALUES ('NV04','NGO THANH TUAN','0913758498','24/06/2006')
INSERT INTO NHANVIEN(MANV,HOTEN,SODT,NGVL) VALUES ('NV05','NGUYEN THI TRUC THANH','0918590387','20/07/2006')

INSERT INTO KHACHHANG(MAKH,HOTEN,DCHI,SODT,NGSINH,NGDK,DOANHSO) VALUES ('KH01','NGUYEN VAN A','731TRAN HUNG DAO,Q5,THHCM','08823451','22/10/1960','22/07/2006',13060000)
INSERT INTO KHACHHANG(MAKH,HOTEN,DCHI,SODT,NGSINH,NGDK,DOANHSO) VALUES ('KH02','TRAN NGOC HAN','23/5NGUYEN TRAI,Q5,TPHCM','0908256478','03/04/1974','30/07/2006',280000)
INSERT INTO KHACHHANG(MAKH,HOTEN,DCHI,SODT,NGSINH,NGDK,DOANHSO) VALUES ('KH03','TRAN NGOC LINH','45NGUYEN CANH CHAN,Q1,TPHCM','0938776266','10/06/1980','05/05/2006',3860000)
INSERT INTO KHACHHANG(MAKH,HOTEN,DCHI,SODT,NGSINH,NGDK,DOANHSO) VALUES ('KH04','TRAN MINH LONG','50/34LE DAI HANH,Q10,TPHCM','0917325476','09/03/1965','02/10/2006',250000)
INSERT INTO KHACHHANG(MAKH,HOTEN,DCHI,SODT,NGSINH,NGDK,DOANHSO) VALUES ('KH05','LE NHAT MINH','34TRUONG DINH,Q3,TPHCM','08246108','10/03/1950','28/10/2006',21000)
INSERT INTO KHACHHANG(MAKH,HOTEN,DCHI,SODT,NGSINH,NGDK,DOANHSO) VALUES ('KH06','LE HOAI THUONG','227NGUYEN VAN CU,Q5,TPHCM','08631738','31/12/1981','24/11/2006',915000)
INSERT INTO KHACHHANG(MAKH,HOTEN,DCHI,SODT,NGSINH,NGDK,DOANHSO) VALUES ('KH07','NGUYEN VAN TAM','32/3 TRAN BINH TRONG,Q5,TPHCM','0916783565','06/06/1971','01/12/2006',12500)
INSERT INTO KHACHHANG(MAKH,HOTEN,DCHI,SODT,NGSINH,NGDK,DOANHSO) VALUES ('KH08','PHAN THI THANH','45/2 AN DUONG VUONG,Q5,TPHCM','0938435756','10/01/1971','13/12/2006',365000)
INSERT INTO KHACHHANG(MAKH,HOTEN,DCHI,SODT,NGSINH,NGDK,DOANHSO) VALUES ('KH09','LE HA VINH','837 LE HONG PHONG,Q5,TPHCM','08654763','03/03/1979','14/01/2007',70000)
INSERT INTO KHACHHANG(MAKH,HOTEN,DCHI,SODT,NGSINH,NGDK,DOANHSO) VALUES ('KH10','HA DUY LAP','34/34B NGUYEN TRAI,Q5,TPHCM','08768904','02/05/1983','16/01/2007',67500)

INSERT INTO SANPHAM(MASP,TENSP,DVT,NUOCSX,GIA) VALUES ('BC01','BUT CHI','CAY','SINGAPORE',3000)
INSERT INTO SANPHAM(MASP,TENSP,DVT,NUOCSX,GIA) VALUES ('BC02','BUT CHI','CAY','SINGAPORE',5000)
INSERT INTO SANPHAM(MASP,TENSP,DVT,NUOCSX,GIA) VALUES ('BC03','BUT CHI','CAY','VIETNAM',3500)
INSERT INTO SANPHAM(MASP,TENSP,DVT,NUOCSX,GIA) VALUES ('BC04','BUT CHI','HOP','VIETNAM',30000)
INSERT INTO SANPHAM(MASP,TENSP,DVT,NUOCSX,GIA) VALUES ('BB01','BUT BI','CAY','VIETNAM',5000)
INSERT INTO SANPHAM(MASP,TENSP,DVT,NUOCSX,GIA) VALUES ('BB02','BUT BI','CAY','TRUNGQUOC',7000)
INSERT INTO SANPHAM(MASP,TENSP,DVT,NUOCSX,GIA) VALUES ('BB03','BUT BI','HOP','THAILAN',100000)
INSERT INTO SANPHAM(MASP,TENSP,DVT,NUOCSX,GIA) VALUES ('TV01','TAP 100 TRANG GIAY MONG','QUYEN','TRUNGQUOC',2500)
INSERT INTO SANPHAM(MASP,TENSP,DVT,NUOCSX,GIA) VALUES ('TV02','TAP 200 TRANG GIAY MONG','QUYEN','TRUNGQUOC',4500)
INSERT INTO SANPHAM(MASP,TENSP,DVT,NUOCSX,GIA) VALUES ('TV03','TAP 100 TRANG GIAY TOT','QUYEN','VIETNAM',3000)
INSERT INTO SANPHAM(MASP,TENSP,DVT,NUOCSX,GIA) VALUES ('TV04','TAP 200 TRANG GIAY TOT','QUYEN','VIETNAM',5500)
INSERT INTO SANPHAM(MASP,TENSP,DVT,NUOCSX,GIA) VALUES ('TV05','TAP 100 TRANG ','CHUC','VIETNAM',23000)
INSERT INTO SANPHAM(MASP,TENSP,DVT,NUOCSX,GIA) VALUES ('TV06','TAP 200 TRANG ','CHUC','VIETNAM',53000)
INSERT INTO SANPHAM(MASP,TENSP,DVT,NUOCSX,GIA) VALUES ('TV07','TAP 100 TRANG ','CHUC','TRUNGQUOC',34000)
INSERT INTO SANPHAM(MASP,TENSP,DVT,NUOCSX,GIA) VALUES ('ST01','SO TAY 500 TRANG','QUYEN','TRUNGQUOC',40000)
INSERT INTO SANPHAM(MASP,TENSP,DVT,NUOCSX,GIA) VALUES ('ST02','SO TAY LOAI 1','QUYEN','VIETNAM',55000)
INSERT INTO SANPHAM(MASP,TENSP,DVT,NUOCSX,GIA) VALUES ('ST03','SO TAY LOAI 2','QUYEN','VIETNAM',51000)
INSERT INTO SANPHAM(MASP,TENSP,DVT,NUOCSX,GIA) VALUES ('ST04','SO TAY','QUYEN','THAILAN',55000)
INSERT INTO SANPHAM(MASP,TENSP,DVT,NUOCSX,GIA) VALUES ('ST05','SO TAY MONG','QUYEN','THAILAN',20000)
INSERT INTO SANPHAM(MASP,TENSP,DVT,NUOCSX,GIA) VALUES ('ST06','PHAN VIET BANG','HOP','VIETNAM',5000)
INSERT INTO SANPHAM(MASP,TENSP,DVT,NUOCSX,GIA) VALUES ('ST07','PHAN KHONG BUI','HOP','VIETNAM',7000)
INSERT INTO SANPHAM(MASP,TENSP,DVT,NUOCSX,GIA) VALUES ('ST08','BONG BAMG','CAI','VIETNAM',1000)
INSERT INTO SANPHAM(MASP,TENSP,DVT,NUOCSX,GIA) VALUES ('ST09','BUT LONG','CAY','VIETNAM',5000)
INSERT INTO SANPHAM(MASP,TENSP,DVT,NUOCSX,GIA) VALUES ('ST10','BUT LONG','CAY','TRUNGQUOC',7000)

INSERT INTO HOADON(SOHD,NGHD,MAKH,MANV,TRIGIA) VALUES (1001,'27/07/2006','KH01','NV01',320000)
INSERT INTO HOADON(SOHD,NGHD,MAKH,MANV,TRIGIA) VALUES (1002,'10/08/2006','KH01','NV02',840000)
INSERT INTO HOADON(SOHD,NGHD,MAKH,MANV,TRIGIA) VALUES (1003,'23/08/2006','KH02','NV01',100000)
INSERT INTO HOADON(SOHD,NGHD,MAKH,MANV,TRIGIA) VALUES (1004,'01/09/2006','KH02','NV01',180000)
INSERT INTO HOADON(SOHD,NGHD,MAKH,MANV,TRIGIA) VALUES (1005,'20/10/2006','KH01','NV02',3800000)
INSERT INTO HOADON(SOHD,NGHD,MAKH,MANV,TRIGIA) VALUES (1006,'16/10/2006','KH01','NV03',2430000)
INSERT INTO HOADON(SOHD,NGHD,MAKH,MANV,TRIGIA) VALUES (1007,'28/10/2006','KH03','NV03',510000)
INSERT INTO HOADON(SOHD,NGHD,MAKH,MANV,TRIGIA) VALUES (1008,'28/10/2006','KH01','NV03',440000)
INSERT INTO HOADON(SOHD,NGHD,MAKH,MANV,TRIGIA) VALUES (1009,'28/10/2006','KH03','NV04',200000)
INSERT INTO HOADON(SOHD,NGHD,MAKH,MANV,TRIGIA) VALUES (1010,'01/11/2006','KH01','NV01',5200000)
INSERT INTO HOADON(SOHD,NGHD,MAKH,MANV,TRIGIA) VALUES (1011,'04/11/2006','KH04','NV03',250000)
INSERT INTO HOADON(SOHD,NGHD,MAKH,MANV,TRIGIA) VALUES (1012,'30/11/2006','KH05','NV03',21000)
INSERT INTO HOADON(SOHD,NGHD,MAKH,MANV,TRIGIA) VALUES (1013,'12/12/2006','KH06','NV01',5000)
INSERT INTO HOADON(SOHD,NGHD,MAKH,MANV,TRIGIA) VALUES (1014,'31/12/2006','KH03','NV02',3150000)
INSERT INTO HOADON(SOHD,NGHD,MAKH,MANV,TRIGIA) VALUES (1015,'01/01/2007','KH06','NV01',910000)
INSERT INTO HOADON(SOHD,NGHD,MAKH,MANV,TRIGIA) VALUES (1016,'01/01/2007','KH07','NV02',12500)
INSERT INTO HOADON(SOHD,NGHD,MAKH,MANV,TRIGIA) VALUES (1017,'02/01/2007','KH08','NV03',35000)
INSERT INTO HOADON(SOHD,NGHD,MAKH,MANV,TRIGIA) VALUES (1018,'13/01/2007','KH08','NV03',330000)
INSERT INTO HOADON(SOHD,NGHD,MAKH,MANV,TRIGIA) VALUES (1019,'13/01/2007','KH01','NV03',30000)
INSERT INTO HOADON(SOHD,NGHD,MAKH,MANV,TRIGIA) VALUES (1020,'14/01/2007','KH09','NV04',70000)
INSERT INTO HOADON(SOHD,NGHD,MAKH,MANV,TRIGIA) VALUES (1021,'16/01/2007','KH10','NV03',67500)
INSERT INTO HOADON(SOHD,NGHD,MAKH,MANV,TRIGIA) VALUES (1022,'16/01/2007',NULL,'NV03',7000)
INSERT INTO HOADON(SOHD,NGHD,MAKH,MANV,TRIGIA) VALUES (1023,'17/01/2007',NULL,'NV01',330000)

INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1001,'TV02',10)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1001,'ST01',5)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1001,'BC01',5)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1001,'BC02',10)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1001,'ST08',10)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1002,'BC04',20)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1002,'BB01',20)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1002,'BB02',20)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1003,'BB03',10)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1004,'TV01',20)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1004,'TV02',10)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1004,'TV03',10)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1004,'TV04',10)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1005,'TV05',50)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1005,'TV06',50)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1006,'TV07',20)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1006,'ST01',30)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1006,'ST02',10)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1007,'ST03',10)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1008,'ST04',8)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1009,'ST05',10)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1010,'TV07',50)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1010,'ST07',50)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1010,'ST08',100)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1010,'ST04',50)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1010,'TV03',100)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1011,'ST06',50)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1012,'ST07',3)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1013,'ST08',5)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1014,'BC02',80)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1014,'BB02',100)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1014,'BC04',60)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1014,'BB01',50)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1015,'BB02',30)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1015,'BB03',7)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1016,'TV01',5)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1017,'TV02',1)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1017,'TV03',1)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1017,'TV04',5)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1018,'ST04',6)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1019,'ST05',1)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1019,'ST06',2)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1020,'ST07',10)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1021,'ST08',5)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1021,'TV01',7)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1021,'TV02',10)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1022,'ST07',1)
INSERT INTO CTHD(SOHD,MASP,SL) VALUES (1023,'ST04',6)
--2.2
SELECT * INTO SANPHAM1 FROM SANPHAM
SELECT * INTO KHACHHANG1 FROM KHACHHANG
--2.3
UPDATE SANPHAM1 SET GIA=GIA*1.05 WHERE NUOCSX='THAILAN'
--2.4
UPDATE SANPHAM1 SET GIA=GIA*0.95 WHERE NUOCSX='TRUNGQUOC' AND GIA<=10000
--2.5
UPDATE KHACHHANG1 SET LOAIKH ='Vip' WHERE (NGDK<'2007/1/1' AND DOANHSO>=10000000) OR (NGDK>'2007/1/1' AND DOANHSO >=2000000)

--3.1
SELECT MASP, TENSP FROM SANPHAM WHERE NUOCSX='TRUNGQUOC'
--3.2
SELECT MASP, TENSP FROM SANPHAM WHERE DVT='CAY' OR DVT='QUYEN'
--3.3
SELECT MASP, TENSP FROM SANPHAM WHERE MASP LIKE'B%01'
--3.4
SELECT MASP, TENSP FROM SANPHAM WHERE NUOCSX='TRUNGQUOC'AND GIA>=30000 AND GIA<=40000
--3.5
SELECT MASP, TENSP FROM SANPHAM WHERE NUOCSX='TRUNGQUOC'OR NUOCSX='THAILAN' AND GIA>=30000 AND GIA<=40000
--3.6
SELECT SOHD, TRIGIA FROM HOADON WHERE NGHD='1/1/2007' OR NGHD='2/1/2007'
--3.7
SELECT SOHD, TRIGIA 
FROM HOADON 
WHERE MONTH(NGHD)=1 AND YEAR(NGHD)=2007 
ORDER BY DAY(NGHD) DESC, TRIGIA ASC
--3.8
SELECT KH.MAKH, HOTEN 
FROM KHACHHANG KH INNER JOIN HOADON HD
ON KH.MAKH=HD.MAKH
WHERE NGHD='1/1/2007'
--3.9
SELECT HD.SOHD, HD.TRIGIA
FROM HOADON HD INNER JOIN NHANVIEN NV
ON HD.MANV=NV.MANV
WHERE HOTEN='NGUYEN VAN B' AND NGHD='28/10/2006'
--3.10
SELECT DISTINCT SP.MASP, TENSP
FROM SANPHAM SP INNER JOIN CTHD CT
ON SP.MASP = CT.MASP
WHERE EXISTS(SELECT *
FROM CTHD CT INNER JOIN HOADON HD
ON CT.SOHD = HD.SOHD 
WHERE SP.MASP = CT.MASP AND MONTH(NGHD) = 10 AND YEAR(NGHD) = 2006 
AND MAKH IN(SELECT HD.MAKH
FROM HOADON HD INNER JOIN KHACHHANG KH
ON HD.MAKH = KH.MAKH
WHERE HOTEN = 'NGUYEN VAN A'))
--3.11
SELECT SOHD
FROM CTHD
WHERE MASP='BB01' OR MASP='BB02'
--3.12
SELECT SOHD
FROM CTHD
WHERE (MASP='BB01' OR MASP='BB02') AND (SL>=10 AND SL<=20)
--3.13
SELECT SOHD
FROM CTHD
WHERE (MASP='BB01') AND (SL>=10 AND SL<=20)
INTERSECT
SELECT SOHD
FROM CTHD
WHERE (MASP='BB02') AND (SL>=10 AND SL<=20)
--3.14
SELECT MASP, TENSP
FROM SANPHAM
WHERE NUOCSX='TRUNGQUOC'
UNION
SELECT SP.MASP, TENSP 
FROM SANPHAM SP, CTHD, HOADON HD
WHERE SP.MASP = CTHD.MASP AND HD.SOHD = CTHD.SOHD OR NGHD='1/1/2007'
--3.15
SELECT MASP, TENSP
FROM SANPHAM
EXCEPT 
SELECT SP.MASP, TENSP 
FROM SANPHAM SP, CTHD
WHERE SP.MASP = CTHD.MASP
--3.16
SELECT MASP, TENSP
FROM SANPHAM
EXCEPT 
SELECT SP.MASP, TENSP 
FROM SANPHAM SP, CTHD , HOADON HD
WHERE SP.MASP = CTHD.MASP  AND HD.SOHD = CTHD.SOHD AND YEAR(NGHD) = 2006
--3.17
SELECT MASP, TENSP
FROM SANPHAM
WHERE NUOCSX='TRUNGQUOC'
EXCEPT 
SELECT SP.MASP, TENSP 
FROM SANPHAM SP, CTHD , HOADON HD
WHERE SP.MASP = CTHD.MASP  AND HD.SOHD = CTHD.SOHD AND YEAR(NGHD) = 2006
--3.20
SELECT COUNT(*) AS SL_KHONGPHAITHANHVIEN
FROM HOADON HD
WHERE MAKH NOT IN(SELECT MAKH
					FROM KHACHHANG KH 
					WHERE KH.MAKH = HD.MAKH)
--3.21
SELECT COUNT(DISTINCT MASP) AS SL_SANPHAM
FROM CTHD, HOADON HD 
WHERE CTHD.SOHD = HD.SOHD AND YEAR(NGHD) = 2006
--3.22
SELECT MAX(TRIGIA) AS MAX_TRIGIA, MIN(TRIGIA) AS MIN_TRIGIA
FROM HOADON
--3.23
SELECT AVG(TRIGIA) TB_TRIGIA
FROM HOADON
WHERE YEAR(NGHD) = 2006
--3.24
SELECT SUM(TRIGIA) AS DOANHTHU
FROM HOADON
WHERE YEAR(NGHD) = 2006
--3.25
SELECT SOHD
FROM HOADON
WHERE YEAR(NGHD) = 2006 AND TRIGIA = (SELECT MAX(TRIGIA)
										FROM HOADON
										WHERE YEAR(NGHD) = 2006)
--3.26
SELECT HOTEN
FROM KHACHHANG KH, HOADON HD
WHERE HD.MAKH = KH.MAKH AND TRIGIA = (SELECT MAX(TRIGIA)
										FROM HOADON
										WHERE YEAR(NGHD) = 2006)
--3.27
SELECT TOP 3 MAKH, HOTEN
FROM KHACHHANG
ORDER BY DOANHSO DESC
--3.28
SELECT MASP, TENSP
FROM SANPHAM
WHERE GIA IN (SELECT DISTINCT TOP 3 GIA
				FROM SANPHAM
				ORDER BY GIA DESC)
--3.29
SELECT MASP, TENSP
FROM SANPHAM
WHERE NUOCSX = 'THAILAN' AND GIA IN (SELECT DISTINCT TOP 3 GIA
										FROM SANPHAM
										ORDER BY GIA DESC)
--3.30
SELECT MASP, TENSP
FROM SANPHAM
WHERE NUOCSX = 'TRUNGQUOC' AND GIA IN (SELECT DISTINCT TOP 3 GIA
										FROM SANPHAM
										WHERE NUOCSX = 'TRUNGQUOC'
										ORDER BY GIA DESC)
--3.32
SELECT COUNT(DISTINCT MASP)
FROM SANPHAM
WHERE NUOCSX = 'TRUNG QUOC'
--3.33
SELECT NUOCSX, COUNT(DISTINCT MASP) AS TONGSOSANPHAM
FROM SANPHAM
GROUP BY NUOCSX
--3.34
SELECT NUOCSX, MAX(GIA) AS MAX, MIN(GIA) AS MIN, AVG(GIA) AS AVG
FROM SANPHAM
GROUP BY NUOCSX
--3.35
SELECT NGHD, SUM(TRIGIA) AS DOANHTHU
FROM HOADON
GROUP BY NGHD
--3.36
SELECT MASP, SUM(SL) AS TONGSL
FROM CTHD
WHERE MASP IN(SELECT MASP
				FROM CTHD, HOADON HD
				WHERE CTHD.SOHD = HD.SOHD AND MONTH(NGHD) = 10 AND YEAR(NGHD) = 2006)
GROUP BY MASP
--3.37
SELECT MONTH(NGHD) AS THANG, SUM(TRIGIA) AS DOANHTHU
FROM HOADON
WHERE YEAR(NGHD) = 2006
GROUP BY MONTH(NGHD)
--3.38
SELECT SOHD
FROM CTHD
GROUP BY SOHD
HAVING COUNT( DISTINCT MASP)>=4
--3.39
SELECT SOHD
FROM CTHD, SANPHAM SP
WHERE CTHD.MASP = SP.MASP AND NUOCSX='VIETNAM'
GROUP BY SOHD
HAVING COUNT( DISTINCT CTHD.MASP) = 3
--3.40
SELECT TOP 1 HD.MAKH, HOTEN
FROM KHACHHANG KH, HOADON HD
WHERE HD.MAKH = KH.MAKH
GROUP BY HD.MAKH, HOTEN
ORDER BY COUNT(HD.MAKH) DESC
--3.41
SELECT TOP 1 MONTH(NGHD) AS THANG
FROM HOADON
WHERE YEAR(NGHD) = 2006
GROUP BY MONTH(NGHD)
ORDER BY SUM(TRIGIA) DESC
--3.42
SELECT TOP 1 CTHD.MASP, TENSP
FROM CTHD, SANPHAM SP, HOADON HD
WHERE CTHD.MASP = SP.MASP AND HD.SOHD = CTHD.SOHD AND YEAR(NGHD) = 2006
GROUP BY CTHD.MASP, TENSP
ORDER BY SUM(SL)
--3.43
SELECT B.NUOCSX, MASP, TENSP
FROM (SELECT NUOCSX, MAX(GIA) AS MAX
		FROM SANPHAM
		GROUP BY NUOCSX) AS B LEFT JOIN SANPHAM SP
ON SP.GIA = B.MAX
WHERE B.NUOCSX = SP.NUOCSX
--3.44
SELECT NUOCSX
FROM SANPHAM
GROUP BY NUOCSX
HAVING COUNT(DISTINCT GIA)>=3
--3.45
SELECT TOP 1 HD.MAKH
FROM (SELECT DISTINCT TOP 10 MAKH, DOANHSO
		FROM KHACHHANG
		GROUP BY MAKH, DOANHSO
		ORDER BY DOANHSO DESC) AS TOP10DS, HOADON HD
WHERE HD.MAKH = TOP10DS.MAKH
GROUP BY HD.MAKH
ORDER BY COUNT(HD.MAKH) DESC
