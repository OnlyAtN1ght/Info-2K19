-- -*- coding:utf-8 -*-
-- Exercice 1:

-- 1.1:
SELECT 'Question 1.1';
CREATE TABLE vins (vin TEXT, prix_unitaire FLOAT);
INSERT INTO vins VALUES('R', 14);
INSERT INTO vins VALUES('GW', 16);
INSERT INTO vins VALUES('PN', 10);
INSERT INTO vins VALUES('PG', 15);

CREATE TABLE achats (client TEXT, vin TEXT, quantité INTEGER);
INSERT INTO achats VALUES('A', 'R', 6);
INSERT INTO achats VALUES('A', 'GW', 12);
INSERT INTO achats VALUES('B', 'R', 12);
INSERT INTO achats VALUES('B', 'GW', 6);
INSERT INTO achats VALUES('B', 'PG', 6);
INSERT INTO achats VALUES('C', 'GW', 6);
INSERT INTO achats VALUES('C', 'PN', 6);
INSERT INTO achats VALUES('C', 'PG', 12);
INSERT INTO achats VALUES('D', 'R', 6);
INSERT INTO achats VALUES('D', 'GW', 6);
INSERT INTO achats VALUES('D', 'PN', 12);
INSERT INTO achats VALUES('E', 'GW', 6);
INSERT INTO achats VALUES('E', 'PG', 12);
SELECT '';
-- 1.2:
SELECT 'Question 1.2';
SELECT * FROM vins NATURAL JOIN achats WHERE client = 'D';
SELECT '';
-- 1.3:
SELECT 'Question 1.3';
SELECT client, vin, quantité FROM vins NATURAL JOIN achats ORDER BY client;
SELECT client, SUM(quantité * prix_unitaire) AS total FROM vins NATURAL JOIN achats GROUP BY client;
SELECT '';
-- 1.4:
SELECT 'Question 1.4';
SELECT SUM(quantité * prix_unitaire) AS vigneron FROM vins NATURAL JOIN achats;
SELECT '';
