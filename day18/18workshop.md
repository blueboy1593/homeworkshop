# 18workshop

1. 아래 표와 같은 스키마를 가진 DB 테이블을 생성하고 , 아래와 같이 데이터를 입력해 봅시다

```sql
CREATE TABLE bands (
    id INT NOT NULL,
    name TEXT NOT NULL,
    debut INT NOT NULL
);
sqlite> INSERT INTO bands
   ...> VALUES (1, "Queen", 1973)
   ...> VALUES (2, 'Coldplay', 1998), (3, 'MCR', 2001);
sqlite> SELECT * FROM bands;
id          name        debut
----------  ----------  ----------
1           Queen       1973
2           Coldplay    1998
3           MCR         2001
```

2. bands 테이블에서 모든 데이터 레코드의 id 와 name 만 조회하는 SQL query 문을 작성하고 실행하시오

```sql
sqlite> SELECT id, name FROM bands;
id          name
----------  ----------
1           Queen
2           Coldplay
3           MCR
```

3. bands 테이블에서 debut 가 2000 보다 작은 밴드들의 이름만을 조회하는 SQL query 문을 작성하고 실행하시오

```sql
sqlite> SELECT name FROM bands WHERE debut<2000;
name
----------
Queen
Coldplay
```