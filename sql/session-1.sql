CREATE DATABASE showroom;
CREATE TABLE car (carID INT, carMake varchar(255), carModel varchar(255));
INSERT INTO car VALUES (1,"Tata","Sumo"),(2,"Tata","Safari"),(3,"Tata","Xenon"),(4,"Tata","Sumo Grande");
SELECT * FROM car;
CREATE TABLE tatasedans (carID INT, carMake varchar(255), carModel varchar(255));
INSERT INTO car VALUES (5,"Tata","Tigor"),(6,"Tata","Zest"),(7,"Tata","Indigo Manza");
DELETE FROM car WHERE carID >4;
SELECT * FROM car;
INSERT INTO tatasedans VALUES (5,"Tata","Tigor"),(6,"Tata","Zest"),(7,"Tata","Indigo Manza");
SELECT *,COUNT(*) as CNT FROM tatasedans
GROUP BY carID;
SELECT *,COUNT(*) as CNT FROM tatasedans
GROUP BY carID
HAVING CNT>1;

SELECT carID, carMake, carModel, 
row_number() OVER(partition by carID, carMake, carModel ORDER BY carID, carMake, carModel) AS SNo
FROM tatasedans;

CREATE TABLE tsduplicate AS 
(SELECT carID, carMake, carModel, row_number() OVER(partition by carID, carMake, carModel ORDER BY carID, carMake, carModel) AS SNo 
FROM tatasedans); 

DELETE FROM tsduplicate WHERE SNo>1;
DROP TABLE tatasedans;
RENAME TABLE tsduplicate TO tatasedans; 
 



