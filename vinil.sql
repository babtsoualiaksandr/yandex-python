sqlite> create table musicians(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(20));
sqlite> insert into musicians (name) values('Петя');
sqlite> insert into musicians (name) values('Маша');
sqlite> select * from musicians;
1|Петя
2|Маша
sqlite> create table labels (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(20));
sqlite> insert into labels (name) values('Граммофон');
sqlite> insert into labels (name) values('Скрипичный ключ');
sqlite> select * from labels;
1|Граммофон
2|Скрипичный ключ
sqlite> create table albums (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(20), rating INTEGER,musician_id INTEGER, label_id INTEGER );
sqlite> insert into albums (name, rating, musician_id, label_id) values('Дебютный альбом', 8, 1,1);sqlite> insert into albums (name, rating, musician_id, label_id) values('Этюды', 10, 2,1); sqlite> insert into albums (name, rating, musician_id, label_id) values('Осень', 6, 2,2);

SELECT
  musicians.name AS musicians_name,
  labels.name AS labels_name, 
  albums.name AS albums_name, 
  albums.rating AS albums_rating
FROM 
 musicians, labels  
 LEFT JOIN albums ON albums.musician_id = musicians.id and albums.label_id = labels.id
 WHERE albums.rating > 5 and albums.rating < 9
