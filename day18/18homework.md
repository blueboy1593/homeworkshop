# 18homework

1. 우리가 사용하는 SQLite는 RDBMS에 속한다. RDBMS의 특징을 2가지만 작성하시오.

- 체계화된 데이터의 모임
- 여러 응용 시스템들의 통합된 정보를 저장하여, 운영할 수 있는 공용 데이터의 묶음
- 논리적으로 연관된 하나 이상의 자료 모음으로, 데이터를 고도로 구조화함으로써 검색/갱신등의 데이터 관리를 효율화함



2. 다음 중 맞으면 T, 틀리면 F를 작성하시오.
   1. RDBMS를 조작하기 위해서는 SQL 문을 사용한다. [ T ]
   2. SQL에서 명령어는 대문자로 써야만 동작한다. [ F ]
   3. 일반적인 SQL 문에서 명령어는 세미콜론(;) 으로 끝난다. [ T ]
   4. SQLite에서 dot(.) 으로 시작하는 명령어는 SQL이 아니다. [ ]
   5. 한 개의 DB 에는 한개의 테이블만 존재한다. [ F ]



3. 다음 코드의 실행결과로 나타나는 값을 작성하세요.
   sqlite> .nullvalue ‘NULL’
   sqlite> CREATE TABLE ssafy (
   …> id INTEGER PRIMARY KEY,
   …> location TEXT,
   …> class INTEGER
   …> );
   sqlite> INSERT INTO ssafy (id, location)
   …> VALUES (1, ‘JEJU’);
   sqlite> SELECT class FROM ssafy WHERE id=1;

NULL

