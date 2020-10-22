# Day23 homeworkshop

## homework

1. Django 에서 Database 에 값을 일괄 삽입하기 위하여 Fixture 기능을 이용한다 . Fixture
   파일은 기본적으로 각각의 app 폴더 안의 fixtures 폴더에 위치해야 하며 , 파일 형식은
   json( 또는 yaml( 를 사용한다 .
2. D23 Workshop 과 같이 Database 에 데이터가 저장되어 있을 때 , Django Fixture 기능을
   이용하여 아래와 같은 yaml 형식의 Fixture 파일을 만들려고 한다 . 입력해야 하는 명령
   어를 작성하시오 . 단 , 파일 이름은 person.yaml 로 한다

```bash
pip install pyyaml
- yaml 모듈 설치
python manage.py dumpdata --format=yaml persons.person > persons.yaml
- data를 yaml 형식에 저장
python manage.py loaddata person.yaml
- yaml에 저장된 데이터를 불러오기
```



## workshop

### musicians.json 파일

```json
[
    {
        "model": "articles.musician",
        "pk": 1,
        "fields": {
            "FIRST_NAME": "Paul",
            "LAST_NAME": "McCartney"
        }
    },
    {
        "model": "articles.musician",
        "pk": 2,
        "fields": {
            "FIRST_NAME": "John",
            "LAST_NAME": "Lennon"
        }
    }
]
```

### models.py에 있는 Musician 모델

```python
class Musician(models.Model):
    # PK = models.IntegerField()
    FIRST_NAME = models.CharField(max_length=20)
    LAST_NAME = models.CharField(max_length=20)
```

migration을 해준 뒤 아래의 명령어를 통해 json 파일에서 데이터를 불러오는 것이 가능하다.

```bash
$ python manage.py loaddata musicians.json
Installed 2 object(s) from 1 fixture(s)
(venv)
```

| #    | id   | FIRST_NAME | LAST_NAME |
| ---- | ---- | ---------- | --------- |
| 1    | 1    | Paul       | McCartney |
| 2    | 2    | John       | Lennon    |

