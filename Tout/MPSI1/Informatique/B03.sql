-- -*- coding:utf-8 -*-
-- Exercice 1:
CREATE TABLE avril (nom TEXT, montant FLOAT, jour INTEGER, id INTEGER PRIMARY KEY);
INSERT INTO avril VALUES('A', 23, 4, 1);
INSERT INTO avril VALUES('A', 17, 8, 2);
INSERT INTO avril VALUES('A', 5, 23, 3);
INSERT INTO avril VALUES('A', 9, 28, 4);
INSERT INTO avril VALUES('B', 53, 6, 5);
INSERT INTO avril VALUES('B', 10, 17, 6);
INSERT INTO avril VALUES('B', 9, 19, 7);
INSERT INTO avril VALUES('B', 16, 30, 8);
INSERT INTO avril VALUES('C', 2, 8, 9);
INSERT INTO avril VALUES('C', 4, 13, 10);
INSERT INTO avril VALUES('C', 3, 17, 11);
INSERT INTO avril VALUES('C', 6, 28, 12);
INSERT INTO avril VALUES('C', -20, 30, 13);
INSERT INTO avril VALUES('D', 4, 15, 14);
INSERT INTO avril VALUES('D', 9, 21, 15);
INSERT INTO avril VALUES('D', -15, 30, 16);
INSERT INTO avril VALUES('E', -4, 13, 17);
INSERT INTO avril VALUES('E', 3, 14, 18);
INSERT INTO avril VALUES('E', 1, 15, 19);
INSERT INTO avril VALUES('E', -10, 30, 20);
INSERT INTO avril VALUES('F', 251, 2, 21);
INSERT INTO avril VALUES('F', 198, 9, 22);
INSERT INTO avril VALUES('F', 174, 17, 23);
INSERT INTO avril VALUES('F', 221, 23, 24);
INSERT INTO avril VALUES('F', 134, 30, 25);

SELECT * FROM avril;
SELECT '';

-- 1.1:
SELECT 'Question 1.1';
SELECT * FROM avril WHERE nom = 'C';
SELECT '';
-- 1.2:
SELECT 'Question 1.2';
SELECT * FROM avril WHERE jour >= 21;
SELECT '';
-- 1.3:
SELECT 'Question 1.3';
SELECT * FROM avril ORDER BY montant;
SELECT '';
-- 1.4:
SELECT 'Question 1.4';
SELECT nom, SUM(montant) FROM avril WHERE nom = 'A';
SELECT '';
-- 1.5:
SELECT 'Question 1.5';
SELECT nom, SUM(montant) AS total FROM avril WHERE jour >= 11 and jour <= 20 GROUP BY nom;
SELECT '';
-- 1.6:
SELECT 'Question 1.6';
SELECT nom, SUM(montant) / 30 AS quotidien FROM avril GROUP BY nom;
SELECT '';
-- 1.7:
SELECT 'Question 1.7';
SELECT nom, SUM(montant) AS somme FROM avril GROUP BY nom ORDER BY somme;
SELECT '';

-- Exercice 2:
-- 2.1:
SELECT 'Question 2.1:';
CREATE TABLE étudiants (nom TEXT, naissance FLOAT);
INSERT INTO étudiants VALUES('A', 1999.0415);
INSERT INTO étudiants VALUES('B', 1999.0205);
INSERT INTO étudiants VALUES('C', 1999.0918);
INSERT INTO étudiants VALUES('D', 1999.0131);
INSERT INTO étudiants VALUES('E', 1999.0708);

CREATE TABLE math (nom TEXT, DS INTEGER, note FLOAT);
INSERT INTO math VALUES('A', 1, 17);
INSERT INTO math VALUES('A', 2, 14);
INSERT INTO math VALUES('A', 3, 11);
INSERT INTO math VALUES('A', 4, 18);
INSERT INTO math VALUES('B', 1, 8);
INSERT INTO math VALUES('B', 2, 9);
INSERT INTO math VALUES('B', 3, 14);
INSERT INTO math VALUES('B', 4, 16);
INSERT INTO math VALUES('C', 1, 15);
INSERT INTO math VALUES('C', 2, 16);
INSERT INTO math VALUES('C', 3, 13);
INSERT INTO math VALUES('C', 4, 16);
INSERT INTO math VALUES('D', 1, 16);
INSERT INTO math VALUES('D', 2, 17);
INSERT INTO math VALUES('D', 3, 18);
INSERT INTO math VALUES('D', 4, 14);
INSERT INTO math VALUES('E', 1, 7);
INSERT INTO math VALUES('E', 2, 8);
INSERT INTO math VALUES('E', 4, 11);

CREATE TABLE français (nom TEXT, DS INTEGER, note FLOAT);
INSERT INTO français VALUES('A', 1, 14);
INSERT INTO français VALUES('A', 2, 13);
INSERT INTO français VALUES('B', 1, 12);
INSERT INTO français VALUES('B', 2, 11);
INSERT INTO français VALUES('C', 1, 15);
INSERT INTO français VALUES('C', 2, 11);
INSERT INTO français VALUES('D', 1, 14);
INSERT INTO français VALUES('D', 2, 15);
INSERT INTO français VALUES('E', 1, 14);
INSERT INTO français VALUES('E', 2, 11);

SELECT * FROM étudiants;
SELECT * FROM math;
SELECT * FROM français;
SELECT '';
-- 2.2:
SELECT 'Question 2.2:';
SELECT nom, MAX(note), MIN(note) FROM math GROUP BY nom;
SELECT '';
-- 2.3:
SELECT 'Question 2.3:';
SELECT AVG(note) FROM math;
SELECT AVG(note) FROM français;
SELECT nom, AVG(note) FROM math GROUP BY nom;
SELECT nom, AVG(note) FROM français GROUP BY nom;
SELECT '';
-- 2.4:
SELECT 'Question 2.4:';
.nullvalue ''
SELECT nom, DS AS DS_F, note AS note_F, NULL AS DS_M, NULL AS note_M FROM français UNION SELECT nom, NULL AS DS_F, NULL AS note_F, DS AS DS_M, note AS note_M FROM math;
SELECT '';
-- 2.5:
SELECT 'Question 2.5:';
SELECT nom, SUM(note * DS) / SUM(DS) AS moyennes_pondérées FROM math GROUP BY nom;
SELECT '';
-- 2.6:
SELECT 'Question 2.6:';
SELECT * FROM français NATURAL JOIN étudiants WHERE DS = 1 ORDER BY naissance;
SELECT '';
