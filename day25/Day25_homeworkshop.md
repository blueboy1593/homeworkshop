# Day25_homeworkshop

## homework

1.
Article 모델과 User 모델을 M:N 관계로 설정하여 좋아요 ’ 기능을 구현하려고 한다 . 이
때 빈 칸 ( 에 들어갈 클래스의 이름을 작성하시오

```python
a) ManyToManyField
```

2.
위의 Article 모델에서는 이미 user 필드에서 User 모델과 1:N 관계가 설정되어 있기 때
문에 M:N 관계를 설정하려 하면 User 모델에서 Article 을 참조하는 이름이 중복되어 오
류가 발생한다 . 이 때 , 이를 방지하기 위하여 별도의 이름을 생성하도록 하는 , 빈 칸 (
에 들어갈 옵션을 작성하시오.

```python
b) related_name
```

## workshop

Article 의 Hashtag 를 구현하기 위하여 아래와 같이 개 체 관계 다이어그램을 작성한 것
이다 . 다이어그램을 바탕으로 models.py 에 Article 모델과 Hashtag 모델을 작성하시오

```python
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()

    class Meta:
        ordering = ('-pk', )
        
class Hashtag(models.Model):
    content = models.TextField()
    articles = models.ManyToManyField(Article, related_name='hashtags')
```

