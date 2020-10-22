# 20 Homeworkshop

## Workshop

*투표를 위한 설문 앱을 만들려고 한다. 이 앱은 질문에 대한 답변을 투표하여 각각의 항목이 몇 표를 받았는지 기록하는 기능을 가지고 있다. 설문 앱은 Question 모델과 Choice 모델로 구성되어 있으며, 각각의 모델은 다음과 같은 컬럼을 가지고 있고 1:N 관계를 형성하고 있다.*

*위와 같은 컬럼을 가지고 있는 Question 모델과 Choice 모델을 정의하는 models.py 코드를 작성하시오.*

```python
class Question(models.Model):
    title = models.CharField(max_length=20)
   
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    content = models.CharField(max_length=200)
    votes = models.IntegerField()
```

## Homework

1. School 모델과 Student 모델을 1:N 관계로 설정하려고 한다. models.py의 Student 모델 에서 필요한 코드를 작성하시오.

```python
class Student(models.Model):
	school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='student')
```

2. Question 모델과 Comment 모델은 1:N 관계를 형성하고 있다.
위와 같은 코드가 있을 때, views.py에서 해당 Question의 모든 Comment를 가져오기 위한 코드를 작성하시오. (단, related_name은 설정하지 않았다고 가정한다.)

```python
question = Questions.objects.get(id=id)
comments = question.comments.all()
```

3. 기본적으로 1:N 관계를 설정할 때, ForeignKey를 이용해서 1에 해당하는 클래스를 지정 한다. 지정한 클래스가 Movie일 때, ForeignKey로 지정된 컬럼의 이름은 무엇인가?

```python
article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
```



