select * from étudiants;
select nom, max(note) from math group by nom;
select nom, min(note) from math group by nom;
select nom, min(note), max(note) from math group by nom;
select avg(note) from français;
select avg(note) from math;
select avg(note) from français union select avg(note) from math;
select nom, avg(note) from math group by nom;
select nom, avg(note) from français group by nom;

select nom, DS, note from math union select nom, DS, note from français;
select 'math' as matière union select 'français' as matière;
select 'math', nom, DS, note from math union select 'français', nom, DS, note from français;
select *,'math' as matière from math union select *, 'français' as matière from français order by matière, nom, DS;
select count(nom) from(select *,'math' as matière from math union select *, 'français' as matière from français order by matière, nom, DS);
select count(nom) from(select *,'math' as matière from math union select *, 'français' as matière from français order by matière, nom, DS) where nom = 'A';

select nom, matière, avg(note) from (select *,'math' as matière from math union select *, 'français' as matière from français order by matière, nom, DS) group by matière, nom;

select note*DS as note from math;
select nom, sum(note*DS) / sum(DS) as moyennes from math group by nom;

select * from français where ds = 1;
select nom, naissance from étudiants;
select * from français join étudiants on français.nom=étudiants.nom where ds=1 order by naissance;