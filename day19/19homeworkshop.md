# 19homeworkshop

## workshop

1. 해당 테이블에 다음과 같이 컬럼을 추가하고 데이터를 삽입하시오

```sql
UPDATE bands SET members = 4 WHERE rowid = 1;
sqlite> UPDATE bands SET members = 5 WHERE rowid = 2;
sqlite> UPDATE bands SET members = 9 WHERE rowid = 3;
sqlite> SELECT * FROM bands;
id          name        debut       members
----------  ----------  ----------  ----------
1           Queen       1973        4
2           Coldplay    1998        5
3           MCR         2001        9
```

2. id 가 3 인 레코드의 members 를 5 로 수정하는 SQL query 문을 작성하고 실행하시오

```sqlite
sqlite> UPDATE bands SET members = 5 WHERE rowid = 3;
sqlite> SELECT * FROM bands;
id          name        debut       members
----------  ----------  ----------  ----------
1           Queen       1973        4
2           Coldplay    1998        5
3           MCR         2001        5
```

3. Id 가 2 인 레코드를 삭제하는 SQL query 를 작성하고 실행하시오

```sql
sqlite> DELETE FROM bands WHERE rowid=2;
sqlite> SELECT * FROM bands;
id          name        debut       members
----------  ----------  ----------  ----------
1           Queen       1973        4
3           MCR         2001        5
```



## homework

1. 다음과 같은 스키마를 가지는 데이터베이스 테이블 friends 를 생성하시오

```sql
sqlite> CREATE TABLE friends (
   ...>     id INTEGER PRIMARY KEY,
   ...>     name TEXT NOT NULL,
   ...>     location TEXT NOT NULL
   ...> );
sqlite> .schema friends
CREATE TABLE friends (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    location TEXT NOT NULL
);
```

2. 해당 테이블에 다음과 같이 데이터를 입력하시오

```sql
sqlite> INSERT INTO friends
   ...> VALUES (1, 'Justin', 'Seoul');
sqlite> INSERT INTO friends
   ...> VALUES (2, 'Simon', 'New York');
sqlite> INSERT INTO friends
   ...> VALUES (3, 'Chang', 'Las Vegas');
sqlite> INSERT INTO friends
   ...> VALUES (4, 'John', 'Sydney');
sqlite> SELECT * FROM friends;
id          name        location
----------  ----------  ----------
1           Justin      Seoul
2           Simon       New York
3           Chang       Las Vegas
4           John        Sydney
```

3. 스키마를 다음과 같이 변경하시오

```sql
sqlite> ALTER TABLE friends ADD COLUMN married INTEGER;
sqlite> SELECT * FROM friends;
id          name        location    married
----------  ----------  ----------  ----------
1           Justin      Seoul
2           Simon       New York
3           Chang       Las Vegas
4           John        Sydney
```

4. 데이터를 다음과 같이 추가하시오

```sql
sqlite> UPDATE friends SET married = 1 WHERE rowid = 1;
sqlite> UPDATE friends SET married = 0 WHERE rowid = 2;
sqlite> UPDATE friends SET married = 0 WHERE rowid = 3;
sqlite> UPDATE friends SET married = 1 WHERE rowid = 4;
sqlite> SELECT * FROM friends;
id          name        location    married
----------  ----------  ----------  ----------
1           Justin      Seoul       1
2           Simon       New York    0
3           Chang       Las Vegas   0
4           John        Sydney      1
```

