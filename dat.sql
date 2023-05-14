drop database productosdb;
create database productosdb;
use productosdb;
CREATE TABLE productos
       (
  	CODIGO int NOT NULL AUTO_INCREMENT primary key,
	DESCRIPCION VARCHAR(20),
	PRECIO NUMERIC(7,2),
     	STOCK BOOL,
      	CATEGORIA VARCHAR(15),
        MARCA VARCHAR(15),
        MODELO VARCHAR(15)
 );


INSERT INTO productos VALUES (1024,'LAPTOP',5426, FALSE,'PORTATILES','ASUS','VIVOBOOK');
INSERT INTO productos VALUES (7643,'LAPTOP', 5324, TRUE,'PORTATILES','ASUS','ZENBOOK 14');
INSERT INTO productos VALUES (3582,'CELULAR',1253, TRUE,'ELECTRONICO','XIAOMI','REDMI 10');
INSERT INTO productos VALUES (1974,'CELULAR', 1636, TRUE,'ELECTRONICO','XIAOMI','REDMI 11');
INSERT INTO productos VALUES (5672,'CELULAR',925,FALSE,'ELECTRONICO','HUAWEI','SMARTH P');
INSERT INTO productos VALUES (2648,'LAPTOP',4522, TRUE,'PORTATILES','ASUS','ZENBOOK');
